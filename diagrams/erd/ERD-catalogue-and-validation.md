# SWD392 Scrum PMS – Conceptual ERD (Chen): catalogue and validation

Iteration 1, Group 05. Date: 2026-10-08. Status: proposed for team review. Nothing in this folder is committed.

## 1. Deliverables

| File | Content |
|---|---|
| `SWD392-ERD-Chen.drawio` | Native, editable draw.io file, one page. Every entity, diamond, label and connector is its own shape. |
| `SWD392-ERD-Chen.svg` / `.png` | Export of that page. The PNG is 2×; use the SVG in Word. |
| `ERD-notes.md` | Reading guide, legend explanation, identifiers and attributes, and the business constraints that used to be printed on the diagram. |
| `ERD-catalogue-and-validation.md` | This file. |

The diagram shows all 15 entities and all 23 relationships, and each entity appears exactly once. Attribute ovals are not drawn (team decision for the single-page format). Identifiers and attributes are listed in §3 and in `ERD-notes.md`, and they are unchanged.

Layout by domain:

- **Left:** account and membership.
- **Centre:** Project, Product Backlog and Sprint.
- **Right:** Task, Subtask and dependency, with the Work Item specialization.
- **Bottom:** activity, comments, notifications, email delivery and audit.

Earlier versions are kept unchanged in `drafts-2026-10-08/` (first draft) and `drafts-2026-10-08/v2-multipage/` (blue six-page version).

## 2. Notation and how to read (min,max)

- **Entity:** rectangle.
- **Relationship:** diamond.
- **Attribute:** not drawn on the single-page diagram; see §3 (identifiers listed first).
- **Associative entity:** rectangle with an inscribed diamond.
- **Supertype:** rectangle with a thick border.
- **Disjoint specialization:** circle marked **d**. A double line from the supertype to the circle means total participation.

No Crow's Foot symbols are used.

**(min,max) is participation, written next to the entity it describes.** It answers: how many instances of this relationship does one instance of this entity take part in? N means "many".

Example: User Account (0,1) — LINKED TO — (1,1) External Identity.

- One User Account is linked to 0 or 1 External Identity.
- One External Identity belongs to exactly 1 User Account.

This is the opposite of the "look-across" 1/M/N convention used in the old drafts. Do not mix the two conventions in the report.

On a recursive relationship, each line carries a role name before its (min,max). For example, Task "dependent task (0,N)" and "prerequisite task (0,N)".

## 3. Entity catalogue

| # | Entity | Kind | Identifier | Attributes | Main sources |
|---|---|---|---|---|---|
| 1 | User Account | entity | <u>account ID</u> | email (unique), display name, account status, system role, email verified at, email notifications enabled | UC-01, UC-02, UC-05.1, UC-05.2, UC-30 AF-02, UC-32.1–32.4; BR-32, BR-36, BR-39, BR-41, BR-42 |
| 2 | External Identity | entity | <u>provider + provider subject</u> | email at link, linked at | UC-02 AF-01, AF-03, EX-04, EX-06; BR-39, BR-41 |
| 3 | Project | entity | <u>project ID</u> | name, description, planned start date, planned end date, project status, current Product Goal | UC-06, UC-07, UC-08, UC-11, UC-14.1–14.3; BR-05, BR-09 |
| 4 | Project Membership | associative | <u>project ID + account ID</u> | access role, Scrum accountability, membership status, joined at, ended at | UC-06, UC-09.1–09.3, UC-10, UC-12, UC-13; BR-02–04, BR-06–08 |
| 5 | Work Item | supertype | <u>work item ID</u> | title, created at | UC-26, UC-28, UC-29 |
| 6 | Product Backlog Item | subtype of Work Item | work item ID (inherited) | description, acceptance criteria, item type, item status, needs refinement, estimate (story points), backlog position | UC-15.1–15.4, UC-16, UC-17, UC-18; BR-10–12 |
| 7 | Sprint | entity | <u>sprint ID</u> | Sprint Goal, start date, end date, sprint status, started at, closed at, cancellation reason | UC-19–UC-22; BR-13–BR-18 |
| 8 | Sprint Backlog Item | associative | <u>sprint ID + work item ID</u> | work status, selection outcome, selected at, closed at | UC-19–UC-23, UC-26; BR-12, BR-17, BR-21 |
| 9 | Task | subtype of Work Item | work item ID (inherited) | description, priority, due date, estimate, work status, deleted at | UC-24.1–24.5, UC-25, UC-26, UC-31; BR-19–21 |
| 10 | Subtask | subtype of Work Item | work item ID (inherited) | details, work status, deleted at | UC-27.1–27.5, UC-26; BR-21, BR-25 |
| 11 | Comment | entity | <u>comment ID</u> | body, created at | UC-28; BR-26 |
| 12 | Activity Event | entity | <u>event ID</u> | event type, subject type, summary, details, occurred at | UC-29 and every "recorded in activity history" postcondition; BR-27 |
| 13 | Notification | entity | <u>notification ID</u> | notification type, message, created at, read at | UC-28 NF5, UC-30; BR-28–30 |
| 14 | Email Delivery | entity | <u>delivery ID</u> | purpose, recipient email address, delivery status, requested at, result at, failure reason | UC-01 NF6–7, EX-01, EX-03; UC-04 NF4, EX-01; UC-28 NF5–6, EX-02; BR-29, BR-30 |
| 15 | System Audit Event | entity | <u>audit event ID</u> | action, target type, target ID, reason, occurred at | UC-05.3, UC-12, UC-32.2–32.4, UC-33; BR-34, BR-37, BR-38 |

