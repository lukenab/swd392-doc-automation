#!/usr/bin/env python3
"""Activity Diagram pipeline for the SWD392 Project Management System.

Sub-commands
------------
render     Render PlantUML sources to report-ready SVG files (needs Java and
           plantuml.jar) and post-process them deterministically.
validate   Validate the manifest, the PlantUML sources, the traceability
           comments and the rendered SVG files against the Use Case YAML.
status     Print the per-domain totals recorded in the manifest.
report     Regenerate docs/activity-diagram-generation-report.md and
           docs/activity-diagram-review-report.md from the manifest.

Only the Use Case YAML and Business Rules in data/ are authoritative. This tool
never edits them.

PlantUML jar resolution order: --plantuml-jar, the PLANTUML_JAR environment
variable, then tools/plantuml.jar (ignored by git). Verified with 1.2024.7.

Examples
--------
    py scripts/activity_diagrams.py validate
    py scripts/activity_diagrams.py render --key UC-SPRINT-TASK-CREATE
    py scripts/activity_diagrams.py render --all
    py scripts/activity_diagrams.py report
"""
from __future__ import annotations

import argparse
import math
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, OrderedDict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from usecase_tool.loader import load_project  # noqa: E402

ACTIVITY_DIR = ROOT / "diagrams" / "activity"
MANIFEST = ACTIVITY_DIR / "manifest.yml"
STYLE_INCLUDE = "!include ../../_shared/activity-style.puml"
EXPECTED_CONCRETE = 55
FONT = "Times New Roman"

SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK_NS)
S = "{%s}" % SVG_NS

# Partition names supported by repository data (actors.yml and the project-
# scoped roles/accountabilities described for the User actor).
ALLOWED_LANES = {
    "Guest", "User", "Project Owner", "Product Owner", "Developer",
    "System Administrator", "System", "Email Service", "Identity Provider",
}
STATUS_BLOCKED = (
    "BLOCKED — REQUIREMENT CONFLICT",
    "BLOCKED — INSUFFICIENT SPECIFICATION",
)
MANIFEST_FIELDS = (
    "key", "display_id", "name", "group", "primary_actor", "secondary_actors",
    "assignee", "source", "svg", "generation_status", "traceability_status",
    "uml_review_status", "visual_review_status", "final_status", "blocked_reason",
)
FORBIDDEN_DIRECTIVES = re.compile(r"^\s*(title|caption|header|footer|legend)\b", re.I | re.M)
LOGIN_ACTION = re.compile(r":[^;]*\b(log ?in|sign ?in)\b", re.I)

FRAME_INK = "#202020"
FRAME_WIDTH = "1.4"
FRAME_MARGIN = 12.0
LANE_PADDING = 8.0


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def fmt(value: float) -> str:
    text = f"{value:.4f}".rstrip("0").rstrip(".")
    return text if text not in ("-0", "") else "0"


def num(value: str | None) -> float:
    return float(str(value).strip())


def load_manifest() -> dict[str, Any]:
    if not MANIFEST.exists():
        raise SystemExit(f"Missing manifest: {MANIFEST.relative_to(ROOT)}")
    with MANIFEST.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def concrete_use_cases() -> list[dict[str, Any]]:
    project = load_project(ROOT / "data")
    return [uc for uc in project.use_cases if not uc.get("abstract")]


def project_data():
    return load_project(ROOT / "data")


def domain_folder(project, use_case: dict[str, Any]) -> str:
    return project.groups[use_case["group"]]["folder"]


# --------------------------------------------------------------------------- #
# PlantUML source parsing
# --------------------------------------------------------------------------- #
ACTION_RE = re.compile(r"^\s*:(.*?);\s*$", re.S)


def parse_source(text: str) -> dict[str, Any]:
    """Return lanes, actions with their trace references and guard refs."""
    lanes: dict[str, str] = {}
    for alias, title in re.findall(r'^\|(\w+)\|\s*\$lane_title\("([^"]+)"\)', text, re.M):
        lanes[alias] = title
    plain = [lane for lane in re.findall(r"^\|([^|\n]+)\|\s*$", text, re.M) if lane not in lanes]
    actions: list[dict[str, Any]] = []
    pending: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        trace = re.match(r"^'\s*\[([^\]]+)\]", stripped)
        if trace:
            pending = [ref.strip() for ref in trace.group(1).split(",") if ref.strip()]
        elif stripped.startswith(":"):
            block = [stripped]
            while not block[-1].endswith(";") and i + 1 < len(lines):
                i += 1
                block.append(lines[i].strip())
            body = " ".join(block)[1:-1].strip()
            actions.append({"text": re.sub(r"\s+", " ", body), "refs": pending})
            pending = []
        elif stripped and not stripped.startswith("'") and not re.match(r"^\|\w+\|$", stripped):
            pending = []  # a trace comment applies only to the action that follows it
        i += 1
    guards = re.findall(r"\[[^\]\n]*?(EX-\d+|AF-\d+)[^\]\n]*\]", text)
    return {"lanes": lanes, "plain_lanes": plain, "actions": actions, "guard_refs": guards}


