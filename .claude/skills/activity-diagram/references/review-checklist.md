# Review checklist

## Traceability

- [ ] Every action has a trace comment, and every reference exists in the YAML (`validate` checks this).
- [ ] Every normal-flow step, alternative flow and exception is represented.
- [ ] No action, decision or guard adds behaviour that the YAML or Business Rules do not state.
- [ ] Undescribed failures are recorded as observations, not drawn.

## UML

- [ ] One initial node; finals merged when the postcondition is the same.
- [ ] Every decision has a question and a guard on each outgoing edge; guards are exclusive and complete.
- [ ] Alternative flows rejoin after the step that raised them, or end when terminal.
- [ ] Each exception ends with a System reject/report action before its final.
- [ ] Actions are in the responsible partition; no Log In outside UC-SIGN-IN; no fork without concurrency.

## Visual (inspect the rendered SVG; PNG only for QA)

- [ ] `validate` reports no crossed, overlapping or touching labels.
- [ ] Nothing clipped; frame, header separator and lane borders complete.
- [ ] Times New Roman only, white background, open arrowheads, no title inside the diagram.
- [ ] Portrait; guard text at least about 6 pt when fitted to 16.5 x 20.5 cm, otherwise `needs-manual-review`.
- [ ] Decisions sit in the partition of whoever decides, or the exception is noted.