Notes on attributes:

- **Status values.** "work status" on Sprint Backlog Item, Task and Subtask uses the fixed board status set, as the team decided. It is a value domain, not an entity.
- **Deleted at.** Task and Subtask carry "deleted at" because deletion is a soft delete, so history and comments survive.
- **Recipient email address.** Email Delivery stores the address it was sent to. A later change to the account email therefore does not rewrite delivery history.

## 4. Relationship catalogue

A = left entity and B = right entity. Each (min,max) is written next to its own entity.

| ID | A (min,max) | Relationship | (min,max) B | Reading and rule beyond cardinality | Sources |
|---|---|---|---|---|---|
| R01 | User Account (0,1) | LINKED TO | (1,1) External Identity | An identity is found by provider subject, never by matching email. | UC-02 AF-01, AF-03, EX-04; BR-39, BR-41 |
| R02 | User Account (0,N) | HOLDS | (1,1) Project Membership | One membership per account per project. | BR-07, BR-40; UC-09.2 NF4, AF-01 |
| R03 | Project (1,N) | GRANTS | (1,1) Project Membership | Exactly one ACTIVE Project Owner per active project. At most one ACTIVE Product Owner. | BR-02, BR-03, BR-06, BR-08; UC-06, UC-12 |
| R04 | Project (0,N) | CONTAINS | (1,1) Product Backlog Item | The Product Backlog is this ordered set. It is not an entity. | UC-06, UC-15.2, UC-16; BR-10 |
| R05 | PBI "derived item" (0,1) | DERIVED FROM | (0,N) PBI "source item" | No self-derivation. Both items are in the same project. | UC-17 AF-01 |
| R06 | Project (0,N) | SCHEDULES | (1,1) Sprint | At most one ACTIVE and one DRAFT Sprint per project. | UC-19, UC-20; BR-13, BR-18 |
| R07 | Sprint (0,N) | INCLUDES | (1,1) Sprint Backlog Item | At least one selection before start (application rule). | UC-19–UC-21 |
| R08 | Product Backlog Item (0,N) | SELECTED AS | (1,1) Sprint Backlog Item | At most one open selection per item. Earlier selections are kept. | BR-12, BR-17; UC-21, UC-22, UC-23 AF-01 |
| R09 | Sprint Backlog Item (0,N) | BROKEN INTO | (1,1) Task | Tasks are created only for items in the active Sprint. | UC-24.2; BR-19 |
| R10 | Task (0,N) | DIVIDED INTO | (1,1) Subtask | Single level: a Subtask has no Subtasks. | UC-27.1, UC-27.2; BR-25 |
| R11 | Task "dependent task" (0,N) | DEPENDS ON | (0,N) Task "prerequisite task" | No self-dependency, no cycle, same project. | UC-24.5 AF-01, UC-24.6, UC-24.7; BR-22–24 |
| R12 | Project Membership (0,N) | ASSIGNED TO | (0,1) Task | The membership is ACTIVE, has Developer accountability and belongs to the Task's project. | UC-24.4, UC-25, UC-13 AF-01; BR-20 |
| R13 | Project Membership (0,N) | ASSIGNED TO | (0,1) Subtask | Same eligibility and same-project rule as R12. | UC-27.2 NF2, UC-27.3; BR-20 |
| R14 | User Account (0,N) | WRITES | (1,1) Comment | The author is an active member of the item's project when writing. | UC-28; BR-26 |
| R15 | Comment (1,1) | DISCUSSES | (0,N) Work Item | Exactly one Work Item, i.e. one PBI, Task or Subtask (see §5). | UC-28 |
| R16 | Project (0,N) | RECORDS | (1,1) Activity Event | Every event, at project level or about a work item, belongs to one project. | UC-08, UC-09.2, UC-09.3, UC-10, UC-14.2, UC-14.3, UC-20; BR-27 |
| R17 | User Account (0,N) | PERFORMS | (1,1) Activity Event | Insert-only. The actor stays attributed after leaving the project. | UC-29 NF3, UC-13; BR-27 |
| R18 | Activity Event (0,1) | CONCERNS | (0,N) Work Item | None for project-level events (goal, membership, Sprint). | UC-29; UC-15.2, UC-24.2, UC-26 postconditions |
| R19 | Activity Event (0,N) | TRIGGERS | (1,1) Notification | Every Iteration 1 notification comes from a recorded project event. | UC-28 NF4–5; UC-30 assumption |
| R20 | User Account (0,N) | RECEIVES | (1,1) Notification | Users see only their own notifications. | BR-28; UC-28 NF5, UC-30 |
| R21 | Notification (0,1) | SENT AS | (0,1) Email Delivery | Exclusive with R22 (see §5). | UC-28 NF5–6, EX-02; BR-29, BR-30 |
| R22 | User Account (0,N) | ADDRESSED TO | (0,1) Email Delivery | Used for verification and password-reset emails. Exclusive with R21. | UC-01 NF6–7, EX-01, EX-03; UC-04 NF4, EX-01 |
| R23 | User Account (0,N) | INITIATES | (1,1) System Audit Event | Insert-only. The target is stored by type and ID, so the record survives deletion of the target. | BR-34, BR-37; UC-12, UC-32.2–32.4, UC-33 |

