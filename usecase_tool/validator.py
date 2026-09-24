from __future__ import annotations

import re
from collections import Counter
from datetime import date
from typing import Any

from .loader import ProjectData


REQUIRED_FIELDS = [
    "id",
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

    if not project.actors:
        errors.append("actors.yml does not define any actors.")
    if not project.business_rules:
        errors.append("business_rules.yml does not define any business rules.")
    if not project.use_cases:
        errors.append("No use case YAML files were found.")
        return errors

    ids = [str(uc.get("id", "")) for uc in project.use_cases]
    for duplicated_id, count in Counter(ids).items():
        if duplicated_id and count > 1:
            errors.append(f"Duplicate Use Case ID: {duplicated_id}.")

    for use_case in project.use_cases:
        source = use_case.get("_source_file", "unknown file")
        use_case_id = str(use_case.get("id") or source)

        for field in REQUIRED_FIELDS:
            if not _non_empty(use_case.get(field)):
                errors.append(f"{use_case_id}: missing required field '{field}' ({source}).")

        if use_case.get("id") and not re.fullmatch(r"UC-\d{2,}", str(use_case["id"])):
            errors.append(f"{use_case_id}: ID must match UC-01, UC-02, ...")

        primary_actor = use_case.get("primary_actor")
        if primary_actor and primary_actor not in project.actors:
            errors.append(f"{use_case_id}: unknown primary actor '{primary_actor}'.")

        secondary_actors = use_case.get("secondary_actors", []) or []
        if not isinstance(secondary_actors, list):
            errors.append(f"{use_case_id}: secondary_actors must be a list.")
        else:
            for actor in secondary_actors:
                if actor not in project.actors:
                    errors.append(f"{use_case_id}: unknown secondary actor '{actor}'.")

        priority = use_case.get("priority")
        if priority and priority not in ALLOWED_PRIORITIES:
            errors.append(
                f"{use_case_id}: priority '{priority}' is invalid. "
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
                errors.append(f"{use_case_id}: '{list_field}' must be a list.")

        normal_flow = use_case.get("normal_flow", [])
        if isinstance(normal_flow, list):
            for step_number, step in enumerate(normal_flow, start=1):
                if not isinstance(step, dict) or not step.get("actor") or not step.get("action"):
                    errors.append(
                        f"{use_case_id}: normal_flow step {step_number} requires actor and action."
                    )
                elif step["actor"] not in project.actors and step["actor"] != "System":
                    errors.append(
                        f"{use_case_id}: normal_flow step {step_number} uses unknown actor "
                        f"'{step['actor']}'."
                    )

        alternative_flows = use_case.get("alternative_flows", []) or []
        if isinstance(alternative_flows, list):
            for flow_number, flow in enumerate(alternative_flows, start=1):
                if isinstance(flow, str):
                    continue
                if not isinstance(flow, dict):
                    errors.append(
                        f"{use_case_id}: alternative_flows item {flow_number} "
                        "must be a string or an object."
                    )
                    continue
                steps = flow.get("steps", []) or []
                if not flow.get("condition"):
                    errors.append(
                        f"{use_case_id}: alternative_flows item {flow_number} "
                        "requires condition."
                    )
                if not isinstance(steps, list):
                    errors.append(
                        f"{use_case_id}: alternative_flows item {flow_number} steps must be a list."
                    )

        exceptions = use_case.get("exceptions", []) or []
        if isinstance(exceptions, list):
            for exception_number, exception in enumerate(exceptions, start=1):
                if isinstance(exception, str):
                    continue
                if not isinstance(exception, dict) or not exception.get("description"):
                    errors.append(
                        f"{use_case_id}: exceptions item {exception_number} "
                        "must be a string or an object with description."
                    )

        for rule_id in use_case.get("business_rules", []) or []:
            if rule_id not in project.business_rules:
                errors.append(f"{use_case_id}: unknown Business Rule '{rule_id}'.")

        created_date = use_case.get("date_created")
        if created_date and not isinstance(created_date, (str, date)):
            errors.append(f"{use_case_id}: date_created must be a date or ISO date string.")

    return errors