def valid_ref(ref: str, use_case: dict[str, Any]) -> bool:
    nf = len(use_case.get("normal_flow") or [])
    post = len(use_case.get("postconditions") or [])
    pre = len(use_case.get("preconditions") or [])
    af_ids = {a.get("id") for a in use_case.get("alternative_flows") or []}
    ex_ids = {e.get("id") for e in use_case.get("exceptions") or []}
    m = re.fullmatch(r"NF(\d+)", ref)
    if m:
        return 1 <= int(m.group(1)) <= nf
    m = re.fullmatch(r"POST(\d+)", ref)
    if m:
        return 1 <= int(m.group(1)) <= post
    m = re.fullmatch(r"PRE(\d+)", ref)
    if m:
        return 1 <= int(m.group(1)) <= pre
    m = re.fullmatch(r"(AF-\d+)(\.\d+)?", ref)
    if m:
        if m.group(1) not in af_ids:
            return False
        if m.group(2):
            flow = next(a for a in use_case["alternative_flows"] if a.get("id") == m.group(1))
            return 1 <= int(m.group(2)[1:]) <= len(flow.get("steps") or [])
        return True
    if re.fullmatch(r"EX-\d+", ref):
        return ref in ex_ids
    if ref.startswith("BR-"):
        return ref in (use_case.get("business_rules") or [])
    if ref in ("OTHER", "TRIGGER"):
        return True
    if ref == "GUIDE-7.3":  # docs/activity-diagram-guideline.md section 7.3
        return True
    return False


# --------------------------------------------------------------------------- #
# Step 1 - render with PlantUML
# --------------------------------------------------------------------------- #
def resolve_jar(cli_value: str | None) -> Path:
    for candidate in (cli_value, os.environ.get("PLANTUML_JAR"), str(ROOT / "tools" / "plantuml.jar")):
        if candidate and Path(candidate).is_file():
            return Path(candidate).resolve()
    raise SystemExit(
        "plantuml.jar not found. Pass --plantuml-jar <path>, set PLANTUML_JAR, "
        "or place the jar at tools/plantuml.jar (ignored by git)."
    )


