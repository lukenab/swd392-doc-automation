from __future__ import annotations

import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

from .loader import ProjectData


REQUIRED_FIELDS = [
    "key",
    "group",
    "order",
    "name",
    "summary",
    "created_by",
    "date_created",
    "primary_actor",
    "trigger",
    "description",
    "preconditions",
    "postconditions",
    "normal_flow",
    "priority",
    "frequency_of_use",
]

ALLOWED_PRIORITIES = {"Must Have", "Should Have", "Could Have", "Won't Have"}


def _non_empty(value: Any) -> bool:
    return value is not None and value != "" and value != []


def validate_project(project: ProjectData) -> list[str]:
    errors: list[str] = []

    if not project.groups:
        errors.append("groups.yml does not define any domains.")
    if not project.actors:
        errors.append("actors.yml does not define any actors.")
    if not project.business_rules:
        errors.append("business_rules.yml does not define any business rules.")
    if not project.use_cases:
        errors.append("No use case YAML files were found.")
        return errors

    keys = [str(uc.get("key", "")) for uc in project.use_cases]
    for duplicated_key, count in Counter(keys).items():
        if duplicated_key and count > 1:
            errors.append(f"Duplicate Use Case key: {duplicated_key}.")

    group_orders = [
        group.get("order")
        for group in project.groups.values()
        if isinstance(group.get("order"), int)
    ]
    for duplicated_order, count in Counter(group_orders).items():
        if count > 1:
            errors.append(f"Duplicate domain order: {duplicated_order}.")

    group_folders = [
        group.get("folder")
        for group in project.groups.values()
        if isinstance(group.get("folder"), str) and group.get("folder")
    ]
    for duplicated_folder, count in Counter(group_folders).items():
        if count > 1:
            errors.append(f"Duplicate domain folder: {duplicated_folder}.")

    for group_key, group in project.groups.items():
        if not re.fullmatch(r"[A-Z][A-Z0-9_]*", group_key):
            errors.append(f"Domain key '{group_key}' is invalid.")
        if not isinstance(group.get("order"), int):
            errors.append(f"{group_key}: domain order must be an integer.")
        if not _non_empty(group.get("name")):
            errors.append(f"{group_key}: missing domain name.")
        folder = group.get("folder")
        if not isinstance(folder, str) or not re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*", folder
        ):
            errors.append(
                f"{group_key}: folder must use lowercase kebab-case, such as task-management."
            )

    orders = [
        (uc.get("group"), uc.get("order"))
        for uc in project.use_cases
        if isinstance(uc.get("order"), int)
    ]
    for (group_key, duplicated_order), count in Counter(orders).items():
        if count > 1:
            errors.append(
                f"Duplicate Use Case order {duplicated_order} in domain '{group_key}'."
            )

    rule_orders = [
        (rule.get("group"), rule.get("order"))
        for rule in project.business_rules.values()
        if isinstance(rule.get("order"), int)
    ]
    for (group_key, duplicated_order), count in Counter(rule_orders).items():
        if count > 1:
            errors.append(
                f"Duplicate Business Rule order {duplicated_order} in domain '{group_key}'."
            )

    for rule_key, rule in project.business_rules.items():
        if not re.fullmatch(r"BR-[A-Z0-9]+(?:-[A-Z0-9]+)*", rule_key):
            errors.append(f"Business Rule key '{rule_key}' is invalid.")
        if not isinstance(rule.get("order"), int):
            errors.append(f"{rule_key}: order must be an integer.")
        if not rule.get("group"):
            errors.append(f"{rule_key}: missing group.")
        elif rule["group"] not in project.groups:
            errors.append(f"{rule_key}: unknown domain '{rule['group']}'.")
        if not _non_empty(rule.get("description")):
            errors.append(f"{rule_key}: missing description.")

    for use_case in project.use_cases:
        source = use_case.get("_source_file", "unknown file")
        use_case_key = str(use_case.get("key") or source)

        for field in REQUIRED_FIELDS:
            if not _non_empty(use_case.get(field)):
                errors.append(f"{use_case_key}: missing required field '{field}' ({source}).")

        if use_case.get("key") and not re.fullmatch(
            r"UC-[A-Z0-9]+(?:-[A-Z0-9]+)*", str(use_case["key"])
        ):
            errors.append(
                f"{use_case_key}: key must use semantic format such as UC-TASK-CREATE."
            )

        if use_case.get("key") and Path(str(source)).name != f"{use_case['key']}.yml":
            errors.append(
                f"{use_case_key}: file name must be {use_case['key']}.yml, got {source}."
            )

        group_key = use_case.get("group")
        if group_key and group_key not in project.groups:
            errors.append(f"{use_case_key}: unknown domain '{group_key}'.")
        elif group_key:
            actual_folder = Path(str(source)).parent.as_posix()
            expected_folder = str(project.groups[group_key]["folder"])
            if actual_folder != expected_folder:
                errors.append(
                    f"{use_case_key}: file must be inside use_cases/{expected_folder}/, "
                    f"got use_cases/{source}."
                )

        if use_case.get("order") is not None and not isinstance(use_case.get("order"), int):
            errors.append(f"{use_case_key}: order must be an integer.")

        primary_actor = use_case.get("primary_actor")
        if primary_actor and primary_actor not in project.actors:
            errors.append(f"{use_case_key}: unknown primary actor '{primary_actor}'.")

        secondary_actors = use_case.get("secondary_actors", []) or []
        if not isinstance(secondary_actors, list):
            errors.append(f"{use_case_key}: secondary_actors must be a list.")
        else:
            for actor in secondary_actors:
                if actor not in project.actors:
                    errors.append(f"{use_case_key}: unknown secondary actor '{actor}'.")

        priority = use_case.get("priority")
        if priority and priority not in ALLOWED_PRIORITIES:
            errors.append(
                f"{use_case_key}: priority '{priority}' is invalid. "
                f"Allowed: {', '.join(sorted(ALLOWED_PRIORITIES))}."
            )

        for list_field in [
            "preconditions",
            "postconditions",
            "normal_flow",
            "alternative_flows",
            "exceptions",
            "business_rules",
            "assumptions",
        ]:
            value = use_case.get(list_field, [])
            if value is not None and not isinstance(value, list):
                errors.append(f"{use_case_key}: '{list_field}' must be a list.")

        normal_flow = use_case.get("normal_flow", [])
        if isinstance(normal_flow, list):
            for step_number, step in enumerate(normal_flow, start=1):
                if not isinstance(step, dict) or not step.get("actor") or not step.get("action"):
                    errors.append(
                        f"{use_case_key}: normal_flow step {step_number} requires actor and action."
                    )
                elif step["actor"] not in project.actors and step["actor"] != "System":
                    errors.append(
                        f"{use_case_key}: normal_flow step {step_number} uses unknown actor "
                        f"'{step['actor']}'."
                    )

        alternative_flows = use_case.get("alternative_flows", []) or []
        if isinstance(alternative_flows, list):
            for flow_number, flow in enumerate(alternative_flows, start=1):
                if isinstance(flow, str):
                    continue
                if not isinstance(flow, dict):
                    errors.append(
                        f"{use_case_key}: alternative_flows item {flow_number} "
                        "must be a string or an object."
                    )
                    continue
                steps = flow.get("steps", []) or []
                if not flow.get("condition"):
                    errors.append(
                        f"{use_case_key}: alternative_flows item {flow_number} "
                        "requires condition."
                    )
                if not isinstance(steps, list):
                    errors.append(
                        f"{use_case_key}: alternative_flows item {flow_number} steps must be a list."
                    )

        exceptions = use_case.get("exceptions", []) or []
        if isinstance(exceptions, list):
            for exception_number, exception in enumerate(exceptions, start=1):
                if isinstance(exception, str):
                    continue
                if not isinstance(exception, dict) or not exception.get("description"):
                    errors.append(
                        f"{use_case_key}: exceptions item {exception_number} "
                        "must be a string or an object with description."
                    )

        for rule_id in use_case.get("business_rules", []) or []:
            if rule_id not in project.business_rules:
                errors.append(f"{use_case_key}: unknown Business Rule key '{rule_id}'.")

        created_date = use_case.get("date_created")
        if created_date and not isinstance(created_date, (str, date)):
            errors.append(f"{use_case_key}: date_created must be a date or ISO date string.")

    return errors
