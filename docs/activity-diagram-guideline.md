# Activity Diagram Delivery and Review Guideline

## 1. Purpose

This document defines the shared rules for creating, reviewing, accepting, and storing Activity Diagrams for the SWD392 Project Management System report.

The objective is to ensure that all team members produce diagrams with the same UML semantics, visual style, file structure, and review criteria.

## 2. Scope

- Create one Activity Diagram for every **concrete Use Case**.
- Do not create a separate Activity Diagram for an abstract `Manage ...` parent Use Case.
- Child Use Cases such as `UC-09.2`, `UC-24.6`, and `UC-27.2` require their own Activity Diagrams.
- The current catalog contains **55 concrete Use Cases**.
- The Use Case YAML files and approved Business Rules are the authoritative sources.
- A diagram must not introduce behavior, validation rules, actors, or exceptions that are absent from the approved specification.

## 3. Assignment

| Assignee | Assigned concrete Use Cases | Total |
|---|---|---:|
| Trần Công Luận | UC-01–04, UC-05.1–05.3, UC-32.1–32.4, UC-33 | 12 |
| Nguyễn An Bình | UC-06–08, UC-09.1–09.3, UC-10–13, UC-28–31 | 14 |
| Nguyễn Quốc Khánh | UC-14.1–14.3, UC-15.1–15.4, UC-16–22 | 14 |
| Nguyễn Tấn Trung | UC-23, UC-24.1–24.7, UC-25–26, UC-27.1–27.5 | 15 |

Target deadline: **03 November 2026**.

## 4. Authoritative Inputs

Before drawing a diagram, review all of the following:

1. The Use Case YAML file.
2. Trigger and preconditions.
3. Normal Flow.
4. Alternative Flows.
5. Exceptions.
6. Postconditions.
7. Referenced Business Rules.

Source precedence: (1) the concrete Use Case YAML, (2) the referenced Business Rules, (3) the actor and group definitions, (4) approved documents. Existing diagrams are never authoritative.

If the sources conflict, mark the use case `BLOCKED — REQUIREMENT CONFLICT`. If the specification lacks the information needed to draw a flow, mark it `BLOCKED — INSUFFICIENT SPECIFICATION`. In both cases record the reason and the question for the BA/PO in `diagrams/activity/manifest.yml`, do not publish a final-looking SVG for that use case, and continue with the others. Do not resolve a conflict by inventing a flow in the diagram.

An exception or alternative flow that describes a state excluded by a precondition is drawn as a defensive System check when the System can detect that state, and is recorded as an observation. When an alternative flow needs the actor to start from a state that the preconditions exclude, the use case is blocked as a requirement conflict.

## 5. Required UML Elements

Each Activity Diagram must contain:

- Exactly one Initial Node.
- At least one Activity Final Node.
- Action nodes written as **verb + object**.
- Directed control flows with visible arrowheads.
- Decision nodes where the flow branches according to a condition.
- Merge nodes where mutually exclusive branches return to one flow.
- Fork and Join nodes only when activities actually execute concurrently.
- Guard conditions on every outgoing branch of a decision.
- Swimlanes for responsibility separation.

UML allows several Activity Final Nodes; reaching any of them ends the whole activity. Merge paths into one Activity Final Node when they share the same postcondition, and use separate Activity Final Nodes only for semantically different outcomes (success, cancellation, exception). Use a Flow Final Node only when other flows of the same activity continue. An exception branch must display or record its outcome before ending; it must not terminate silently immediately after a decision.

## 6. Swimlane Rules

Use the minimum number of partitions needed to show responsibility clearly. Partitions name the **responsibility**, not the account type, so a role is not collapsed into `User` when the role matters.

| Partition | Use when |
|---|---|
| `Guest` | An unauthenticated visitor acts (registration, sign-in, password reset). |
| `User` | Any active member or account holder acts and no project role is required. |
| `Project Owner` | The action requires the Project Owner role. |
| `Product Owner` | The YAML step says "Acting as the Product Owner" or the rule requires Product Owner accountability. |
| `Developer` | The YAML step says "Acting as a Developer" or the rule requires Developer accountability. |
| `System Administrator` | A system-level administrator acts. |
| `System` | The Project Management System. Every diagram has this partition. |
| `Email Service`, `Identity Provider` | An external service participates in the flow. |

Order from left to right: the primary actor, the System, then other human roles and external services that participate. Declare every partition once with an alias before `start`, for example `|DEV| $lane_title("Developer")`.

Do not add a partition for a database, repository, UI screen, or internal implementation component unless the assignment explicitly requests a lower-level design diagram.

> This replaces the earlier rule that used `User` for every project role. The Stage 2 instruction requires responsibility-specific partitions.

## 7. Flow Construction Rules