def run_plantuml(jar: Path, source: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / (source.stem + ".svg")
    if target.exists():
        target.unlink()
    cmd = ["java", "-Djava.awt.headless=true", "-jar", str(jar), "-charset", "UTF-8",
           "-failfast2", "-nometadata", "-tsvg", "-o", str(out_dir.resolve()), str(source.resolve())]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        output = (proc.stdout + proc.stderr).strip()
        raise RuntimeError(f"PlantUML failed (exit {proc.returncode}) for {source}:\n{output}")
    if not target.exists():
        raise RuntimeError(f"PlantUML produced no SVG for {source}")
    return target


# --------------------------------------------------------------------------- #
# Step 2 - deterministic SVG post-processing
# --------------------------------------------------------------------------- #
def _iter(root: ET.Element, tag: str):
    return list(root.iter(S + tag))


def format_svg(svg_path: Path) -> tuple[float, float]:
    tree = ET.parse(svg_path)
    root = tree.getroot()
    if root.get("data-pres-formatted") == "1":
        vb = [num(v) for v in root.get("viewBox").split()]
        return vb[2], vb[3]

    parent_of = {child: parent for parent in root.iter() for child in parent}
    vb = [num(v) for v in re.split(r"[\s,]+", root.get("viewBox", "").strip()) if v]
    if len(vb) != 4:
        raise RuntimeError(f"SVG has no usable viewBox: {svg_path}")

    # open UML arrowheads: PlantUML draws filled 4-point polygons (wing, tip, wing, notch)
    for poly in _iter(root, "polygon"):
        fill = (poly.get("fill") or "").lower()
        nums = [p for p in re.split(r"[\s,]+", poly.get("points", "").strip()) if p]
        if len(nums) != 8 or fill in ("", "none", "#ffffff", "#fff", "white"):
            continue
        parent = parent_of[poly]
        index = list(parent).index(poly)
        chevron = ET.Element(S + "polyline", {
            "points": f"{nums[0]},{nums[1]} {nums[2]},{nums[3]} {nums[4]},{nums[5]}",
            "fill": "none", "stroke": poly.get("fill"), "stroke-width": "1.4",
            "stroke-linejoin": "miter", "stroke-linecap": "butt", "class": "open-arrowhead",
        })
        parent.remove(poly)
        parent.insert(index, chevron)

    # swimlane borders (vertical lines spanning most of the drawing)
    lanes = []
    for line in _iter(root, "line"):
        x1, x2, y1, y2 = (num(line.get(a)) for a in ("x1", "x2", "y1", "y2"))
        if abs(x1 - x2) < 0.01 and abs(y2 - y1) >= 0.6 * vb[3]:
            lanes.append(line)
    if lanes:
        # a long bypass flow line can also span most of the drawing; real borders all start at the
        # top of the partitions, so keep only the lines that start there
        lanes_top = min(min(num(l.get("y1")), num(l.get("y2"))) for l in lanes)
        lanes = [l for l in lanes if min(num(l.get("y1")), num(l.get("y2"))) - lanes_top < 1]
    if len(lanes) < 2:
        raise RuntimeError(f"No swimlane borders found in {svg_path}; activity diagrams must use partitions.")
    xs = [num(l.get("x1")) for l in lanes]
    left, right = min(xs), max(xs)
    top = min(min(num(l.get("y1")), num(l.get("y2"))) for l in lanes)
    bottom = max(max(num(l.get("y1")), num(l.get("y2"))) for l in lanes)

    # lane padding: outer borders move outwards, every border extends downwards
    for line in lanes:
        x = num(line.get("x1"))
        if abs(x - left) < 0.01:
            line.set("x1", fmt(left - LANE_PADDING)); line.set("x2", fmt(left - LANE_PADDING))
        elif abs(x - right) < 0.01:
            line.set("x1", fmt(right + LANE_PADDING)); line.set("x2", fmt(right + LANE_PADDING))
        if num(line.get("y2")) >= num(line.get("y1")):
            line.set("y2", fmt(bottom + LANE_PADDING))
        else:
            line.set("y1", fmt(bottom + LANE_PADDING))
    left -= LANE_PADDING
    right += LANE_PADDING
    bottom += LANE_PADDING

    # header separator: below the bold lane titles, never closer to the first node
    titles = [t for t in _iter(root, "text")
              if t.get("font-weight") == "bold" and num(t.get("y")) < top + 60
              and num(t.get("font-size", "0")) >= 12]
    if not titles:
        raise RuntimeError(f"Swimlane titles not found in {svg_path}")
    title_bottom = max(num(t.get("y")) + 0.25 * num(t.get("font-size")) for t in titles)
    content_top = math.inf
    for e in _iter(root, "ellipse"):
        content_top = min(content_top, num(e.get("cy")) - num(e.get("ry")))
    for r in _iter(root, "rect"):
        if r.get("rx"):
            content_top = min(content_top, num(r.get("y")))
    header = min(title_bottom + 5, (title_bottom + content_top) / 2)

    # canvas: equal margin round the frame without clipping any text
    min_x, max_x = left - FRAME_MARGIN, right + FRAME_MARGIN
    min_y, max_y = top - FRAME_MARGIN, bottom + FRAME_MARGIN
    for t in _iter(root, "text"):
        if t.get("x") is None:
            continue
        tx = num(t.get("x"))
        tw = num(t.get("textLength")) if t.get("textLength") else 0.0
        min_x = min(min_x, tx - 4)
        max_x = max(max_x, tx + tw + 4)
    width = math.ceil(max_x - min_x)
    height = math.ceil(max_y - min_y)
    root.set("viewBox", f"{fmt(min_x)} {fmt(min_y)} {fmt(width)} {fmt(height)}")
    root.set("width", f"{fmt(width)}px")
    root.set("height", f"{fmt(height)}px")
    root.set("style", f"width:{fmt(width)}px;height:{fmt(height)}px;background:#FFFFFF;")
    root.set("data-pres-formatted", "1")

    background = ET.Element(S + "rect", {
        "id": "pres-background", "x": fmt(min_x), "y": fmt(min_y),
        "width": fmt(width), "height": fmt(height), "fill": "#FFFFFF", "stroke": "none",
    })
    root.insert(0, background)
    frame = ET.SubElement(root, S + "g", {
        "id": "pres-frame", "fill": "none", "stroke": FRAME_INK, "stroke-width": FRAME_WIDTH,
    })
    ET.SubElement(frame, S + "rect", {
        "x": fmt(left), "y": fmt(top), "width": fmt(right - left), "height": fmt(bottom - top),
    })
    ET.SubElement(frame, S + "line", {
        "x1": fmt(left), "x2": fmt(right), "y1": fmt(header), "y2": fmt(header),
    })
    tree.write(svg_path, encoding="utf-8", xml_declaration=False)
    return width, height


def cmd_render(args) -> int:
    jar = resolve_jar(args.plantuml_jar)
    project = project_data()
    manifest = load_manifest()
    entries = manifest.get("use_cases", [])
    if args.key:
        entries = [e for e in entries if e["key"] in set(args.key)]
        if len(entries) != len(set(args.key)):
            raise SystemExit("Unknown key(s): " + ", ".join(sorted(set(args.key) - {e['key'] for e in entries})))
    elif not args.all:
        raise SystemExit("Use --all or --key KEY.")
    failures = 0
    rendered = 0
    for entry in entries:
        if entry["final_status"] in STATUS_BLOCKED:
            print(f"SKIP   {entry['key']}: {entry['final_status']}")
            continue
        source = ROOT / entry["source"]
        svg_target = ROOT / entry["svg"]
        try:
            produced = run_plantuml(jar, source, svg_target.parent)
            if produced != svg_target:
                produced.replace(svg_target)
            width, height = format_svg(svg_target)
            rendered += 1
            print(f"OK     {entry['key']:<34} {entry['svg']}  ({fmt(width)} x {fmt(height)})")
        except Exception as exc:  # noqa: BLE001 - report every failure
            failures += 1
            print(f"FAIL   {entry['key']}: {exc}")
    print(f"\nRendered {rendered} diagram(s); {failures} failure(s).")
    return 1 if failures else 0


# --------------------------------------------------------------------------- #
# layout check (visual QA aid): text overlapping connectors, shapes or text
# --------------------------------------------------------------------------- #
def _seg_hits_box(x1, y1, x2, y2, box) -> bool:
    bx1, by1, bx2, by2 = box
    if abs(x1 - x2) < 0.01:  # vertical
        return bx1 < x1 < bx2 and max(min(y1, y2), by1) < min(max(y1, y2), by2)
    if abs(y1 - y2) < 0.01:  # horizontal
        return by1 < y1 < by2 and max(min(x1, x2), bx1) < min(max(x1, x2), bx2)
    return False


def layout_issues(svg_path: Path) -> list[str]:
    root = ET.parse(svg_path).getroot()
    texts = []
    for t in root.iter(S + "text"):
        content = (t.text or "").replace(" ", " ").strip()
        if not content or t.get("x") is None:
            continue
        fs = num(t.get("font-size", "14"))
        x = num(t.get("x")); y = num(t.get("y"))
        w = num(t.get("textLength")) if t.get("textLength") else len(content) * fs * 0.5
        texts.append((content, (x + 0.5, y - 0.74 * fs, x + w - 0.5, y + 0.3 * fs)))
    vb = [num(v) for v in root.get("viewBox").split()]
    frame = None
    for g in root.iter(S + "g"):
        if g.get("id") == "pres-frame":
            frame = g
    frame_children = set(frame) if frame is not None else set()
    segments = []
    for line in root.iter(S + "line"):
        if line in frame_children:
            continue
        x1, x2, y1, y2 = (num(line.get(a)) for a in ("x1", "x2", "y1", "y2"))
        if abs(x1 - x2) < 0.01 and abs(y2 - y1) >= 0.6 * vb[3]:
            continue  # swimlane border
        segments.append((x1, y1, x2, y2))
    for pl in root.iter(S + "polyline"):
        pts = [num(v) for v in re.split(r"[\s,]+", pl.get("points", "").strip()) if v]
        xs, ys = pts[0::2], pts[1::2]
        segments.append(("box", min(xs), min(ys), max(xs), max(ys)))
    shapes = []
    for r in root.iter(S + "rect"):
        if r.get("rx"):
            x, y = num(r.get("x")), num(r.get("y"))
            shapes.append(("action", (x, y, x + num(r.get("width")), y + num(r.get("height")))))
    for p in root.iter(S + "polygon"):
        pts = [num(v) for v in re.split(r"[\s,]+", p.get("points", "").strip()) if v]
        xs, ys = pts[0::2], pts[1::2]
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        hw, hh = (max(xs) - min(xs)) / 2, (max(ys) - min(ys)) / 2
        shapes.append(("diamond", (cx - hw * 0.5, cy - hh * 0.5, cx + hw * 0.5, cy + hh * 0.5)))
    for e in root.iter(S + "ellipse"):
        cx, cy, rx = num(e.get("cx")), num(e.get("cy")), num(e.get("rx"))
        shapes.append(("node", (cx - rx, cy - rx, cx + rx, cy + rx)))
    issues = []
    for content, box in texts:
        for seg in segments:
            if seg[0] == "box":
                _, a, b, c, d = seg
                if a < box[2] and box[0] < c and b < box[3] and box[1] < d:
                    issues.append(f"text '{content}' touches an arrowhead")
            elif _seg_hits_box(*seg, box):
                issues.append(f"text '{content}' is crossed by a flow line")
        for kind, sb in shapes:
            inter = sb[0] < box[2] and box[0] < sb[2] and sb[1] < box[3] and box[1] < sb[3]
            inside = sb[0] <= box[0] and box[2] <= sb[2] and sb[1] <= box[1] and box[3] <= sb[3]
            if inter and not (kind == "action" and inside):
                issues.append(f"text '{content}' overlaps a {kind}")
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i][1], texts[j][1]
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                issues.append(f"text '{texts[i][0]}' overlaps text '{texts[j][0]}'")
    return sorted(set(issues))


