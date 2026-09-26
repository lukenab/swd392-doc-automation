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
    group_order_field: str = "order",
) -> None:
    """Sort items and assign stable presentation IDs, including child IDs."""
    groups = groups or {}

    def sort_key(item: dict[str, Any]) -> tuple[int, Any, int, Any, str]:
        group = groups.get(str(item.get("group", "")), {})
        group_order = group.get(group_order_field, group.get("order"))
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

    # Business Rules and legacy flat Use Case collections keep sequential IDs.
    if not any(item.get("parent") for item in items):
        for index, item in enumerate(items, start=1):
            item["_display_id"] = f"{prefix}-{index:02d}"
        return

    by_key = {str(item.get("key")): item for item in items if item.get("key")}
    children: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        parent = item.get("parent")
        if parent:
            children.setdefault(str(parent), []).append(item)

    ordered: list[dict[str, Any]] = []
    visited: set[str] = set()

    def visit(item: dict[str, Any], display_id: str) -> None:
        key = str(item.get("key", ""))
        if key in visited:
            return
        visited.add(key)
        item["_display_id"] = display_id
        ordered.append(item)
        for child_index, child in enumerate(children.get(key, []), start=1):
            visit(child, f"{display_id}.{child_index}")

    roots = [
        item
        for item in items
        if not item.get("parent") or str(item.get("parent")) not in by_key
    ]
    for root_index, root in enumerate(roots, start=1):
        visit(root, f"{prefix}-{root_index:02d}")

    # Keep invalid cycles visible so the validator can report them.
    for item in items:
        if str(item.get("key", "")) not in visited:
            visit(item, f"{prefix}-{len(roots) + 1:02d}")

    items[:] = ordered


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

    assign_display_ids(use_cases, "UC", groups, group_order_field="use_case_order")
    return ProjectData(
        data_dir=data_dir,
        groups=groups,
        actors=actors,
        business_rules=business_rules,
        use_cases=use_cases,
    )