### 7.1 Main Flow

- The primary successful flow should be readable from top to bottom.
- Keep the main flow close to the vertical center of the diagram.
- Switch partitions only when responsibility changes.
- Do not model Log In inside other diagrams. Authentication is a precondition; Log In appears only in `UC-SIGN-IN`.

### 7.2 Alternative Flows

- Place the decision at the step where the alternative actually occurs.
- An alternative flow resumes after the step where it was raised, or returns to the step it re-performs. Cancelling and terminal alternative flows end the activity.
- Use a Merge Node when alternative branches rejoin.
- Reference the approved identifier where useful, for example `[information invalid — AF-01]`.

### 7.3 Exceptions

- Label the branch with the approved exception ID, for example `[account inactive — EX-01]`.
- Add one explicit System action such as `Reject ...`, `Report ...` or `Record ...` before the final node. When the YAML names the exception but not its outcome, trace that action to `GUIDE-7.3` (this rule).
- Do not create new exception conditions that are absent from the Use Case specification or Business Rules.
- Validation failures that the YAML does not describe are not drawn; record them as observations in the manifest.

### 7.4 Decisions and Guards

- A Decision Node should contain a short question or condition.
- Every outgoing edge must have a guard enclosed in square brackets.
- Guards must be mutually exclusive and cover all valid outcomes.
- Prefer meaningful guards over plain `yes` and `no` when space permits.

Preferred:

```text
[belongs to the active Sprint]
[no longer belongs to the active Sprint — EX-01]
```

Avoid:

```text
yes
no
error
```

### 7.5 Loops

- A retry flow must visibly return to the appropriate validation or input activity.
- Do not duplicate the entire successful flow after retrying.
- The loop guard and the exit guard must both be labelled. In PlantUML use `while (...) is ([...]) ... endwhile ([...])`; `repeat while` loses its labels with diamond decisions.

## 8. Visual Standard

Use the following presentation standard for every diagram:

| Element | Standard |
|---|---|
| Flow direction | Top to bottom |
| Lane direction | Left to right |
| Background | White |
| Font | Times New Roman |
| Lane heading | 18 pt, bold |
| Action and decision text | 16 pt |
| Guard text | 14 pt or visually smaller than action text |
| Action shape | Rounded rectangle |
| Decision/Merge shape | Diamond |
| Lines | Dark gray or black, consistent thickness |
| Effects | No gradients or shadows |
| Internal title | Omit; the Word caption supplies the title |
| Presentation frame | Complete outer border with top, bottom, and lane-header separator |

Additional layout requirements:

- Avoid crossing connectors.
- Avoid placing two connectors directly on top of each other.
- Keep consistent spacing between actions.
- Keep guard labels clear of node borders and arrows.
- Break long action text into two or three lines.
- Use portrait orientation. Landscape is a documented exception recorded in the manifest.
- The final diagram must remain readable when fitted within approximately 16.5 cm × 20.5 cm in the report. Diagrams whose guard text falls below about 6 pt at that size are marked `needs-manual-review`.
- Arrowheads are open (UML style); the renderer converts PlantUML's filled heads.

## 9. Naming and Repository Structure

Use the semantic Use Case key for filenames. The generated display ID (for example `UC-24.2`) appears only in the manifest, the header comment and the reports.

```text
diagrams/activity/
├── manifest.yml                      one entry per concrete Use Case
├── _shared/activity-style.puml       shared style and label helpers
└── <domain-folder>/
    ├── source/UC-<SEMANTIC-KEY>.puml editable source
    └── svg/UC-<SEMANTIC-KEY>.svg     final SVG for the report
```

Domain folders: `account-authentication`, `project-membership`, `product-backlog`, `sprint-management`, `sprint-work`, `collaboration-notification`, `scrum-reporting`, `system-administration`.

Commit only `.puml` and `.svg`. PNG files are QA previews; generate them locally or for Jira and do not commit them. Never commit an exported image without its editable source.

### 9.1 Source conventions

- The first lines are a header comment with the display ID, name, semantic key, YAML path and Business Rules.
- `!include ../../_shared/activity-style.puml` supplies the style; no `title`, `caption`, `header`, `footer` or `legend`.
- Every action is preceded by a trace comment such as `' [NF4, POST1, BR-SPRINT-TASK-ACTIVE-SPRINT]`. Accepted references: `NFn`, `PREn`, `POSTn`, `AF-xx`, `AF-xx.n`, `EX-xx`, the UC's Business Rule keys, `TRIGGER`, `OTHER` (other_information) and `GUIDE-7.3`.
- Decisions use `$question(...)` (or `$question_x(...)` when the flow enters from another partition) and guards use `$guard_left`, `$guard_right` and `$guard`. These helpers only add invisible padding.

