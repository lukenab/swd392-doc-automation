from copy import deepcopy
from pathlib import Path
import unittest

from usecase_tool.loader import load_project
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
        changed[0]["business_rules"].append("BR-99")
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("BR-99" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