All relationship names are stable structural verb phrases. None of them names a use-case action such as "creates", "updates" or "removes".

## 5. Specialization and exclusivity rules

### Work Item specialization

Work Item → {Product Backlog Item, Task, Subtask} is **disjoint (d) and total** (double line). Every Work Item is exactly one of the three, and each subtype inherits the work item ID, title and created at.

This gives Comment (R15) and Activity Event (R18) a single target, Work Item. The diagram therefore states the exclusivity rule directly, instead of using three separate DISCUSSED IN / DESCRIBES diamonds, which cardinality alone could not keep mutually exclusive:

- Comment DISCUSSES exactly one Work Item (1,1), so it targets exactly one of PBI, Task or Subtask.
- Activity Event CONCERNS at most one Work Item (0,1). Project-level events concern none and are identified by "subject type".

### Email Delivery exclusivity

Each Email Delivery takes part in exactly one of SENT AS (R21, a notification email) or ADDRESSED TO (R22, a verification or reset email). It never takes part in both or neither.

Both ends are drawn (0,1) because Chen cardinality cannot express an exclusive OR. The rule is stated in the legend, in view D2 and here.

## 6. Associative entities

**Project Membership** resolves the many-to-many relationship between User Account and Project. It is an entity rather than a plain diamond because:

- it has its own attributes (access role, Scrum accountability, membership status, joined at, ended at);
- it takes part in other relationships, since Task and Subtask assignment reference the membership (R12, R13);
- ended memberships are kept for history.

**Sprint Backlog Item** resolves the many-to-many relationship between Sprint and Product Backlog Item. It is an entity because:

