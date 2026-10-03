# Activity Diagram Audit Report

Audit of every Activity Diagram on branch `docs/activity-diagrams`, baseline commit `72215fd`, performed 2026-10-03.
Reviewer role: Senior Business Analyst / UML Activity Diagram reviewer (AI-assisted; peer review and team-leader acceptance are still required by the Definition of Done).

## Method and sources

- Concrete use cases were found by scanning `data/use_cases/**.yml` (62 use cases, 7 abstract `Manage …` parents, **55 concrete**). The count was not assumed.
- Every element of every `.puml` source (initial node, action, decision, guard, loop, merge, final) was extracted and compared with the Use Case YAML (normal_flow, alternative_flows, exceptions, pre/postconditions, other_information) and the referenced Business Rules in `data/business_rules.yml`. Trace comments in the sources were used only to locate the claimed source; each action text was compared with the step text itself.
- Each rendered SVG was checked against its source: every action, decision and guard text and the number of final nodes must appear in the SVG (`0` mismatches after the fixes).
- Business Rules were treated as constraints. No action exists only because of a Business Rule.
- Support levels: EXPLICIT (described directly in the YAML), NECESSARY REPRESENTATION (UML notation that connects described flows: initial node, merge, complementary guard, a decision that carries an AF/EX condition), DERIVED (inferred from written content; the inference is stated), UNSUPPORTED, CONFLICT, UNCLEAR.
- UML rule vs. convention: UML 2.5.1 allows several ActivityFinalNodes, and the first one reached terminates the activity (OMG UML 2.5.1, clause 15.3 Control Nodes; classifier descriptions 15.7.3 ActivityFinalNode and 15.7.16 FlowFinalNode, located through the specification table of contents). "One final per outcome" is the team convention in `docs/activity-diagram-guideline.md` §5, not a UML rule. The 6 pt legibility threshold is a team recommendation.

## A. Audit summary

| Measure | Before fixes | After fixes |
|---|---:|---:|
| Concrete use cases found | 55 | 55 |
| `.puml` sources / SVG files | 53 / 53 | 53 / 53 |
| Use cases without source or SVG | 2 (UC-25, UC-27.4 — BLOCKED) | 2 (unchanged) |
| Diagrams with an UNSUPPORTED or CONFLICT element | 3 (UC-15.2, UC-18, UC-22) | 0 |
| Diagrams whose end nodes needed changes | 25 | 0 (UC-13 keeps two same-outcome finals, explained) |
| Activity Final nodes in total | 143 | 104 |
| Flow Final nodes | 0 | 0 |
| Spec exceptions not represented on every path that can raise them | 1 (UC-01 EX-03 on the Google path) | 0 |
| Source comments citing an unrelated Business Rule | 3 (UC-19, UC-24.5, UC-33) | 0 |
| Diagrams below the 6 pt legibility threshold (portrait A4) | 8 | 7 |

## Findings by severity (baseline)

