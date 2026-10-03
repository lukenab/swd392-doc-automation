# UML activity rules and PlantUML patterns

## UML semantics (UML 2.5.1, clause 15)

- **Initial node**: exactly one per diagram in this project (`start`).
- **Activity final**: ends the whole activity when reached. Several are allowed (UML); the team convention is
  one per distinct outcome: merge paths with the same outcome, and use one shared final when different
  outcomes are interleaved on nested branches. A **flow final** ends one flow only; use it only when another flow
  continues.
- **Decision node**: one incoming edge, guarded outgoing edges. Guards are in `[ ]`, mutually exclusive and
  complete. A combined merge/decision is allowed.
- **Merge node**: brings alternative paths together before they continue.
- **Fork/join**: only for real concurrency. None of the current use cases need it.
- **Partitions**: show responsibility. A decision's partition has no extra semantics, but place it in the
  partition of whoever decides when the layout allows.

## Flow rules used in this repository

- Normal flow top to bottom; one action per YAML step (split a step only when two actors are involved).
- Alternative flow (R-AF-REJOIN): resume after the step where it was raised, or return to the step it
  re-performs; cancellation and terminal AFs end.
- Exception (R-EX): one System reject/report action; it then joins the final of its outcome (merge).
- A precondition contradicted by an EX/AF the System can detect → defensive System check + observation.
  An AF that needs the actor to start from a state the preconditions exclude → `BLOCKED — REQUIREMENT CONFLICT`.

## PlantUML patterns (verified with 1.2024.7 and 1.2025.10)

| Need | Pattern | Avoid |
|---|---|---|
| Exception in the same partition | empty `then`, `else` with reject + `stop` (only when no other path has the same outcome) | long guard text on the bypass side |
| Several paths with the same outcome | nest the remaining flow in `then`; put each reject in `else`; one `stop` after the outer `endif` | a `stop` in every branch |
| Two outcomes in different partitions | both branches non-empty; the cross-partition branch in `else` | a `then` branch whose first node is in another partition (its label is crossed) |
| Loop | `while (q) is ([loop guard]) ... endwhile ([exit guard])` | `repeat while` (guards dropped), `backward`, `goto` |
| Three-way choice | nested binary `if` | `elseif` (hexagons), `switch` |
| Flow entering a decision from another partition | `$question_x(...)` | `$question(...)` (question text is crossed) |
| After an if-block whose branch switched partition | re-declare the partition before the next node | relying on the previous partition |
| Action text | no `;` inside the text | `;` (ends the action) |
| Wide exception action | one line, so the bypass line passes outside the label | short boxes next to long guards |

Keep guard lines short (about 16 characters per line); use `$guard_right("[first line", "second line]")`.