- it has a work status and a selection outcome;
- Tasks hang off it (R09);
- every selection is kept, as the team decided. A returned item can be selected again in a later Sprint, and the earlier selection stays as history.

**DEPENDS ON** stays a plain recursive diamond. It has no attributes, takes part in no other relationship and needs no history in Iteration 1.

## 7. Derived views, value domains and externally managed data

| Concept | Modelled as | Reason |
|---|---|---|
| Product Backlog | Derived view: a Project's PBIs with item status Draft or Open, ordered by backlog position | It has no identity or attributes of its own (R04). |
| Sprint Backlog | Derived view: a Sprint's Sprint Backlog Items | Covered by R07. |
| Sprint Board | Derived view: work items of the active Sprint grouped by work status | The board columns are the fixed status set the team chose. |
| Sprint Progress, dashboard, parent-task progress, readiness | Derived and computed when read | Values come from statuses and counts. Storing them would duplicate data. |
| Product Goal | Attribute of Project ("current Product Goal") | One current goal per project. Its history is kept through Activity Events (UC-14). |
| Board status set | Fixed value domain | Team decision. |
| Password, password hash, password-reset token, email verification token, session or refresh token | External, owned by the managed authentication provider | UC-01, UC-02 and UC-04 assume a managed provider. Email Delivery records only that a verification or reset email was requested and whether it was delivered. |
| Google account | External Identity entity (local link record only) | Lookup is by provider subject (UC-02 EX-04). |

## 8. Answers to the review questions

1. **Is the identity link 1:1?**
   - Yes, read as User Account (0,1) and External Identity (1,1).
   - Only Google is in scope, and no use case links a second provider. If a second provider is added later, only the User Account side changes, to (0,N).
2. **Is "SIGNS IN WITH" a stable name?**
   - No. Signing in is a transient use-case action, so it was renamed **LINKED TO**.
3. **Is "SPLIT INTO" supported?**
   - The only support is UC-17 AF-01, which creates new items traceable to the original.
   - It is modelled as **DERIVED FROM** with roles "derived item" (0,1) and "source item" (0,N).
   - The old name SPLIT INTO named the action, and its old 1/N labels did not say that most items have no source.
4. **Does Sprint Backlog Item link Sprint and PBI, and is history kept?**
   - Yes. It is associative, linked by R07 and R08 with (1,1) on its side, and every selection is kept (team decision).
   - "At most one open selection per item" is a constraint outside cardinality.
5. **Should assignment reference User Account or Membership?**
   - **Project Membership.** Eligibility depends on that membership's status and accountability in the Task's project (BR-20).
   - The same-project condition still needs a rule (§9).
6. **Is project-level activity covered?**
   - Yes. RECORDS (1,1) ties every Activity Event to its Project, and CONCERNS (0,1) is empty for goal, membership and Sprint events.
7. **Can a Notification exist without an Activity Event?**
   - Not in Iteration 1. No deadline or system-generated notification exists, so TRIGGERS is (1,1) on the Notification side.
   - This is a design choice and is listed in §10.
8. **Should Email Delivery be an entity?**
   - Yes, covering all system emails (team decision).
   - It records purpose, recipient address, status and failure. This supports BR-30 and the email exception flows without changing Notification.
9. **Should audit be separate from activity?**
   - Yes. The scope, readers and retention differ:
     - **Activity Event:** project-scoped, visible to project members.
     - **System Audit Event:** system-wide, for the System Administrator, and survives deletion of its target.

## 9. Invariants that cardinality cannot express

These are enforced by business rules or application logic, and each one is also stated in the notes of its view.

