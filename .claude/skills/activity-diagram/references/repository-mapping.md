# Repository mapping

| Group (YAML `group`) | Domain folder | Display IDs |
|---|---|---|
| ACCOUNT_AUTHENTICATION | `account-authentication` | UC-01 – UC-05.3 |
| PROJECT_MEMBERSHIP | `project-membership` | UC-06 – UC-13 |
| PRODUCT_BACKLOG | `product-backlog` | UC-14.1 – UC-18 |
| SPRINT_MANAGEMENT | `sprint-management` | UC-19 – UC-22 |
| SPRINT_WORK | `sprint-work` | UC-23 – UC-27.5 |
| COLLABORATION_NOTIFICATION | `collaboration-notification` | UC-28 – UC-30 |
| SCRUM_REPORTING | `scrum-reporting` | UC-31 |
| SYSTEM_ADMINISTRATION | `system-administration` | UC-32.1 – UC-33 |

Paths: `diagrams/activity/<folder>/source/<KEY>.puml` and `diagrams/activity/<folder>/svg/<KEY>.svg`.

## Partitions

`Guest`, `User`, `Project Owner`, `Product Owner`, `Developer`, `System Administrator`, `System`,
`Email Service`, `Identity Provider`. The YAML writes most actors as `User`; use the role named in the
preconditions or in "Acting as the ..." steps.

## Trace references accepted by the validator

`NFn`, `PREn`, `POSTn`, `AF-xx`, `AF-xx.n`, `EX-xx`, the UC's own Business Rule keys, `TRIGGER`, `OTHER`
(other_information) and `GUIDE-7.3` (exception outcome not specified in the YAML).

## Manifest (`diagrams/activity/manifest.yml`)

Fields per entry: `key`, `display_id`, `name`, `group`, `primary_actor`, `secondary_actors`, `assignee` (from the
guideline's assignment table, otherwise `TBD`), `source`, `svg`, `generation_status` (`generated`, `missing`,
`blocked`), `traceability_status`, `uml_review_status`, `visual_review_status`, `final_status`, `blocked_reason`,
plus optional `questions`, `observations` and `review_notes`.

`final_status` values: `ready-for-peer-review` (all gates passed; peer and leader approval still needed),
`needs-manual-review` (generated, but a reviewer must decide something, for example A4 legibility),
`BLOCKED — REQUIREMENT CONFLICT`, `BLOCKED — INSUFFICIENT SPECIFICATION`.
