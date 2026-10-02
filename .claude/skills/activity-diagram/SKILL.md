---
name: activity-diagram
description: Generate, fix or review SWD392 UML Activity Diagrams (PlantUML) from the concrete Use Case YAML files in this repository, using the shared style, trace comments, manifest and the scripts/activity_diagrams.py render/validate pipeline.
---

# Activity Diagram generation (SWD392)

Use this skill to create, update or review an Activity Diagram for one or more **concrete** Use Cases in
`data/use_cases/**`. Abstract `Manage ...` parents never get a diagram. The rules here implement
`docs/activity-diagram-guideline.md`; when the two disagree, the guideline wins.

## Inputs, in order of authority

1. The concrete Use Case YAML (`data/use_cases/<domain>/<KEY>.yml`).
2. The Business Rules it references (`data/business_rules`).
3. Actor and group definitions in `data/`.
4. Approved documents in `docs/`.
5. Existing diagrams — reference only, never authoritative.

Never add behaviour, validations, actors or exceptions that these sources do not contain.

## Workflow

1. Read the YAML: trigger, preconditions, normal flow, alternative flows, exceptions, postconditions,
   business rules, other information. Read each referenced Business Rule.
2. Decide whether the UC can be drawn. Stop for that UC and record it in `diagrams/activity/manifest.yml` when:
   - two sources conflict, or an alternative flow needs a starting state that a precondition excludes →
     `final_status: BLOCKED — REQUIREMENT CONFLICT`;
   - a step the flow depends on is missing (for example an AF refers to a step that does not exist) →
     `final_status: BLOCKED — INSUFFICIENT SPECIFICATION`.
   Give `blocked_reason` and `questions`, create no `.puml`/`.svg`, and continue with other UCs.
3. Choose partitions (see `references/repository-mapping.md`): the responsible role, `System`, and any external
   service that acts. Never collapse Project Owner, Product Owner or Developer into `User` when the role matters.
4. Copy `templates/activity-template.puml` to `diagrams/activity/<domain>/source/<KEY>.puml` and write the flow
   following `references/uml-activity-rules.md`. Put a trace comment before **every** action.
5. Render and check:
   ```powershell
   py scripts/activity_diagrams.py render --key <KEY> --plantuml-jar tools/plantuml.jar
   py scripts/activity_diagrams.py validate
   ```
   Fix every reported layout issue (crossed labels, overlaps) by re-arranging branches, not by moving text by hand.
6. Inspect the SVG visually (convert to PNG for QA only — never commit PNGs) with
   `references/review-checklist.md`.
7. Update the manifest entry statuses and run `py scripts/activity_diagrams.py report`.

## Non-negotiable rules

- Authentication is a precondition. Log In appears only in `UC-SIGN-IN`.
- English, Times New Roman, portrait, top to bottom, white background, no title inside the diagram.
- One `start`. Merge paths that share a postcondition into one final; separate finals only for different
  outcomes. Never claim UML requires exactly one final node.
- Every decision has a question and a guard on every outgoing edge; AF/EX identifiers appear in guards.
- Each exception: one System reject/report action (trace `GUIDE-7.3` when the YAML gives no outcome), then a final.
- Undescribed validation failures are not drawn; they become manifest `observations`.
- Filenames use the semantic key; the display ID goes only in the header comment, manifest and reports.

## Files

- `templates/activity-template.puml` — skeleton with header, partitions, an exception and a loop.
- `templates/activity-style.puml` — copy of `diagrams/activity/_shared/activity-style.puml` (the shared file is
  the one that sources include).
- `references/uml-activity-rules.md` — UML semantics and PlantUML patterns that render cleanly.
- `references/repository-mapping.md` — domains, folders, partitions, manifest fields and statuses.
- `references/review-checklist.md` — traceability, UML and visual review gates.