| # | Rule | Source |
|---|---|---|
| I-1 | One membership per (account, project). This is enforced by the composite identifier. | BR-07, BR-40 |
| I-2 | Exactly one ACTIVE Project Owner per active project. The owner cannot leave before transferring ownership. | BR-02, BR-03 |
| I-3 | At most one ACTIVE Product Owner per project. | BR-08 |
| I-4 | At most one ACTIVE and at most one DRAFT Sprint per project. End date is after start date, and the Sprint lasts at most one month. | BR-13, BR-15, BR-18 |
| I-5 | Only ready items can be selected. Each item has at most one open selection, and earlier selections are kept. | BR-12, BR-17 |
| I-6 | Tasks are created only for Sprint Backlog Items of the active Sprint. | BR-19 |
| I-7 | Assignee membership is ACTIVE, has Developer accountability and belongs to the same project as the Task or Subtask. | BR-20 |
| I-8 | DEPENDS ON: no self-dependency, no direct or indirect cycle, both Tasks in the same project. | BR-22, BR-23, BR-24 |
| I-9 | Single-level breakdown: a Subtask has no Subtasks. This is structural, because DIVIDED INTO has a Task on the parent side. | BR-25 |
| I-10 | DERIVED FROM: different items in the same project. | UC-17 AF-01 |
| I-11 | The comment author is an active member of the item's project when writing. | BR-26 |
| I-12 | Activity Events and System Audit Events are insert-only. | BR-27, BR-34, BR-37 |
| I-13 | The Work Item that an Activity Event concerns belongs to the event's project. | design consistency |
| I-14 | Each Email Delivery is in exactly one of R21 or R22. At most one email per Notification. | BR-29, BR-30; design |
| I-15 | Notification email only to verified, opted-in recipients. Email failure never removes the in-app Notification. | BR-29, BR-30 |
| I-16 | Users read only their own Notifications. | BR-28 |
| I-17 | Email is unique per account. An External Identity is never linked by matching email. Registration grants no membership. | BR-39, BR-40; UC-02 EX-04 |

## 10. Open decisions and source conflicts

None of these blocks the ERD, because the cardinalities above do not change whichever way each is decided. The team should still confirm them.

| # | Item | What I did | Decision needed |
|---|---|---|---|
| C-1 | Word UC-01 still has AF-01 "register with Google" and EX-04. The repository YAML does not. | Followed the repository: Google is a sign-in identity linked by subject (UC-02). | Update Word UC-01 to match the repository. |
| C-2 | Word UC-02 still has the old AF-01 and EX-04 ("directed to Register Account"). | Followed the repository UC-02 (EX-04: no linking by email). | Update Word UC-02. |
| C-3 | Word II.1 and FE-02 list "Scrum Master" as a role. | Modelled Scrum accountability as a membership attribute, not an actor or entity. Its value set comes from the business rules. | Confirm the accountability values and update II.1 / FE-02. |
| C-4 | Word NFR row 4 says "planned". | No ERD impact. | Wording only. |
| C-5 | Word NFR row 7 lists notification triggers that go beyond the use cases. | Only triggers backed by use cases are assumed. TRIGGERS is (1,1) on the Notification side. | If deadline or system notifications are added, change it to (0,1). |
| C-6 | Word NFR row 9 describes an audit scope that does not match the use-case list. | System Audit Event covers the actions in UC-05.3, UC-12, UC-32.x and UC-33. | Align the NFR wording. |
| C-7 | FE-08 (Word and YAML) says "backlog items and tasks", while UC-28 also covers Subtask. | Resolved by the team: comments apply to PBI, Task and Subtask. | Update the FE-08 wording. |
| D-1 | One email per Notification. | Notification (0,1) on SENT AS. | Change to (0,N) only if email retries become a use case. |
| D-2 | Activity subject for project-level events. | Stored as the "subject type" attribute, with no extra relationships to Sprint or Membership. | Add explicit relationships later if reports need them. |
| D-3 | One External Identity per account. | (0,1). | Change to (0,N) if a second provider is added. |

## 11. Validation report

### Sources read (md5 at review time)

- **Word specification:** `Iter1_Group05_BinhNA_TrungNT_KhanhNQ_LuanTC.docx` (973f086a16885202a1004648d04ed8e1).
- **Repository data:** `data/business_rules.yml` (1c424eaf…), `data/major_features.yml` (d003f18b…), `data/actors.yml` (25e9054b…) and all 62 YAML files under `data/use_cases/`.
- **Draft images:** ERD-00 (ea608abe…), ERD-01 (3182b0a4…), ERD-02a (f0379c87…), ERD-02b (cd229533…), ERD-03a (9f6b3eca…) and ERD-03b (e37ff788…). These were used as drafts only.

