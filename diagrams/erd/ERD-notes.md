# SWD392 Conceptual ERD – notes accompanying the diagram

These notes go with `SWD392-ERD-Chen.drawio` / `.svg` / `.png`. The legend on the diagram is deliberately short. This file holds the longer explanations and the business constraints that were previously printed on the diagram. Nothing was removed; full sources (UC/BR) per entity and relationship are in `ERD-catalogue-and-validation.md`.

## 1. Legend explained

| Symbol | Meaning |
|---|---|
| Rectangle | Entity. |
| Rectangle with an inscribed diamond | Associative entity: a relationship promoted to an entity because it has its own attributes and history and takes part in other relationships (Project Membership, Sprint Backlog Item). |
| Rectangle with a thick border | Supertype (Work Item). |
| Diamond | Relationship. The name is a stable structural verb phrase, never a use-case action. |
| Circle marked "d" | Disjoint specialization: a Work Item is exactly one of its subtypes. |
| Double line (Work Item to "d") | Total participation: every Work Item belongs to some subtype. |
| Single lines (PBI, Task, Subtask to "d") | The three subtypes. They are not relationships and carry no (min,max). |
| Line jump (small arc) | Two connectors cross without connecting. There is one, where WRITES crosses TRIGGERS. |

## 2. How to read (min,max)

(min,max) is written next to the entity it describes. It is the number of times one instance of that entity takes part in the relationship (N = many).

Example: User Account (0,1) — LINKED TO — (1,1) External Identity.

- An account has zero or one linked identity.
- Each identity belongs to exactly one account.

On a recursive relationship each line carries a role before its (min,max):

- **DERIVED FROM:** "derived item (0,1)" and "source item (0,N)".
- **DEPENDS ON:** "dependent task (0,N)" and "prerequisite task (0,N)".

## 3. Identifiers and attributes (not drawn on the single-page diagram)

Identifiers are listed first. Subtypes inherit work item ID, title and created at from Work Item.

| Entity | Kind | Identifier | Attributes |
|---|---|---|---|
| User Account | entity | account ID | email (unique), display name, account status, system role, email verified at, email notifications enabled |
| External Identity | entity | provider + provider subject | email at link, linked at |
| Project | entity | project ID | name, description, planned start date, planned end date, project status, current Product Goal |
| Project Membership | associative entity | project ID + account ID | access role, Scrum accountability, membership status, joined at, ended at |
| Work Item | supertype | work item ID | title, created at |
| Product Backlog Item | subtype of Work Item | work item ID (inherited) | description, acceptance criteria, item type, item status, needs refinement, estimate (story points), backlog position |
| Sprint | entity | sprint ID | Sprint Goal, start date, end date, sprint status, started at, closed at, cancellation reason |
| Sprint Backlog Item | associative entity | sprint ID + work item ID | work status, selection outcome, selected at, closed at |
| Task | subtype of Work Item | work item ID (inherited) | description, priority, due date, estimate, work status, deleted at |
| Subtask | subtype of Work Item | work item ID (inherited) | details, work status, deleted at |
| Comment | entity | comment ID | body, created at |
| Activity Event | entity | event ID | event type, subject type, summary, details, occurred at |
| Notification | entity | notification ID | notification type, message, created at, read at |
| Email Delivery | entity | delivery ID | purpose, recipient email address, delivery status, requested at, result at, failure reason |
| System Audit Event | entity | audit event ID | action, target type, target ID, reason, occurred at |

## 4. Exclusivity rules shown only in words

- **Comment DISCUSSES exactly one Work Item (1,1).** Because the specialization is disjoint, that is exactly one Product Backlog Item, Task or Subtask.
- **Activity Event CONCERNS at most one Work Item (0,1).** Project-level events (Product Goal, membership, Sprint) concern none and are identified by "subject type". Every event still belongs to one Project (RECORDS, (1,1)).
- **Email Delivery** takes part in exactly one of SENT AS (a notification email) or ADDRESSED TO (an account verification or password-reset email), never both and never neither. Chen cardinality cannot express an exclusive OR, so both ends are drawn (0,1).

## 5. Business constraints not expressed by cardinality

### Account and membership

- **BR-02:** exactly one ACTIVE Project Owner membership per active project.
- **BR-03:** an owner membership cannot end before ownership is transferred.
- **BR-08:** at most one ACTIVE Product Owner per project.
- **BR-07, BR-40:** one membership per (account, project). Registration grants no project membership.
- **BR-39:** email is unique per account.
- **UC-02 EX-04:** an External Identity is never linked by matching email.

### Product Backlog and Sprint

- **BR-13, BR-18:** at most one ACTIVE and at most one DRAFT Sprint per project.
- **BR-15:** a Sprint ends after it starts and lasts at most one month.
- **BR-12:** only ready items can be selected.
- **BR-12, BR-17:** an item has at most one open selection, and returned selections are kept.
- **UC-17 AF-01:** DERIVED FROM links different items of the same project.
- **Product Backlog:** a derived view, i.e. the project's items with status Draft or Open, ordered by backlog position.

### Task, Subtask and dependency

- **BR-19:** Tasks are created only for Sprint Backlog Items of the active Sprint.
- **BR-20:** the assignee membership is ACTIVE, has Developer accountability and belongs to the same project as the Task or Subtask.
- **BR-23:** no self-dependency.
- **BR-22:** no direct or indirect dependency cycle.
- **BR-24:** a dependent Task and its prerequisite Task are in the same project.
- **BR-25:** single-level breakdown; a Subtask never has Subtasks. This is structural, because DIVIDED INTO has Task on the parent side.

### Comments and activity

- **BR-26:** the comment author is an active member of the item's project when writing.
- **BR-27:** Activity Events are insert-only, and the actor stays attributed after leaving the project.
- **Activity scope:** the Work Item an Activity Event concerns belongs to the event's project.

### Notifications, email delivery and audit

- **TRIGGERS:** every Iteration 1 notification comes from a recorded Activity Event.
- **BR-28:** a User reads only their own Notifications.
- **BR-29:** notification email is sent only to verified, opted-in recipients.
- **BR-30:** email failure never removes the in-app Notification.
- **Email per notification:** at most one Email Delivery per Notification; there is no retry use case.
- **BR-34, BR-37:** System Audit Events are insert-only. They record actor, time, action, target type and target ID, so they survive deletion of the target.

## 6. Derived views and externally managed data (not entities)

- **Derived views:** Product Backlog, Sprint Backlog, Sprint Board, Sprint Progress, dashboards, parent-task progress and readiness are derived or computed when read.
- **Product Goal:** an attribute of Project; its history is kept through Activity Events.
- **Board statuses:** a fixed value domain.
- **External data:** passwords, password-reset tokens, email verification tokens and sessions belong to the managed authentication provider.