# --------------------------------------------------------------------------- #
# validate
# --------------------------------------------------------------------------- #
def validate_svg(path: Path, entry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"{entry['key']}: SVG is not valid XML ({exc})"]
    vb = [v for v in re.split(r"[\s,]+", root.get("viewBox", "").strip()) if v]
    if len(vb) != 4 or num(vb[2]) <= 0 or num(vb[3]) <= 0:
        errors.append(f"{entry['key']}: SVG viewBox missing or invalid")
    if root.get("data-pres-formatted") != "1":
        errors.append(f"{entry['key']}: SVG was not post-processed by the renderer")
    ids = {e.get("id") for e in root.iter()}
    for needed in ("pres-frame", "pres-background"):
        if needed not in ids:
            errors.append(f"{entry['key']}: SVG lacks {needed}")
    fonts = {t.get("font-family") for t in root.iter(S + "text")}
    if fonts - {FONT}:
        errors.append(f"{entry['key']}: unexpected font(s) {sorted(f for f in fonts if f)}")
    if any(True for _ in root.iter(S + "foreignObject")) or any(True for _ in root.iter(S + "image")):
        errors.append(f"{entry['key']}: SVG contains foreignObject/image content")
    texts = {re.sub(r"\s+", " ", (t.text or "")).strip() for t in root.iter(S + "text")}
    if entry["name"] in texts or entry["display_id"] in texts:
        errors.append(f"{entry['key']}: a title/ID appears inside the diagram")
    for issue in layout_issues(path):
        errors.append(f"{entry['key']}: layout: {issue}")
    return errors