No use-case specification, business rule or other source file was modified.

### Audit of the old drafts

The following problems were found and are fixed in this version:

- **Cardinality notation.** Only maxima were shown, using the look-across 1/M/N convention, and minima were left to a separate table. All lines now carry (min,max).
- **Membership.** MEMBER OF was an M:N relationship carrying attributes (overview, view 01). A relationship cannot take part in ASSIGNED TO, so it is now the associative entity Project Membership, the same on every page.
- **SIGNS IN WITH** (transient action, orange review mark) is now **LINKED TO**, with User Identity renamed External Identity.
- **SPLIT INTO** "original/split item" with 1/N is now **DERIVED FROM** with roles and (0,1)/(0,N).
- **Assignment.** Task and Subtask assignment pointed to User Account. They now point to Project Membership, as BR-20 eligibility depends on it.
- **Comment and Activity targets.** These were three DESCRIBES and three DISCUSSED IN diamonds with no stated exclusivity, and one of them was still under team review. They are now a single Work Item target with a disjoint total specialization.
- **Notification "email delivery status".** This was an attribute and covered only notification emails. It is now the **Email Delivery** entity covering all system emails, with an exclusivity rule.
- **TRIGGERS** was marked for review and is now settled as (0,N)/(1,1), with the decision recorded (D-1, C-5).
- **Relationship names.** PLANS/SELECTS are renamed SCHEDULES/INCLUDES so they read correctly from the Project and Sprint sides.

### Rendering

- **Format.** One page, black on white, Times New Roman throughout (draw.io font sizes):
  - entity names 22 (bold);
  - relationship names 18;
  - (min,max) and role labels 16 (bold);
  - legend 16.
- **Re-opening and export.** The .drawio file was re-opened with the draw.io 31.4.5 engine (headless Chromium) and exported to SVG. The SVG uses plain `<text>`, with no `foreignObject` and no embedded image. The PNG was rendered from that SVG at 2×.

### Automated checks on the final file

**Native content check** (parsed from the .drawio XML):

- It has 1 page and 0 image cells.
- It has 15 entities and 23 relationship diamonds, with names identical to the model.
- Each diamond connects exactly to its two model entities. A recursive diamond has two arms to the same entity.
- Each arm carries the model's (min,max), with roles on DERIVED FROM and DEPENDS ON. Each label is attached to the arm of the entity it describes. 0 mismatches.
- The specialization consists of the circle "d", a double (link) line from Work Item and three plain lines from PBI, Task and Subtask. It is not drawn as a relationship.

**Layout check** (on the rendered geometry):

- All connectors are orthogonal.
- No connector passes through a shape or a label.
- No label overlaps a shape, a connector or another label, and no label sits nearer a diamond than its entity.
- No shapes overlap, and no text is clipped.

The only reported item is one deliberate crossing: WRITES (User Account → Comment) crosses TRIGGERS (Activity Event → Notification). It is drawn with a line jump. Given the requested domain layout, one crossing is needed here; avoiding it would mean a connector wrapping around the whole bottom area.

### Visual inspection

The exported PNG was inspected section by section after the final build.

Labels on arms that leave the same side of an entity are placed on the outer side of their own line, so they cannot be read as belonging to the neighbouring arm. This applies to:

- User Account: LINKED TO and INITIATES on the left; PERFORMS and WRITES on the right; ADDRESSED TO and RECEIVES at the bottom;
- Task: dependent and prerequisite task;
- Product Backlog Item: derived and source item.

### Readability

- **Canvas:** about 3280 × 1970 px.
- **Fonts:** sizes were not reduced to fit a page.
- **Print:** at A3 landscape (≈ 39 cm usable width) the smallest label prints at about 5.5 pt; at A1 it prints at about 11 pt.
- **Recommended use:**
  - In the report, insert the SVG at full page width so it stays sharp when zoomed.
  - Print it as a poster (A2/A1) when a printed copy must be read without zooming.

### Assumptions

- (min,max) is read as participation, as explained in §2.
- Identifiers are conceptual; surrogate versus natural keys are left to the logical design.
- Passwords, tokens and sessions belong to the managed authentication provider (§7).
