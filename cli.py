from __future__ import annotations

import argparse
import sys
from pathlib import Path

from usecase_tool.generator import build_outputs
from usecase_tool.loader import load_project
from usecase_tool.validator import validate_project


ROOT = Path(__file__).resolve().parent


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pms-usecase",
        description="Kiểm tra và sinh tài liệu Use Case từ dữ liệu YAML.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=ROOT / "data",
        help="Thư mục chứa groups.yml, actors.yml, business_rules.yml và use_cases/.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="Kiểm tra tính hợp lệ và đồng bộ của dữ liệu.")
    subparsers.add_parser("list", help="Hiển thị danh sách Use Case.")

    build_parser = subparsers.add_parser("build", help="Sinh Markdown, DOCX và PlantUML.")
    build_parser.add_argument(
        "--format",
        choices=["all", "markdown", "docx", "plantuml", "business-rules"],
        default="all",
        help=(
            "Định dạng cần sinh. Dùng business-rules để chỉ sinh bảng "
            "Business Rule dạng Markdown và DOCX. Mặc định: all."
        ),
    )
    build_parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "output",
        help="Thư mục nhận kết quả.",
    )
    build_parser.add_argument(
        "--use-case",
        help=(
            "Chỉ sinh một Use Case theo semantic key hoặc generated ID, "
            "ví dụ UC-TASK-CREATE hoặc UC-04."
        ),
    )
    build_parser.add_argument(
        "--diagram-dir",
        type=Path,
        help=(
            "Thư mục output của swd392-usecase-diagram-tool. "
            "Khi sinh DOCX, các PNG trong manifest.json sẽ được chèn vào tài liệu."
        ),
    )
    return parser


def print_errors(errors: list[str]) -> None:
    print(f"Validation failed: {len(errors)} error(s).")
    for error in errors:
        print(f"  [ERROR] {error}")


def main() -> int:
    args = create_parser().parse_args()
    try:
        project = load_project(args.data_dir)
    except (OSError, ValueError) as exc:
        print(f"Cannot load project data: {exc}", file=sys.stderr)
        return 2

    errors = validate_project(project)

    if args.command == "validate":
        if errors:
            print_errors(errors)
            return 1
        print(f"Validation completed: {len(project.use_cases)} use case(s), 0 errors.")
        for use_case in project.use_cases:
            print(
                f"  [OK] {use_case['_display_id']} - {use_case['name']} "
                f"({use_case['key']})"
            )
        return 0

    if errors:
        print_errors(errors)
        print("Fix validation errors before listing or building outputs.")
        return 1

    if args.command == "list":
        print(f"{'ID':<8} {'Domain':<22} {'Semantic Key':<32} {'Priority':<13} Name")
        print("-" * 116)
        for use_case in project.use_cases:
            print(
                f"{use_case['_display_id']:<8} "
                f"{project.groups[use_case['group']]['name']:<22} "
                f"{use_case['key']:<32} "
                f"{use_case['priority']:<13} "
                f"{use_case['name']}"
            )
        return 0

    selected_use_cases = project.use_cases
    if args.use_case:
        wanted = args.use_case.upper()
        matches = [
            uc
            for uc in project.use_cases
            if uc["key"].upper() == wanted or uc["_display_id"].upper() == wanted
        ]
        if not matches:
            print(f"Use Case not found: {args.use_case}", file=sys.stderr)
            return 2
        selected_keys = {item["key"] for item in matches}
        changed = True
        while changed:
            changed = False
            for use_case in project.use_cases:
                if use_case.get("parent") in selected_keys and use_case["key"] not in selected_keys:
                    selected_keys.add(use_case["key"])
                    changed = True
        selected_use_cases = [
            use_case for use_case in project.use_cases if use_case["key"] in selected_keys
        ]

    try:
        generated = build_outputs(
            project=project,
            use_cases=selected_use_cases,
            output_dir=args.output_dir,
            output_format=args.format,
            diagram_dir=args.diagram_dir,
        )
    except PermissionError as error:
        print(
            f"Cannot write output file: {error.filename}\n"
            "Close the file if it is open in Word/Google Drive, then run the build again.\n"
            "You can also generate into another folder with --output-dir.",
            file=sys.stderr,
        )
        return 1
    except (OSError, ValueError) as error:
        print(f"Cannot build output: {error}", file=sys.stderr)
        return 1
    print(f"Build completed: {len(selected_use_cases)} use case(s).")
    for path in generated:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