| # | Severity | Diagram / file | Element | Evidence | Minimal fix | Status |
|---|---|---|---|---|---|---|
| 1 | Major | UC-22 `sprint-management/source/UC-SPRINT-CANCEL.puml` | Action “Cancel the confirmation” in the System partition | `UC-SPRINT-CANCEL.yml` AF-01 step 1: «The Product Owner cancels the confirmation.» The else-branch inherited the System partition from the then-branch | Declare the Product Owner partition at the start of the AF-01 branch | Fixed |
| 2 | Major | UC-15.2 `product-backlog/source/UC-BACKLOG-ITEM-CREATE.puml` | Action “Save the incomplete information as a draft item” in the System partition | `UC-BACKLOG-ITEM-CREATE.yml` AF-01 condition: «The User saves incomplete information as a draft item.» The System action also repeated the storing of AF-01.1 | Make it the Product Owner's action “Save the incomplete information as a draft”; keep AF-01.1 as the System action | Fixed |
| 3 | Major | UC-01 `account-authentication/source/UC-ACCOUNT-REGISTER.puml` | EX-03 shown only after NF5 (email path) | EX-03 «Account data cannot be persisted, so no User account is created.»; AF-01 step 3 also creates an account | Add the EX-03 decision after AF-01.3 | Fixed |
| 4 | Major | 25 diagrams (see section C) | Several Activity Finals with the same outcome; UC-30 also shared one final between two different outcomes | Guideline §5 convention: same outcome → one final | Nest the remaining flow and merge the same-outcome paths into one final | Fixed (UC-13 kept, explained) |
| 5 | Minor | UC-18 `product-backlog/source/UC-BACKLOG-ITEM-ESTIMATE.puml` | Action “Return the item **to the Product Owner** for further refinement” | AF-01 step 2: «The item is returned for further refinement.» — no recipient | Remove “to the Product Owner” | Fixed |
| 6 | Minor | UC-02 `UC-SIGN-IN.puml` | Decision “Password forgotten?” in the System partition reads as a System judgement | AF-02 condition: «The User has forgotten the locally managed password.»; NF1: the User chooses the log-in option | Rename to “Forgot Password chosen?” (routes the User's choice). Moving the decision to the User partition made flow lines cross the action texts | Fixed (renamed) |
| 7 | Minor | UC-17 `UC-BACKLOG-ITEM-REFINE.puml` | Decision “Too large for one Sprint?” in the System partition | NF4: the Developer proposes decomposition when needed; AF-01 condition has no System actor | Move the decision to the Developer partition | Fixed |
| 8 | Minor | UC-01 `UC-ACCOUNT-REGISTER.puml` | Decision “Registration method?” in the System partition | NF1: the Guest chooses the method; the decision only routes that choice | None needed; kept | No change |
| 9 | Minor | UC-19 `UC-SPRINT-PLAN.puml` | Trace comment on the EX-01 rejection cites BR-SPRINT-DATE-RANGE | BR-SPRINT-DATE-RANGE: end date after start date, at most one month; EX-01 is about a conflict with another Sprint | Remove the BR from the comment (not visible in the SVG) | Fixed |
| 10 | Minor | UC-24.5 `UC-SPRINT-TASK-DELETE.puml` | Trace comment on the EX-01 rejection cites BR-SPRINT-TASK-ACTIVE-SPRINT | EX-01: the task has already entered execution; the BR is about belonging to the active Sprint | Remove the BR from the comment | Fixed |
| 11 | Minor | UC-33 `UC-SYSTEM-AUDIT-LOG-REVIEW.puml` | Trace comment on NF2 cites BR-SYSADMIN-NO-PROJECT-AUTO-ACCESS | The BR concerns project content, not the audit list | Remove the BR from the comment | Fixed |

No Critical finding: no diagram contradicts a business outcome of its Use Case.

## B. Actions and steps not supported by the Use Case

| UC | Element (baseline) | Level | Evidence | Resolution |
|---|---|---|---|---|
| UC-22 | “Cancel the confirmation” (System) | CONFLICT | AF-01.1 names the Product Owner as actor | Moved to the Product Owner partition |
| UC-15.2 | “Save the incomplete information as a draft item” (System) | CONFLICT | AF-01 condition names the User as actor; storing is already AF-01.1 | Re-drawn as the Product Owner's action |
| UC-18 | “Return the item to the Product Owner for further refinement” | UNSUPPORTED (added recipient) | AF-01.2 names no recipient | Recipient removed |

Generic steps that are often added were checked one by one. All remaining ones have a concrete source:

- **Validate / verify / check**: each is a YAML step (for example UC-24.3 NF4 «Validates and saves the changes», UC-07 NF2 «Verifies the actor's active project membership»).
- **Record … activity history / audit event / security event**: each comes from a postcondition (POST2 in UC-05.3, 08, 09.2, 10, 14.2, 14.3, 15.2, 15.3, 18, 24.2, 24.3) or from the step text (UC-09.3 NF5, UC-24.5 NF4, UC-32.2–32.4 NF4); UC-20 comes from other_information «The Sprint start time is recorded in the activity history». Classified DERIVED where only a postcondition states it.
- **Reject / report / deny** after an exception: DERIVED when the YAML names the exception but not its outcome (trace `GUIDE-7.3`); EXPLICIT when the exception text states the outcome (for example UC-01 EX-01, UC-04 EX-01, UC-28 EX-02).
- **Refresh**: only where the step says so (UC-09.2 NF5, UC-26 NF4). **Notify / send email**: only UC-28 NF5–NF6. **Confirm**: only where a step or condition names a confirmation; UC-10 “Confirm the replacement” is DERIVED from AF-01.1 (request confirmation) and AF-01.2 («after confirmation»).
- **Retry loops**: only where an AF re-performs a step (UC-01 AF-02, 06 AF-01, 08 AF-01, 12 AF-01, 16 AF-01, 19 AF-01, 20 AF-01, 21 AF-01, 26 AF-01, 28 AF-01). **Initialize default data**: only UC-06 NF6.

Spec → diagram: every normal-flow step, alternative-flow step and exception of every drawn use case is represented (checked by `scripts/activity_diagrams.py validate` and by step-level coverage). Postconditions that only state that nothing else changes (UC-01 POST2, UC-02 POST2, UC-03 POST3, UC-04 POST3, UC-07 POST2, UC-12 POST2) need no action.

## C. End nodes

### C.1 Per-diagram summary (changed diagrams)

| UC | Actions before → after | Decisions before → after | Activity Finals before → after | Guard text on A4 (pt) before → after | AF/EX still represented |
|---|---|---|---|---|---|
| UC-01 `UC-ACCOUNT-REGISTER` | 17 → 18 | 5 → 6 | 4 → 1 | 4.4 → 3.3 | yes |
| UC-02 `UC-SIGN-IN` | 15 → 14 | 7 → 6 | 7 → 1 | 4.6 → 3.7 | yes |
| UC-04 `UC-PASSWORD-RESET` | 13 → 13 | 5 → 5 | 6 → 2 | 4.3 → 3.5 | yes |
| UC-05.2 `UC-PROFILE-UPDATE` | 8 → 8 | 2 → 2 | 3 → 2 | 6.3 → 7.0 | yes |
| UC-05.3 `UC-PASSWORD-CHANGE` | 9 → 9 | 3 → 3 | 4 → 2 | 6.2 → 6.6 | yes |
| UC-09.2 `UC-PROJECT-MEMBER-ADD` | 8 → 8 | 2 → 2 | 3 → 2 | 7.5 → 7.1 | yes |
| UC-09.3 `UC-PROJECT-MEMBER-REMOVE` | 7 → 7 | 2 → 2 | 3 → 2 | 8.1 → 6.7 | yes |
| UC-11 `UC-PROJECT-ARCHIVE` | 7 → 7 | 2 → 2 | 3 → 2 | 8.5 → 6.2 | yes |
| UC-13 `UC-PROJECT-LEAVE` | 8 → 8 | 3 → 3 | 3 → 3 | 7.0 → 7.0 | yes |
| UC-14.3 `UC-PRODUCT-GOAL-UPDATE` | 8 → 8 | 2 → 2 | 3 → 2 | 5.8 → 6.6 | yes |
| UC-15.2 `UC-BACKLOG-ITEM-CREATE` | 9 → 9 | 2 → 2 | 2 → 2 | 6.1 → 7.7 | yes |
| UC-15.4 `UC-BACKLOG-ITEM-REMOVE` | 6 → 6 | 2 → 2 | 3 → 2 | 9.2 → 6.4 | yes |
| UC-17 `UC-BACKLOG-ITEM-REFINE` | 9 → 9 | 2 → 2 | 2 → 2 | 6.7 → 6.5 | yes |
| UC-18 `UC-BACKLOG-ITEM-ESTIMATE` | 10 → 10 | 3 → 3 | 3 → 3 | 4.9 → 5.4 | yes |
| UC-19 `UC-SPRINT-PLAN` | 9 → 9 | 2 → 2 | 2 → 2 | 6.2 → 6.2 | yes |
| UC-22 `UC-SPRINT-CANCEL` | 8 → 8 | 2 → 2 | 3 → 2 | 7.6 → 6.5 | yes |
| UC-23 `UC-SPRINT-BOARD-REVIEW` | 7 → 7 | 3 → 3 | 3 → 2 | 6.5 → 6.5 | yes |
| UC-24.3 `UC-SPRINT-TASK-UPDATE` | 8 → 8 | 2 → 2 | 3 → 2 | 6.1 → 6.8 | yes |
| UC-24.5 `UC-SPRINT-TASK-DELETE` | 6 → 6 | 2 → 2 | 3 → 2 | 8.8 → 6.9 | yes |
| UC-24.6 `UC-TASK-DEPENDENCY-ADD` | 7 → 7 | 2 → 2 | 3 → 2 | 8.6 → 8.2 | yes |
| UC-24.7 `UC-TASK-DEPENDENCY-REMOVE` | 7 → 7 | 2 → 2 | 3 → 2 | 7.0 → 7.4 | yes |
| UC-27.3 `UC-SUBTASK-UPDATE` | 8 → 8 | 3 → 3 | 3 → 2 | 6.5 → 6.4 | yes |
| UC-27.5 `UC-SUBTASK-DELETE` | 6 → 6 | 2 → 2 | 3 → 2 | 6.1 → 6.7 | yes |
| UC-30 `UC-NOTIFICATIONS-REVIEW` | 9 → 9 | 5 → 5 | 4 → 1 | 4.5 → 4.6 | yes |
| UC-32.1 `UC-USER-ACCOUNTS-SEARCH` | 6 → 6 | 2 → 2 | 3 → 2 | 8.6 → 7.9 | yes |
| UC-32.2 `UC-USER-ACCOUNT-SUSPEND` | 7 → 6 | 3 → 2 | 4 → 2 | 7.4 → 6.2 | yes |
| UC-32.3 `UC-USER-ACCOUNT-REACTIVATE` | 6 → 6 | 2 → 2 | 3 → 2 | 8.1 → 6.4 | yes |
| UC-32.4 `UC-USER-ACCOUNT-DELETE` | 7 → 6 | 3 → 2 | 4 → 2 | 7.4 → 6.3 | yes |
| UC-33 `UC-SYSTEM-AUDIT-LOG-REVIEW` | 7 → 7 | 2 → 2 | 3 → 2 | 8.1 → 8.8 | yes |

Action-count changes: UC-01 +1 (EX-03 rejection on the Google path); UC-02 −1 (EX-01 and EX-02 share one rejection on the email path, NF4 checks both); UC-32.2 and UC-32.4 −1 (EX-01 and EX-02 share one rejection; precondition 3 groups both as protected accounts). No alternative or exception flow was removed.

### C.2 Every end node before the fixes (baseline `72215fd`)

| UC | End node | Đường đi đến node | Kết quả/postcondition | Loại UML hiện dùng | Đánh giá | Hướng sửa |
|---|---|---|---|---|---|---|
| UC-01 | F1 | [email and password] > [not persisted — EX-03] → “Reject the registration so that no account is created” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-01 | F2 | [email and password] > [not delivered — EX-01] → “Keep the account pending so that verification can be requested again” | account stays pending; verification can be requested again | Activity Final (`stop`) | Distinct outcome | Keep |
| UC-01 | F3 | [Google — AF-01] > [not returned — EX-02] → “Cancel the registration because no valid verified identity was returned” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-01 | F4 | (main flow) → “Validate email uniqueness and create an active User account” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-02 | F1 | [forgotten — AF-02] → “Direct the User to Forgot Password” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2, F3, F4, F5, F6 | Merge into one Activity Final |
| UC-02 | F2 | [email and password] > [invalid — EX-01] → “Reject the log-in without creating a session” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F3, F4, F5, F6 | Merge into one Activity Final |
| UC-02 | F3 | [email and password] > [pending, suspended or deleted — EX-02] → “Reject the log-in for the inactive account” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2, F4, F5, F6 | Merge into one Activity Final |
| UC-02 | F4 | [Google — AF-01] > [unavailable or rejected — EX-03] → “End the log-in without creating a session” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2, F3, F5, F6 | Merge into one Activity Final |
| UC-02 | F5 | [Google — AF-01] > [no matching account — EX-04] → “Direct the person to Register Account without creating a session” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2, F3, F4, F6 | Merge into one Activity Final |
| UC-02 | F6 | [Google — AF-01] > [not active — EX-02] → “Reject the log-in for the inactive account” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2, F3, F4, F5 | Merge into one Activity Final |
| UC-02 | F7 | (main flow) → “Create an authenticated session” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-03 | F1 | [still valid] > [cannot be revoked — EX-01] → “Remove the local credentials and report that remote revocation could not be confirmed” | local credentials removed; remote revocation not confirmed | Activity Final (`stop`) | Distinct outcome: local credentials removed but remote revocation not confirmed (EX-01). Keep | Keep |
| UC-03 | F2 | (main flow) → “Display the public log-in page” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-04 | F1 | [Google only — AF-02] → “Continue to authenticate through Google” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2, F3, F4, F5 | Merge into one Activity Final |
| UC-04 | F2 | [no eligible account] → “Continue to authenticate through Google” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F3, F4, F5 | Merge into one Activity Final |
| UC-04 | F3 | [not delivered — EX-01] → “Record the delivery failure without exposing whether the account exists” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2, F4, F5 | Merge into one Activity Final |
| UC-04 | F4 | [invalid, expired or used — AF-01] → “Allow the User to submit a new Forgot Password request” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2, F3, F5 | Merge into one Activity Final |
| UC-04 | F5 | [status changed — EX-02] → “Reject the password reset for the changed account” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2, F3, F4 | Merge into one Activity Final |
| UC-04 | F6 | (main flow) → “Update the password and invalidate the used token” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.1 | F1 | [unavailable — EX-01] → “Report that the profile information is temporarily unavailable” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.1 | F2 | (main flow) → “Display the User's profile and non-sensitive account information” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.2 | F1 | [submit] > [invalid values — EX-01] → “Reject the profile changes and keep the stored profile” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-05.2 | F2 | [submit] → “Display the updated profile” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.2 | F3 | [cancel before saving — AF-01] → “Discard the unsaved changes” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-05.3 | F1 | [provider only — AF-01] → “Inform the User that the password must be changed through that provider” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2, F3 | Merge into one Activity Final |
| UC-05.3 | F2 | [incorrect — EX-01] → “Reject the password change” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F3 | Merge into one Activity Final |
| UC-05.3 | F3 | [not satisfied — EX-02] → “Reject the new password” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2 | Merge into one Activity Final |
| UC-05.3 | F4 | (main flow) → “Record the password change as a security event” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-06 | F1 | [not persisted — EX-01] → “Reject the project creation because the data cannot be persisted” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-06 | F2 | (main flow) → “Initialize the Product Backlog and default Sprint Board” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-07 | F1 | [project or membership removed — EX-01] → “Deny access to the project dashboard for this actor” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-07 | F2 | (main flow) → “Display the dashboard in read-only mode” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-08 | F1 | [ownership changed — EX-01] → “Reject the update because ownership changed” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-08 | F2 | (main flow) → “Confirm the successful update” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.1 | F1 | [unavailable — EX-01] → “Report that membership information is temporarily unavailable” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.1 | F2 | (main flow) → “Display only the Project Owner” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.2 | F1 | [already a member — AF-01] → “Report that no new membership is required” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-09.2 | F2 | [became inactive — EX-01] → “Reject the addition of the inactive account” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-09.2 | F3 | (main flow) → “Record the membership change in project activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.3 | F1 | [own membership — EX-01] → “Reject the removal of the Project Owner's own membership” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-09.3 | F2 | [owns unfinished work — AF-01] → “Require the work to be reassigned before removal” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-09.3 | F3 | (main flow) → “Record the removal and refresh the member list” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-10 | F1 | [left or removed — EX-01] → “Reject the assignment for the departed member” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-10 | F2 | (main flow) → “Record the accountability change in activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-11 | F1 | [active Sprint — EX-01] → “Reject the archival because the project has an active Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-11 | F2 | [confirm] → “Mark the project and its contained work as read-only” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-11 | F3 | [cancel — AF-01] → “Leave the project active and unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-12 | F1 | [changed concurrently — EX-01] → “Reject the transfer because ownership changed concurrently” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-12 | F2 | (main flow) → “Transfer ownership atomically and record the change” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-13 | F1 | [current owner — EX-01] → “Reject the request until ownership is transferred” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-13 | F2 | [owns tasks — AF-01] > [cancel — AF-01] → “Cancel the leave request” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-13 | F3 | (main flow) → “Remove active membership and project-scoped permissions” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.1 | F1 | (main flow) → “Display that the Product Goal is not yet available” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.2 | F1 | [empty — EX-01] → “Reject the empty Product Goal” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.2 | F2 | (main flow) → “Record the creation in project activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.3 | F1 | [save] > [accountability lost — EX-01] → “Reject the revision from the former Product Owner” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-14.3 | F2 | [save] → “Record the change in project activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.3 | F3 | [cancel before saving — AF-01] → “Keep the current Product Goal unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-15.1 | F1 | [no longer available — EX-01] → “Report that the selected item is no longer available” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.1 | F2 | (main flow) → “Display the item details and related Sprint information” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.2 | F1 | [complete] > [missing — EX-01] → “Reject the item without identifying information” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.2 | F2 | (main flow) → “Record the creation in item activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.3 | F1 | [changed by another User — EX-01] → “Reject the update because the item was changed concurrently” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.3 | F2 | (main flow) → “Record the update in item activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.4 | F1 | [locked in the active Sprint — EX-01] → “Reject the removal of the locked item” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-15.4 | F2 | [confirm] → “Remove the item and record the action” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.4 | F3 | [cancel — AF-01] → “Leave the Product Backlog Item unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-16 | F1 | [cannot be saved — EX-01] → “Reject the order because it cannot be saved completely and uniquely” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-16 | F2 | (main flow) → “Display the updated Product Backlog” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-17 | F1 | [too large — AF-01] > [selected — EX-01] → “Reject the decomposition of the item in the active Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Kept. UNCLEAR whether refinement should continue with NF5–NF6 after EX-01 (the exception only forbids substantial decomposition) | Keep |
| UC-17 | F2 | (main flow) → “Save the refined item and record the participants” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-18 | F1 | [not refined — AF-01] → “Return the item to the Product Owner for further refinement” | estimate unset; item returned for further refinement | Activity Final (`stop`) | Distinct outcome: the item is returned for further refinement (AF-01.2). Keep | Keep |
| UC-18 | F2 | [unavailable — EX-01] → “Reject the estimate because the item was removed or is in a completed Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-18 | F3 | (main flow) → “Record the estimate change in item activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-19 | F1 | [conflict — EX-01] → “Reject saving the Sprint because its date range conflicts with another Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-19 | F2 | (main flow) → “Create the Draft Sprint and its initial Sprint Backlog” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-20 | F1 | [already active — EX-01] → “Reject the start because another Sprint is already active” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-20 | F2 | (main flow) → “Record the Sprint start time in the activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-21 | F1 | [state changed — EX-01] → “Reject the completion because the Sprint state has changed” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-21 | F2 | (main flow) → “Record the Sprint result for reporting” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-22 | F1 | [already completed or cancelled — EX-01] → “Reject the cancellation because the Sprint is no longer active” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-22 | F2 | [confirm] → “Record the cancellation reason and timestamp” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-22 | F3 | [continue the Sprint — AF-01] → “Leave the Sprint unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-23 | F1 | [active Sprint] > [unavailable — EX-01] → “Report that the Sprint Board cannot be loaded at this time” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-23 | F2 | [active Sprint] → “Display item priority, assignee, estimate and status” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-23 | F3 | [no active Sprint — AF-01] → “Offer access to previous Sprint information” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-24.1 | F1 | [no longer available — EX-01] → “Report that the selected Sprint Task is no longer available” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.1 | F2 | (main flow) → “Display the Sprint Task” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.2 | F1 | [belongs to the active Sprint] → “Record the creation in work item activity” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.2 | F2 | [no longer belongs to the active Sprint — EX-01] → “Reject the task creation” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.3 | F1 | [submit] > [no longer in the active Sprint — EX-01] → “Reject the update because the task is no longer in the active Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-24.3 | F2 | [submit] → “Record the update in work item activity” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.3 | F3 | [cancel before saving — AF-01] → “Discard the unsaved task changes” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-24.4 | F1 | [assign] > [no longer active — EX-01] → “Reject the assignment to the inactive member” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.4 | F2 | [assign] → “Save the assignment and record the change” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.4 | F3 | [clear the current assignment — AF-01] → “Mark the Sprint Task as unassigned” | task left unassigned | Activity Final (`stop`) | Distinct outcome: the task is left unassigned (AF-01). Keep | Keep |
| UC-24.5 | F1 | [in execution — EX-01] → “Reject the deletion of the started task” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-24.5 | F2 | [dependent tasks — AF-01] → “Require the dependencies to be removed before deletion” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-24.5 | F3 | (main flow) → “Delete the task and record the action” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.6 | F1 | [same task — EX-02] → “Reject the dependency of the task on itself” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-24.6 | F2 | [direct or indirect cycle — EX-01] → “Reject the dependency that would create a cycle” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-24.6 | F3 | (main flow) → “Store the dependency” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.7 | F1 | [confirm] > [already removed — EX-01] → “Report that the dependency was already removed” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-24.7 | F2 | [confirm] → “Remove the relationship and record the change” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.7 | F3 | [cancel — AF-01] → “Leave the dependency unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-26 | F1 | [no longer available — EX-01] → “Reject the change to the unavailable status” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-26 | F2 | (main flow) → “Refresh the Sprint Board and record the change” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.1 | F1 | (main flow) → “Display an empty subtask list” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.2 | F1 | [subtask — EX-01] → “Reject the subtask below another subtask” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.2 | F2 | (main flow) → “Recalculate parent-task progress” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.3 | F1 | [submit] > [no longer in the active Sprint — EX-01] → “Reject the update because the parent task left the active Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-27.3 | F2 | [submit] → “Recalculate parent-task progress” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.3 | F3 | [cancel editing — AF-01] → “Keep the subtask unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-27.5 | F1 | [confirm] > [completed or Sprint ended — EX-01] → “Reject the deletion because the subtask was completed or the Sprint ended” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-27.5 | F2 | [confirm] → “Remove the subtask and recalculate parent-task progress” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.5 | F3 | [cancel — AF-01] → “Leave the subtask unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-28 | F1 | [removed — EX-01] → “Reject the comment because the work item was removed” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-28 | F2 | (main flow) → “Record the failed delivery and keep the saved comment” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-29 | F1 | [cannot be retrieved — EX-01] → “Report that the activity history cannot be retrieved” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-29 | F2 | (main flow) → “Review the displayed history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-30 | F1 | [review] > [inaccessible — EX-01] → “Report that the related project item is no longer accessible” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-30 | F2 | [review] → “Mark it as read and display its related project context” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-30 | F3 | [other request] > [mark all — AF-01] → “Mark all visible notifications as read” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-30 | F4 | [other request] > [change email delivery — AF-02] → “Keep the previous preference and report the failure” | Shared by different outcomes | Activity Final (`stop`) | Different outcomes share this final (AF-02 saved and EX-02 unchanged) while the other finals separate the outcomes | Use one consistent rule: one shared final for the interleaved outcomes |
| UC-31 | F1 | [no active Sprint — EX-01] → “Report that no active Sprint exists for the project” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-31 | F2 | (main flow) → “Display the resulting Sprint indicators and charts” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.1 | F1 | [unavailable — EX-01] → “Report that account administration data is temporarily unavailable” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.1 | F2 | [no match — AF-01] → “Report that no matching account was found” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-32.1 | F3 | (main flow) → “Display its administrative status and relevant account metadata” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |
| UC-32.2 | F1 | [current owner — EX-01] → “Reject the suspension of the current Project Owner” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2, F4 | Merge into one Activity Final |
| UC-32.2 | F2 | [last administrator — EX-02] → “Reject the suspension of the last active System Administrator” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F4 | Merge into one Activity Final |
| UC-32.2 | F3 | [confirm] → “Suspend the account and record the audit event” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.2 | F4 | [cancel — AF-01] → “Leave the account active” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2 | Merge into one Activity Final |
| UC-32.3 | F1 | [deleted — EX-01] → “Reject the reactivation of the deleted account” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-32.3 | F2 | [confirm] → “Reactivate the account and record the audit event” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.3 | F3 | [cancel — AF-01] → “Leave the account suspended” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1 | Merge into one Activity Final |
| UC-32.4 | F1 | [current owner — EX-01] → “Reject the deletion of the current Project Owner” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F2, F4 | Merge into one Activity Final |
| UC-32.4 | F2 | [last administrator — EX-02] → “Reject the deletion of the last active System Administrator” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F4 | Merge into one Activity Final |
| UC-32.4 | F3 | [confirm] → “Delete the account and record the audit event” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.4 | F4 | [cancel — AF-01] → “Leave the account unchanged” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Same outcome as F1, F2 | Merge into one Activity Final |
| UC-33 | F1 | [unavailable — EX-01] → “Report that the audit store is temporarily unavailable” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-33 | F2 | [no match — AF-01] → “Report that no matching events were found” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F3 | Merge into one Activity Final |
| UC-33 | F3 | (main flow) → “Review the results” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Same outcome as F2 | Merge into one Activity Final |

### C.3 Every end node after the fixes

All end nodes are Activity Finals produced by PlantUML `stop`; there are no Flow Finals (`kill`/`detach`) and no implicit ends. No branch ends without a final, and no end node exists only because of an invented exception.

| UC | End node | Đường đi đến node | Kết quả/postcondition | Loại UML hiện dùng | Đánh giá | Hướng sửa |
|---|---|---|---|---|---|---|
| UC-01 | F1 | NF9 and AF-01.3 (active account); EX-01 (account stays pending); EX-02 and EX-03 on both paths (no account) | Shared by different outcomes — One shared final. Separate finals per outcome would need two finals for the active-account outcome and two for the no-account outcome, because those outcomes occur on both the email and the Google branch; the last action on each path states the outcome | Activity Final (`stop`) | Shared final, explained in the source header | Keep (layout: see legibility) |
| UC-02 | F1 | NF5 and AF-01.3 (session created); AF-02, EX-01/EX-02, EX-02, EX-03, EX-04 (no session) | Shared by different outcomes — One shared final, for the same reason as UC-01: both outcomes occur on the email and the Google branch | Activity Final (`stop`) | Shared final, explained in the source header | Keep (layout: see legibility) |
| UC-03 | F1 | [still valid] > [cannot be revoked — EX-01] → “Remove the local credentials and report that remote revocation could not be confirmed” | local credentials removed; remote revocation not confirmed | Activity Final (`stop`) | Distinct outcome: local credentials removed but remote revocation not confirmed (EX-01). Keep | Keep |
| UC-03 | F2 | (main flow) → “Display the public log-in page” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-04 | F1 | NF6 (token and status valid) | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-04 | F2 | AF-02, no eligible account, EX-01, AF-01, EX-02 (merged) | Password unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-05.1 | F1 | [unavailable — EX-01] → “Report that the profile information is temporarily unavailable” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.1 | F2 | (main flow) → “Display the User's profile and non-sensitive account information” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.2 | F1 | NF4 → NF5 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.2 | F2 | EX-01, AF-01 (merged) | Stored profile unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-05.3 | F1 | NF5 → POST2 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-05.3 | F2 | AF-01, EX-01, EX-02 (merged) | Password unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-06 | F1 | [not persisted — EX-01] → “Reject the project creation because the data cannot be persisted” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-06 | F2 | (main flow) → “Initialize the Product Backlog and default Sprint Board” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-07 | F1 | [project or membership removed — EX-01] → “Deny access to the project dashboard for this actor” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-07 | F2 | (main flow) → “Display the dashboard in read-only mode” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-08 | F1 | [ownership changed — EX-01] → “Reject the update because ownership changed” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-08 | F2 | (main flow) → “Confirm the successful update” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.1 | F1 | [unavailable — EX-01] → “Report that membership information is temporarily unavailable” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.1 | F2 | (main flow) → “Display only the Project Owner” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.2 | F1 | NF5 → POST2 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.2 | F2 | EX-01, AF-01 (merged) | No membership change | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-09.3 | F1 | NF3 → NF5 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-09.3 | F2 | AF-01, EX-01 (merged) | Membership unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-10 | F1 | [left or removed — EX-01] → “Reject the assignment for the departed member” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-10 | F2 | (main flow) → “Record the accountability change in activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-11 | F1 | NF4 → NF5 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-11 | F2 | AF-01, EX-01 (merged) | Project unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-12 | F1 | [changed concurrently — EX-01] → “Reject the transfer because ownership changed concurrently” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-12 | F2 | (main flow) → “Transfer ownership atomically and record the change” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-13 | F1 | EX-01 | Membership unchanged (request rejected) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-13 | F2 | AF-01.2 cancel | Membership unchanged (request cancelled) | Activity Final (`stop`) | Same outcome as F1, kept separate: the cancel path must bypass NF5, which the confirm path of AF-01.2 shares with the normal flow; merging would require drawing NF5 twice | Keep |
| UC-13 | F3 | NF4 or AF-01.2 confirm → NF5 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.1 | F1 | (main flow) → “Display that the Product Goal is not yet available” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.2 | F1 | [empty — EX-01] → “Reject the empty Product Goal” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.2 | F2 | (main flow) → “Record the creation in project activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.3 | F1 | NF4 → POST2 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-14.3 | F2 | EX-01, AF-01 (merged) | Current Product Goal unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-15.1 | F1 | [no longer available — EX-01] → “Report that the selected item is no longer available” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.1 | F2 | (main flow) → “Display the item details and related Sprint information” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.2 | F1 | [complete] > [missing — EX-01] → “Reject the item without identifying information” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.2 | F2 | (main flow) → “Record the creation in item activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.3 | F1 | [changed by another User — EX-01] → “Reject the update because the item was changed concurrently” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.3 | F2 | (main flow) → “Record the update in item activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.4 | F1 | NF3 → NF4 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-15.4 | F2 | EX-01, AF-01 (merged) | Item unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-16 | F1 | [cannot be saved — EX-01] → “Reject the order because it cannot be saved completely and uniquely” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-16 | F2 | (main flow) → “Display the updated Product Backlog” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-17 | F1 | [too large — AF-01] > [selected — EX-01] → “Reject the decomposition of the item in the active Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Kept. UNCLEAR whether refinement should continue with NF5–NF6 after EX-01 (the exception only forbids substantial decomposition) | Keep |
| UC-17 | F2 | (main flow) → “Save the refined item and record the participants” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-18 | F1 | [not refined — AF-01] → “Return the item for further refinement” | estimate unset; item returned for further refinement | Activity Final (`stop`) | Distinct outcome: the item is returned for further refinement (AF-01.2). Keep | Keep |
| UC-18 | F2 | [unavailable — EX-01] → “Reject the estimate because the item was removed or is in a completed Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-18 | F3 | (main flow) → “Record the estimate change in item activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-19 | F1 | [conflict — EX-01] → “Reject saving the Sprint because its date range conflicts with another Sprint” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-19 | F2 | (main flow) → “Create the Draft Sprint and its initial Sprint Backlog” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-20 | F1 | [already active — EX-01] → “Reject the start because another Sprint is already active” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-20 | F2 | (main flow) → “Record the Sprint start time in the activity history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-21 | F1 | [state changed — EX-01] → “Reject the completion because the Sprint state has changed” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-21 | F2 | (main flow) → “Record the Sprint result for reporting” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-22 | F1 | NF3 → NF5 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-22 | F2 | AF-01, EX-01 (merged) | Sprint unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-23 | F1 | EX-01 | Board cannot be loaded | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-23 | F2 | NF4, AF-01 (merged) | Review completed: the current board, or the notice that no Sprint is active | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-24.1 | F1 | [no longer available — EX-01] → “Report that the selected Sprint Task is no longer available” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.1 | F2 | (main flow) → “Display the Sprint Task” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.2 | F1 | [belongs to the active Sprint] → “Record the creation in work item activity” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.2 | F2 | [no longer belongs to the active Sprint — EX-01] → “Reject the task creation” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.3 | F1 | NF4 → POST2 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.3 | F2 | EX-01, AF-01 (merged) | Task unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-24.4 | F1 | [assign] > [no longer active — EX-01] → “Reject the assignment to the inactive member” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.4 | F2 | [assign] → “Save the assignment and record the change” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.4 | F3 | [clear the current assignment — AF-01] → “Mark the Sprint Task as unassigned” | task left unassigned | Activity Final (`stop`) | Distinct outcome: the task is left unassigned (AF-01). Keep | Keep |
| UC-24.5 | F1 | NF3 → NF4 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.5 | F2 | AF-01, EX-01 (merged) | Task unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-24.6 | F1 | NF4 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.6 | F2 | EX-01, EX-02 (merged) | No dependency stored | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-24.7 | F1 | NF4 → NF5 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-24.7 | F2 | EX-01, AF-01 (merged) | No removal by this use case | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-26 | F1 | [no longer available — EX-01] → “Reject the change to the unavailable status” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-26 | F2 | (main flow) → “Refresh the Sprint Board and record the change” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.1 | F1 | (main flow) → “Display an empty subtask list” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.2 | F1 | [subtask — EX-01] → “Reject the subtask below another subtask” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.2 | F2 | (main flow) → “Recalculate parent-task progress” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.3 | F1 | NF4 → POST2 (when relevant) | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.3 | F2 | EX-01, AF-01 (merged) | Subtask unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-27.5 | F1 | NF3 → NF4 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-27.5 | F2 | EX-01, AF-01 (merged) | Subtask unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-28 | F1 | [removed — EX-01] → “Reject the comment because the work item was removed” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-28 | F2 | (main flow) → “Record the failed delivery and keep the saved comment” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-29 | F1 | [cannot be retrieved — EX-01] → “Report that the activity history cannot be retrieved” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-29 | F2 | (main flow) → “Review the displayed history” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-30 | F1 | NF4, AF-01, AF-02 saved (request completed); EX-01, EX-02 (nothing changed) | Shared by different outcomes — One shared final: the completed and the unchanged outcomes are interleaved on three branches | Activity Final (`stop`) | Shared final, explained in the source header | Keep (layout: see legibility) |
| UC-31 | F1 | [no active Sprint — EX-01] → “Report that no active Sprint exists for the project” | Use case ends without its postconditions; no persistent change | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-31 | F2 | (main flow) → “Display the resulting Sprint indicators and charts” | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.1 | F1 | EX-01 | Administration data unavailable | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.1 | F2 | NF4, AF-01 (merged) | Search completed, with the selected account or with the report that none match | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-32.2 | F1 | NF3 → NF4 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.2 | F2 | AF-01, EX-01/EX-02 (merged) | Account stays active | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-32.3 | F1 | NF3 → NF4 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.3 | F2 | AF-01, EX-01 (merged) | Account stays suspended | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-32.4 | F1 | NF3 → NF4 | Use-case goal reached (postconditions met) | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-32.4 | F2 | AF-01, EX-01/EX-02 (merged) | Account unchanged | Activity Final (`stop`) | Paths with the same outcome merged | Keep |
| UC-33 | F1 | EX-01 | Audit store unavailable | Activity Final (`stop`) | Only final for this outcome | Keep |
| UC-33 | F2 | NF5, AF-01 (merged) | Review completed, with matching events or with the report that none match | Activity Final (`stop`) | Paths with the same outcome merged | Keep |

## D. Files changed

| File | Reason |
|---|---|
| `diagrams/activity/account-authentication/source/UC-ACCOUNT-REGISTER.puml` and `diagrams/activity/account-authentication/svg/UC-ACCOUNT-REGISTER.svg` | One shared final (outcomes interleaved on two branches); EX-03 added on the Google path; NF4/AF-01 trace BRs |
| `diagrams/activity/account-authentication/source/UC-SIGN-IN.puml` and `diagrams/activity/account-authentication/svg/UC-SIGN-IN.svg` | One shared final; EX-01/EX-02 share one rejection on the email path; decision renamed “Forgot Password chosen?” |
| `diagrams/activity/account-authentication/source/UC-PASSWORD-RESET.puml` and `diagrams/activity/account-authentication/svg/UC-PASSWORD-RESET.svg` | Five no-change paths merged into one final |
| `diagrams/activity/account-authentication/source/UC-PROFILE-UPDATE.puml` and `diagrams/activity/account-authentication/svg/UC-PROFILE-UPDATE.svg` | EX-01 and AF-01 merged into one final |
| `diagrams/activity/account-authentication/source/UC-PASSWORD-CHANGE.puml` and `diagrams/activity/account-authentication/svg/UC-PASSWORD-CHANGE.svg` | AF-01, EX-01, EX-02 merged into one final; narrower texts for legibility |
| `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-ADD.puml` and `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-ADD.svg` | AF-01 and EX-01 merged |
| `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-REMOVE.puml` and `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-REMOVE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/project-membership/source/UC-PROJECT-ARCHIVE.puml` and `diagrams/activity/project-membership/svg/UC-PROJECT-ARCHIVE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/project-membership/source/UC-PROJECT-LEAVE.puml` and `diagrams/activity/project-membership/svg/UC-PROJECT-LEAVE.svg` | Header comment explains why two same-outcome finals remain |
| `diagrams/activity/product-backlog/source/UC-PRODUCT-GOAL-UPDATE.puml` and `diagrams/activity/product-backlog/svg/UC-PRODUCT-GOAL-UPDATE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/product-backlog/source/UC-BACKLOG-ITEM-CREATE.puml` and `diagrams/activity/product-backlog/svg/UC-BACKLOG-ITEM-CREATE.svg` | AF-01 actor action moved to the Product Owner partition; narrower texts |
| `diagrams/activity/product-backlog/source/UC-BACKLOG-ITEM-REMOVE.puml` and `diagrams/activity/product-backlog/svg/UC-BACKLOG-ITEM-REMOVE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/product-backlog/source/UC-BACKLOG-ITEM-REFINE.puml` and `diagrams/activity/product-backlog/svg/UC-BACKLOG-ITEM-REFINE.svg` | AF-01 decision moved to the Developer partition |
| `diagrams/activity/product-backlog/source/UC-BACKLOG-ITEM-ESTIMATE.puml` and `diagrams/activity/product-backlog/svg/UC-BACKLOG-ITEM-ESTIMATE.svg` | Unsupported recipient removed from AF-01.2 |
| `diagrams/activity/sprint-management/source/UC-SPRINT-PLAN.puml` and `diagrams/activity/sprint-management/svg/UC-SPRINT-PLAN.svg` | Unrelated BR removed from a trace comment |
| `diagrams/activity/sprint-management/source/UC-SPRINT-CANCEL.puml` and `diagrams/activity/sprint-management/svg/UC-SPRINT-CANCEL.svg` | AF-01.1 moved to the Product Owner partition; EX-01 and AF-01 merged |
| `diagrams/activity/sprint-work/source/UC-SPRINT-BOARD-REVIEW.puml` and `diagrams/activity/sprint-work/svg/UC-SPRINT-BOARD-REVIEW.svg` | NF4 and AF-01 (both complete the review) merged |
| `diagrams/activity/sprint-work/source/UC-SPRINT-TASK-UPDATE.puml` and `diagrams/activity/sprint-work/svg/UC-SPRINT-TASK-UPDATE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/sprint-work/source/UC-SPRINT-TASK-DELETE.puml` and `diagrams/activity/sprint-work/svg/UC-SPRINT-TASK-DELETE.svg` | EX-01 and AF-01 merged; unrelated BR removed from a trace comment |
| `diagrams/activity/sprint-work/source/UC-TASK-DEPENDENCY-ADD.puml` and `diagrams/activity/sprint-work/svg/UC-TASK-DEPENDENCY-ADD.svg` | EX-01 and EX-02 merged |
| `diagrams/activity/sprint-work/source/UC-TASK-DEPENDENCY-REMOVE.puml` and `diagrams/activity/sprint-work/svg/UC-TASK-DEPENDENCY-REMOVE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/sprint-work/source/UC-SUBTASK-UPDATE.puml` and `diagrams/activity/sprint-work/svg/UC-SUBTASK-UPDATE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/sprint-work/source/UC-SUBTASK-DELETE.puml` and `diagrams/activity/sprint-work/svg/UC-SUBTASK-DELETE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/collaboration-notification/source/UC-NOTIFICATIONS-REVIEW.puml` and `diagrams/activity/collaboration-notification/svg/UC-NOTIFICATIONS-REVIEW.svg` | One shared final instead of a mixed final; consistent outcome handling |
| `diagrams/activity/system-administration/source/UC-USER-ACCOUNTS-SEARCH.puml` and `diagrams/activity/system-administration/svg/UC-USER-ACCOUNTS-SEARCH.svg` | NF4 and AF-01 (both complete the search) merged |
| `diagrams/activity/system-administration/source/UC-USER-ACCOUNT-SUSPEND.puml` and `diagrams/activity/system-administration/svg/UC-USER-ACCOUNT-SUSPEND.svg` | EX-01/EX-02 share one decision; EX and AF-01 merged |
| `diagrams/activity/system-administration/source/UC-USER-ACCOUNT-REACTIVATE.puml` and `diagrams/activity/system-administration/svg/UC-USER-ACCOUNT-REACTIVATE.svg` | EX-01 and AF-01 merged |
| `diagrams/activity/system-administration/source/UC-USER-ACCOUNT-DELETE.puml` and `diagrams/activity/system-administration/svg/UC-USER-ACCOUNT-DELETE.svg` | EX-01/EX-02 share one decision; EX and AF-01 merged |
| `diagrams/activity/system-administration/source/UC-SYSTEM-AUDIT-LOG-REVIEW.puml` and `diagrams/activity/system-administration/svg/UC-SYSTEM-AUDIT-LOG-REVIEW.svg` | NF5 and AF-01 (both complete the review) merged; unrelated BR removed from a trace comment |
| `diagrams/activity/manifest.yml` | audit_status added; legibility notes and observations updated |
| `scripts/activity_diagrams.py` | Review report shows the audit status |
| `docs/activity-diagram-guideline.md` | §5 end-node convention made explicit (UML rule vs team convention) |
| `.claude/skills/activity-diagram/SKILL.md, references/uml-activity-rules.md, references/review-checklist.md` | Same end-node convention; rule against unsourced generic steps |
| `docs/activity-diagram-generation-report.md, docs/activity-diagram-review-report.md` | Regenerated |
| `docs/activity-diagram-audit-report.md, docs/activity-diagram-traceability.md` | New: this report and the element-level traceability matrix |

No Use Case YAML or Business Rule was changed.

## E. BLOCKED and UNCLEAR cases

| UC | Status | Question for the BA / Product Owner |
|---|---|---|
| UC-25 Claim Sprint Task | BLOCKED — INSUFFICIENT SPECIFICATION | AF-01 «withdraws before confirmation» refers to a confirmation step the normal flow does not have. Add a confirmation step or remove AF-01? |
| UC-27.4 Complete Subtask | BLOCKED — REQUIREMENT CONFLICT | AF-01 restores a completed subtask, but precondition 3 says the subtask is not complete. Separate use case, or relax precondition 3? |
| UC-10 Assign Scrum Accountability | UNCLEAR — possible UC/BR conflict | AF-01 asks for confirmation before replacing the Product Owner; BR-PRODUCT-OWNER-ACCOUNTABILITY-UNIQUE says a new Product Owner «automatically replaces» the previous one. Which applies, and what happens if the replacement is not confirmed? |
| UC-01 Register Account | UNCLEAR | What happens when Google returns an email address that already has an account (other_information says duplicate handling applies)? |
| UC-04 Forgot Password | UNCLEAR | What happens when the new password fails the strength requirements? |
| UC-15.2 Create Backlog Item | UNCLEAR | Does EX-01 (missing identifying information) also apply to a draft saved through AF-01? |
| UC-17 Refine Backlog Item | UNCLEAR | After EX-01 (no substantial decomposition in an active Sprint), does refinement continue with NF5–NF6? |
| UC-18 Estimate Backlog Item | UNCLEAR | Who returns the item for further refinement (AF-01.2)? It is drawn in the System partition. |
| UC-20 Start Sprint | UNCLEAR | What happens when the revalidation in AF-01.2 fails? |
| UC-24.2 Create Sprint Task | UNCLEAR | What happens when the task information is invalid? |
| UC-24.5 Delete Sprint Task | UNCLEAR | Can the Developer decline the confirmation? No alternative flow covers it. |
| UC-26 Update Work Item Status | UNCLEAR | Is NF2 validation repeated when another status is chosen in AF-01.2? |
| UC-30 Review Notifications | UNCLEAR | What happens when the actor enables email delivery without a verified email address? |
| UC-32.1 Search User Accounts | UNCLEAR | After “no matching account”, may the administrator search again within the use case? |
| 15 exception/alternative flows in UC-05.3, 09.3, 11, 13, 15.4, 20, 22, 23, 24.5, 31, 32.2 (2), 32.3, 32.4 (2) | UNCLEAR (kept) | Each describes a state that a precondition excludes; drawn as a defensive System check. Confirm that the checks are intended. |

The diagrams keep these cases as they are; none was resolved by guessing.

## F. Validation and rendering

- `python cli.py validate`: 62 use cases, 0 errors (before and after).
- `python scripts/activity_diagrams.py validate`: 0 errors, 0 warnings (before and after). It checks the manifest, trace references, NF/AF/EX coverage, partitions, one initial node, Log In only in UC-02, fonts, frame and text/line collisions in every SVG.
- `python scripts/activity_diagrams.py render --all`: 53 rendered, 0 failures; a second full render produced byte-identical SVGs.
- Source/SVG consistency: every action, decision and guard text and the number of final nodes of each source appear in its SVG (0 mismatches).
- Partition check: every action whose YAML step names an actor is in that actor's partition (one DERIVED exception: UC-10 “Confirm the replacement”).
- Visual inspection of all 29 changed diagrams (rendered previews): no clipped node, missing border, overlapping text, guard on the wrong edge or ambiguous arrow.

## G. Audit status

| Status | Count | Use cases |
|---|---:|---|
| APPROVED | 46 | All drawn use cases except the seven below (approval by this audit; peer review and team-leader acceptance still required) |
| REQUEST CHANGES | 7 | UC-01, UC-02, UC-04, UC-18, UC-21, UC-28, UC-30 — layout only: guard text below 6 pt on portrait A4 (3.3, 3.7, 3.5, 5.4, 5.5, 5.3, 4.6 pt). Content is correct; a full page, acceptance by the team, or splitting the use case is needed |
| BLOCKED | 2 | UC-25, UC-27.4 |

Merging the end nodes of UC-01, UC-02 and UC-04 made them wider (guard text 4.4 → 3.3, 4.6 → 3.7 and 4.3 → 3.5 pt): PlantUML can only merge paths by nesting the rest of the flow, which places the branches side by side. The team should decide between the merged versions (fewer end nodes, as requested) and a full-page or landscape placement.

## H. Before/after examples

**UC-32.2 Suspend User Account — end nodes 4 → 2.** Before: EX-01, EX-02, success and AF-01 each ended in its own final; three of them (EX-01, EX-02, AF-01) have the same outcome, the account stays active. After: EX-01 and EX-02 share one decision (“Account protected?”, precondition 3 groups both) and one rejection; the rejection and the AF-01 cancellation merge into one final; the success path keeps its own final. The guard still names EX-01 and EX-02, every YAML reference is kept, and the action count drops by one (7 → 6); guard text 7.4 → 6.2 pt.

**UC-22 Cancel Sprint — step drawn in the wrong partition.** Before: “Cancel the confirmation” (AF-01.1, actor: Product Owner) was in the System partition, so the diagram attributed the Product Owner's action to the System. After: it is in the Product Owner partition, followed by the System's AF-01.2 “Leave the Sprint unchanged”; EX-01 and AF-01 share one final (3 → 2).

**UC-18 Estimate Backlog Item — added detail.** Before: “Return the item to the Product Owner for further refinement”. After: “Return the item for further refinement”, exactly AF-01.2.

## Appendix — Stage 1 traceability of the changed diagrams (baseline `72215fd`)

The element-level traceability of the current diagrams (all 53) is in `docs/activity-diagram-traceability.md`. Unchanged diagrams have the same table before and after.


#### UC-01 — Register Account (`UC-ACCOUNT-REGISTER`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-01 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-01 | Action [Guest] “Open account registration and choose a registration method” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[1] «Opens account registration and chooses email and password.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Decision [System] “Registration method?” | Decision | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-01 condition «The Guest chooses to register with Google.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-01 | Guard [email and password] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-01 | Action [System] “Request the display name, email address, and password” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[2] «Requests the display name, email address, and password.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Action [Guest] “Provide the required registration information” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[3] «Provides the required registration information.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Action [System] “Validate the information, email uniqueness, and password strength” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[4] «Validates the information, email uniqueness, and password strength.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Loop decision [System] “Information invalid?” | Loop | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-02 condition «The registration information is invalid.» | DERIVED | Return path of AF-02: the alternative flow re-performs the step and the condition is evaluated again. Keep |
| UC-01 | Guard [invalid — AF-02] | Guard | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-02 condition «The registration information is invalid.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-01 | Action [System] “Request the registration information again” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-02 step 1 «The system requests registration information again.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Action [Guest] “Provide the registration information again” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[3] «Provides the required registration information.» | DERIVED | AF-02.1 requests the information again; the Guest provides it again (NF3 re-performed). Keep |
| UC-01 | Guard [valid] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-01 | Action [System] “Create a pending account” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[5] «Creates a pending account.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Decision [System] “Account data persisted?” | Decision | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-03 «Account data cannot be persisted, so no User account is created.» | NECESSARY REPRESENTATION | Branch point for EX-03; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-01 | Guard [persisted] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-01 | Guard [not persisted — EX-03] | Guard | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-03 «Account data cannot be persisted, so no User account is created.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-01 | Action [System] “Reject the registration so that no account is created” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-03 «Account data cannot be persisted, so no User account is created.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-03 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-01 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-01 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-01 | Action [System] “Request an email verification message for the account” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[6] «Requests an email verification message for the account.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Action [Email Service] “Deliver the verification message to the submitted email address” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[7] «Delivers the verification message to the submitted email address.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Decision [System] “Message delivered?” | Decision | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-01 «The Email Service cannot deliver the verification message; the account remains pending and ver…» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-01 | Guard [delivered] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-01 | Guard [not delivered — EX-01] | Guard | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-01 «The Email Service cannot deliver the verification message; the account remains pending and ver…» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-01 | Action [System] “Keep the account pending so that verification can be requested again” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-01 «The Email Service cannot deliver the verification message; the account remains pending and ver…» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-01 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-01 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-01 | Action [Guest] “Open the valid verification link” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[8] «Opens the valid verification link.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Action [System] “Activate the User account and confirm registration” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › normal_flow[9] «Activates the User account and confirms registration.»<br>`data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › postconditions[1] «One active User account is linked to the verified email address.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Guard [Google — AF-01] | Guard | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-01 condition «The Guest chooses to register with Google.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-01 | Action [System] “Redirect the Guest to the Identity Provider” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-01 step 1 «The system redirects the Guest to the Identity Provider.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Action [Identity Provider] “Authenticate the Guest and return a verified identity” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-01 step 2 «The Identity Provider authenticates the Guest and returns a verified identity.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Decision [System] “Valid verified identity?” | Decision | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-02 «The Identity Provider does not return a valid verified identity; registration is cancelled.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-01 | Guard [valid] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-01 | Guard [not returned — EX-02] | Guard | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-02 «The Identity Provider does not return a valid verified identity; registration is cancelled.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-01 | Action [System] “Cancel the registration because no valid verified identity was returned” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › EX-02 «The Identity Provider does not return a valid verified identity; registration is cancelled.» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-01 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-01 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-01 | Action [System] “Validate email uniqueness and create an active User account” | Action | `data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › AF-01 step 3 «The system validates email uniqueness and creates an active User account.»<br>`data/use_cases/account-authentication/UC-ACCOUNT-REGISTER.yml` › postconditions[1] «One active User account is linked to the verified email address.» | EXPLICIT | Matches the step text. Keep |
| UC-01 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-01 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-02 — Log In (`UC-SIGN-IN`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-02 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-02 | Action [User] “Open the log-in page and choose a log-in option” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › normal_flow[1] «Opens the log-in page and chooses email and password.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Decision [System] “Password forgotten?” | Decision | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-02 condition «The User has forgotten the locally managed password.» | NECESSARY REPRESENTATION | Branch point for AF-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-02 | Guard [not forgotten] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-02 | Guard [forgotten — AF-02] | Guard | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-02 condition «The User has forgotten the locally managed password.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-02 | Action [System] “Direct the User to Forgot Password” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-02 step 1 «The system directs the User to Forgot Password.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-02 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-02 | Decision [System] “Log-in option?” | Decision | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-01 condition «The User chooses to log in with Google.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-02 | Guard [email and password] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-02 | Action [System] “Request the registered email address and password” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › normal_flow[2] «Requests the registered email address and password.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Action [User] “Submit the credentials” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › normal_flow[3] «Submits the credentials.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Action [System] “Validate the credentials and confirm that the account is active” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › normal_flow[4] «Validates the credentials and confirms that the account is active.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Decision [System] “Credentials valid?” | Decision | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-01 «The submitted credentials are invalid; no session is created.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-02 | Guard [valid] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-02 | Guard [invalid — EX-01] | Guard | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-01 «The submitted credentials are invalid; no session is created.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-02 | Action [System] “Reject the log-in without creating a session” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-01 «The submitted credentials are invalid; no session is created.» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-02 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-02 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-02 | Decision [System] “Account active?” | Decision | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-02 «The User account is pending, suspended, or deleted; log-in is rejected.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-02 | Guard [active] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-02 | Guard [pending, suspended or deleted — EX-02] | Guard | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-02 «The User account is pending, suspended, or deleted; log-in is rejected.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-02 | Action [System] “Reject the log-in for the inactive account” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-02 «The User account is pending, suspended, or deleted; log-in is rejected.» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-02 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-02 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-02 | Action [System] “Create an authenticated session and display the User's available projects” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › normal_flow[5] «Creates an authenticated session and displays the User's available projects.»<br>`data/use_cases/account-authentication/UC-SIGN-IN.yml` › postconditions[1] «An authenticated session is established for the User.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Guard [Google — AF-01] | Guard | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-01 condition «The User chooses to log in with Google.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-02 | Action [System] “Redirect the User to the Identity Provider” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-01 step 1 «The system redirects the User to the Identity Provider.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Action [Identity Provider] “Authenticate the User and return a verified identity” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-01 step 2 «The Identity Provider authenticates the User and returns a verified identity.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Decision [System] “Identity verified?” | Decision | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-03 «The Identity Provider is unavailable or rejects authentication; no session is created.» | NECESSARY REPRESENTATION | Branch point for EX-03; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-02 | Guard [verified] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-02 | Guard [unavailable or rejected — EX-03] | Guard | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-03 «The Identity Provider is unavailable or rejects authentication; no session is created.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-02 | Action [System] “End the log-in without creating a session” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-03 «The Identity Provider is unavailable or rejects authentication; no session is created.» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-02 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-02 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-02 | Action [System] “Match the identity to an existing User account” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-01 step 3 «The system matches the identity to an existing active User account and creates a session.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Decision [System] “Matching account found?” | Decision | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-04 «The Identity Provider returns a verified identity but no matching User account exists; no sess…» | NECESSARY REPRESENTATION | Branch point for EX-04; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-02 | Guard [found] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-02 | Guard [no matching account — EX-04] | Guard | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-04 «The Identity Provider returns a verified identity but no matching User account exists; no sess…» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-02 | Action [System] “Direct the person to Register Account without creating a session” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-04 «The Identity Provider returns a verified identity but no matching User account exists; no sess…» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-02 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-02 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-02 | Decision [System] “Account active?” | Decision | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-02 «The User account is pending, suspended, or deleted; log-in is rejected.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-02 | Guard [active] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-02 | Guard [not active — EX-02] | Guard | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-02 «The User account is pending, suspended, or deleted; log-in is rejected.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-02 | Action [System] “Reject the log-in for the inactive account” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › EX-02 «The User account is pending, suspended, or deleted; log-in is rejected.» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-02 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-02 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-02 | Action [System] “Create an authenticated session” | Action | `data/use_cases/account-authentication/UC-SIGN-IN.yml` › AF-01 step 3 «The system matches the identity to an existing active User account and creates a session.»<br>`data/use_cases/account-authentication/UC-SIGN-IN.yml` › postconditions[1] «An authenticated session is established for the User.» | EXPLICIT | Matches the step text. Keep |
| UC-02 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-02 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-04 — Forgot Password (`UC-PASSWORD-RESET`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-04 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-04 | Action [User] “Open Forgot Password and submit an email address” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › normal_flow[1] «Opens Forgot Password and submits an email address.» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Action [System] “Display the same generic response whether or not the account exists” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › normal_flow[2] «Displays the same generic response regardless of whether the account exists.»<br>`data/business_rules.yml` › BR-PASSWORD-RESET-PRIVACY «A password-reset request must not reveal whether the submitted email address be…» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Decision [System] “Google-only account?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-02 condition «The account uses Google only and has no locally managed password.» | NECESSARY REPRESENTATION | Branch point for AF-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-04 | Guard [password account] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-04 | Guard [Google only — AF-02] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-02 condition «The account uses Google only and has no locally managed password.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-04 | Action [System] “Keep the generic response without creating a reset token” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-02 step 1 «The system keeps the generic response and does not create a reset token.» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Action [User] “Continue to authenticate through Google” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-02 step 2 «The User continues to authenticate through Google.» | EXPLICIT | Matches AF-02.2. Keep |
| UC-04 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-04 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-04 | Decision [System] “Eligible account?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` | DERIVED | NF3 generates a token only "when the email belongs to an eligible password account"; otherwise only NF2 applies. Keep |
| UC-04 | Guard [eligible] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-04 | Guard [no eligible account] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-04 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-04 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-04 | Action [System] “Generate a single-use expiring reset token” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › normal_flow[3] «Generates a single-use expiring token when the email belongs to an eligible password account.»<br>`data/business_rules.yml` › BR-PASSWORD-RESET-TOKEN «A password-reset token is single-use and must expire after the configured valid…» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Action [Email Service] “Deliver the password-reset link to the eligible email address” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › normal_flow[4] «Delivers the password-reset link to the eligible email address.» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Decision [System] “Link delivered?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › EX-01 «The Email Service cannot deliver the reset message; the failure is recorded without exposing a…» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-04 | Guard [delivered] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-04 | Guard [not delivered — EX-01] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › EX-01 «The Email Service cannot deliver the reset message; the failure is recorded without exposing a…» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-04 | Action [System] “Record the delivery failure without exposing whether the account exists” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › EX-01 «The Email Service cannot deliver the reset message; the failure is recorded without exposing a…»<br>`data/business_rules.yml` › BR-PASSWORD-RESET-PRIVACY «A password-reset request must not reveal whether the submitted email address be…» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-04 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-04 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-04 | Action [User] “Open the link and submit a new password” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › normal_flow[5] «Opens the valid link and submits a new password.» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Action [System] “Validate the token and the password strength” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › normal_flow[6] «Validates the token and password strength, updates the password, and invalidates the token.»<br>`data/business_rules.yml` › BR-PASSWORD-STRENGTH «A locally managed password must satisfy the configured password-strength requir…» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Decision [System] “Token valid?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-01 condition «The reset token is invalid, expired, or already used.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-04 | Guard [valid] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-04 | Guard [invalid, expired or used — AF-01] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-01 condition «The reset token is invalid, expired, or already used.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-04 | Action [System] “Reject the password change” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-01 step 1 «The system rejects the password change.» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Action [System] “Allow the User to submit a new Forgot Password request” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › AF-01 step 2 «The system allows the User to submit a new Forgot Password request.» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-04 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-04 | Decision [System] “Account status unchanged?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › EX-02 «The account status changes before the new password is saved; the reset is rejected.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-04 | Guard [unchanged] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-04 | Guard [status changed — EX-02] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › EX-02 «The account status changes before the new password is saved; the reset is rejected.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-04 | Action [System] “Reject the password reset for the changed account” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › EX-02 «The account status changes before the new password is saved; the reset is rejected.» | EXPLICIT | Outcome stated in the exception description. Keep |
| UC-04 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-04 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-04 | Action [System] “Update the password and invalidate the used token” | Action | `data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › normal_flow[6] «Validates the token and password strength, updates the password, and invalidates the token.»<br>`data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › postconditions[1] «If a valid reset is completed, the new password replaces the previous password.»<br>`data/use_cases/account-authentication/UC-PASSWORD-RESET.yml` › postconditions[2] «The used reset token is invalidated.» | EXPLICIT | Matches the step text. Keep |
| UC-04 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-05.2 — Update Personal Profile (`UC-PROFILE-UPDATE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-05.2 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-05.2 | Action [User] “Open profile editing” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › normal_flow[1] «Opens profile editing.» | EXPLICIT | Matches the step text. Keep |
| UC-05.2 | Action [System] “Display the current editable profile values” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › normal_flow[2] «Displays the current editable profile values.» | EXPLICIT | Matches the step text. Keep |
| UC-05.2 | Decision [User] “Save the changes?” | Decision | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › AF-01 condition «The User cancels before saving.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-05.2 | Guard [submit] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-05.2 | Action [User] “Change the desired values and submit the profile” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › normal_flow[3] «Changes the desired values and submits the profile.» | EXPLICIT | Matches the step text. Keep |
| UC-05.2 | Action [System] “Validate the profile changes” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › normal_flow[4] «Validates and saves the profile changes.» | EXPLICIT | Matches the step text. Keep |
| UC-05.2 | Decision [System] “Values valid?” | Decision | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › EX-01 «One or more submitted values do not satisfy the configured format or length constraints.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-05.2 | Guard [valid] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-05.2 | Guard [invalid values — EX-01] | Guard | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › EX-01 «One or more submitted values do not satisfy the configured format or length constraints.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-05.2 | Action [System] “Reject the profile changes and keep the stored profile” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › EX-01 «One or more submitted values do not satisfy the configured format or length constraints.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-05.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-05.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-05.2 | Action [System] “Save the profile changes” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › normal_flow[4] «Validates and saves the profile changes.»<br>`data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › postconditions[1] «Valid profile changes are stored for the authenticated User.» | EXPLICIT | Matches the step text. Keep |
| UC-05.2 | Action [System] “Display the updated profile” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › normal_flow[5] «Displays the updated profile.» | EXPLICIT | Matches the step text. Keep |
| UC-05.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-05.2 | Guard [cancel before saving — AF-01] | Guard | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › AF-01 condition «The User cancels before saving.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-05.2 | Action [System] “Discard the unsaved changes” | Action | `data/use_cases/account-authentication/UC-PROFILE-UPDATE.yml` › AF-01 step 1 «The system discards the unsaved changes.» | EXPLICIT | Matches the step text. Keep |
| UC-05.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-05.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-05.3 — Change Password (`UC-PASSWORD-CHANGE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-05.3 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-05.3 | Decision [System] “Password managed locally?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › AF-01 condition «The account is managed only through an external Identity Provider.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-05.3 | Guard [locally managed] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-05.3 | Guard [provider only — AF-01] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › AF-01 condition «The account is managed only through an external Identity Provider.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-05.3 | Action [System] “Inform the User that the password must be changed through that provider” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › AF-01 step 1 «The system informs the User that the password must be changed through that provider.» | EXPLICIT | Matches the step text. Keep |
| UC-05.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-05.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-05.3 | Action [User] “Enter the current password and a new password” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › normal_flow[1] «Enters the current password and a new password.» | EXPLICIT | Matches the step text. Keep |
| UC-05.3 | Action [System] “Verify the current password” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › normal_flow[2] «Verifies the current password.» | EXPLICIT | Matches the step text. Keep |
| UC-05.3 | Decision [System] “Current password correct?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › EX-01 «The current password is incorrect.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-05.3 | Guard [correct] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-05.3 | Guard [incorrect — EX-01] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › EX-01 «The current password is incorrect.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-05.3 | Action [System] “Reject the password change” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › EX-01 «The current password is incorrect.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-05.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-05.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-05.3 | Action [System] “Validate the new password against the password policy” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › normal_flow[3] «Validates the new password against the password policy.»<br>`data/business_rules.yml` › BR-PASSWORD-STRENGTH «A locally managed password must satisfy the configured password-strength requir…» | EXPLICIT | Matches the step text. Keep |
| UC-05.3 | Decision [System] “Policy satisfied?” | Decision | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › EX-02 «The new password does not satisfy the configured password-strength requirements.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-05.3 | Guard [satisfied] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-05.3 | Guard [not satisfied — EX-02] | Guard | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › EX-02 «The new password does not satisfy the configured password-strength requirements.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-05.3 | Action [System] “Reject the new password” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › EX-02 «The new password does not satisfy the configured password-strength requirements.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-02 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-05.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-05.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-05.3 | Action [User] “Confirm the password change” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › normal_flow[4] «Confirms the password change.» | EXPLICIT | Matches the step text. Keep |
| UC-05.3 | Action [System] “Store the new password securely and confirm success” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › normal_flow[5] «Stores the new password securely and confirms success.»<br>`data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › postconditions[1] «The new password replaces the previous password.» | EXPLICIT | Matches the step text. Keep |
| UC-05.3 | Action [System] “Record the password change as a security event” | Action | `data/use_cases/account-authentication/UC-PASSWORD-CHANGE.yml` › postconditions[2] «The password change is recorded as a security event.» | DERIVED | Stated as a postcondition/other information; the flow does not name the step that performs it, so it is shown as the last System action. Keep |
| UC-05.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-09.2 — Add Project Member (`UC-PROJECT-MEMBER-ADD`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-09.2 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-09.2 | Action [Project Owner] “Open project membership management and choose to add a member” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › normal_flow[1] «Opens project membership management and chooses to add a member.» | EXPLICIT | Matches the step text. Keep |
| UC-09.2 | Action [System] “Request an existing User account” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › normal_flow[2] «Requests an existing User account.» | EXPLICIT | Matches the step text. Keep |
| UC-09.2 | Action [Project Owner] “Select the User and confirm the addition” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › normal_flow[3] «Selects the User and confirms the addition.» | EXPLICIT | Matches the step text. Keep |
| UC-09.2 | Action [System] “Verify that the User is active and is not already a member” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › normal_flow[4] «Verifies that the User is active and is not already a member.»<br>`data/business_rules.yml` › BR-ACTIVE-USER-REQUIRED «Only an active authenticated User can create or access a project.» | EXPLICIT | Matches the step text. Keep |
| UC-09.2 | Decision [System] “Already a member?” | Decision | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › AF-01 condition «The selected User is already a project member.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-09.2 | Guard [not a member] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-09.2 | Guard [already a member — AF-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › AF-01 condition «The selected User is already a project member.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-09.2 | Action [System] “Report that no new membership is required” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › AF-01 step 1 «The system reports that no new membership is required.» | EXPLICIT | Matches the step text. Keep |
| UC-09.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-09.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-09.2 | Decision [System] “Account still active?” | Decision | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › EX-01 «The selected User account becomes inactive before confirmation.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-09.2 | Guard [active] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-09.2 | Guard [became inactive — EX-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › EX-01 «The selected User account becomes inactive before confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-09.2 | Action [System] “Reject the addition of the inactive account” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › EX-01 «The selected User account becomes inactive before confirmation.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-09.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-09.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-09.2 | Action [System] “Create the membership and refresh the member list” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › normal_flow[5] «Creates the membership and refreshes the member list.»<br>`data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › postconditions[1] «The target User becomes an active Project Member.» | EXPLICIT | Matches the step text. Keep |
| UC-09.2 | Action [System] “Record the membership change in project activity history” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` › postconditions[2] «The membership change is recorded in project activity history.» | DERIVED | Stated as a postcondition/other information; the flow does not name the step that performs it, so it is shown as the last System action. Keep |
| UC-09.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-09.3 — Remove Project Member (`UC-PROJECT-MEMBER-REMOVE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-09.3 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-09.3 | Action [Project Owner] “Select a project member and request removal” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › normal_flow[1] «Selects a project member and requests removal.» | EXPLICIT | Matches the step text. Keep |
| UC-09.3 | Decision [System] “Own membership selected?” | Decision | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › EX-01 «The Project Owner attempts to remove their own membership.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-09.3 | Guard [another member] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-09.3 | Guard [own membership — EX-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › EX-01 «The Project Owner attempts to remove their own membership.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-09.3 | Action [System] “Reject the removal of the Project Owner's own membership” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › EX-01 «The Project Owner attempts to remove their own membership.»<br>`data/business_rules.yml` › BR-PROJECT-ONE-OWNER «Every active project must have exactly one Project Owner.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-09.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-09.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-09.3 | Action [System] “Display the member's active assignments and ask for confirmation” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › normal_flow[2] «Displays the member's active assignments and asks for confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-09.3 | Decision [System] “Unfinished Sprint work?” | Decision | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › AF-01 condition «The target member owns unfinished Sprint work.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-09.3 | Guard [none] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-09.3 | Guard [owns unfinished work — AF-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › AF-01 condition «The target member owns unfinished Sprint work.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-09.3 | Action [System] “Require the work to be reassigned before removal” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › AF-01 step 1 «The system requires the work to be reassigned before removal.» | EXPLICIT | Matches the step text. Keep |
| UC-09.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-09.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-09.3 | Action [Project Owner] “Confirm the removal” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › normal_flow[3] «Confirms removal after active work has been reassigned or cleared.» | EXPLICIT | Matches the step text. Keep |
| UC-09.3 | Action [System] “Remove Scrum accountabilities and project membership” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › normal_flow[4] «Removes Scrum accountabilities and project membership.»<br>`data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › postconditions[1] «The target User no longer has access through project membership.» | EXPLICIT | Matches the step text. Keep |
| UC-09.3 | Action [System] “Record the removal and refresh the member list” | Action | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › normal_flow[5] «Records the removal and refreshes the member list.»<br>`data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` › postconditions[2] «The removal is recorded in project activity history.» | EXPLICIT | Matches the step text. Keep |
| UC-09.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-11 — Archive Project (`UC-PROJECT-ARCHIVE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-11 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-11 | Action [Project Owner] “Request project archival” | Action | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › normal_flow[1] «Requests project archival.» | EXPLICIT | Matches the step text. Keep |
| UC-11 | Action [System] “Check that the project has no active Sprint” | Action | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › normal_flow[2] «Checks that the project has no active Sprint.» | EXPLICIT | Matches the step text. Keep |
| UC-11 | Decision [System] “Active Sprint?” | Decision | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › EX-01 «The project has an active Sprint and cannot be archived.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-11 | Guard [none] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-11 | Guard [active Sprint — EX-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › EX-01 «The project has an active Sprint and cannot be archived.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-11 | Action [System] “Reject the archival because the project has an active Sprint” | Action | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › EX-01 «The project has an active Sprint and cannot be archived.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-11 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-11 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-11 | Action [System] “Summarize the effects of archival and request confirmation” | Action | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › normal_flow[3] «Summarizes the effects of archival and requests confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-11 | Decision [Project Owner] “Confirm archival?” | Decision | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › AF-01 condition «The Project Owner cancels the confirmation.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-11 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-11 | Action [Project Owner] “Confirm archival” | Action | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › normal_flow[4] «Confirms archival.» | EXPLICIT | Matches the step text. Keep |
| UC-11 | Action [System] “Mark the project and its contained work as read-only” | Action | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › normal_flow[5] «Marks the project and its contained work as read-only.»<br>`data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › postconditions[1] «The project is archived.»<br>`data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › postconditions[2] «Project information remains available in read-only mode.»<br>`data/business_rules.yml` › BR-PROJECT-ARCHIVED-READ-ONLY «An archived project and its contained work are read-only.» | EXPLICIT | Matches the step text. Keep |
| UC-11 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-11 | Guard [cancel — AF-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › AF-01 condition «The Project Owner cancels the confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-11 | Action [System] “Leave the project active and unchanged” | Action | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` › AF-01 step 1 «The system leaves the project active and unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-11 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-11 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-13 — Leave Project (`UC-PROJECT-LEAVE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-13 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-13 | Action [User] “Request to leave the project” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › normal_flow[1] «Requests to leave the project.» | EXPLICIT | Matches the step text. Keep |
| UC-13 | Action [System] “Check ownership and unfinished work constraints” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › normal_flow[2] «Checks ownership and unfinished work constraints.» | EXPLICIT | Matches the step text. Keep |
| UC-13 | Decision [System] “Current Project Owner?” | Decision | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › EX-01 «The current Project Owner attempts to leave before transferring ownership.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-13 | Guard [not the owner] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-13 | Guard [current owner — EX-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › EX-01 «The current Project Owner attempts to leave before transferring ownership.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-13 | Action [System] “Reject the request until ownership is transferred” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › EX-01 «The current Project Owner attempts to leave before transferring ownership.»<br>`data/business_rules.yml` › BR-PROJECT-OWNER-TRANSFER-BEFORE-LEAVE «A Project Owner must transfer ownership before leaving the project.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-13 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-13 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-13 | Decision [System] “Unfinished Sprint Tasks?” | Decision | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › AF-01 condition «The member owns unfinished Sprint Tasks.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-13 | Guard [none] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-13 | Action [System] “Explain the effects of leaving and request confirmation” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › normal_flow[3] «Explains the effects of leaving and requests confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-13 | Action [User] “Confirm leaving the project” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › normal_flow[4] «Confirms leaving the project.» | EXPLICIT | Matches the step text. Keep |
| UC-13 | Guard [owns tasks — AF-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › AF-01 condition «The member owns unfinished Sprint Tasks.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-13 | Action [System] “Warn that unfinished work will become unclaimed” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › AF-01 step 1 «The system warns that unfinished work will become unclaimed.» | EXPLICIT | Matches the step text. Keep |
| UC-13 | Decision [User] “Leave anyway?” | Decision | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › AF-01 condition «The member owns unfinished Sprint Tasks.» | NECESSARY REPRESENTATION | Branch point for AF-01, AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-13 | Guard [confirm — AF-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › AF-01 condition «The member owns unfinished Sprint Tasks.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-13 | Guard [cancel — AF-01] | Guard | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › AF-01 condition «The member owns unfinished Sprint Tasks.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-13 | Action [User] “Cancel the leave request” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › AF-01 step 2 «The member confirms leaving or cancels the request.» | EXPLICIT | Matches the step text. Keep |
| UC-13 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-13 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-13 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-13 | Action [System] “Remove active membership and project-scoped permissions” | Action | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › normal_flow[5] «Removes active membership and project-scoped permissions.»<br>`data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › postconditions[1] «The actor is no longer a member of the project.»<br>`data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › postconditions[2] «Project-scoped access and Scrum accountability are removed.»<br>`data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` › postconditions[3] «Historical contributions remain attributed to the actor.» | EXPLICIT | Matches the step text. Keep |
| UC-13 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-14.3 — Update Product Goal (`UC-PRODUCT-GOAL-UPDATE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-14.3 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-14.3 | Action [Product Owner] “Open the current Product Goal and choose to edit it” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › normal_flow[1] «Opens the current Product Goal and chooses to edit it.» | EXPLICIT | Matches the step text. Keep |
| UC-14.3 | Action [System] “Display the current goal text” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › normal_flow[2] «Displays the current goal text.» | EXPLICIT | Matches the step text. Keep |
| UC-14.3 | Decision [Product Owner] “Save the revision?” | Decision | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › AF-01 condition «The User cancels before saving.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-14.3 | Guard [save] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-14.3 | Action [Product Owner] “Revise the Product Goal and confirm the change” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › normal_flow[3] «Revises the Product Goal and confirms the change.» | EXPLICIT | Matches the step text. Keep |
| UC-14.3 | Action [System] “Validate the revised Product Goal” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › normal_flow[4] «Validates and saves the revised Product Goal.» | EXPLICIT | Matches the step text. Keep |
| UC-14.3 | Decision [System] “Still the Product Owner?” | Decision | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › EX-01 «The actor loses Product Owner accountability before confirmation.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-14.3 | Guard [yes] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-14.3 | Guard [accountability lost — EX-01] | Guard | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › EX-01 «The actor loses Product Owner accountability before confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-14.3 | Action [System] “Reject the revision from the former Product Owner” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › EX-01 «The actor loses Product Owner accountability before confirmation.»<br>`data/business_rules.yml` › BR-PRODUCT-ONE-GOAL «A Scrum project has one current Product Goal at a time, and only the Product Ow…»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-14.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-14.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-14.3 | Action [System] “Save the revised Product Goal” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › normal_flow[4] «Validates and saves the revised Product Goal.»<br>`data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › postconditions[1] «The revised Product Goal becomes the project's current Product Goal.» | EXPLICIT | Matches the step text. Keep |
| UC-14.3 | Action [System] “Record the change in project activity history” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › postconditions[2] «The change is recorded in project activity history.» | DERIVED | Stated as a postcondition/other information; the flow does not name the step that performs it, so it is shown as the last System action. Keep |
| UC-14.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-14.3 | Guard [cancel before saving — AF-01] | Guard | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › AF-01 condition «The User cancels before saving.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-14.3 | Action [System] “Keep the current Product Goal unchanged” | Action | `data/use_cases/product-backlog/UC-PRODUCT-GOAL-UPDATE.yml` › AF-01 step 1 «The system keeps the current Product Goal unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-14.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-14.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-15.2 — Create Product Backlog Item (`UC-BACKLOG-ITEM-CREATE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-15.2 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-15.2 | Action [Product Owner] “Choose to create a Product Backlog Item” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › normal_flow[1] «Chooses to create a Product Backlog Item.» | EXPLICIT | Matches the step text. Keep |
| UC-15.2 | Action [System] “Request the title, description, acceptance criteria, and item type” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › normal_flow[2] «Requests the title, description, acceptance criteria, and item type.» | EXPLICIT | Matches the step text. Keep |
| UC-15.2 | Decision [Product Owner] “Information complete?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › AF-01 condition «The User saves incomplete information as a draft item.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-15.2 | Guard [complete] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-15.2 | Action [Product Owner] “Provide the required information and confirm creation” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › normal_flow[3] «Provides the required information and confirms creation.» | EXPLICIT | Matches the step text. Keep |
| UC-15.2 | Action [System] “Validate the new item” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › normal_flow[4] «Validates and stores the new item.» | EXPLICIT | Matches the step text. Keep |
| UC-15.2 | Decision [System] “Identifying information present?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › EX-01 «Required identifying information is missing.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-15.2 | Guard [present] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-15.2 | Guard [missing — EX-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › EX-01 «Required identifying information is missing.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-15.2 | Action [System] “Reject the item without identifying information” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › EX-01 «Required identifying information is missing.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-15.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-15.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-15.2 | Action [System] “Store the new item in the Product Backlog” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › normal_flow[4] «Validates and stores the new item.»<br>`data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › postconditions[1] «A new Product Backlog Item is stored in the Product Backlog.» | EXPLICIT | Matches the step text. Keep |
| UC-15.2 | Guard [incomplete, saved as draft — AF-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › AF-01 condition «The User saves incomplete information as a draft item.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-15.2 | Action [System] “Save the incomplete information as a draft item” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › AF-01 condition «The User saves incomplete information as a draft item.» | CONFLICT | The AF-01 condition makes the User (Product Owner) the actor, but the action is in the System partition and repeats the storing already shown by AF-01.1. Make it the Product Owner's action |
| UC-15.2 | Action [System] “Store the item without marking it ready for Sprint planning” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › AF-01 step 1 «The system stores the item but does not mark it ready for Sprint planning.»<br>`data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › postconditions[1] «A new Product Backlog Item is stored in the Product Backlog.» | EXPLICIT | Matches the step text. Keep |
| UC-15.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-15.2 | Action [System] “Record the creation in item activity history” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-CREATE.yml` › postconditions[2] «The creation is recorded in item activity history.» | DERIVED | Stated as a postcondition/other information; the flow does not name the step that performs it, so it is shown as the last System action. Keep |
| UC-15.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-15.4 — Remove Product Backlog Item (`UC-BACKLOG-ITEM-REMOVE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-15.4 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-15.4 | Action [Product Owner] “Select a Product Backlog Item and request removal” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › normal_flow[1] «Selects a Product Backlog Item and requests removal.» | EXPLICIT | Matches the step text. Keep |
| UC-15.4 | Decision [System] “Item in the active Sprint?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › EX-01 «The item is locked because it belongs to the active Sprint.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-15.4 | Guard [not in the active Sprint] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-15.4 | Guard [locked in the active Sprint — EX-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › EX-01 «The item is locked because it belongs to the active Sprint.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-15.4 | Action [System] “Reject the removal of the locked item” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › EX-01 «The item is locked because it belongs to the active Sprint.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-15.4 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-15.4 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-15.4 | Action [System] “Display the impact and request confirmation” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › normal_flow[2] «Displays the impact and requests confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-15.4 | Decision [Product Owner] “Confirm removal?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › AF-01 condition «The User cancels removal.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-15.4 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-15.4 | Action [Product Owner] “Confirm removal” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › normal_flow[3] «Confirms removal.» | EXPLICIT | Matches the step text. Keep |
| UC-15.4 | Action [System] “Remove the item and record the action” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › normal_flow[4] «Removes the item and records the action.»<br>`data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › postconditions[1] «The item is removed from the active Product Backlog.»<br>`data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › postconditions[2] «The removal is recorded in activity history.» | EXPLICIT | Matches the step text. Keep |
| UC-15.4 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-15.4 | Guard [cancel — AF-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › AF-01 condition «The User cancels removal.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-15.4 | Action [System] “Leave the Product Backlog Item unchanged” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REMOVE.yml` › AF-01 step 1 «The system leaves the Product Backlog Item unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-15.4 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-15.4 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-17 — Refine Backlog Item (`UC-BACKLOG-ITEM-REFINE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-17 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-17 | Action [Product Owner] “Select an item that requires refinement” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › normal_flow[1] «Acting as the Product Owner, selects an item that requires refinement.» | EXPLICIT | Matches the step text. Keep |
| UC-17 | Action [System] “Display the item's current details and estimate” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › normal_flow[2] «Displays the item's current details and estimate.» | EXPLICIT | Matches the step text. Keep |
| UC-17 | Action [Product Owner] “Clarify the expected outcome and acceptance criteria” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › normal_flow[3] «Acting as the Product Owner, clarifies the expected outcome and acceptance criteria.» | EXPLICIT | Matches the step text. Keep |
| UC-17 | Action [Developer] “Add implementation-relevant clarification and propose decomposition when needed” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › normal_flow[4] «Acting as a Developer, adds implementation-relevant clarification and proposes decomposition w…» | EXPLICIT | Matches the step text. Keep |
| UC-17 | Decision [System] “Too large for one Sprint?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › AF-01 condition «The item is too large for one Sprint.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-17 | Guard [fits one Sprint] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-17 | Guard [too large — AF-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › AF-01 condition «The item is too large for one Sprint.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-17 | Decision [System] “Selected into an active Sprint?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › EX-01 «The item is selected into an active Sprint and can no longer be substantially decomposed.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-17 | Guard [not selected] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-17 | Guard [selected — EX-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › EX-01 «The item is selected into an active Sprint and can no longer be substantially decomposed.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-17 | Action [System] “Reject the decomposition of the item in the active Sprint” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › EX-01 «The item is selected into an active Sprint and can no longer be substantially decomposed.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-17 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-17 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-17 | Action [Product Owner] “Define smaller independent backlog items with the Developer” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › AF-01 step 1 «The actors define smaller independent backlog items.»<br>`data/business_rules.yml` › BR-PRODUCT-OWNER-BACKLOG «Only the Product Owner may create, update, remove, or reorder Product Backlog I…» | DERIVED | AF-01.1 "The actors define smaller independent backlog items"; drawn in the Product Owner partition because BR-PRODUCT-OWNER-BACKLOG lets only the Product Owner create items. Keep |
| UC-17 | Action [System] “Preserve traceability to the original item” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › AF-01 step 2 «The system preserves traceability to the original item.» | EXPLICIT | Matches the step text. Keep |
| UC-17 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-17 | Action [Product Owner] “Confirm the refined scope and description” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › normal_flow[5] «Acting as the Product Owner, confirms the refined scope and description.» | EXPLICIT | Matches the step text. Keep |
| UC-17 | Action [System] “Save the refined item and record the participants” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › normal_flow[6] «Saves the refined item and records the participants.»<br>`data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › postconditions[1] «The item contains the clarified information agreed during refinement.»<br>`data/use_cases/product-backlog/UC-BACKLOG-ITEM-REFINE.yml` › postconditions[2] «The item can be evaluated for Sprint selection readiness.» | EXPLICIT | Matches the step text. Keep |
| UC-17 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-18 — Estimate Backlog Item (`UC-BACKLOG-ITEM-ESTIMATE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-18 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-18 | Action [Developer] “Select a refined Product Backlog Item” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › normal_flow[1] «Acting as a Developer, selects a refined Product Backlog Item.» | EXPLICIT | Matches the step text. Keep |
| UC-18 | Action [System] “Display the item's details and current estimate” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › normal_flow[2] «Displays the item's details and current estimate.» | EXPLICIT | Matches the step text. Keep |
| UC-18 | Decision [Product Owner] “Clarification requested?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` | DERIVED | NF3: the Product Owner clarifies the expected outcome "when requested". Keep |
| UC-18 | Guard [requested] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-18 | Action [Product Owner] “Clarify the expected outcome” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › normal_flow[3] «Acting as the Product Owner, clarifies the expected outcome when requested.» | EXPLICIT | Matches the step text. Keep |
| UC-18 | Guard [not requested] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-18 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-18 | Decision [Developer] “Sufficiently refined?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › AF-01 condition «Developers determine that the item is not sufficiently refined.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-18 | Guard [sufficient] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-18 | Action [Developer] “Provide the agreed estimate” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › normal_flow[4] «Acting as a Developer, provides the agreed estimate.»<br>`data/business_rules.yml` › BR-DEVELOPER-ESTIMATION «Only Developers who will perform the work may set or revise the estimate of a P…» | EXPLICIT | Matches the step text. Keep |
| UC-18 | Guard [not refined — AF-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › AF-01 condition «Developers determine that the item is not sufficiently refined.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-18 | Action [System] “Leave the estimate unset for this item” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › AF-01 step 1 «The system leaves the estimate unset.» | EXPLICIT | Matches the step text. Keep |
| UC-18 | Action [System] “Return the item to the Product Owner for further refinement” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › AF-01 step 2 «The item is returned for further refinement.» | UNSUPPORTED | AF-01.2 says only that the item is returned for further refinement; the recipient "the Product Owner" is added. Remove the added recipient |
| UC-18 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-18 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-18 | Action [System] “Validate the estimate” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › normal_flow[5] «Validates and records the estimate.» | EXPLICIT | Matches the step text. Keep |
| UC-18 | Decision [System] “Item still estimable?” | Decision | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › EX-01 «The item was removed or selected into a completed Sprint before the estimate was saved.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-18 | Guard [estimable] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-18 | Guard [unavailable — EX-01] | Guard | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › EX-01 «The item was removed or selected into a completed Sprint before the estimate was saved.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-18 | Action [System] “Reject the estimate because the item was removed or is in a completed Sprint” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › EX-01 «The item was removed or selected into a completed Sprint before the estimate was saved.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-18 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-18 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-18 | Action [System] “Record the estimate” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › normal_flow[5] «Validates and records the estimate.»<br>`data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › postconditions[1] «The agreed estimate is associated with the Product Backlog Item.» | EXPLICIT | Matches the step text. Keep |
| UC-18 | Action [System] “Record the estimate change in item activity history” | Action | `data/use_cases/product-backlog/UC-BACKLOG-ITEM-ESTIMATE.yml` › postconditions[2] «The estimate change is recorded in item activity history.» | DERIVED | Stated as a postcondition/other information; the flow does not name the step that performs it, so it is shown as the last System action. Keep |
| UC-18 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-19 — Plan Sprint (`UC-SPRINT-PLAN`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-19 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-19 | Action [Product Owner] “Start Sprint planning and propose the Sprint Goal and date range” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › normal_flow[1] «Acting as the Product Owner, starts Sprint planning and proposes the Sprint Goal and date rang…»<br>`data/business_rules.yml` › BR-SPRINT-GOAL-REQUIRED «A Sprint must have a Sprint Goal before it can start.» | EXPLICIT | Matches the step text. Keep |
| UC-19 | Action [System] “Display the ordered Product Backlog Items that are ready for selection” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › normal_flow[2] «Displays ordered Product Backlog Items that are ready for selection.»<br>`data/business_rules.yml` › BR-BACKLOG-ITEM-READY «A Product Backlog Item may be selected for a Sprint only after its description,…» | EXPLICIT | Matches the step text. Keep |
| UC-19 | Action [Product Owner] “Propose backlog items that support the Sprint Goal” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › normal_flow[3] «Acting as the Product Owner, proposes backlog items that support the Sprint Goal.» | EXPLICIT | Matches the step text. Keep |
| UC-19 | Action [Developer] “Review capacity, estimates and item readiness” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › normal_flow[4] «Acting as a Developer, reviews capacity, estimates, and item readiness.» | EXPLICIT | Matches the step text. Keep |
| UC-19 | Loop decision [System] “A selected item not ready?” | Loop | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › AF-01 condition «A selected item is not ready.» | DERIVED | Return path of AF-01: the alternative flow re-performs the step and the condition is evaluated again. Keep |
| UC-19 | Guard [not ready — AF-01] | Guard | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › AF-01 condition «A selected item is not ready.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-19 | Action [System] “Identify the missing readiness information” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › AF-01 step 1 «The system identifies the missing readiness information.»<br>`data/business_rules.yml` › BR-BACKLOG-ITEM-READY «A Product Backlog Item may be selected for a Sprint only after its description,…» | EXPLICIT | Matches the step text. Keep |
| UC-19 | Action [Product Owner] “Refine the item or remove it from the Sprint selection with the Developer” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › AF-01 step 2 «The actors refine the item or remove it from the Sprint selection.» | DERIVED | AF-01.2 "The actors refine the item or remove it"; Product Owner partition because the Product Owner owns the selection (NF3, NF5). Keep |
| UC-19 | Guard [all ready] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-19 | Action [Product Owner] “Confirm the Sprint Goal and selected items with the Developer” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › normal_flow[5] «Acting as the Product Owner, confirms the Sprint Goal and selected items with the Developer.» | EXPLICIT | Matches the step text. Keep |
| UC-19 | Decision [System] “Date range conflicts?” | Decision | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › EX-01 «The Sprint cannot be saved because its date range conflicts with another Sprint.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-19 | Guard [no conflict] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-19 | Guard [conflict — EX-01] | Guard | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › EX-01 «The Sprint cannot be saved because its date range conflicts with another Sprint.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-19 | Action [System] “Reject saving the Sprint because its date range conflicts with another Sprint” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › EX-01 «The Sprint cannot be saved because its date range conflicts with another Sprint.»<br>`data/business_rules.yml` › BR-SPRINT-DATE-RANGE «A Sprint end date must be later than its start date and the Sprint duration mus…»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-19 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-19 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-19 | Action [System] “Create the Draft Sprint and its initial Sprint Backlog” | Action | `data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › normal_flow[6] «Creates the Draft Sprint and its initial Sprint Backlog.»<br>`data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › postconditions[1] «A Draft Sprint exists with a proposed Sprint Goal, dates, and selected backlog items.»<br>`data/use_cases/sprint-management/UC-SPRINT-PLAN.yml` › postconditions[2] «Selected items are associated with the Draft Sprint.»<br>`data/business_rules.yml` › BR-SPRINT-ONE-DRAFT «A project may have at most one Draft Sprint at a time.» | EXPLICIT | Matches the step text. Keep |
| UC-19 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-22 — Cancel Sprint (`UC-SPRINT-CANCEL`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-22 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-22 | Action [Product Owner] “Request Sprint cancellation and provide a reason” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › normal_flow[1] «Requests Sprint cancellation and provides a reason.»<br>`data/business_rules.yml` › BR-SPRINT-CANCEL-PO-ONLY «Only the Product Owner can cancel an active Sprint when its Sprint Goal becomes…» | EXPLICIT | Matches the step text. Keep |
| UC-22 | Decision [System] “Sprint still active?” | Decision | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › EX-01 «The Sprint has already been completed or cancelled.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-22 | Guard [active] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-22 | Guard [already completed or cancelled — EX-01] | Guard | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › EX-01 «The Sprint has already been completed or cancelled.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-22 | Action [System] “Reject the cancellation because the Sprint is no longer active” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › EX-01 «The Sprint has already been completed or cancelled.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-22 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-22 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-22 | Action [System] “Display the impact on selected and completed work” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › normal_flow[2] «Displays the impact on selected and completed work.» | EXPLICIT | Matches the step text. Keep |
| UC-22 | Decision [Product Owner] “Confirm the cancellation?” | Decision | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › AF-01 condition «The Product Owner decides to continue the Sprint.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-22 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-22 | Action [Product Owner] “Confirm the cancellation” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › normal_flow[3] «Confirms the cancellation.» | EXPLICIT | Matches the step text. Keep |
| UC-22 | Action [System] “Cancel the Sprint and return incomplete items to the Product Backlog” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › normal_flow[4] «Cancels the Sprint and returns incomplete items to the Product Backlog.»<br>`data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › postconditions[1] «The Sprint is cancelled and cannot receive further work updates.»<br>`data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › postconditions[2] «Incomplete items are returned to the Product Backlog.»<br>`data/business_rules.yml` › BR-SPRINT-INCOMPLETE-RETURN-BACKLOG «Incomplete Product Backlog Items return to the Product Backlog when a Sprint is…» | EXPLICIT | Matches the step text. Keep |
| UC-22 | Action [System] “Record the cancellation reason and timestamp” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › normal_flow[5] «Records the cancellation reason and timestamp.» | EXPLICIT | Matches the step text. Keep |
| UC-22 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-22 | Guard [continue the Sprint — AF-01] | Guard | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › AF-01 condition «The Product Owner decides to continue the Sprint.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-22 | Action [System] “Cancel the confirmation” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › AF-01 step 1 «The Product Owner cancels the confirmation.» | CONFLICT | AF-01.1 says the Product Owner cancels the confirmation, but the action is drawn in the System partition (the else-branch inherited the partition of the then-branch). Move it to the Product Owner partition |
| UC-22 | Action [System] “Leave the Sprint unchanged” | Action | `data/use_cases/sprint-management/UC-SPRINT-CANCEL.yml` › AF-01 step 2 «The system leaves the Sprint unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-22 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-22 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-23 — Review Sprint Board (`UC-SPRINT-BOARD-REVIEW`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-23 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-23 | Action [User] “Open the Sprint Board” | Action | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › normal_flow[1] «Opens the Sprint Board.»<br>`data/business_rules.yml` › BR-PROJECT-MEMBER-ACCESS «Project information is available only to active members of that project.» | EXPLICIT | Matches the step text. Keep |
| UC-23 | Decision [System] “Active Sprint exists?” | Decision | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › AF-01 condition «The project has no active Sprint.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-23 | Guard [active Sprint] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-23 | Action [System] “Load the active Sprint and its work items” | Action | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › normal_flow[2] «Loads the active Sprint and its work items.» | EXPLICIT | Matches the step text. Keep |
| UC-23 | Decision [System] “Sprint data available?” | Decision | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › EX-01 «The board cannot be loaded because Sprint data is temporarily unavailable.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-23 | Guard [available] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-23 | Guard [unavailable — EX-01] | Guard | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › EX-01 «The board cannot be loaded because Sprint data is temporarily unavailable.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-23 | Action [System] “Report that the Sprint Board cannot be loaded at this time” | Action | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › EX-01 «The board cannot be loaded because Sprint data is temporarily unavailable.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-23 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-23 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-23 | Action [System] “Group the items by their current workflow status” | Action | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › normal_flow[3] «Groups items by current workflow status.» | EXPLICIT | Matches the step text. Keep |
| UC-23 | Action [System] “Display item priority, assignee, estimate and status” | Action | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › normal_flow[4] «Displays item priority, assignee, estimate, and status.»<br>`data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › postconditions[1] «The actor sees the current Sprint Board without changing project data.» | EXPLICIT | Matches the step text. Keep |
| UC-23 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-23 | Guard [no active Sprint — AF-01] | Guard | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › AF-01 condition «The project has no active Sprint.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-23 | Action [System] “Display that no Sprint is active” | Action | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › AF-01 step 1 «The system displays that no Sprint is active.» | EXPLICIT | Matches the step text. Keep |
| UC-23 | Decision [System] “Previous Sprint information available?” | Decision | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` | DERIVED | AF-01.2 offers previous Sprint information "when available". Keep |
| UC-23 | Guard [available] | Guard | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-23 | Action [System] “Offer access to previous Sprint information” | Action | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` › AF-01 step 2 «The system offers access to previous Sprint information when available.» | EXPLICIT | Matches the step text. Keep |
| UC-23 | Guard [not available] | Guard | `data/use_cases/sprint-work/UC-SPRINT-BOARD-REVIEW.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-23 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-23 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-23 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-24.3 — Update Sprint Task (`UC-SPRINT-TASK-UPDATE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-24.3 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-24.3 | Action [Developer] “Open a Sprint Task for editing” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › normal_flow[1] «Opens a Sprint Task for editing.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-DEVELOPER «Only an active Developer in the project may create, update, assign, claim, or r…» | EXPLICIT | Matches the step text. Keep |
| UC-24.3 | Action [System] “Display the editable task information” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › normal_flow[2] «Displays the editable task information.» | EXPLICIT | Matches the step text. Keep |
| UC-24.3 | Decision [Developer] “Submit the changes?” | Decision | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › AF-01 condition «The User cancels before saving.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.3 | Guard [submit] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.3 | Action [Developer] “Update the desired values and submit the task” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › normal_flow[3] «Updates the desired values and submits the task.» | EXPLICIT | Matches the step text. Keep |
| UC-24.3 | Action [System] “Validate the changes” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › normal_flow[4] «Validates and saves the changes.» | EXPLICIT | Matches the step text. Keep |
| UC-24.3 | Decision [System] “Task still in the active Sprint?” | Decision | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › EX-01 «The task is no longer part of the active Sprint.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.3 | Guard [in the active Sprint] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.3 | Guard [no longer in the active Sprint — EX-01] | Guard | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › EX-01 «The task is no longer part of the active Sprint.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.3 | Action [System] “Reject the update because the task is no longer in the active Sprint” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › EX-01 «The task is no longer part of the active Sprint.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-ACTIVE-SPRINT «A Sprint Work Item must belong to the project's active Sprint.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-24.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-24.3 | Action [System] “Save the changes” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › normal_flow[4] «Validates and saves the changes.»<br>`data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › postconditions[1] «Valid task changes are stored.» | EXPLICIT | Matches the step text. Keep |
| UC-24.3 | Action [System] “Record the update in work item activity” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › postconditions[2] «The update is recorded in work item activity.» | DERIVED | Stated as a postcondition/other information; the flow does not name the step that performs it, so it is shown as the last System action. Keep |
| UC-24.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.3 | Guard [cancel before saving — AF-01] | Guard | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › AF-01 condition «The User cancels before saving.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.3 | Action [System] “Discard the unsaved task changes” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-UPDATE.yml` › AF-01 step 1 «The system discards unsaved task changes.» | EXPLICIT | Matches the step text. Keep |
| UC-24.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-24.5 — Delete Sprint Task (`UC-SPRINT-TASK-DELETE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-24.5 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-24.5 | Action [Developer] “Select a Sprint Task and request deletion” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › normal_flow[1] «Selects a Sprint Task and requests deletion.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-DEVELOPER «Only an active Developer in the project may create, update, assign, claim, or r…» | EXPLICIT | Matches the step text. Keep |
| UC-24.5 | Decision [System] “Task already in execution?” | Decision | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › EX-01 «The Sprint Task has already entered execution.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.5 | Guard [not started] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.5 | Guard [in execution — EX-01] | Guard | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › EX-01 «The Sprint Task has already entered execution.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.5 | Action [System] “Reject the deletion of the started task” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › EX-01 «The Sprint Task has already entered execution.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-ACTIVE-SPRINT «A Sprint Work Item must belong to the project's active Sprint.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-24.5 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.5 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-24.5 | Decision [System] “Other tasks depend on it?” | Decision | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › AF-01 condition «Other tasks depend on the selected task.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.5 | Guard [no dependent tasks] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.5 | Guard [dependent tasks — AF-01] | Guard | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › AF-01 condition «Other tasks depend on the selected task.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.5 | Action [System] “Require the dependencies to be removed before deletion” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › AF-01 step 1 «The system requires the dependencies to be removed before deletion.» | EXPLICIT | Matches the step text. Keep |
| UC-24.5 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.5 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-24.5 | Action [System] “Display the dependency impact and ask for confirmation” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › normal_flow[2] «Displays the task's dependency impact and asks for confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-24.5 | Action [Developer] “Confirm deletion” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › normal_flow[3] «Confirms deletion.» | EXPLICIT | Matches the step text. Keep |
| UC-24.5 | Action [System] “Delete the task and record the action” | Action | `data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › normal_flow[4] «Deletes the task and records the action.»<br>`data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › postconditions[1] «The Sprint Task is removed from active Sprint work.»<br>`data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › postconditions[2] «The deletion is recorded in activity history.»<br>`data/use_cases/sprint-work/UC-SPRINT-TASK-DELETE.yml` › other_information «Historical audit information is preserved after deletion.» | EXPLICIT | Matches the step text. Keep |
| UC-24.5 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-24.6 — Add Task Dependency (`UC-TASK-DEPENDENCY-ADD`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-24.6 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-24.6 | Action [Developer] “Open a Sprint Task and choose to add a dependency” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › normal_flow[1] «Opens a Sprint Task and chooses to add a dependency.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-DEVELOPER «Only an active Developer in the project may create, update, assign, claim, or r…» | EXPLICIT | Matches the step text. Keep |
| UC-24.6 | Action [System] “Display eligible tasks in the same project” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › normal_flow[2] «Displays eligible tasks in the same project.»<br>`data/business_rules.yml` › BR-TASK-DEPENDENCY-SAME-PROJECT «A task may only depend on another task within the same project.» | EXPLICIT | Matches the step text. Keep |
| UC-24.6 | Action [Developer] “Select the dependency target and confirm the relationship” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › normal_flow[3] «Selects the dependency target and confirms the relationship.» | EXPLICIT | Matches the step text. Keep |
| UC-24.6 | Action [System] “Validate the dependency” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › normal_flow[4] «Validates and stores the dependency.» | EXPLICIT | Matches the step text. Keep |
| UC-24.6 | Decision [System] “Same task selected?” | Decision | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › EX-02 «The User selects the same task as its own dependency.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.6 | Guard [different task] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.6 | Guard [same task — EX-02] | Guard | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › EX-02 «The User selects the same task as its own dependency.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.6 | Action [System] “Reject the dependency of the task on itself” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › EX-02 «The User selects the same task as its own dependency.»<br>`data/business_rules.yml` › BR-TASK-NO-SELF-DEPENDENCY «A task must not depend on itself.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-02 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-24.6 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.6 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-24.6 | Decision [System] “Would it create a cycle?” | Decision | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › EX-01 «The selected relationship would create a direct or indirect cycle.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.6 | Guard [no cycle] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.6 | Guard [direct or indirect cycle — EX-01] | Guard | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › EX-01 «The selected relationship would create a direct or indirect cycle.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.6 | Action [System] “Reject the dependency that would create a cycle” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › EX-01 «The selected relationship would create a direct or indirect cycle.»<br>`data/business_rules.yml` › BR-TASK-DEPENDENCY-ACYCLIC «Task dependency relationships must not create direct or indirect cycles.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-24.6 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.6 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-24.6 | Action [System] “Store the dependency” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › normal_flow[4] «Validates and stores the dependency.»<br>`data/use_cases/sprint-work/UC-TASK-DEPENDENCY-ADD.yml` › postconditions[1] «A valid dependency relationship is stored between the selected tasks.» | EXPLICIT | Matches the step text. Keep |
| UC-24.6 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-24.7 — Remove Task Dependency (`UC-TASK-DEPENDENCY-REMOVE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-24.7 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-24.7 | Action [Developer] “Open a Sprint Task and select an existing dependency” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › normal_flow[1] «Opens a Sprint Task and selects an existing dependency.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-DEVELOPER «Only an active Developer in the project may create, update, assign, claim, or r…» | EXPLICIT | Matches the step text. Keep |
| UC-24.7 | Action [Developer] “Request removal of the dependency” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › normal_flow[2] «Requests removal of the dependency.» | EXPLICIT | Matches the step text. Keep |
| UC-24.7 | Action [System] “Request confirmation and display the affected tasks” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › normal_flow[3] «Requests confirmation and displays the affected tasks.» | EXPLICIT | Matches the step text. Keep |
| UC-24.7 | Decision [Developer] “Confirm removal?” | Decision | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › AF-01 condition «The User cancels before confirmation.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.7 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.7 | Action [Developer] “Confirm removal” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › normal_flow[4] «Confirms removal.» | EXPLICIT | Matches the step text. Keep |
| UC-24.7 | Decision [System] “Dependency still exists?” | Decision | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › EX-01 «The dependency was already removed by another User.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-24.7 | Guard [exists] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-24.7 | Guard [already removed — EX-01] | Guard | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › EX-01 «The dependency was already removed by another User.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.7 | Action [System] “Report that the dependency was already removed” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › EX-01 «The dependency was already removed by another User.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-24.7 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.7 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-24.7 | Action [System] “Remove the relationship and record the change” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › normal_flow[5] «Removes the relationship and records the change.»<br>`data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › postconditions[1] «The selected dependency relationship no longer affects the tasks.»<br>`data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › postconditions[2] «The removal is recorded in work item activity.» | EXPLICIT | Matches the step text. Keep |
| UC-24.7 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.7 | Guard [cancel — AF-01] | Guard | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › AF-01 condition «The User cancels before confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-24.7 | Action [System] “Leave the dependency unchanged” | Action | `data/use_cases/sprint-work/UC-TASK-DEPENDENCY-REMOVE.yml` › AF-01 step 1 «The system leaves the dependency unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-24.7 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-24.7 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-27.3 — Update Subtask (`UC-SUBTASK-UPDATE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-27.3 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-27.3 | Action [Developer] “Open a subtask for editing” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › normal_flow[1] «Opens a subtask for editing.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-DEVELOPER «Only an active Developer in the project may create, update, assign, claim, or r…» | EXPLICIT | Matches the step text. Keep |
| UC-27.3 | Action [System] “Display its current editable values” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › normal_flow[2] «Displays its current editable values.» | EXPLICIT | Matches the step text. Keep |
| UC-27.3 | Decision [Developer] “Submit the changes?” | Decision | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › AF-01 condition «The User cancels editing.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-27.3 | Guard [submit] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-27.3 | Action [Developer] “Revise the information and submit the subtask” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › normal_flow[3] «Revises the information and submits the subtask.» | EXPLICIT | Matches the step text. Keep |
| UC-27.3 | Action [System] “Validate the changes” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › normal_flow[4] «Validates and saves the changes.» | EXPLICIT | Matches the step text. Keep |
| UC-27.3 | Decision [System] “Parent still in the active Sprint?” | Decision | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › EX-01 «The parent task is no longer part of the active Sprint.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-27.3 | Guard [in the active Sprint] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-27.3 | Guard [no longer in the active Sprint — EX-01] | Guard | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › EX-01 «The parent task is no longer part of the active Sprint.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-27.3 | Action [System] “Reject the update because the parent task left the active Sprint” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › EX-01 «The parent task is no longer part of the active Sprint.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-ACTIVE-SPRINT «A Sprint Work Item must belong to the project's active Sprint.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-27.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-27.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-27.3 | Action [System] “Save the changes” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › normal_flow[4] «Validates and saves the changes.»<br>`data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › postconditions[1] «Valid subtask changes are stored.» | EXPLICIT | Matches the step text. Keep |
| UC-27.3 | Decision [System] “Parent progress affected?” | Decision | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` | DERIVED | POST2: parent-task progress is recalculated "when relevant". Keep |
| UC-27.3 | Guard [affected] | Guard | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-27.3 | Action [System] “Recalculate parent-task progress” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › postconditions[2] «Parent-task progress is recalculated when relevant.» | DERIVED | Stated as a postcondition/other information; the flow does not name the step that performs it, so it is shown as the last System action. Keep |
| UC-27.3 | Guard [not affected] | Guard | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-27.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-27.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-27.3 | Guard [cancel editing — AF-01] | Guard | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › AF-01 condition «The User cancels editing.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-27.3 | Action [System] “Keep the subtask unchanged” | Action | `data/use_cases/sprint-work/UC-SUBTASK-UPDATE.yml` › AF-01 step 1 «The system keeps the subtask unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-27.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-27.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-27.5 — Delete Subtask (`UC-SUBTASK-DELETE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-27.5 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-27.5 | Action [Developer] “Select an incomplete subtask and request deletion” | Action | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › normal_flow[1] «Selects an incomplete subtask and requests deletion.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-DEVELOPER «Only an active Developer in the project may create, update, assign, claim, or r…» | EXPLICIT | Matches the step text. Keep |
| UC-27.5 | Action [System] “Request confirmation” | Action | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › normal_flow[2] «Requests confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-27.5 | Decision [Developer] “Confirm deletion?” | Decision | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › AF-01 condition «The User cancels deletion.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-27.5 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-27.5 | Action [Developer] “Confirm deletion” | Action | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › normal_flow[3] «Confirms deletion.» | EXPLICIT | Matches the step text. Keep |
| UC-27.5 | Decision [System] “Deletion still allowed?” | Decision | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › EX-01 «The subtask was completed or the Sprint ended before confirmation.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-27.5 | Guard [allowed] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-27.5 | Guard [completed or Sprint ended — EX-01] | Guard | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › EX-01 «The subtask was completed or the Sprint ended before confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-27.5 | Action [System] “Reject the deletion because the subtask was completed or the Sprint ended” | Action | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › EX-01 «The subtask was completed or the Sprint ended before confirmation.»<br>`data/business_rules.yml` › BR-SPRINT-TASK-ACTIVE-SPRINT «A Sprint Work Item must belong to the project's active Sprint.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-27.5 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-27.5 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-27.5 | Action [System] “Remove the subtask and recalculate parent-task progress” | Action | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › normal_flow[4] «Removes the subtask and recalculates parent-task progress.»<br>`data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › postconditions[1] «The subtask is removed from the parent task.»<br>`data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › postconditions[2] «Parent-task progress is recalculated.»<br>`data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › other_information «Historical activity referring to the removed subtask remains available.» | EXPLICIT | Matches the step text. Keep |
| UC-27.5 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-27.5 | Guard [cancel — AF-01] | Guard | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › AF-01 condition «The User cancels deletion.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-27.5 | Action [System] “Leave the subtask unchanged” | Action | `data/use_cases/sprint-work/UC-SUBTASK-DELETE.yml` › AF-01 step 1 «The system leaves the subtask unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-27.5 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-27.5 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-30 — Review Notifications (`UC-NOTIFICATIONS-REVIEW`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-30 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-30 | Action [User] “Open the notification center” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › normal_flow[1] «Opens the notification center.»<br>`data/business_rules.yml` › BR-NOTIFICATION-OWNER-ONLY «A User can review only notifications addressed to that User.» | EXPLICIT | Matches the step text. Keep |
| UC-30 | Action [System] “Display the actor's notifications and email delivery preference in reverse chronological order” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › normal_flow[2] «Displays the actor's notifications and email delivery preference in reverse chronological orde…»<br>`data/business_rules.yml` › BR-NOTIFICATION-OWNER-ONLY «A User can review only notifications addressed to that User.» | EXPLICIT | Matches the step text. Keep |
| UC-30 | Decision [User] “Review a notification?” | Decision | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` | DERIVED | NF3, AF-01 and AF-02 are alternative actor choices after NF2; the YAML does not order them. Keep |
| UC-30 | Guard [review] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-30 | Action [User] “Select a notification to review” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › normal_flow[3] «Selects a notification to review.» | EXPLICIT | Matches the step text. Keep |
| UC-30 | Decision [System] “Related item accessible?” | Decision | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › EX-01 «The related project item is no longer accessible to the actor.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-30 | Guard [accessible] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-30 | Guard [inaccessible — EX-01] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › EX-01 «The related project item is no longer accessible to the actor.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-30 | Action [System] “Report that the related project item is no longer accessible” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › EX-01 «The related project item is no longer accessible to the actor.»<br>`data/business_rules.yml` › BR-PROJECT-MEMBER-ACCESS «Project information is available only to active members of that project.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-30 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-30 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-30 | Action [System] “Mark it as read and display its related project context” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › normal_flow[4] «Marks it as read and displays its related project context.»<br>`data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › postconditions[1] «Selected notifications may be marked as read.»<br>`data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › postconditions[3] «No project work data is changed.» | EXPLICIT | Matches the step text. Keep |
| UC-30 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-30 | Guard [other request] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-30 | Decision [System] “Requested action?” | Decision | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › AF-01 condition «The actor chooses to mark all notifications as read.» | NECESSARY REPRESENTATION | Branch point for AF-01, AF-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-30 | Guard [mark all — AF-01] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › AF-01 condition «The actor chooses to mark all notifications as read.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-30 | Action [System] “Mark all visible notifications as read” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › AF-01 step 1 «The system marks all visible notifications as read.»<br>`data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › postconditions[1] «Selected notifications may be marked as read.»<br>`data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › postconditions[3] «No project work data is changed.» | EXPLICIT | Matches the step text. Keep |
| UC-30 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-30 | Guard [change email delivery — AF-02] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › AF-02 condition «The actor enables or disables email notification delivery.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-30 | Decision [System] “Enabling email delivery?” | Decision | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` | DERIVED | AF-02.1 verifies the email address only "when email delivery is enabled". Keep |
| UC-30 | Guard [enabling] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-30 | Action [System] “Verify that the actor has a verified email address” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › AF-02 step 1 «The system verifies that the actor has a verified email address when email delivery is enabled.»<br>`data/business_rules.yml` › BR-NOTIFICATION-EMAIL-PREFERENCE «An email notification is sent only to the intended recipient's verified email a…» | EXPLICIT | Matches the step text. Keep |
| UC-30 | Guard [disabling] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` | DERIVED | Guard of the derived decision above. Keep |
| UC-30 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-30 | Action [System] “Save the updated email delivery preference” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › AF-02 step 2 «The system saves the updated email delivery preference.»<br>`data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › postconditions[2] «The email delivery preference may be updated.» | EXPLICIT | Matches the step text. Keep |
| UC-30 | Decision [System] “Preference saved?” | Decision | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › EX-02 «The email delivery preference cannot be saved; the previous preference remains unchanged.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-30 | Guard [saved] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-30 | Guard [cannot be saved — EX-02] | Guard | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › EX-02 «The email delivery preference cannot be saved; the previous preference remains unchanged.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-30 | Action [System] “Keep the previous preference and report the failure” | Action | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` › EX-02 «The email delivery preference cannot be saved; the previous preference remains unchanged.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-02 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-30 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-30 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-30 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-30 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-32.1 — Search and View User Accounts (`UC-USER-ACCOUNTS-SEARCH`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-32.1 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-32.1 | Action [System Administrator] “Open user account administration and enter search criteria” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › normal_flow[1] «Opens user account administration and enters search criteria.»<br>`data/business_rules.yml` › BR-SYSADMIN-USER-ACCOUNT «Only a System Administrator can search, review, suspend, reactivate, or delete …» | EXPLICIT | Matches the step text. Keep |
| UC-32.1 | Decision [System] “Administration data available?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › EX-01 «Account administration data is temporarily unavailable.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.1 | Guard [available] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.1 | Guard [unavailable — EX-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › EX-01 «Account administration data is temporarily unavailable.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.1 | Action [System] “Report that account administration data is temporarily unavailable” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › EX-01 «Account administration data is temporarily unavailable.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-32.1 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.1 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-32.1 | Decision [System] “Matching accounts found?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › AF-01 condition «No account matches the search criteria.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.1 | Guard [found] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.1 | Guard [no match — AF-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › AF-01 condition «No account matches the search criteria.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.1 | Action [System] “Report that no matching account was found” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › AF-01 step 1 «The system reports that no matching account was found.» | EXPLICIT | Matches the step text. Keep |
| UC-32.1 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.1 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-32.1 | Action [System] “Display matching User accounts” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › normal_flow[2] «Displays matching User accounts.» | EXPLICIT | Matches the step text. Keep |
| UC-32.1 | Action [System Administrator] “Select an account” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › normal_flow[3] «Selects an account.» | EXPLICIT | Matches the step text. Keep |
| UC-32.1 | Action [System] “Display its administrative status and relevant account metadata” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › normal_flow[4] «Displays its administrative status and relevant account metadata.»<br>`data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › postconditions[1] «Matching account information is displayed without modification.»<br>`data/business_rules.yml` › BR-SYSADMIN-NO-PROJECT-AUTO-ACCESS «System Administrator status does not automatically grant membership in or acces…»<br>`data/use_cases/system-administration/UC-USER-ACCOUNTS-SEARCH.yml` › other_information «Project content is not exposed through system account administration.» | EXPLICIT | Matches the step text. Keep |
| UC-32.1 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |

#### UC-32.2 — Suspend User Account (`UC-USER-ACCOUNT-SUSPEND`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-32.2 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-32.2 | Action [System Administrator] “Select an active User account and request suspension” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › normal_flow[1] «Selects an active User account and requests suspension.»<br>`data/business_rules.yml` › BR-SYSADMIN-USER-ACCOUNT «Only a System Administrator can search, review, suspend, reactivate, or delete …» | EXPLICIT | Matches the step text. Keep |
| UC-32.2 | Decision [System] “Project Owner of an active project?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › EX-01 «The account is the current Project Owner of an active project.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.2 | Guard [not an owner] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.2 | Guard [current owner — EX-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › EX-01 «The account is the current Project Owner of an active project.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.2 | Action [System] “Reject the suspension of the current Project Owner” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › EX-01 «The account is the current Project Owner of an active project.»<br>`data/business_rules.yml` › BR-OWNER-ACCOUNT-DELETION-GUARD «A System Administrator must not delete or suspend a User account that is the cu…»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-32.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-32.2 | Decision [System] “Last active System Administrator?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › EX-02 «The account is the last active System Administrator.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.2 | Guard [not the last] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.2 | Guard [last administrator — EX-02] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › EX-02 «The account is the last active System Administrator.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.2 | Action [System] “Reject the suspension of the last active System Administrator” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › EX-02 «The account is the last active System Administrator.»<br>`data/business_rules.yml` › BR-LAST-ADMINISTRATOR-PROTECTION «The system must not allow the suspension or deletion of the last active System …»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-02 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-32.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-32.2 | Action [System] “Display the impact and request a reason and confirmation” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › normal_flow[2] «Displays the impact and requests a reason and confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-32.2 | Decision [System Administrator] “Confirm suspension?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › AF-01 condition «The administrator cancels before confirmation.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.2 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.2 | Action [System Administrator] “Provide a reason and confirm suspension” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › normal_flow[3] «Provides a reason and confirms suspension.» | EXPLICIT | Matches the step text. Keep |
| UC-32.2 | Action [System] “Suspend the account and record the audit event” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › normal_flow[4] «Suspends the account and records the audit event.»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › postconditions[1] «The target account is suspended.»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › postconditions[2] «The suspension reason and actor are recorded in the system audit log.»<br>`data/business_rules.yml` › BR-AUDIT-EVENT-COMPLETENESS «Every audit event must record the actor identity, timestamp, action performed, …» | EXPLICIT | Matches the step text. Keep |
| UC-32.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.2 | Guard [cancel — AF-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › AF-01 condition «The administrator cancels before confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.2 | Action [System] “Leave the account active” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-SUSPEND.yml` › AF-01 step 1 «The system leaves the account active.» | EXPLICIT | Matches the step text. Keep |
| UC-32.2 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.2 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-32.3 — Reactivate User Account (`UC-USER-ACCOUNT-REACTIVATE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-32.3 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-32.3 | Action [System Administrator] “Select a suspended User account and request reactivation” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › normal_flow[1] «Selects a suspended User account and requests reactivation.»<br>`data/business_rules.yml` › BR-SYSADMIN-USER-ACCOUNT «Only a System Administrator can search, review, suspend, reactivate, or delete …» | EXPLICIT | Matches the step text. Keep |
| UC-32.3 | Decision [System] “Account deleted?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › EX-01 «The account has been deleted and cannot be reactivated.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.3 | Guard [not deleted] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.3 | Guard [deleted — EX-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › EX-01 «The account has been deleted and cannot be reactivated.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.3 | Action [System] “Reject the reactivation of the deleted account” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › EX-01 «The account has been deleted and cannot be reactivated.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-32.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-32.3 | Action [System] “Display the account status and request confirmation” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › normal_flow[2] «Displays the account status and requests confirmation.» | EXPLICIT | Matches the step text. Keep |
| UC-32.3 | Decision [System Administrator] “Confirm reactivation?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › AF-01 condition «The administrator cancels before confirmation.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.3 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.3 | Action [System Administrator] “Confirm reactivation” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › normal_flow[3] «Confirms reactivation.» | EXPLICIT | Matches the step text. Keep |
| UC-32.3 | Action [System] “Reactivate the account and record the audit event” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › normal_flow[4] «Reactivates the account and records the audit event.»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › postconditions[1] «The target account is active.»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › postconditions[2] «The reactivation is recorded in the system audit log.»<br>`data/business_rules.yml` › BR-AUDIT-EVENT-COMPLETENESS «Every audit event must record the actor identity, timestamp, action performed, …»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › other_information «Reactivation does not automatically restore removed project memberships.» | EXPLICIT | Matches the step text. Keep |
| UC-32.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.3 | Guard [cancel — AF-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › AF-01 condition «The administrator cancels before confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.3 | Action [System] “Leave the account suspended” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-REACTIVATE.yml` › AF-01 step 1 «The system leaves the account suspended.» | EXPLICIT | Matches the step text. Keep |
| UC-32.3 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.3 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-32.4 — Delete User Account (`UC-USER-ACCOUNT-DELETE`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-32.4 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-32.4 | Action [System Administrator] “Select a User account and request deletion” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › normal_flow[1] «Selects a User account and requests deletion.»<br>`data/business_rules.yml` › BR-SYSADMIN-USER-ACCOUNT «Only a System Administrator can search, review, suspend, reactivate, or delete …» | EXPLICIT | Matches the step text. Keep |
| UC-32.4 | Decision [System] “Project Owner of an active project?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › EX-01 «The account is the current Project Owner of an active project.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.4 | Guard [not an owner] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.4 | Guard [current owner — EX-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › EX-01 «The account is the current Project Owner of an active project.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.4 | Action [System] “Reject the deletion of the current Project Owner” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › EX-01 «The account is the current Project Owner of an active project.»<br>`data/business_rules.yml` › BR-OWNER-ACCOUNT-DELETION-GUARD «A System Administrator must not delete or suspend a User account that is the cu…»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-32.4 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.4 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-32.4 | Decision [System] “Last active System Administrator?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › EX-02 «The account is the last active System Administrator.» | NECESSARY REPRESENTATION | Branch point for EX-02; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.4 | Guard [not the last] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.4 | Guard [last administrator — EX-02] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › EX-02 «The account is the last active System Administrator.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.4 | Action [System] “Reject the deletion of the last active System Administrator” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › EX-02 «The account is the last active System Administrator.»<br>`data/business_rules.yml` › BR-LAST-ADMINISTRATOR-PROTECTION «The system must not allow the suspension or deletion of the last active System …»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-02 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-32.4 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.4 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-32.4 | Action [System] “Display ownership, membership and administrative impact” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › normal_flow[2] «Displays ownership, membership, and administrative impact.» | EXPLICIT | Matches the step text. Keep |
| UC-32.4 | Decision [System Administrator] “Confirm deletion?” | Decision | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › AF-01 condition «The administrator cancels before confirmation.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-32.4 | Guard [confirm] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-32.4 | Action [System Administrator] “Provide a reason and confirm deletion” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › normal_flow[3] «Provides a reason and confirms deletion.» | EXPLICIT | Matches the step text. Keep |
| UC-32.4 | Action [System] “Delete the account and record the audit event” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › normal_flow[4] «Deletes the account and records the audit event.»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › postconditions[1] «The User account can no longer authenticate.»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › postconditions[2] «Required audit and historical attribution data are preserved.»<br>`data/business_rules.yml` › BR-AUDIT-EVENT-COMPLETENESS «Every audit event must record the actor identity, timestamp, action performed, …»<br>`data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › other_information «Deletion preserves immutable audit records and historical work attribution.» | EXPLICIT | Matches the step text. Keep |
| UC-32.4 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.4 | Guard [cancel — AF-01] | Guard | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › AF-01 condition «The administrator cancels before confirmation.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-32.4 | Action [System] “Leave the account unchanged” | Action | `data/use_cases/system-administration/UC-USER-ACCOUNT-DELETE.yml` › AF-01 step 1 «The system leaves the account unchanged.» | EXPLICIT | Matches the step text. Keep |
| UC-32.4 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-32.4 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |

#### UC-33 — Review System Audit Log (`UC-SYSTEM-AUDIT-LOG-REVIEW`)

| UC | Diagram element | Loại phần tử | Nguồn chính xác | Mức độ hỗ trợ | Kết luận |
|---|---|---|---|---|---|
| UC-33 | Initial node | Initial node | UML InitialNode (one per diagram, guideline §5) | NECESSARY REPRESENTATION | Keep |
| UC-33 | Action [System Administrator] “Open the system audit log” | Action | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › normal_flow[1] «Opens the system audit log.»<br>`data/business_rules.yml` › BR-AUDIT-VIEW-SYSADMIN-ONLY «Only an authenticated System Administrator may search or review the system audi…» | EXPLICIT | Matches the step text. Keep |
| UC-33 | Decision [System] “Audit store available?” | Decision | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › EX-01 «The audit store is temporarily unavailable.» | NECESSARY REPRESENTATION | Branch point for EX-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-33 | Guard [available] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-33 | Guard [unavailable — EX-01] | Guard | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › EX-01 «The audit store is temporarily unavailable.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-33 | Action [System] “Report that the audit store is temporarily unavailable” | Action | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › EX-01 «The audit store is temporarily unavailable.»<br>`docs/activity-diagram-guideline.md` §7.3 (exception outcome must be visible) | DERIVED | EX-01 names the condition but not the outcome; the action only states that the operation is not completed. Keep |
| UC-33 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-33 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-33 | Action [System] “Display recent audit events” | Action | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › normal_flow[2] «Displays recent audit events.»<br>`data/business_rules.yml` › BR-SYSADMIN-NO-PROJECT-AUTO-ACCESS «System Administrator status does not automatically grant membership in or acces…» | EXPLICIT | Matches the step text. Keep |
| UC-33 | Action [System Administrator] “Filter events by time, actor, event type or target” | Action | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › normal_flow[3] «Filters events by time, actor, event type, or target.» | EXPLICIT | Matches the step text. Keep |
| UC-33 | Decision [System] “Matching events found?” | Decision | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › AF-01 condition «No event matches the selected filters.» | NECESSARY REPRESENTATION | Branch point for AF-01; its position in the flow is not stated in the YAML and follows the step that produces the checked data. Keep |
| UC-33 | Guard [found] | Guard | Complement of the other guard(s) on the same decision | NECESSARY REPRESENTATION | Keep |
| UC-33 | Guard [no match — AF-01] | Guard | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › AF-01 condition «No event matches the selected filters.» | EXPLICIT | Condition stated in the YAML. Keep |
| UC-33 | Action [System] “Report that no matching events were found” | Action | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › AF-01 step 1 «The system reports that no matching events were found.» | EXPLICIT | Matches the step text. Keep |
| UC-33 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
| UC-33 | Merge node | Merge | Rejoins mutually exclusive branches | NECESSARY REPRESENTATION | Keep |
| UC-33 | Action [System] “Display matching events and their recorded details” | Action | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › normal_flow[4] «Displays matching events and their recorded details.»<br>`data/business_rules.yml` › BR-AUDIT-IMMUTABLE «System audit records cannot be manually edited or deleted.»<br>`data/business_rules.yml` › BR-AUDIT-EVENT-COMPLETENESS «Every audit event must record the actor identity, timestamp, action performed, …» | EXPLICIT | Matches the step text. Keep |
| UC-33 | Action [System Administrator] “Review the results” | Action | `data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › normal_flow[5] «Reviews the results.»<br>`data/use_cases/system-administration/UC-SYSTEM-AUDIT-LOG-REVIEW.yml` › postconditions[1] «Matching audit events have been displayed without modification.» | EXPLICIT | Matches the step text. Keep |
| UC-33 | Activity Final | End node | See end-node table | NECESSARY REPRESENTATION | See end-node table |
