from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any, Iterable

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

from .loader import ProjectData


def _format_date(value: Any) -> str:
    if isinstance(value, date):
        return value.strftime("%d/%m/%Y")
    text = str(value or "")
    try:
        return date.fromisoformat(text).strftime("%d/%m/%Y")
    except ValueError:
        return text


def _escape_markdown(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", "<br>")


def _actor_text(use_case: dict[str, Any]) -> str:
    actors = [use_case["primary_actor"], *(use_case.get("secondary_actors") or [])]
    return ", ".join(dict.fromkeys(actors))


def _use_case_id(use_case: dict[str, Any]) -> str:
    return str(use_case["_display_id"])


def _business_rule_ids(project: ProjectData, use_case: dict[str, Any]) -> str:
    keys = use_case.get("business_rules", []) or []
    return ", ".join(project.business_rules[key]["_display_id"] for key in keys) or "N/A"


def _numbered(items: Iterable[Any]) -> str:
    values = list(items or [])
    if not values:
        return "N/A"
    return "\n".join(f"{index}. {item}" for index, item in enumerate(values, start=1))


def _normal_flow_text(use_case: dict[str, Any]) -> str:
    return "\n".join(
        f"{index}. {step['actor']}: {step['action']}"
        for index, step in enumerate(use_case.get("normal_flow", []), start=1)
    ) or "N/A"


def _alternative_flow_text(use_case: dict[str, Any]) -> str:
    flows = use_case.get("alternative_flows", []) or []
    if not flows:
        return "N/A"
    parts: list[str] = []
    for index, flow in enumerate(flows, start=1):
        if isinstance(flow, str):
            parts.append(f"AF-{index:02d}: {flow}")
            continue
        heading = f"{flow.get('id', 'AF')}: {flow.get('condition', '')}".strip()
        steps = flow.get("steps", []) or []
        parts.append(heading + ("\n" + _numbered(steps) if steps else ""))
    return "\n\n".join(parts)


def _exception_text(use_case: dict[str, Any]) -> str:
    exceptions = use_case.get("exceptions", []) or []
    if not exceptions:
        return "N/A"
    lines: list[str] = []
    for index, item in enumerate(exceptions, start=1):
        if isinstance(item, str):
            lines.append(f"EX-{index:02d}: {item}")
        else:
            lines.append(f"{item.get('id', 'EX')}: {item.get('description', '')}")
    return "\n".join(lines)


def _detail_fields(project: ProjectData, use_case: dict[str, Any]) -> list[tuple[str, str]]:
    return [
        ("Trigger", str(use_case.get("trigger") or "N/A")),
        ("Description", str(use_case.get("description") or "N/A")),
        ("Preconditions", _numbered(use_case.get("preconditions", []))),
        ("Postconditions", _numbered(use_case.get("postconditions", []))),
        ("Normal Flow", _normal_flow_text(use_case)),
        ("Alternative Flows", _alternative_flow_text(use_case)),
        ("Exceptions", _exception_text(use_case)),
        ("Priority", str(use_case.get("priority") or "N/A")),
        ("Frequency of Use", str(use_case.get("frequency_of_use") or "N/A")),
        ("Business Rules", _business_rule_ids(project, use_case)),
        ("Other Information", str(use_case.get("other_information") or "N/A")),
        ("Assumptions", _numbered(use_case.get("assumptions", []))),
    ]


def _generate_markdown(project: ProjectData, use_cases: list[dict[str, Any]], output_dir: Path) -> list[Path]:
    summary_lines = [
        "# Use Case List",
        "",
        "| ID | Use Case | Actors | Use Case Description |",
        "|---|---|---|---|",
    ]
    for use_case in use_cases:
        summary_lines.append(
            "| {id} | {name} | {actors} | {summary} |".format(
                id=_escape_markdown(_use_case_id(use_case)),
                name=_escape_markdown(use_case["name"]),
                actors=_escape_markdown(_actor_text(use_case)),
                summary=_escape_markdown(use_case["summary"]),
            )
        )

    details_lines = ["# Use Case Descriptions", ""]
    for use_case in use_cases:
        details_lines.extend(
            [
                f"## {_use_case_id(use_case)} - {use_case['name']}",
                "",
                "| Field | Value |",
                "|---|---|",
                f"| UC ID and Name | {_escape_markdown(_use_case_id(use_case))} - {_escape_markdown(use_case['name'])} |",
                f"| Created By | {_escape_markdown(use_case['created_by'])} |",
                f"| Date Created | {_escape_markdown(_format_date(use_case['date_created']))} |",
                f"| Primary Actor | {_escape_markdown(use_case['primary_actor'])} |",
                f"| Secondary Actors | {_escape_markdown(', '.join(use_case.get('secondary_actors', [])) or 'None')} |",
            ]
        )
        for label, value in _detail_fields(project, use_case):
            details_lines.append(f"| {_escape_markdown(label)} | {_escape_markdown(value)} |")
        details_lines.append("")

    summary_path = output_dir / "use-case-list.md"
    details_path = output_dir / "use-case-descriptions.md"
    mapping_path = output_dir / "id-mapping.md"
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    details_path.write_text("\n".join(details_lines) + "\n", encoding="utf-8")

    mapping_lines = [
        "# Generated ID Mapping",
        "",
        "## Use Cases",
        "",
        "| Generated ID | Semantic Key | Name | Order |",
        "|---|---|---|---|",
    ]
    for use_case in use_cases:
        mapping_lines.append(
            f"| {_use_case_id(use_case)} | `{use_case['key']}` | "
            f"{_escape_markdown(use_case['name'])} | {use_case['order']} |"
        )
    mapping_lines.extend(
        [
            "",
            "## Business Rules",
            "",
            "| Generated ID | Semantic Key | Description | Order |",
            "|---|---|---|---|",
        ]
    )
    for rule in project.business_rules.values():
        mapping_lines.append(
            f"| {rule['_display_id']} | `{rule['key']}` | "
            f"{_escape_markdown(rule['description'])} | {rule['order']} |"
        )
    mapping_path.write_text("\n".join(mapping_lines) + "\n", encoding="utf-8")
    return [summary_path, details_path, mapping_path]


def _set_cell_shading(cell, fill: str) -> None:
    cell_properties = cell._tc.get_or_add_tcPr()
    shading = cell_properties.find(qn("w:shd"))
    if shading is None:
        shading = OxmlElement("w:shd")
        cell_properties.append(shading)
    shading.set(qn("w:fill"), fill)


def _set_cell_text(cell, text: str, bold: bool = False, center: bool = False) -> None:
    cell.text = ""
    paragraph = cell.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.space_after = Pt(0)
    for line_number, line in enumerate(str(text).split("\n")):
        if line_number:
            paragraph.add_run().add_break()
        run = paragraph.add_run(line)
        run.bold = bold
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def _style_table(table) -> None:
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    for row in table.rows:
        for cell in row.cells:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def _generate_docx(project: ProjectData, use_cases: list[dict[str, Any]], output_dir: Path) -> Path:
    document = Document()
    section = document.sections[0]
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2)
    section.right_margin = Cm(2)

    normal_style = document.styles["Normal"]
    normal_style.font.name = "Times New Roman"
    normal_style.font.size = Pt(11)

    title = document.add_heading("II.5.2.2 Use Case Descriptions", level=1)
    title.style.font.name = "Times New Roman"

    summary_table = document.add_table(rows=1, cols=4)
    summary_table.style = "Table Grid"
    _style_table(summary_table)
    headers = ["ID", "Use Case", "Actors", "Use Case Description"]
    for index, header in enumerate(headers):
        _set_cell_text(summary_table.rows[0].cells[index], header, bold=True, center=True)
        _set_cell_shading(summary_table.rows[0].cells[index], "FCE4D6")
    widths = [Cm(1.5), Cm(4), Cm(4), Cm(7)]
    for use_case in use_cases:
        cells = summary_table.add_row().cells
        values = [_use_case_id(use_case), use_case["name"], _actor_text(use_case), use_case["summary"]]
        for index, value in enumerate(values):
            _set_cell_text(cells[index], value, center=index == 0)
            cells[index].width = widths[index]

    document.add_paragraph()

    for position, use_case in enumerate(use_cases):
        heading = document.add_heading(f"{_use_case_id(use_case)} - {use_case['name']}", level=2)
        heading.style.font.name = "Times New Roman"

        table = document.add_table(rows=3, cols=4)
        table.style = "Table Grid"
        _style_table(table)

        first_row = table.rows[0].cells
        _set_cell_text(first_row[0], "UC ID and Name", bold=True)
        merged = first_row[1].merge(first_row[3])
        _set_cell_text(merged, f"{_use_case_id(use_case)} - {use_case['name']}")

        second_row = table.rows[1].cells
        _set_cell_text(second_row[0], "Created By", bold=True)
        _set_cell_text(second_row[1], use_case["created_by"])
        _set_cell_text(second_row[2], "Date Created", bold=True)
        _set_cell_text(second_row[3], _format_date(use_case["date_created"]))

        third_row = table.rows[2].cells
        _set_cell_text(third_row[0], "Primary Actor", bold=True)
        _set_cell_text(third_row[1], use_case["primary_actor"])
        _set_cell_text(third_row[2], "Secondary Actors", bold=True)
        _set_cell_text(third_row[3], ", ".join(use_case.get("secondary_actors", [])) or "None")

        for label, value in _detail_fields(project, use_case):
            cells = table.add_row().cells
            _set_cell_text(cells[0], label, bold=True)
            merged_value = cells[1].merge(cells[3])
            _set_cell_text(merged_value, value)

        for row in table.rows:
            row.cells[0].width = Cm(3.7)
            for label_cell in [row.cells[0]]:
                _set_cell_shading(label_cell, "F2F2F2")

        if position < len(use_cases) - 1:
            document.add_page_break()

    output_path = output_dir / "use-case-descriptions.docx"
    document.save(output_path)
    return output_path


