from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ProjectData:
    data_dir: Path
    actors: dict[str, dict[str, Any]]
    business_rules: dict[str, dict[str, Any]]
    use_cases: list[dict[str, Any]]


def _read_yaml(path: Path) -> Any:
    if not path.exists():
        raise ValueError(f"Missing required file: {path}")
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_project(data_dir: Path) -> ProjectData:
    data_dir = data_dir.resolve()
    actors_data = _read_yaml(data_dir / "actors.yml") or {}
    rules_data = _read_yaml(data_dir / "business_rules.yml") or {}

    actors = {
        item["name"]: item
        for item in actors_data.get("actors", [])
        if isinstance(item, dict) and item.get("name")
    }
    business_rules = {
        item["id"]: item
        for item in rules_data.get("business_rules", [])
        if isinstance(item, dict) and item.get("id")
    }

    use_case_dir = data_dir / "use_cases"
    if not use_case_dir.exists():
        raise ValueError(f"Missing use case directory: {use_case_dir}")

    use_cases: list[dict[str, Any]] = []
    for path in sorted(use_case_dir.glob("*.yml")):
        use_case = _read_yaml(path)
        if not isinstance(use_case, dict):
            raise ValueError(f"Use case file must contain a YAML object: {path}")
        use_case["_source_file"] = path.name
        use_cases.append(use_case)

    use_cases.sort(key=lambda item: str(item.get("id", "")))
    return ProjectData(
        data_dir=data_dir,
        actors=actors,
        business_rules=business_rules,
        use_cases=use_cases,
    )

