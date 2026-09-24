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
        help="Thư mục chứa actors.yml, business_rules.yml và use_cases/.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="Kiểm tra tính hợp lệ và đồng bộ của dữ liệu.")
    subparsers.add_parser("list", help="Hiển thị danh sách Use Case.")

    build_parser = subparsers.add_parser("build", help="Sinh Markdown, DOCX và PlantUML.")
    build_parser.add_argument(
        "--format",
        choices=["all", "markdown", "docx", "plantuml"],
        default="all",
        help="Định dạng cần sinh. Mặc định: all.",
    )
    build_parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "output",
        help="Thư mục nhận kết quả.",
    )
    build_parser.add_argument(
        "--use-case",
        help="Chỉ sinh một Use Case, ví dụ UC-04. Bảng tổng hợp vẫn chứa Use Case được chọn.",
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
            print(f"  [OK] {use_case['id']} - {use_case['name']}")
        return 0

    if errors:
        print_errors(errors)
        print("Fix validation errors before listing or building outputs.")
        return 1

    if args.command == "list":
        print(f"{'ID':<8} {'Priority':<13} {'Primary Actor':<22} Name")
        print("-" * 82)
        for use_case in project.use_cases:
            print(
                f"{use_case['id']:<8} "
                f"{use_case['priority']:<13} "
                f"{use_case['primary_actor']:<22} "
                f"{use_case['name']}"
            )
        return 0

    selected_use_cases = project.use_cases
    if args.use_case:
        wanted = args.use_case.upper()
        selected_use_cases = [uc for uc in project.use_cases if uc["id"].upper() == wanted]
        if not selected_use_cases:
            print(f"Use Case not found: {args.use_case}", file=sys.stderr)
            return 2

    try:
        generated = build_outputs(
            project=project,
            use_cases=selected_use_cases,
            output_dir=args.output_dir,
            output_format=args.format,
        )
    except PermissionError as error:
        print(
            f"Cannot write output file: {error.filename}\n"
            "Close the file if it is open in Word/Google Drive, then run the build again.\n"
            "You can also generate into another folder with --output-dir.",
            file=sys.stderr,
        )
        return 1
    print(f"Build completed: {len(selected_use_cases)} use case(s).")
    for path in generated:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
