from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ProjectData:
    data_dir: Path
    groups: dict[str, dict[str, Any]]
    actors: dict[str, dict[str, Any]]
    business_rules: dict[str, dict[str, Any]]
    use_cases: list[dict[str, Any]]


def _read_yaml(path: Path) -> Any:
    if not path.exists():
        raise ValueError(f"Missing required file: {path}")
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def assign_display_ids(
    items: list[dict[str, Any]],
    prefix: str,
    groups: dict[str, dict[str, Any]] | None = None,
) -> None:
    """Sort items by order and assign presentation-only sequential IDs."""
    groups = groups or {}

    def sort_key(item: dict[str, Any]) -> tuple[int, Any, int, Any, str]:
        group = groups.get(str(item.get("group", "")), {})
        group_order = group.get("order")
        order = item.get("order")
        group_rank = group_order if isinstance(group_order, int) else str(group_order)
        item_rank = order if isinstance(order, int) else str(order)
        return (
            0 if isinstance(group_order, int) else 1,
            group_rank,
            0 if isinstance(order, int) else 1,
            item_rank,
            str(item.get("key", "")),
        )

    items.sort(key=sort_key)
    for index, item in enumerate(items, start=1):
        item["_display_id"] = f"{prefix}-{index:02d}"


def load_project(data_dir: Path) -> ProjectData:
    data_dir = data_dir.resolve()
    groups_data = _read_yaml(data_dir / "groups.yml") or {}
    actors_data = _read_yaml(data_dir / "actors.yml") or {}
    rules_data = _read_yaml(data_dir / "business_rules.yml") or {}

    group_items = [
        item
        for item in groups_data.get("groups", [])
        if isinstance(item, dict) and item.get("key")
    ]
    group_items.sort(
        key=lambda item: (
            0 if isinstance(item.get("order"), int) else 1,
            item.get("order") if isinstance(item.get("order"), int) else str(item.get("order")),
            item["key"],
        )
    )
    groups = {item["key"]: item for item in group_items}

    actors = {
        item["name"]: item
        for item in actors_data.get("actors", [])
        if isinstance(item, dict) and item.get("name")
    }
    rule_items = [
        item
        for item in rules_data.get("business_rules", [])
        if isinstance(item, dict) and item.get("key")
    ]
    assign_display_ids(rule_items, "BR", groups)
    business_rules = {item["key"]: item for item in rule_items}

    use_case_dir = data_dir / "use_cases"
    if not use_case_dir.exists():
        raise ValueError(f"Missing use case directory: {use_case_dir}")

    use_cases: list[dict[str, Any]] = []
    for path in sorted(use_case_dir.rglob("*.yml")):
        use_case = _read_yaml(path)
        if not isinstance(use_case, dict):
            raise ValueError(f"Use case file must contain a YAML object: {path}")
        use_case["_source_file"] = str(path.relative_to(use_case_dir))
        use_cases.append(use_case)

    assign_display_ids(use_cases, "UC", groups)
    return ProjectData(
        data_dir=data_dir,
        groups=groups,
        actors=actors,
        business_rules=business_rules,
        use_cases=use_cases,
    )