def cmd_validate(args) -> int:
    project = project_data()
    concrete = [uc for uc in project.use_cases if not uc.get("abstract")]
    abstract = [uc for uc in project.use_cases if uc.get("abstract")]
    by_key = {uc["key"]: uc for uc in concrete}
    manifest = load_manifest()
    entries = manifest.get("use_cases", [])
    errors: list[str] = []
    warnings: list[str] = []

    if len(concrete) != EXPECTED_CONCRETE:
        errors.append(f"Expected {EXPECTED_CONCRETE} concrete use cases, repository has {len(concrete)}")
    keys = [e.get("key") for e in entries]
    for key, count in Counter(keys).items():
        if count > 1:
            errors.append(f"Duplicate manifest entry: {key}")
    missing = sorted(set(by_key) - set(keys))
    extra = sorted(set(keys) - set(by_key))
    for key in missing:
        errors.append(f"Concrete use case missing from manifest: {key}")
    for key in extra:
        errors.append(f"Manifest entry is not a concrete use case: {key}")

    tracked_files: set[Path] = set()
    for entry in entries:
        key = entry.get("key")
        if key not in by_key:
            continue
        uc = by_key[key]
        for field in MANIFEST_FIELDS:
            if field not in entry:
                errors.append(f"{key}: manifest field '{field}' missing")
        if entry.get("display_id") != uc["_display_id"]:
            errors.append(f"{key}: display_id {entry.get('display_id')} != {uc['_display_id']}")
        if entry.get("name") != uc["name"]:
            errors.append(f"{key}: name differs from YAML")
        folder = domain_folder(project, uc)
        source = ROOT / entry["source"]
        svg = ROOT / entry["svg"]
        expected_source = ACTIVITY_DIR / folder / "source" / f"{key}.puml"
        expected_svg = ACTIVITY_DIR / folder / "svg" / f"{key}.svg"
        if source != expected_source or svg != expected_svg:
            errors.append(f"{key}: paths must be {expected_source.relative_to(ROOT)} and {expected_svg.relative_to(ROOT)}")
        tracked_files.update({expected_source, expected_svg})
        blocked = entry.get("final_status") in STATUS_BLOCKED
        if blocked:
            if not entry.get("blocked_reason"):
                errors.append(f"{key}: blocked entry needs blocked_reason")
            if svg.exists():
                errors.append(f"{key}: blocked use case must not have a final-looking SVG")
            if source.exists():
                errors.append(f"{key}: blocked use case must not have a committed source")
            continue
        if not source.exists():
            errors.append(f"{key}: source missing {entry['source']}")
            continue
        if not svg.exists():
            errors.append(f"{key}: SVG missing {entry['svg']}")
        text = source.read_text(encoding="utf-8")
        if not text.lstrip().startswith("@startuml") or "@enduml" not in text:
            errors.append(f"{key}: source must start with @startuml and end with @enduml")
        if STYLE_INCLUDE not in text:
            errors.append(f"{key}: source must contain '{STYLE_INCLUDE}'")
        if FORBIDDEN_DIRECTIVES.search(text):
            errors.append(f"{key}: title/caption/header/footer/legend directives are not allowed")
        if key not in text or uc["_display_id"] not in text:
            errors.append(f"{key}: header comment must name the semantic key and display ID")
        if key != "UC-SIGN-IN" and LOGIN_ACTION.search(text):
            errors.append(f"{key}: Log In must not be modelled outside UC-SIGN-IN")
        parsed = parse_source(text)
        if parsed["plain_lanes"]:
            errors.append(f"{key}: declare lanes with an alias and $lane_title(...)")
        lane_names = set(parsed["lanes"].values())
        if lane_names - ALLOWED_LANES:
            errors.append(f"{key}: unsupported lane(s) {sorted(lane_names - ALLOWED_LANES)}")
        if "System" not in lane_names:
            errors.append(f"{key}: a System partition is required")
        if len(re.findall(r"^\s*start\s*$", text, re.M)) != 1:
            errors.append(f"{key}: exactly one initial node (start) expected")
        if not re.search(r"^\s*(stop|end)\s*$", text, re.M):
            errors.append(f"{key}: no activity final node")
        if re.search(r"^\s*(fork|split)\b", text, re.M):
            warnings.append(f"{key}: fork/split used - confirm true concurrency")
        for action in parsed["actions"]:
            if not action["refs"]:
                errors.append(f"{key}: action without trace reference: '{action['text']}'")
            for ref in action["refs"]:
                if not valid_ref(ref, uc):
                    errors.append(f"{key}: invalid trace reference [{ref}] on '{action['text']}'")
        for ref in parsed["guard_refs"]:
            if not valid_ref(ref, uc):
                errors.append(f"{key}: guard refers to unknown {ref}")
        covered = {r for a in parsed["actions"] for r in a["refs"]} | set(parsed["guard_refs"])
        for n in range(1, len(uc.get("normal_flow") or []) + 1):
            if f"NF{n}" not in covered:
                errors.append(f"{key}: normal-flow step NF{n} is not traced to any action")
        for flow in uc.get("alternative_flows") or []:
            if not any(r == flow["id"] or r.startswith(flow["id"] + ".") for r in covered):
                errors.append(f"{key}: alternative flow {flow['id']} is not represented")
        for exc in uc.get("exceptions") or []:
            if exc["id"] not in covered:
                errors.append(f"{key}: exception {exc['id']} is not represented")
        if svg.exists():
            errors.extend(validate_svg(svg, entry))

    for path in sorted([*ACTIVITY_DIR.glob("*/*"), *ACTIVITY_DIR.glob("*/*/*")]):
        if path.parts[-2] == "_shared" or path.parent.name == "_shared":
            continue
        if path.suffix in (".puml", ".svg", ".png") and path not in tracked_files:
            errors.append(f"Unexpected extra file: {path.relative_to(ROOT)}")

    for warning in warnings:
        print(f"[WARN]  {warning}")
    for error in errors:
        print(f"[ERROR] {error}")
    counts = Counter(e.get("final_status") for e in entries)
    print(f"Concrete use cases: {len(concrete)} (abstract excluded: {len(abstract)})")
    for status, count in sorted(counts.items()):
        print(f"  {status}: {count}")
    print("Validation " + ("failed" if errors else "passed") + f": {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


# --------------------------------------------------------------------------- #
# status / report
# --------------------------------------------------------------------------- #
def domain_totals(entries, project):
    totals: "OrderedDict[str, Counter]" = OrderedDict()
    for group in project.groups.values():
        totals[group["folder"]] = Counter()
    for entry in entries:
        folder = Path(entry["source"]).parts[2]
        c = totals.setdefault(folder, Counter())
        c["expected"] += 1
        status = entry["final_status"]
        if status == STATUS_BLOCKED[0]:
            c["blocked_conflict"] += 1
        elif status == STATUS_BLOCKED[1]:
            c["blocked_spec"] += 1
        else:
            c["puml"] += int((ROOT / entry["source"]).exists())
            c["svg"] += int((ROOT / entry["svg"]).exists())
            c["passed"] += int(status == "ready-for-peer-review")
            c["needs_review"] += int(status == "needs-manual-review")
    return totals


def cmd_status(args) -> int:
    project = project_data()
    entries = load_manifest().get("use_cases", [])
    totals = domain_totals(entries, project)
    print(f"{'domain':<28}{'expected':>9}{'puml':>6}{'svg':>6}{'passed':>8}{'review':>8}{'conflict':>10}{'spec':>6}")
    grand = Counter()
    for folder, c in totals.items():
        grand.update(c)
        print(f"{folder:<28}{c['expected']:>9}{c['puml']:>6}{c['svg']:>6}{c['passed']:>8}{c['needs_review']:>8}{c['blocked_conflict']:>10}{c['blocked_spec']:>6}")
    print(f"{'TOTAL':<28}{grand['expected']:>9}{grand['puml']:>6}{grand['svg']:>6}{grand['passed']:>8}{grand['needs_review']:>8}{grand['blocked_conflict']:>10}{grand['blocked_spec']:>6}")
    return 0


def _md_escape(text: Any) -> str:
    return str(text if text is not None else "").replace("|", "\\|").replace("\n", " ")


def cmd_report(args) -> int:
    project = project_data()
    manifest = load_manifest()
    entries = manifest.get("use_cases", [])
    by_key = {uc["key"]: uc for uc in project.use_cases}
    totals = domain_totals(entries, project)
    grand = Counter()
    for c in totals.values():
        grand.update(c)
    meta = manifest.get("generation", {})

    gen = ["# Activity Diagram Generation Report", "",
           "Generated by `py scripts/activity_diagrams.py report` from `diagrams/activity/manifest.yml`.", ""]
    for k in ("date", "plantuml", "renderer", "source_of_truth"):
        if k in meta:
            gen.append(f"- **{k.replace('_', ' ').capitalize()}:** {meta[k]}")
    gen += ["", "## Totals", "",
            "| Measure | Count |", "|---|---:|",
            f"| Expected concrete use cases | {grand['expected']} |",
            f"| Generated PlantUML sources | {grand['puml']} |",
            f"| Generated SVG files | {grand['svg']} |",
            f"| Passed all review gates (awaiting peer and leader approval) | {grand['passed']} |",
            f"| Generated, needs manual review before approval | {grand['needs_review']} |",
            f"| Blocked — requirement conflict | {grand['blocked_conflict']} |",
            f"| Blocked — insufficient specification | {grand['blocked_spec']} |",
            f"| Render failures | {meta.get('render_failures', 0)} |",
            f"| Missing | {grand['expected'] - grand['puml'] - grand['blocked_conflict'] - grand['blocked_spec']} |",
            f"| Unexpected extra files | {meta.get('extra_files', 0)} |",
            "", "## Totals per domain", "",
            "| Domain | Expected | PlantUML | SVG | Passed gates | Needs manual review | Blocked (conflict) | Blocked (specification) |",
            "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for folder, c in totals.items():
        gen.append(f"| {folder} | {c['expected']} | {c['puml']} | {c['svg']} | {c['passed']} | {c['needs_review']} | {c['blocked_conflict']} | {c['blocked_spec']} |")
    gen += ["", "## Use cases", "",
            "| ID | Semantic key | Name | Assignee | Source | SVG | Generation | Final status |",
            "|---|---|---|---|---|---|---|---|"]
    for e in entries:
        src = e["source"] if (ROOT / e["source"]).exists() else "—"
        svg = e["svg"] if (ROOT / e["svg"]).exists() else "—"
        gen.append(f"| {e['display_id']} | `{e['key']}` | {_md_escape(e['name'])} | {_md_escape(e['assignee'])} | "
                   f"{'`'+src+'`' if src != '—' else src} | {'`'+svg+'`' if svg != '—' else svg} | "
                   f"{e['generation_status']} | {e['final_status']} |")
    for extra in manifest.get("landscape_exceptions", []) or []:
        gen.append(f"\nLandscape exception: {extra}")
    (ROOT / "docs" / "activity-diagram-generation-report.md").write_text("\n".join(gen) + "\n", encoding="utf-8")

    rev = ["# Activity Diagram Review Report", "",
           "Generated by `py scripts/activity_diagrams.py report` from `diagrams/activity/manifest.yml`.",
           "Every expected concrete use case has one row. Review gates: traceability (every action and guard",
           "traced to the Use Case YAML or a referenced Business Rule), UML (one initial node, guarded decisions,",
           "merge before re-entry, correct final nodes, responsibility partitions) and visual QA (rendered SVG",
           "inspected for clipping, overlap, borders, guard legibility, arrow direction, font and title).", "",
           "`ready-for-peer-review` means all automated and AI review gates passed; peer review and team-leader",
           "acceptance are still required by the Definition of Done in `docs/activity-diagram-guideline.md`.", "",
           "The Audit column is the result of the element-by-element audit in",
           "`docs/activity-diagram-audit-report.md` (APPROVED, REQUEST CHANGES or BLOCKED).", "",
           "| ID | Semantic key | Traceability | UML | Visual | Audit | Final status | Notes / blocked reason |",
           "|---|---|---|---|---|---|---|---|"]
    for e in entries:
        notes = e.get("blocked_reason") or e.get("review_notes") or ""
        rev.append(f"| {e['display_id']} | `{e['key']}` | {e['traceability_status']} | {e['uml_review_status']} | "
                   f"{e['visual_review_status']} | {e.get('audit_status', '')} | {e['final_status']} | {_md_escape(notes)} |")
    blocked = [e for e in entries if e["final_status"] in STATUS_BLOCKED]
    if blocked:
        rev += ["", "## Blocked use cases — questions for BA/PO", ""]
        for e in blocked:
            rev.append(f"### {e['display_id']} `{e['key']}` — {e['final_status']}")
            rev.append("")
            rev.append(f"- **Reason:** {e['blocked_reason']}")
            for q in e.get("questions", []) or []:
                rev.append(f"- **Question:** {q}")
            rev.append("")
    observations = [e for e in entries if e.get("observations")]
    if observations:
        rev += ["", "## Specification observations (non-blocking)", ""]
        for e in observations:
            for obs in e["observations"]:
                rev.append(f"- {e['display_id']} `{e['key']}`: {obs}")
    for section in manifest.get("review_sections", []) or []:
        rev += ["", f"## {section['title']}", "", section["body"].rstrip()]
    (ROOT / "docs" / "activity-diagram-review-report.md").write_text("\n".join(rev) + "\n", encoding="utf-8")
    print("Wrote docs/activity-diagram-generation-report.md and docs/activity-diagram-review-report.md")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    render = sub.add_parser("render", help="Render PlantUML sources to post-processed SVG.")
    render.add_argument("--key", action="append", help="Semantic key to render (repeatable).")
    render.add_argument("--all", action="store_true", help="Render every non-blocked manifest entry.")
    render.add_argument("--plantuml-jar", help="Path to plantuml.jar.")
    sub.add_parser("validate", help="Validate manifest, sources, traceability and SVG files.")
    sub.add_parser("status", help="Print totals per domain.")
    sub.add_parser("report", help="Regenerate the generation and review reports.")
    args = parser.parse_args(argv)
    return {"render": cmd_render, "validate": cmd_validate, "status": cmd_status, "report": cmd_report}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
