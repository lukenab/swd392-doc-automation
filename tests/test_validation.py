from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
import unittest

import yaml
from docx import Document
from docx.oxml.ns import qn
from docx.shared import RGBColor

from usecase_tool.generator import (
    build_outputs,
    _alternative_flow_text,
    _exception_text,
    _generate_business_rules_docx,
    _generate_business_rules_markdown,
    _generate_docx,
)
from usecase_tool.loader import assign_display_ids, load_project
from usecase_tool.validator import validate_project


ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.project = load_project(ROOT / "data")

    def test_sample_data_is_valid(self):
        self.assertEqual([], validate_project(self.project))

    def test_actor_catalog_separates_staff_and_project_roles(self):
        self.assertEqual(
            {
                "Guest", "Staff", "Project Member", "Project Owner",
                "Product Owner", "Developer", "System Administrator",
                "Identity Provider", "Email Service",
            },
            set(self.project.actors),
        )
        self.assertNotIn("User", self.project.actors)
        self.assertNotIn("Scrum Master", self.project.actors)
        self.assertIn("not a Scrum accountability", self.project.actors["Project Owner"]["description"])
        self.assertNotIn("operational statistics", self.project.actors["System Administrator"]["description"])
        accountability = next(
            uc for uc in self.project.use_cases
            if uc["key"] == "UC-SCRUM-ACCOUNTABILITY-ASSIGN"
        )
        self.assertEqual("Project Owner", accountability["primary_actor"])
        self.assertIn("Selects Product Owner or Developer.", [
            step["action"] for step in accountability["normal_flow"]
        ])

    def test_use_case_actors_match_project_and_scrum_responsibilities(self):
        expected = {
            "UC-ACCOUNT-REGISTER": "Guest",
            "UC-SIGN-IN": "Guest",
            "UC-PASSWORD-RESET": "Guest",
            "UC-SIGN-OUT": "Staff",
            "UC-PROFILE-MANAGE": "Staff",
            "UC-PROFILE-VIEW": "Staff",
            "UC-PROFILE-UPDATE": "Staff",
            "UC-PASSWORD-CHANGE": "Staff",
            "UC-PROJECT-CREATE": "Staff",
            "UC-PROJECTS-MANAGE": "Staff",
            "UC-NOTIFICATIONS-REVIEW": "Staff",
            "UC-PROJECT-DASHBOARD-VIEW": "Project Member",
            "UC-PROJECT-MEMBERS-VIEW": "Project Member",
            "UC-PROJECT-LEAVE": "Project Member",
            "UC-PRODUCT-GOAL-VIEW": "Project Member",
            "UC-BACKLOG-ITEM-VIEW": "Project Member",
            "UC-SPRINT-BOARD-REVIEW": "Project Member",
            "UC-SPRINT-TASK-VIEW": "Project Member",
            "UC-SUBTASKS-VIEW": "Project Member",
            "UC-WORK-ITEM-COMMENT": "Project Member",
            "UC-WORK-ITEM-ACTIVITY-REVIEW": "Project Member",
            "UC-SPRINT-PROGRESS-MONITOR": "Project Member",
            "UC-PROJECT-UPDATE": "Project Owner",
            "UC-PROJECT-MEMBERS-MANAGE": "Project Owner",
            "UC-PROJECT-MEMBER-ADD": "Project Owner",
            "UC-PROJECT-MEMBER-REMOVE": "Project Owner",
            "UC-SCRUM-ACCOUNTABILITY-ASSIGN": "Project Owner",
            "UC-PROJECT-ARCHIVE": "Project Owner",
            "UC-PROJECT-OWNERSHIP-TRANSFER": "Project Owner",
            "UC-PRODUCT-GOAL-MANAGE": "Product Owner",
            "UC-PRODUCT-GOAL-SET": "Product Owner",
            "UC-PRODUCT-GOAL-UPDATE": "Product Owner",
            "UC-BACKLOG-ITEMS-MANAGE": "Product Owner",
            "UC-BACKLOG-ITEM-CREATE": "Product Owner",
            "UC-BACKLOG-ITEM-UPDATE": "Product Owner",
            "UC-BACKLOG-ITEM-REMOVE": "Product Owner",
            "UC-BACKLOG-ORDER": "Product Owner",
            "UC-BACKLOG-ITEM-REFINE": "Product Owner",
            "UC-SPRINT-PLAN": "Product Owner",
            "UC-SPRINTS-MANAGE": "Product Owner",
            "UC-SPRINT-START": "Product Owner",
            "UC-SPRINT-COMPLETE": "Product Owner",
            "UC-SPRINT-CANCEL": "Product Owner",
            "UC-BACKLOG-ITEM-ESTIMATE": "Developer",
            "UC-SPRINT-TASKS-MANAGE": "Developer",
            "UC-SPRINT-TASK-CREATE": "Developer",
            "UC-SPRINT-TASK-UPDATE": "Developer",
            "UC-SPRINT-TASK-ASSIGN": "Developer",
            "UC-SPRINT-TASK-DELETE": "Developer",
            "UC-TASK-DEPENDENCY-ADD": "Developer",
            "UC-TASK-DEPENDENCY-REMOVE": "Developer",
            "UC-SPRINT-TASK-CLAIM": "Developer",
            "UC-WORK-ITEM-STATUS-UPDATE": "Developer",
            "UC-SUBTASKS-MANAGE": "Developer",
            "UC-SUBTASK-CREATE": "Developer",
            "UC-SUBTASK-UPDATE": "Developer",
            "UC-SUBTASK-DELETE": "Developer",
            "UC-USER-ACCOUNTS-MANAGE": "System Administrator",
            "UC-USER-ACCOUNTS-SEARCH": "System Administrator",
            "UC-USER-ACCOUNT-SUSPEND": "System Administrator",
            "UC-USER-ACCOUNT-REACTIVATE": "System Administrator",
            "UC-USER-ACCOUNT-DELETE": "System Administrator",
            "UC-SYSTEM-AUDIT-LOG-REVIEW": "System Administrator",
        }
        self.assertEqual(set(expected), {uc["key"] for uc in self.project.use_cases})
        for uc in self.project.use_cases:
            with self.subTest(key=uc["key"]):
                self.assertEqual(expected[uc["key"]], uc["primary_actor"])
                declared = {uc["primary_actor"], *(uc.get("secondary_actors") or [])}
                for step in uc["normal_flow"]:
                    self.assertIn(step["actor"], declared | {"System"})
                    self.assertNotEqual("User", step["actor"])
                    self.assertFalse(step["action"].startswith("Acting as "))
                self.assertNotIn("User", uc.get("secondary_actors", []))

    def test_collaborative_use_cases_declare_both_scrum_actors(self):
        # Catalog groups describe organization, not inherited execution behavior.
        expected = {
            "UC-BACKLOG-ITEM-REFINE": ("Product Owner", "Developer"),
            "UC-BACKLOG-ITEM-ESTIMATE": ("Developer", "Product Owner"),
            "UC-SPRINT-PLAN": ("Product Owner", "Developer"),
            "UC-SPRINT-START": ("Product Owner", "Developer"),
            "UC-SPRINT-COMPLETE": ("Product Owner", "Developer"),
        }
        use_cases = {uc["key"]: uc for uc in self.project.use_cases}
        for key, (primary, supporting) in expected.items():
            with self.subTest(key=key):
                uc = use_cases[key]
                self.assertEqual(primary, uc["primary_actor"])
                self.assertIn(supporting, uc["secondary_actors"])
                participants = {step["actor"] for step in uc["normal_flow"]}
                self.assertIn(primary, participants)
                self.assertIn(supporting, participants)

    def test_user_account_entity_and_existing_use_case_names_are_preserved(self):
        expected = {
            "UC-USER-ACCOUNTS-MANAGE": "Manage User Accounts",
            "UC-USER-ACCOUNTS-SEARCH": "Search and View User Accounts",
            "UC-USER-ACCOUNT-SUSPEND": "Suspend User Account",
            "UC-USER-ACCOUNT-REACTIVATE": "Reactivate User Account",
            "UC-USER-ACCOUNT-DELETE": "Delete User Account",
        }
        use_cases = {uc["key"]: uc for uc in self.project.use_cases}
        for key, name in expected.items():
            with self.subTest(key=key):
                self.assertEqual(name, use_cases[key]["name"])
        self.assertTrue(any(
            "User account" in condition
            for condition in use_cases["UC-SIGN-IN"]["postconditions"]
        ))

    def test_approved_catalog_grouping_and_standalone_authentication(self):
        use_cases = {uc["key"]: uc for uc in self.project.use_cases}
        self.assertEqual(63, len(use_cases))
        self.assertEqual(54, sum(not uc.get("abstract") for uc in use_cases.values()))
        self.assertEqual(9, sum(uc.get("grouping_only") is True for uc in use_cases.values()))
        self.assertEqual(13, sum(not uc.get("abstract") and not uc.get("parent") for uc in use_cases.values()))
        for key in ("UC-ACCOUNT-REGISTER", "UC-SIGN-IN", "UC-SIGN-OUT", "UC-PASSWORD-RESET"):
            self.assertFalse(use_cases[key].get("parent"))
        self.assertNotIn("Manage Account Access", {uc["name"] for uc in use_cases.values()})
        expected_parents = {
            "UC-PROJECT-CREATE": "UC-PROJECTS-MANAGE",
            "UC-PROJECT-DASHBOARD-VIEW": "UC-PROJECTS-MANAGE",
            "UC-PROJECT-UPDATE": "UC-PROJECTS-MANAGE",
            "UC-PROJECT-ARCHIVE": "UC-PROJECTS-MANAGE",
            "UC-PROJECT-OWNERSHIP-TRANSFER": "UC-PROJECTS-MANAGE",
            "UC-PROJECT-LEAVE": "UC-PROJECT-MEMBERS-MANAGE",
            "UC-BACKLOG-ORDER": "UC-BACKLOG-ITEMS-MANAGE",
            "UC-BACKLOG-ITEM-REFINE": "UC-BACKLOG-ITEMS-MANAGE",
            "UC-SPRINT-PLAN": "UC-SPRINTS-MANAGE",
            "UC-SPRINT-START": "UC-SPRINTS-MANAGE",
            "UC-SPRINT-COMPLETE": "UC-SPRINTS-MANAGE",
            "UC-SPRINT-CANCEL": "UC-SPRINTS-MANAGE",
            "UC-SPRINT-TASK-CLAIM": "UC-SPRINT-TASKS-MANAGE",
        }
        for key, parent in expected_parents.items():
            with self.subTest(key=key):
                self.assertEqual(parent, use_cases[key]["parent"])
        self.assertEqual("View Project Overview", use_cases["UC-PROJECT-DASHBOARD-VIEW"]["name"])
        self.assertEqual("Manage Product Backlog", use_cases["UC-BACKLOG-ITEMS-MANAGE"]["name"])

    def test_catalog_groups_have_no_inherited_execution_contract(self):
        for uc in self.project.use_cases:
            if not uc.get("grouping_only"):
                continue
            with self.subTest(key=uc["key"]):
                self.assertTrue(uc["abstract"])
                self.assertFalse(uc["trigger"])
                for field in ("preconditions", "postconditions", "normal_flow", "alternative_flows", "exceptions"):
                    self.assertEqual([], uc[field])
                self.assertTrue(any(child.get("parent") == uc["key"] for child in self.project.use_cases))

    def test_grouping_flag_cannot_disable_validation_on_concrete_use_case(self):
        changed = deepcopy(self.project.use_cases)
        changed[0]["grouping_only"] = True
        changed[0]["normal_flow"] = []
        invalid_project = self.project.__class__(
            self.project.data_dir, self.project.groups, self.project.actors,
            self.project.business_rules, changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("grouping_only requires abstract: true" in error for error in errors))

    def test_grouping_flag_rejects_execution_fields_and_non_boolean_value(self):
        changed = deepcopy(self.project.use_cases)
        group = next(uc for uc in changed if uc.get("grouping_only"))
        group["preconditions"] = ["The actor is the Project Owner."]
        changed[0]["grouping_only"] = "true"
        invalid_project = self.project.__class__(
            self.project.data_dir, self.project.groups, self.project.actors,
            self.project.business_rules, changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("catalog group must not define execution field 'preconditions'" in error for error in errors))
        self.assertTrue(any("grouping_only must be true or false" in error for error in errors))

    def test_subtask_completion_is_merged_without_losing_behavior(self):
        use_cases = {uc["key"]: uc for uc in self.project.use_cases}
        self.assertNotIn("UC-SUBTASK-COMPLETE", use_cases)
        status = use_cases["UC-WORK-ITEM-STATUS-UPDATE"]
        self.assertIn("BR-SPRINT-TASK-ACTIVE-SPRINT", status["business_rules"])
        self.assertEqual({"AF-01", "AF-02"}, {af["id"] for af in status["alternative_flows"]})
        self.assertIn("completed subtask", status["alternative_flows"][1]["condition"])
        self.assertIn("EX-02", {ex["id"] for ex in status["exceptions"]})
        self.assertTrue(any("Sprint ends" in ex["description"] for ex in status["exceptions"]))
        self.assertTrue(any("Recalculates parent-task progress" in step["action"] for step in status["normal_flow"]))
        self.assertIn("does not", status["other_information"])
        self.assertIn("automatically complete the parent task", status["other_information"])
        self.assertIn("Update Work Item Status", use_cases["UC-SUBTASK-UPDATE"]["other_information"])
        archived = ROOT / "docs/archive/use-cases/2026-10-09/UC-SUBTASK-COMPLETE.yml"
        self.assertTrue(archived.exists())
        self.assertEqual("UC-SUBTASK-COMPLETE", yaml.safe_load(archived.read_text(encoding="utf-8"))["key"])

    def test_activity_manifest_catalog_is_current_but_not_false_accepted(self):
        manifest = yaml.safe_load((ROOT / "diagrams/activity/manifest.yml").read_text(encoding="utf-8"))
        concrete = {uc["key"]: uc for uc in self.project.use_cases if not uc.get("abstract")}
        entries = manifest["use_cases"]
        self.assertEqual(len(concrete), len(entries))
        self.assertEqual(set(concrete), {entry["key"] for entry in entries})
        for entry in entries:
            with self.subTest(key=entry["key"]):
                uc = concrete[entry["key"]]
                for source, target in (("_display_id", "display_id"), ("name", "name"), ("primary_actor", "primary_actor"), ("secondary_actors", "secondary_actors")):
                    self.assertEqual(uc[source], entry[target])
                if entry.get("catalog_sync_status") == "needs-source-review":
                    self.assertEqual("needs-manual-review", entry["final_status"])
                    self.assertNotEqual("pass", entry["traceability_status"])
                    self.assertIn("rendered_display_id", entry)
        retired = manifest["retired_use_cases"]
        self.assertEqual(["UC-SUBTASK-COMPLETE"], [entry["key"] for entry in retired])
        self.assertEqual("UC-WORK-ITEM-STATUS-UPDATE", retired[0]["merged_into"])

    def test_actor_markdown_is_generated_from_the_catalog(self):
        with TemporaryDirectory(prefix="swd392-actors-") as temporary_dir:
            output_dir = Path(temporary_dir)
            outputs = build_outputs(
                self.project, self.project.use_cases, output_dir, "markdown"
            )
            actor_file = output_dir / "actors.md"
            self.assertIn(actor_file, outputs)
            actor_text = actor_file.read_text(encoding="utf-8")
            self.assertIn("| # | Actor | Description |", actor_text)
            for number, actor in enumerate(self.project.actors.values(), start=1):
                self.assertIn(
                    f"| {number} | {actor['name']} | {actor['description']} |",
                    actor_text,
                )
            self.assertEqual([], list(output_dir.glob("*.docx")))

    def test_email_notifications_are_in_iteration_scope(self):
        feature_data = yaml.safe_load((ROOT / "data" / "major_features.yml").read_text(encoding="utf-8"))
        feature = next(item for item in feature_data["major_features"] if item["key"] == "FE-09")
        notification_use_case = next(
            item for item in self.project.use_cases if item["key"] == "UC-NOTIFICATIONS-REVIEW"
        )
        comment_use_case = next(
            item for item in self.project.use_cases if item["key"] == "UC-WORK-ITEM-COMMENT"
        )

        self.assertIn("email notifications", feature["description"])
        self.assertIn("Email Service", comment_use_case["secondary_actors"])
        self.assertIn("email delivery", notification_use_case["other_information"])
        self.assertIn("push delivery remains outside", notification_use_case["other_information"].lower())
        self.assertEqual(
            [
                "BR-NOTIFICATION-OWNER-ONLY",
                "BR-PROJECT-MEMBER-ACCESS",
                "BR-NOTIFICATION-EMAIL-PREFERENCE",
            ],
            notification_use_case["business_rules"],
        )
        self.assertTrue(
            any(
                "email notification cannot be delivered" in exception["description"]
                for exception in comment_use_case["exceptions"]
            )
        )

    def test_authentication_use_cases_and_rules_are_synchronized(self):
        authentication_cases = [
            item
            for item in self.project.use_cases
            if item["group"] == "ACCOUNT_AUTHENTICATION"
        ]
        self.assertEqual(
            ["UC-01", "UC-02", "UC-03", "UC-04", "UC-05", "UC-05.1", "UC-05.2", "UC-05.3"],
            [item["_display_id"] for item in authentication_cases],
        )
        self.assertEqual(
            [
                "Register Account",
                "Log In",
                "Log Out",
                "Forgot Password",
                "Manage Personal Profile",
                "View Personal Profile",
                "Update Personal Profile",
                "Change Password",
            ],
            [item["name"] for item in authentication_cases],
        )
        self.assertEqual("Guest", authentication_cases[0]["primary_actor"])
        self.assertNotIn("Identity Provider", authentication_cases[0]["secondary_actors"])
        self.assertEqual(
            ["AF-01"],
            [flow["id"] for flow in authentication_cases[0]["alternative_flows"]],
        )
        self.assertEqual(
            ["EX-01", "EX-02", "EX-03"],
            [exception["id"] for exception in authentication_cases[0]["exceptions"]],
        )
        self.assertEqual("Guest", authentication_cases[1]["primary_actor"])
        self.assertIn("Identity Provider", authentication_cases[1]["secondary_actors"])
        self.assertIn(
            "AF-03",
            [flow["id"] for flow in authentication_cases[1]["alternative_flows"]],
        )
        self.assertIn(
            "BR-ACCOUNT-NO-PROJECT-AUTO-MEMBERSHIP",
            authentication_cases[1]["business_rules"],
        )
        sign_in_exceptions = {
            exception["id"]: exception["description"]
            for exception in authentication_cases[1]["exceptions"]
        }
        self.assertIn("does not link accounts by email alone", sign_in_exceptions["EX-04"])
        self.assertIn("EX-06", sign_in_exceptions)
        self.assertIn("Email Service", authentication_cases[3]["secondary_actors"])
        self.assertTrue(authentication_cases[4]["abstract"])
        self.assertTrue(
            all(item["parent"] == "UC-PROFILE-MANAGE" for item in authentication_cases[5:])
        )

        account_rule = self.project.business_rules["BR-SYSADMIN-USER-ACCOUNT"]
        self.assertNotIn("create", account_rule["description"].lower())
        for use_case in authentication_cases:
            for rule_key in use_case["business_rules"]:
                self.assertIn(rule_key, self.project.business_rules)

    def test_audit_feedback_changes_are_synchronized(self):
        use_cases = {item["key"]: item for item in self.project.use_cases}

        self.assertIn(
            "BR-PROJECT-OWNER-ADMINISTRATION",
            use_cases["UC-PROJECT-OWNERSHIP-TRANSFER"]["business_rules"],
        )
        self.assertNotIn(
            "BR-PRODUCT-OWNER-BACKLOG",
            use_cases["UC-PRODUCT-GOAL-MANAGE"]["business_rules"],
        )
        self.assertIn(
            "BR-SPRINT-ONE-DRAFT",
            use_cases["UC-SPRINT-PLAN"]["business_rules"],
        )
        self.assertEqual(
            ["BR-NOTIFICATION-OWNER-ONLY", "BR-PROJECT-MEMBER-ACCESS", "BR-NOTIFICATION-EMAIL-PREFERENCE"],
            use_cases["UC-NOTIFICATIONS-REVIEW"]["business_rules"],
        )
        self.assertIn(
            "BR-AUDIT-VIEW-SYSADMIN-ONLY",
            use_cases["UC-SYSTEM-AUDIT-LOG-REVIEW"]["business_rules"],
        )
        self.assertTrue(
            any(
                exception["id"] == "EX-04"
                for exception in use_cases["UC-SIGN-IN"]["exceptions"]
            )
        )
        self.assertEqual(
            "BR-14",
            self.project.business_rules["BR-SPRINT-GOAL-REQUIRED"]["_display_id"],
        )

    def test_unknown_actor_is_reported(self):
        changed = deepcopy(self.project.use_cases)
        changed[0]["primary_actor"] = "Unknown Actor"
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            groups=self.project.groups,
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
            groups=self.project.groups,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("BR-UNKNOWN-RULE" in error for error in errors))

    def test_display_ids_are_generated_from_domain_and_order(self):
        groups = {
            "PROJECT": {"key": "PROJECT", "order": 100},
            "TASK": {"key": "TASK", "order": 400},
        }
        use_cases = [
            {"key": "UC-TASK-CREATE", "group": "TASK", "order": 100},
            {"key": "UC-PROJECT-ARCHIVE", "group": "PROJECT", "order": 200},
            {"key": "UC-PROJECT-CREATE", "group": "PROJECT", "order": 100},
        ]
        assign_display_ids(use_cases, "UC", groups)
        self.assertEqual(
            [
                ("UC-PROJECT-CREATE", "UC-01"),
                ("UC-PROJECT-ARCHIVE", "UC-02"),
                ("UC-TASK-CREATE", "UC-03"),
            ],
            [(item["key"], item["_display_id"]) for item in use_cases],
        )

    def test_hierarchical_display_ids_follow_abstract_parent(self):
        groups = {"PROJECT": {"key": "PROJECT", "order": 100}}
        use_cases = [
            {"key": "UC-PROJECT-CREATE", "group": "PROJECT", "order": 100},
            {
                "key": "UC-MEMBERS-MANAGE",
                "group": "PROJECT",
                "order": 200,
                "abstract": True,
            },
            {
                "key": "UC-MEMBER-VIEW",
                "parent": "UC-MEMBERS-MANAGE",
                "group": "PROJECT",
                "order": 210,
            },
            {
                "key": "UC-MEMBER-ADD",
                "parent": "UC-MEMBERS-MANAGE",
                "group": "PROJECT",
                "order": 220,
            },
            {"key": "UC-PROJECT-ARCHIVE", "group": "PROJECT", "order": 300},
        ]

        assign_display_ids(use_cases, "UC", groups)

        self.assertEqual(
            [
                ("UC-PROJECT-CREATE", "UC-01"),
                ("UC-MEMBERS-MANAGE", "UC-02"),
                ("UC-MEMBER-VIEW", "UC-02.1"),
                ("UC-MEMBER-ADD", "UC-02.2"),
                ("UC-PROJECT-ARCHIVE", "UC-03"),
            ],
            [(item["key"], item["_display_id"]) for item in use_cases],
        )

    def test_abstract_parent_is_listed_but_has_no_detail_table(self):
        root = ROOT / "tests" / "_tmp_abstract_use_case"
        if root.exists():
            shutil.rmtree(root)
        root.mkdir()
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))
        try:
            generated = _generate_docx(self.project, self.project.use_cases, root)
            document = Document(generated)
            summary_ids = [row.cells[0].text for row in document.tables[0].rows[1:]]
            detail_ids = [
                table.rows[0].cells[1].text.split(" - ", 1)[0]
                for table in document.tables[1:]
            ]

            self.assertIn("UC-05", summary_ids)
            self.assertIn("UC-05.1", summary_ids)
            self.assertNotIn("UC-05", detail_ids)
            self.assertIn("UC-05.1", detail_ids)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_use_case_domain_order_can_differ_from_business_rule_order(self):
        groups = {
            "PROJECT": {"key": "PROJECT", "order": 100, "use_case_order": 200},
            "AUTH": {"key": "AUTH", "order": 200, "use_case_order": 100},
        }
        use_cases = [
            {"key": "UC-PROJECT", "group": "PROJECT", "order": 100},
            {"key": "UC-SIGN-IN", "group": "AUTH", "order": 100},
        ]
        rules = [
            {"key": "BR-PROJECT", "group": "PROJECT", "order": 100},
            {"key": "BR-AUTH", "group": "AUTH", "order": 100},
        ]

        assign_display_ids(use_cases, "UC", groups, group_order_field="use_case_order")
        assign_display_ids(rules, "BR", groups)

        self.assertEqual("UC-SIGN-IN", use_cases[0]["key"])
        self.assertEqual("BR-PROJECT", rules[0]["key"])

    def test_non_integer_order_is_reported(self):
        changed = deepcopy(self.project.use_cases)
        changed[0]["order"] = "first"
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            groups=self.project.groups,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("order must be an integer" in error for error in errors))

    def test_unknown_domain_is_reported(self):
        changed = deepcopy(self.project.use_cases)
        changed[0]["group"] = "UNKNOWN_DOMAIN"
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            groups=self.project.groups,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(any("unknown domain 'UNKNOWN_DOMAIN'" in error for error in errors))

    def test_use_case_in_wrong_domain_folder_is_reported(self):
        changed = deepcopy(self.project.use_cases)
        project_create = next(item for item in changed if item["key"] == "UC-PROJECT-CREATE")
        project_create["_source_file"] = "sprint-work/UC-PROJECT-CREATE.yml"
        invalid_project = self.project.__class__(
            data_dir=self.project.data_dir,
            groups=self.project.groups,
            actors=self.project.actors,
            business_rules=self.project.business_rules,
            use_cases=changed,
        )
        errors = validate_project(invalid_project)
        self.assertTrue(
            any(
                "file must be inside use_cases/project-membership/" in error
                for error in errors
            )
        )

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

    def test_business_rule_outputs_include_all_rules(self):
        root = ROOT / "tests" / "_tmp_business_rules"
        if root.exists():
            shutil.rmtree(root)
        root.mkdir()
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))
        try:
            markdown_path = _generate_business_rules_markdown(self.project, root)
            docx_path = _generate_business_rules_docx(self.project, root)

            markdown = markdown_path.read_text(encoding="utf-8")
            document = Document(docx_path)
            table_rows = sum(len(table.rows) - 1 for table in document.tables)

            self.assertIn("# Business Rules", markdown)
            self.assertIn("BR-01", markdown)
            self.assertIn(f"BR-{len(self.project.business_rules):02d}", markdown)
            self.assertEqual(1, markdown.count("| ID | Business Rule | Description |"))
            self.assertEqual(1, len(document.tables))
            self.assertEqual(len(self.project.business_rules), table_rows)
            self.assertEqual("II.4 Business Rules", document.paragraphs[0].text)
            self.assertIsNone(
                document.tables[0].rows[0]._tr.get_or_add_trPr().find(qn("w:tblHeader"))
            )
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_use_case_summary_table_has_balanced_columns_and_navy_header(self):
        root = ROOT / "tests" / "_tmp_summary_table_style"
        if root.exists():
            shutil.rmtree(root)
        root.mkdir()
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))
        try:
            generated = _generate_docx(
                self.project,
                self.project.use_cases,
                root,
            )
            document = Document(generated)
            summary_table = document.tables[0]

            self.assertIsNone(
                summary_table.rows[0]._tr.get_or_add_trPr().find(qn("w:tblHeader"))
            )

            self.assertEqual(
                [1.6, 3.6, 3.7, 8.1],
                [round(column.width.cm, 1) for column in summary_table.columns],
            )
            for cell in summary_table.rows[0].cells:
                shading = cell._tc.get_or_add_tcPr().find(qn("w:shd"))
                self.assertIsNotNone(shading)
                self.assertEqual("1F4E78", shading.get(qn("w:fill")))
                visible_runs = [
                    run for paragraph in cell.paragraphs for run in paragraph.runs if run.text
                ]
                self.assertTrue(visible_runs)
                self.assertTrue(
                    all(run.font.color.rgb == RGBColor(255, 255, 255) for run in visible_runs)
                )
                self.assertTrue(all(run.font.size.pt == 12 for run in visible_runs))

            summary_body_runs = [
                run
                for paragraph in summary_table.rows[1].cells[1].paragraphs
                for run in paragraph.runs
                if run.text
            ]
            self.assertTrue(summary_body_runs)
            self.assertTrue(all(run.font.size.pt == 11 for run in summary_body_runs))

            detail_table = document.tables[1]
            self.assertTrue(
                all(
                    row._tr.get_or_add_trPr().find(qn("w:cantSplit")) is not None
                    for table in document.tables
                    for row in table.rows
                )
            )
            label_runs = [
                run
                for paragraph in detail_table.rows[0].cells[0].paragraphs
                for run in paragraph.runs
                if run.text
            ]
            value_runs = [
                run
                for paragraph in detail_table.rows[0].cells[1].paragraphs
                for run in paragraph.runs
                if run.text
            ]
            self.assertTrue(label_runs)
            self.assertTrue(value_runs)
            self.assertTrue(all(run.font.size.pt == 12 for run in label_runs))
            self.assertTrue(all(run.font.size.pt == 11 for run in value_runs))
            for row in detail_table.rows:
                shading = row.cells[0]._tc.get_or_add_tcPr().find(qn("w:shd"))
                self.assertIsNone(shading)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