def _plantuml_alias(value: str) -> str:
    return "".join(character if character.isalnum() else "_" for character in value)


def _generate_plantuml(project: ProjectData, use_cases: list[dict[str, Any]], output_dir: Path) -> Path:
    used_actor_names = {
        actor
        for use_case in use_cases
        for actor in [use_case["primary_actor"], *(use_case.get("secondary_actors") or [])]
    }
    lines = [
        "@startuml",
        "left to right direction",
        "skinparam packageStyle rectangle",
        "skinparam actorStyle awesome",
        "",
    ]
    for actor_name in sorted(used_actor_names):
        lines.append(f'actor "{actor_name}" as ACT_{_plantuml_alias(actor_name)}')
    lines.extend(["", 'rectangle "Project Management System" {'])
    for use_case in use_cases:
        lines.append(
            f'  usecase "{_use_case_id(use_case)}\\n{use_case["name"]}" '
            f'as {_plantuml_alias(use_case["key"])}'
        )
    lines.append("}")
    lines.append("")
    for use_case in use_cases:
        use_case_alias = _plantuml_alias(use_case["key"])
        actors = [use_case["primary_actor"], *(use_case.get("secondary_actors") or [])]
        for actor_name in dict.fromkeys(actors):
            lines.append(f"ACT_{_plantuml_alias(actor_name)} --> {use_case_alias}")
    lines.extend(["", "@enduml", ""])

    output_path = output_dir / "use-case-diagram.puml"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def build_outputs(
    project: ProjectData,
    use_cases: list[dict[str, Any]],
    output_dir: Path,
    output_format: str,
) -> list[Path]:
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    generated: list[Path] = []

    if output_format in {"all", "markdown"}:
        generated.extend(_generate_markdown(project, use_cases, output_dir))
    if output_format in {"all", "docx"}:
        generated.append(_generate_docx(project, use_cases, output_dir))
    if output_format in {"all", "plantuml"}:
        generated.append(_generate_plantuml(project, use_cases, output_dir))
    return generated
