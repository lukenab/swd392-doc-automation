# Legacy Activity Diagrams — archived 2026-10-03

These files were created before the Stage 2 Activity Diagram pipeline (`scripts/activity_diagrams.py`,
`diagrams/activity/manifest.yml`). They are kept unchanged, with their original relative paths under this folder,
so that no editable source is lost. They are **not authoritative**; the current diagrams are listed in
`diagrams/activity/manifest.yml`.

Reason for archiving: the old files do not follow the Stage 2 structure (`<domain>/source` and `<domain>/svg`,
semantic-key filenames, trace comments, shared style, responsibility-specific partitions, Times New Roman) and
would otherwise be reported as unexpected files by `py scripts/activity_diagrams.py validate`.

| Original location | Archived copy | Editable source? | Replaced by |
|---|---|---|---|
| `diagrams/activity/nguyen-an-binh/UC-06-create-project.puml` | `diagrams/activity/nguyen-an-binh/UC-06-create-project.puml` | Yes (PlantUML) | `diagrams/activity/project-membership/source/UC-PROJECT-CREATE.puml` |
| `diagrams/activity/nguyen-an-binh/UC-09.2-add-project-member.puml` | `diagrams/activity/nguyen-an-binh/UC-09.2-add-project-member.puml` | Yes (PlantUML) | `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-ADD.puml` |
| `diagrams/activity/nguyen-an-binh/UC-12-transfer-project-ownership.puml` | `diagrams/activity/nguyen-an-binh/UC-12-transfer-project-ownership.puml` | Yes (PlantUML) | `diagrams/activity/project-membership/source/UC-PROJECT-OWNERSHIP-TRANSFER.puml` |
| `diagrams/activity/nguyen-an-binh/UC-13-leave-project.puml` | `diagrams/activity/nguyen-an-binh/UC-13-leave-project.puml` | Yes (PlantUML) | `diagrams/activity/project-membership/source/UC-PROJECT-LEAVE.puml` |
| `diagrams/activity/sprint-work/UC-SPRINT-TASK-CREATE.puml` (never committed before) | `diagrams/activity/sprint-work/UC-SPRINT-TASK-CREATE.puml` | Yes (PlantUML) | `diagrams/activity/sprint-work/source/UC-SPRINT-TASK-CREATE.puml` |
| `diagrams/activity/sprint-work/UC-SPRINT-TASK-CREATE.svg` (never committed before) | `diagrams/activity/sprint-work/UC-SPRINT-TASK-CREATE.svg` | Export of the source above | `diagrams/activity/sprint-work/svg/UC-SPRINT-TASK-CREATE.svg` |

Not committed, left in the working copy only:

- `diagrams/activity/sprint-work/UC-SPRINT-TASK-CREATE.png` was moved next to its archived source but is not
  committed, because PNG files are QA previews only.
- `output/activity-diagrams/nguyen-an-binh/` (SVG and PNG renders of the four archived sources) stays where it
  is; `output/` is ignored by Git.

`scripts/render-activity-diagrams.ps1`, which rendered the archived sources, is left unchanged and is superseded
by `scripts/activity_diagrams.py`.
