from copy import deepcopy
from pathlib import Path
import unittest

from usecase_tool.generator import _alternative_flow_text, _exception_text
from usecase_tool.loader import assign_display_ids, load_project
from usecase_tool.validator import validate_project


ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.project = load_project(ROOT / "data")

    def test_sample_data_is_valid(self):
        self.assertEqual([], validate_project(self.project))

    def test_unknown_actor_is_reported(self):
        changed = deepcopy(self.project.use_cases)
        changed[0]["primary_actor"] = "Unknown Actor"
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("unknown primary actor" in error for error in errors))

    def test_unknown_business_rule_is_reported(self):
        changed = deepcopy(self.project.use_cases)
        changed[0]["business_rules"].append("BR-UNKNOWN-RULE")
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("BR-UNKNOWN-RULE" in error for error in errors))

    def test_display_ids_are_generated_from_order(self):
        use_cases = [
            {"key": "UC-TASK-ASSIGN", "order": 300},
            {"key": "UC-TASK-CREATE", "order": 100},
            {"key": "UC-TASK-MODIFY", "order": 200},
        ]
        assign_display_ids(use_cases, "UC")
        self.assertEqual(
            [
                ("UC-TASK-CREATE", "UC-01"),
                ("UC-TASK-MODIFY", "UC-02"),
                ("UC-TASK-ASSIGN", "UC-03"),
            ],
            [(item["key"], item["_display_id"]) for item in use_cases],
        )

    def test_non_integer_order_is_reported(self):
        changed = deepcopy(self.project.use_cases)
        changed[0]["order"] = "first"
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("order must be an integer" in error for error in errors))

    def test_string_alternative_flow_and_exception_can_be_generated(self):
        use_case = {
            "alternative_flows": ["The actor cancels the operation."],
            "exceptions": ["The database is unavailable."],
        }
        self.assertEqual(
            "AF-01: The actor cancels the operation.",
            _alternative_flow_text(use_case),
        )
        self.assertEqual(
            "EX-01: The database is unavailable.",
            _exception_text(use_case),
        )


if __name__ == "__main__":
    unittest.main()