### 9.2 Pipeline

```powershell
py scripts/activity_diagrams.py render --all --plantuml-jar tools/plantuml.jar   # or --key UC-...
py scripts/activity_diagrams.py validate   # manifest, traceability, UML and SVG layout checks
py scripts/activity_diagrams.py status     # totals per domain
py scripts/activity_diagrams.py report     # regenerates the two reports in docs/
```

`render` runs PlantUML (1.2024.7 or later) and post-processes the SVG deterministically: white background, presentation frame and header separator, padded outer lane borders and open arrowheads. `tools/plantuml.jar` is not committed; download it or pass `--plantuml-jar`/`PLANTUML_JAR`. `scripts/render-activity-diagrams.ps1` is superseded by this pipeline.

Reports: `docs/activity-diagram-generation-report.md` and `docs/activity-diagram-review-report.md`.

## 10. Report Caption

Use the following caption format below each diagram:

```text
Figure <number>. <Use Case Name> Activity Diagram (<Generated UC ID>)
```

Example:

```text
Figure 2.14. Create Sprint Task Activity Diagram (UC-24.2)
```

## 11. Reference Template

Use **UC-24.2 – Create Sprint Task** as the default two-partition template:

```text
diagrams/activity/sprint-work/source/UC-SPRINT-TASK-CREATE.puml
diagrams/activity/sprint-work/svg/UC-SPRINT-TASK-CREATE.svg
```

The template demonstrates:

- Developer and System partitions.
- Top-to-bottom control flow.
- An exception branch with visible feedback.
- Activity history recording.
- Separate final nodes for the successful and the exceptional outcome.
- Trace comments on every action.

The YAML of UC-24.2 does not describe an invalid-input retry, so the template has no retry loop. Copy the visual configuration, not the UC-24.2 business flow. The generic skeleton is in `.claude/skills/activity-diagram/templates/activity-template.puml`.

## 12. Jira Workflow

Use one Jira subtask for each concrete Use Case Activity Diagram.

Recommended workflow:

1. `To Do`: the diagram has not been started.
2. `In Progress`: the assignee is creating or revising it.
3. `In Review`: source and exported files are available for review.
4. Return to `In Progress` with a **Changes requested** comment if corrections are required.
5. `Done`: one peer reviewer has approved it and the team leader has completed final acceptance.

Attach a PNG preview to Jira when useful. Store the editable source and final SVG in GitHub (no PNG). Copy only accepted final exports to Google Drive for report assembly. The manifest `final_status` is `ready-for-peer-review` when all automated and AI review gates passed; it does not replace peer review or the team leader's acceptance.

## 13. Definition of Done

An Activity Diagram may be moved to `Done` only when all conditions below are satisfied:

- [ ] It represents one concrete Use Case.
- [ ] It matches the current Use Case YAML and referenced Business Rules.
- [ ] Main Flow, relevant Alternative Flows, and Exceptions are represented.
- [ ] Preconditions are assumed rather than redrawn as unrelated activities.
- [ ] Postconditions are visible in the final System actions where appropriate.
- [ ] It contains one Initial Node and valid final outcome nodes.
- [ ] All decisions have complete, mutually exclusive guards.
- [ ] Retry paths return to the correct action.
- [ ] Every action is placed in the responsible swimlane.
- [ ] No exception branch ends without visible feedback or recorded outcome.
- [ ] There are no dangling, overlapping, or ambiguous connectors.
- [ ] Font, colors, line thickness, and spacing match the template.
- [ ] The diagram has a complete presentation frame.
- [ ] No title is placed inside the diagram.
- [ ] The editable source and SVG use the semantic key filename and the `source/` and `svg/` folders.
- [ ] `py scripts/activity_diagrams.py validate` passes.
- [ ] The SVG remains readable when inserted into the Word report.
- [ ] One peer reviewer has approved the diagram.
- [ ] The team leader has completed final acceptance.

## 14. Reviewer Comment Template

Use this format when requesting changes:

```text
Changes requested

UC: <Generated UC ID> — <Use Case Name>

Required corrections:
1. <Mismatch with Main Flow, AF, EX, postcondition, or Business Rule>
2. <Incorrect UML node, guard, merge, lane, or connector>
3. <Visual inconsistency or unreadable export>

Acceptance evidence:
- Updated editable source
- Updated SVG
- Validation output
- Confirmation that the diagram was checked against the current YAML
```

## 15. Short Jira Parent Description

```text
Create and review one UML Activity Diagram for every concrete Use Case. Follow the attached Activity Diagram guideline and use the UC-24.2 diagram as the visual template. Each subtask must provide an editable source and SVG; match the approved Use Case YAML and Business Rules; pass one peer review; and receive final approval from the team leader.
```
