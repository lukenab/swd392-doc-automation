# Báo cáo rà soát nhãn và ngữ nghĩa Activity Diagram — 45 Use Case (trừ UC-06 → UC-13)

Ngày: 2026-10-05 · Nhánh: `docs/activity-diagram-labels` (tách từ `docs/activity-binh-review` @ `7c08559`) · Nguồn sự thật theo thứ tự: UC YAML → Business Rules → actors/groups → `docs/activity-diagram-guideline.md`. Sơ đồ cũ chỉ là đầu vào audit. Không sửa YAML/BR.

Verdict cao nhất là **READY FOR PEER REVIEW**, không phải Accepted. Người nghiệm thu là leader/peer reviewer.

## 1. Phạm vi

Manifest có 55 Use Case cụ thể. Loại trừ 10 UC (UC-06 → UC-13, domain `project-membership`): `UC-PROJECT-CREATE`, `UC-PROJECT-DASHBOARD-VIEW`, `UC-PROJECT-UPDATE`, `UC-PROJECT-MEMBERS-VIEW`, `UC-PROJECT-MEMBER-ADD`, `UC-PROJECT-MEMBER-REMOVE`, `UC-SCRUM-ACCOUNTABILITY-ASSIGN`, `UC-PROJECT-ARCHIVE`, `UC-PROJECT-OWNERSHIP-TRANSFER`, `UC-PROJECT-LEAVE`. Còn **45 UC** trong phạm vi; không tạo UC mới để khớp con số.

## 2. Quy ước áp dụng

Nhãn action là "động từ + tân ngữ", mục tiêu 2–7 từ và tối đa 2 dòng; điều kiện/nguyên nhân nằm ở guard (ví dụ `[account inactive — EX-01]`), giải thích dài nằm ở comment đầu file `.puml` hoặc báo cáo này. `Reject …` chỉ dùng cho từ chối theo business rule, quyền hoặc trạng thái. Không thêm Display error / Notify / Retry / Rollback / Log nếu spec không nói.

Chính sách kết cục ngoại lệ: (a) spec mô tả phản hồi → vẽ đúng các bước đó; (b) từ chối nghiệp vụ/quyền/trạng thái không mô tả phản hồi → một action `Reject <request>` (trace `GUIDE-7.3`); (c) lỗi kỹ thuật / dữ liệu không có / không lưu được / không gửi được mà spec không mô tả phản hồi → **không vẽ action**, guard đi thẳng tới Activity Final, ghi kết cục ở comment đầu file và ghi NEEDS CLARIFICATION kèm câu đề xuất cho spec. Mục (c) **lệch** khỏi guideline §5/§7.3 ("không kết thúc im lặng"); đây là quyết định của leader và cần được ghi nhận khi peer review.

Các bước System được YAML ghi rõ (ví dụ "The system leaves the account active") được giữ thành action, thống nhất với UC-10/11/24.5.

## 3. Bảng tổng hợp

| UC | Semantic key | Source traceability | UML | A4 readability | Verdict | Files changed | Clarification needed |
|---|---|---|---|---|---|---|---|
| UC-01 | `UC-ACCOUNT-REGISTER` | pass | pass | 4.3 pt — dưới 6 pt | REQUEST CHANGES | `.puml`, `.svg` | EX-01, EX-02, EX-03 |
| UC-02 | `UC-SIGN-IN` | pass | pass | 5.0 pt — dưới 6 pt | REQUEST CHANGES | `.puml`, `.svg` | EX-03 |
| UC-03 | `UC-SIGN-OUT` | pass | pass | 7.9 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-04 | `UC-PASSWORD-RESET` | pass | pass | 4.7 pt — dưới 6 pt | REQUEST CHANGES | `.puml`, `.svg` | — |
| UC-05.1 | `UC-PROFILE-VIEW` | pass | pass | 10.5 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-05.2 | `UC-PROFILE-UPDATE` | pass | pass | 6.9 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-05.3 | `UC-PASSWORD-CHANGE` | pass | pass | 6.3 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-14.1 | `UC-PRODUCT-GOAL-VIEW` | pass | pass | 10.5 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-14.2 | `UC-PRODUCT-GOAL-SET` | pass | pass | 9.9 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-14.3 | `UC-PRODUCT-GOAL-UPDATE` | pass | pass | 6.6 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-15.1 | `UC-BACKLOG-ITEM-VIEW` | pass | pass | 10.5 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-15.2 | `UC-BACKLOG-ITEM-CREATE` | pass | pass | 7.1 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-15.3 | `UC-BACKLOG-ITEM-UPDATE` | pass | pass | 9.8 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-15.4 | `UC-BACKLOG-ITEM-REMOVE` | pass | pass | 6.9 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-16 | `UC-BACKLOG-ORDER` | pass | pass | 8.6 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-17 | `UC-BACKLOG-ITEM-REFINE` | pass | pass | 6.1 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-18 | `UC-BACKLOG-ITEM-ESTIMATE` | pass | pass | 6.7 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-19 | `UC-SPRINT-PLAN` | pass | pass | 7.6 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-20 | `UC-SPRINT-START` | pass | pass | 6.3 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-21 | `UC-SPRINT-COMPLETE` | pass | pass | 6.7 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-22 | `UC-SPRINT-CANCEL` | pass | pass | 6.4 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-23 | `UC-SPRINT-BOARD-REVIEW` | pass | pass | 8.1 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-24.1 | `UC-SPRINT-TASK-VIEW` | pass | pass | 10.5 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-24.2 | `UC-SPRINT-TASK-CREATE` | pass | pass | 8.9 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-24.3 | `UC-SPRINT-TASK-UPDATE` | pass | pass | 7.3 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-24.4 | `UC-SPRINT-TASK-ASSIGN` | pass | pass | 7.3 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-24.5 | `UC-SPRINT-TASK-DELETE` | pass | pass | 6.1 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-24.6 | `UC-TASK-DEPENDENCY-ADD` | pass | pass | 8.1 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-24.7 | `UC-TASK-DEPENDENCY-REMOVE` | pass | pass | 7.0 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-25 | `UC-SPRINT-TASK-CLAIM` | pass | pass | 10.5 pt ✓ | READY FOR PEER REVIEW | `.puml` (mới), `.svg` (mới) | NF2 |
| UC-26 | `UC-WORK-ITEM-STATUS-UPDATE` | pass | pass | 8.0 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-27.1 | `UC-SUBTASKS-VIEW` | pass | pass | 10.5 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-27.2 | `UC-SUBTASK-CREATE` | pass | pass | 10.3 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-27.3 | `UC-SUBTASK-UPDATE` | pass | pass | 7.0 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-27.4 | `UC-SUBTASK-COMPLETE` | pass | pass | 7.3 pt ✓ | READY FOR PEER REVIEW | `.puml` (mới), `.svg` (mới) | — |
| UC-27.5 | `UC-SUBTASK-DELETE` | pass | pass | 7.0 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-28 | `UC-WORK-ITEM-COMMENT` | pass | pass | 6.5 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-29 | `UC-WORK-ITEM-ACTIVITY-REVIEW` | pass | pass | 9.3 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-30 | `UC-NOTIFICATIONS-REVIEW` | pass | pass | 6.0 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-02 |
| UC-31 | `UC-SPRINT-PROGRESS-MONITOR` | pass | pass | 10.3 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-32.1 | `UC-USER-ACCOUNTS-SEARCH` | pass | pass | 8.6 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |
| UC-32.2 | `UC-USER-ACCOUNT-SUSPEND` | pass | pass | 7.0 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-32.3 | `UC-USER-ACCOUNT-REACTIVATE` | pass | pass | 6.8 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-32.4 | `UC-USER-ACCOUNT-DELETE` | pass | pass | 7.0 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | — |
| UC-33 | `UC-SYSTEM-AUDIT-LOG-REVIEW` | pass | pass | 9.2 pt ✓ | READY FOR PEER REVIEW | `.puml`, `.svg` | EX-01 |

"Source traceability: pass" = `scripts/activity_diagrams.py validate` 0 lỗi (mọi NF/AF/EX có action hoặc guard tham chiếu, không có ref lạ). "UML: pass" = không còn layout issue (chữ bị đường cắt / chữ đè action), PNG đã được xem. A4 = cỡ chữ guard khi fit vào vùng chữ 16.5 × 20.5 cm; ngưỡng 6 pt.

## 4. Chi tiết từng UC

### UC-01 Register Account (`UC-ACCOUNT-REGISTER`) — REQUEST CHANGES

Kích thước 1517×1604 px · 4.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-04 | (not drawn) | YAML added EX-04 (IdP returns an email already linked to an account); validator error "EX-04 is not represented". | AF-01.3 split: "Validate email uniqueness" -> decision "Email address unused?" -> [already registered — EX-04] -> "Direct Guest to sign-in" -> F4 | no (new flow from YAML) | MODEL CORRECTION |
| AF-01.3 / EX-03 | Validate email uniqueness and create an active User account | One box hid two checks (EX-04 at uniqueness, EX-03 at persistence). | "Validate email uniqueness" + "Create active User account" with separate decisions | yes | EDITORIAL |
| EX-01 | Keep the account pending so that verification can be requested again | Outcome written as a fake action; delivery failure has no described System response (policy c). | no action: [not delivered — EX-01] -> F2 (account remains pending) | yes | MODEL CORRECTION |
| EX-02 | Cancel the registration because no valid verified identity was returned | Action + cause in one box; "registration is cancelled" is the outcome of an IdP failure (policy c). | no action: [no valid identity — EX-02] -> F4 | yes | MODEL CORRECTION |
| EX-03 | Reject the registration so that no account is created (x2) | "Reject" used for a persistence failure (rule 9); outcome as action. | no action: [not persisted — EX-03] -> F4 (both paths) | yes | MODEL CORRECTION |
| Finals | one Activity Final for all outcomes | Different outcomes (active / pending / no account) shared one final. | F1/F3 active, F2 pending, F4 no account | yes | EDITORIAL |
| NF1 / TRIGGER | Open account registration and choose a registration method | Article/length; trigger not traced. | Open account registration [NF1, TRIGGER] | yes | EDITORIAL |
| NF2..NF9 labels | Request the display name, email address, and password; Validate the information, email uniqueness, and password strength; ... | Articles, long wrap (3.3 pt). | Request display name, email and password; Validate information, email uniqueness and password strength; Create pending account; Request email verification message; Deliver verification message to submitted email address; Open valid verification link; Activate User account and confirm registration | yes | EDITORIAL |
| POST2 / BR-ACCOUNT-NO-PROJECT-AUTO-MEMBERSHIP | not traced | POST2 and BR not traced. | traced on NF9 "Activate User account and confirm registration" | yes | EDITORIAL |
| EX-04 wording | Directed to Log In (YAML) | Validator regex forbids "log in"/"sign in" in action text outside UC-SIGN-IN, so the action reads "Direct Guest to sign-in". | Direct Guest to sign-in | yes (wording only; reviewer may prefer another phrasing) | EDITORIAL |
| Legibility | 3.3 pt | Below 6 pt at A4. | 4.3 pt after narrower wrapping, no-action exception guards, decision in System lane; two parallel registration-method branches across 4 lanes keep it wide (stacking the Google branch below gives ~3.7 pt). | yes | NEEDS CLARIFICATION |

Final nodes: F1 = User account active via email verification (POST1, POST2); F2 = account remains pending (EX-01); F3 = active account created with Google (POST1, POST2 once AF-01.3 is persisted); F4 = no account created (EX-02, EX-03 on both paths, EX-04). F1/F3 kept separate: the two method branches have no common last step; merging them would split F4..

NEEDS CLARIFICATION — EX-01: Is the Guest informed that the verification message could not be delivered, and how is verification requested again? Đề xuất cho spec: "EX-01: The Email Service cannot deliver the verification message; the account remains pending, and the system informs the Guest that the message could not be sent and that verification can be requested again."

NEEDS CLARIFICATION — EX-02: Is the Guest informed when the Identity Provider returns no valid verified identity? Đề xuất cho spec: "EX-02: The Identity Provider does not return a valid verified identity; registration is cancelled and the system informs the Guest that Google registration could not be completed."

NEEDS CLARIFICATION — EX-03: Is the Guest informed when account data cannot be persisted? Đề xuất cho spec: "EX-03: Account data cannot be persisted, so no User account is created; the system informs the Guest that registration could not be completed and can be tried again later."

NEEDS CLARIFICATION — POST1 on the Google path: POST1/POST2 hold on the Google path only after AF-01.3 is persisted; there is no action after the persistence check to carry the trace. Accept the trace in the header (F3) only? Đề xuất cho spec: "(no spec change; diagram convention question)"

Ghi chú: EX-04 drawn (validator error fixed). Layout issues empty, PNG inspected, but 4.3 pt < 6 pt -> needs-manual-review. Old manifest observation (EX-04 outcome unspecified) is obsolete.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open account registration and choose a registration method | Open account registration |
| NF2 | Request the display name, email address, and password | Request display name, email and password |
| NF3 | Provide the required registration information / Provide the registration information again | Provide registration information / Provide registration information |
| NF4 | Validate the information, email uniqueness, and password strength | Validate information, email uniqueness and password strength |
| AF-02.1 | Request the registration information again | Request registration information again |
| NF5 | Create a pending account | Create pending account |
| NF6 | Request an email verification message for the account | Request email verification message |
| NF7 | Deliver the verification message to the submitted email address | Deliver verification message to submitted email address |
| NF8 | Open the valid verification link | Open valid verification link |
| NF9 | Activate the User account and confirm registration | Activate User account and confirm registration |
| AF-01.1 | Redirect the Guest to the Identity Provider | Redirect Guest to Identity Provider |
| AF-01.2 | Authenticate the Guest and return a verified identity | Authenticate Guest and return verified identity |
| AF-01.3 | Validate email uniqueness and create an active User account | Validate email uniqueness / Create active User account |
| EX-04 | — | Direct Guest to sign-in |
| EX-01 | Keep the account pending so that verification can be requested again | — |
| EX-03 | Reject the registration so that no account is created / Reject the registration so that no account is created | — |
| EX-02 | Cancel the registration because no valid verified identity was returned | — |

</details>

### UC-02 Log In (`UC-SIGN-IN`) — REQUEST CHANGES

Kích thước 1093×1627 px · 5.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-02 | Forgot Password chosen? (System lane, before the option choice) | AF-02 concerns the locally managed password only; decision was a System decision before the option was chosen. | User-lane decision "Password forgotten?" after NF2 on the email path: [forgotten — AF-02] -> "Direct User to Forgot Password" -> F3 | yes (placement; same condition and step) | EDITORIAL |
| EX-01, EX-02 (email) | Reject the log-in without creating a session | Outcome folded into the action. | Reject log-in [EX-01, EX-02, BR-AUTH-ACTIVE-ACCOUNT, GUIDE-7.3] | yes | EDITORIAL |
| EX-02 (Google) | Reject the log-in for the inactive account | Cause in the box. | guard [not active — EX-02] + Reject log-in | yes | EDITORIAL |
| EX-03 | End the log-in without creating a session | Fake action for an IdP failure (policy c). | no action: [unavailable or rejected — EX-03] -> F5 | yes | MODEL CORRECTION |
| EX-04 | Direct the person to Register Account without creating a session | Outcome in the box. | Direct person to Register Account | yes | EDITORIAL |
| POST2 | not traced | POST2 not traced. | traced with POST1 on both session-creation actions | yes | EDITORIAL |
| NF/AF labels | Request the registered email address and password; Validate the credentials and confirm that the account is active; Create an authenticated session and display the User's available projects; ... | Articles, long wraps. | Request registered email and password; Submit credentials; Validate credentials and confirm account is active; Create authenticated session and display available projects; Redirect User to Identity Provider; Authenticate User and return verified identity; Match identity to existing active User account; Create authenticated session | yes | EDITORIAL |
| Finals / layout | one Activity Final for all outcomes; branches side by side (3.7 pt) | Different outcomes shared one final; illegible at A4. | Google branch drawn below the email branch; F1 session (email), F2 rejected (EX-01/02), F3 Forgot Password (AF-02), F4 session (Google), F5 no session (Google EX-02/03/04). F1/F4 and F2/F5 share outcomes but end separate branches (stacked layout); 5.0 pt. | yes | NEEDS CLARIFICATION |
| Leader edit (post-agent) | (agent label) | Label shortened further after the agent pass to meet the 2–7 word / 2-line target; see auto label table. | see auto label table | yes | EDITORIAL |

Final nodes: F1 = session via email and password (POST1, POST2); F2 = log-in rejected, no session (EX-01, EX-02); F3 = User directed to Forgot Password (AF-02); F4 = session via Google (POST1, POST2); F5 = no session on the Google path (EX-02, EX-03, EX-04)..

NEEDS CLARIFICATION — EX-03: Is the User informed when the Identity Provider is unavailable or rejects authentication? Đề xuất cho spec: "EX-03: The Identity Provider is unavailable or rejects authentication; no session is created and the system informs the User that Google log-in could not be completed."

Ghi chú: Layout issues empty, PNG inspected, but 5.0 pt < 6 pt (height-bound) -> needs-manual-review. Same-outcome finals are duplicated because of the stacked layout chosen for legibility (side-by-side with merged finals = 3.7 pt); reviewer to accept the trade-off. The method decision stays in the System lane ($question_x): placing it in the User lane produced 6 text-crossing issues; NF1 box states the User's choice.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the log-in page and choose a log-in option | Open log-in page and choose log-in option |
| NF2 | Request the registered email address and password | Request registered email and password |
| NF3 | Submit the credentials | Submit credentials |
| NF4 | Validate the credentials and confirm that the account is active | Validate credentials and confirm account is active |
| NF5 | Create an authenticated session and display the User's available projects | Create authenticated session and display available projects |
| EX-01 | Reject the log-in without creating a session | Reject log-in |
| AF-02.1 | Direct the User to Forgot Password | Direct User to Forgot Password |
| AF-01.1 | Redirect the User to the Identity Provider | Redirect User to Identity Provider |
| AF-01.2 | Authenticate the User and return a verified identity | Authenticate User and return verified identity |
| AF-01.3 | Match the identity to an existing User account / Create an authenticated session | Match identity to existing active User account / Create authenticated session |
| EX-02 | Reject the log-in for the inactive account | Reject log-in |
| EX-04 | Direct the person to Register Account without creating a session | Direct to Register Account |
| EX-03 | End the log-in without creating a session | — |

</details>

### UC-03 Log Out (`UC-SIGN-OUT`) — READY FOR PEER REVIEW

Kích thước 830×689 px · 7.9 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF2 / POST1 | Invalidate the current session and its refresh credential [NF2, POST1] | POST1 traced on a step that can still fail (EX-01). | Invalidate current session and its refresh credential [NF2, BR-LOG-OUT-SESSION]; POST1 moved to NF3 | yes | MODEL CORRECTION |
| EX-01 | Remove the local credentials and report that remote revocation could not be confirmed | YAML lists two things (policy a): split. | Remove local credentials [EX-01, POST2]; Report remote revocation could not be confirmed [EX-01] | yes | EDITORIAL |
| Structure | old pattern (exception below, NF3 after endif) | Brief layout pattern. | NF3 inside then, EX-01 sideways | yes | EDITORIAL |
| Labels | Remove the local authentication credentials and display the public log-in page; Remove any remaining local authentication credentials; Display the public log-in page | Articles. | Remove local credentials and display public log-in page; Remove remaining local credentials; Display public log-in page | yes | EDITORIAL |
| POST3 / BR-LOG-OUT-SESSION / TRIGGER | not traced | Not traced. | POST3 on NF3 and AF-01.2; BR on NF2; TRIGGER on NF1 | yes | EDITORIAL |

Final nodes: F1 = local credentials removed, remote revocation unconfirmed (EX-01); F2 = User logged out, public log-in page displayed (NF3 and AF-01 merge)..

Ghi chú: Client-side EX-01 actions stay in the System lane (no client partition allowed).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Request to log out | Request to log out |
| NF2 | Invalidate the current session and its refresh credential | Invalidate current session and its refresh credential |
| NF3 | Remove the local authentication credentials and display the public log-in page | Remove local credentials and display public log-in page |
| EX-01 | Remove the local credentials and report that remote revocation could not be confirmed | Remove local credentials / Report remote revocation could not be confirmed |
| AF-01.1 | Remove any remaining local authentication credentials | Remove remaining local credentials |
| AF-01.2 | Display the public log-in page | Display public log-in page |

</details>

### UC-04 Forgot Password (`UC-PASSWORD-RESET`) — REQUEST CHANGES

Kích thước 1396×1729 px · 4.7 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-03 | (not drawn) | YAML added AF-03 (weak new password); validator error "AF-03 is not represented". | while "Password too weak?" [weak — AF-03]: Reject new password and state password requirements (AF-03.1) -> Submit another new password (User, AF-03.2) -> loop; [strong] continues | no (new flow from YAML) | MODEL CORRECTION |
| AF-02 | Keep the generic response without creating a reset token; Continue to authenticate through Google | AF-02.1 is an outcome (generic response already shown in NF2), not an action. | AF-02.1 not drawn as action (noted in header); [Google only — AF-02] -> Continue authentication through Google -> F1 | yes | MODEL CORRECTION |
| EX-01 | Record the delivery failure without exposing whether the account exists | Long label. | Record delivery failure without exposing account [EX-01, BR-PASSWORD-RESET-PRIVACY] | yes | EDITORIAL |
| EX-02 | Reject the password reset for the changed account | Cause in box. | guard [status changed — EX-02] + Reject password reset | yes | EDITORIAL |
| AF-01 | Reject the password change; Allow the User to submit a new Forgot Password request | Articles. | Reject password change; Allow new Forgot Password request | yes | EDITORIAL |
| NF labels | Open Forgot Password and submit an email address; Display the same generic response whether or not the account exists; ... | Articles. | Open Forgot Password and submit email address; Display same generic response whether or not account exists; Generate single-use expiring reset token; Deliver password-reset link to eligible email address; Open valid link and submit new password; Validate token and password strength; Update password and invalidate used token | yes | EDITORIAL |
| Legibility | 3.5 pt | Below 6 pt. | 4.7 pt (AF-02 drawn in line with its own final to keep the User lane narrow; narrow side-branch labels). Still < 6 pt. | yes | NEEDS CLARIFICATION |
| Leader edit (post-agent) | (agent label) | Label shortened further after the agent pass to meet the 2–7 word / 2-line target; see auto label table. | see auto label table | yes | EDITORIAL |

Final nodes: F1 = Google-only account, no token, User continues through Google (AF-02); F2 = password updated and token invalidated (POST1-3); F3 = password unchanged (no eligible account, EX-01, AF-01, EX-02)..

Ghi chú: AF-03 drawn (validator error fixed); old manifest observation (weak password outcome unspecified) is obsolete. Layout issues empty, PNG inspected, 4.7 pt < 6 pt -> needs-manual-review. AF-03.2 "while the reset token remains valid" is not re-checked in the loop (no branch defined in YAML).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open Forgot Password and submit an email address | Open Forgot Password and submit email address |
| NF2 | Display the same generic response whether or not the account exists | Display generic response for any email |
| AF-02.2 | Continue to authenticate through Google | Continue authentication through Google |
| NF3 | Generate a single-use expiring reset token | Generate single-use expiring reset token |
| NF4 | Deliver the password-reset link to the eligible email address | Deliver password-reset link to eligible email address |
| NF5 | Open the link and submit a new password | Open valid link and submit new password |
| NF6 | Validate the token and the password strength / Update the password and invalidate the used token | Validate token and password strength / Update password and invalidate used token |
| AF-03.1 | — | Reject new password and state password requirements |
| AF-03.2 | — | Submit another new password |
| EX-02 | Reject the password reset for the changed account | Reject password reset |
| AF-01.1 | Reject the password change | Reject password change |
| AF-01.2 | Allow the User to submit a new Forgot Password request | Allow new Forgot Password request |
| EX-01 | Record the delivery failure without exposing whether the account exists | Record delivery failure without exposing account |
| AF-02.1 | Keep the generic response without creating a reset token | — |

</details>

### UC-05.1 View Personal Profile (`UC-PROFILE-VIEW`) — READY FOR PEER REVIEW

Kích thước 561×472 px · 10.5 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Report that the profile information is temporarily unavailable [EX-01, GUIDE-7.3] | Data unavailable with no described response: no action (policy c). | no action: [temporarily unavailable — EX-01] -> F2 | yes | MODEL CORRECTION |
| Structure | exception below with bypass | Brief layout pattern. | NF3 inside then, EX-01 sideways to its own final | yes | EDITORIAL |
| Labels | Open the personal profile page; Retrieve the profile belonging to the authenticated User; Display the User's profile and non-sensitive account information | Articles. | Open personal profile page; Retrieve profile of authenticated User; Display profile and non-sensitive account information [NF3, POST1, OTHER] | yes | EDITORIAL |

Final nodes: F1 = profile displayed (POST1); F2 = profile not displayed (EX-01)..

NEEDS CLARIFICATION — EX-01: Is the User told that the profile is temporarily unavailable? Đề xuất cho spec: "EX-01: The profile information is temporarily unavailable; the system informs the User that the profile cannot be displayed at the moment."

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the personal profile page | Open personal profile page |
| NF2 | Retrieve the profile belonging to the authenticated User | Retrieve profile of authenticated User |
| NF3 | Display the User's profile and non-sensitive account information | Display profile and non-sensitive account information |
| EX-01 | Report that the profile information is temporarily unavailable | — |

</details>

### UC-05.2 Update Personal Profile (`UC-PROFILE-UPDATE`) — READY FOR PEER REVIEW

Kích thước 950×798 px · 6.9 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF3 / AF-01 | decision "Save the changes?" before "Change the desired values and submit the profile" | Cancel decision came before the User changed anything. | Change desired values (NF3) -> decision "Submit or cancel?" -> [submit] Submit profile (NF3) / [cancel before saving — AF-01] Discard unsaved changes | yes | EDITORIAL |
| NF4 | Validate the profile changes; Save the profile changes | Articles. | Validate profile changes; Save profile changes [NF4, POST1, BR-PROFILE-SELF-ACCESS] | yes | EDITORIAL |
| EX-01 | Reject the profile changes and keep the stored profile | Outcome folded into the action. | Reject profile changes [EX-01, GUIDE-7.3] | yes | EDITORIAL |
| Decision | $question_x("Values valid?") | Flow enters from the same lane. | $question("Values valid?") | yes | EDITORIAL |

Final nodes: F1 = profile changes saved (POST1); F2 = stored profile unchanged (EX-01, AF-01)..

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open profile editing | Open profile editing |
| NF2 | Display the current editable profile values | Display current editable profile values |
| NF3 | Change the desired values and submit the profile | Change desired values / Submit profile |
| NF4 | Validate the profile changes / Save the profile changes | Validate profile changes / Save profile changes |
| NF5 | Display the updated profile | Display updated profile |
| EX-01 | Reject the profile changes and keep the stored profile | Reject profile changes |
| AF-01.1 | Discard the unsaved changes | Discard unsaved changes |

</details>

### UC-05.3 Change Password (`UC-PASSWORD-CHANGE`) — READY FOR PEER REVIEW

Kích thước 1038×1145 px · 6.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-01 (manifest observation) | "AF-01 contradicts a precondition" | Precondition now only requires an authenticated active account; AF-01 no longer contradicts it. Observation obsolete. | kept as normal alternative check; label Inform User to change password through Identity Provider | yes | EDITORIAL |
| TRIGGER | (no first action) | Trigger not traced; diagram started with a System decision. | Choose to change password [TRIGGER] (User lane) | yes | EDITORIAL |
| EX-02 | Reject the new password [EX-02, GUIDE-7.3] | BR not traced. | Reject new password [EX-02, BR-PASSWORD-STRENGTH, GUIDE-7.3] | yes | EDITORIAL |
| Labels | Enter the current password and a new password; Verify the current password; ... | Articles. | Enter current password and new password; Verify current password; Validate new password against password policy; Confirm password change; Store new password securely and confirm success; Record password change as security event; Reject password change | yes | EDITORIAL |

Final nodes: F1 = new password stored and recorded (POST1, POST2); F2 = password unchanged (AF-01, EX-01, EX-02)..

Ghi chú: "Record password change as security event" is kept because POST2 states it.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| TRIGGER | — | Choose to change password |
| NF1 | Enter the current password and a new password | Enter current password and new password |
| NF2 | Verify the current password | Verify current password |
| NF3 | Validate the new password against the password policy | Validate new password against password policy |
| NF4 | Confirm the password change | Confirm password change |
| NF5 | Store the new password securely and confirm success | Store new password securely and confirm success |
| POST2 | Record the password change as a security event | Record password change as security event |
| EX-02 | Reject the new password | Reject new password |
| EX-01 | Reject the password change | Reject password change |
| AF-01.1 | Inform the User that the password must be changed through that provider | Inform User to change password through Identity Provider |

</details>

### UC-14.1 View Product Goal (`UC-PRODUCT-GOAL-VIEW`) — READY FOR PEER REVIEW

Kích thước 626×431 px · 10.5 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1 | Open the Product Goal view | article / extra words removed (label rule 1) | Open Product Goal view | yes | EDITORIAL |
| NF2 | Retrieve the current Product Goal | article / extra words removed (label rule 1) | Retrieve current Product Goal | yes | EDITORIAL |
| NF2 / POST1 | Display the current Product Goal | article / extra words removed (label rule 1); fits one line | Display current Product Goal | yes | EDITORIAL |
| AF-01.1 | Display that the Product Goal is not yet available | article / extra words removed (label rule 1) | Display Product Goal not yet available | yes | EDITORIAL |

Final nodes: F1 = single final (goal or 'not yet available' displayed, both merged).

Ghi chú: Structure unchanged; labels only.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the Product Goal view | Open Product Goal view |
| NF2 | Retrieve the current Product Goal / Display the current Product Goal | Retrieve current Product Goal / Display current Product Goal |
| AF-01.1 | Display that the Product Goal is not yet available | Display Product Goal not yet available |

</details>

### UC-14.2 Set Product Goal (`UC-PRODUCT-GOAL-SET`) — READY FOR PEER REVIEW

Kích thước 664×601 px · 9.9 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1 | Choose to define the Product Goal | article / extra words removed (label rule 1) | Choose to define Product Goal | yes | EDITORIAL |
| NF2 | Request the desired future product outcome | article / extra words removed (label rule 1) | Request desired future product outcome | yes | EDITORIAL |
| NF3 | Enter the Product Goal and confirm it | verbose | Enter and confirm Product Goal | yes | EDITORIAL |
| NF4 | Validate the Product Goal / Store the Product Goal / Record the creation in project activity history | article / extra words removed (label rule 1) | Validate Product Goal / Store Product Goal / Record creation in project activity history | yes | EDITORIAL |
| EX-01 | Reject the empty Product Goal | article / extra words removed (label rule 1); policy (b) single Reject action | Reject empty Product Goal (guard [empty — EX-01]) | yes | EDITORIAL |
| structure | empty then + else-reject-stop, main flow after endif | brief layout pattern: main flow in then, exception sideways | main flow inside then, EX-01 in else | yes (layout only) | EDITORIAL |
| header | no Final nodes comment with 2 finals | header must explain finals | F1/F2 added | yes | EDITORIAL |

Final nodes: F1 = Product Goal stored and recorded (POST1, POST2); F2 = empty Product Goal rejected, no goal stored (EX-01).

Ghi chú: EX-01 empty input treated as policy (b) (validation rule rejection).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Choose to define the Product Goal | Choose to define Product Goal |
| NF2 | Request the desired future product outcome | Request desired future product outcome |
| NF3 | Enter the Product Goal and confirm it | Enter and confirm Product Goal |
| NF4 | Validate the Product Goal / Store the Product Goal | Validate Product Goal / Store Product Goal |
| POST2 | Record the creation in project activity history | Record creation in project activity history |
| EX-01 | Reject the empty Product Goal | Reject empty Product Goal |

</details>

### UC-14.3 Update Product Goal (`UC-PRODUCT-GOAL-UPDATE`) — READY FOR PEER REVIEW

Kích thước 991×832 px · 6.6 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF3 / AF-01 | PO decision 'Save the revision?' BEFORE 'Revise the Product Goal and confirm the change' | actor decided to save/cancel before revising; YAML: user revises and confirms, AF-01 cancels before saving | ':Revise Product Goal;' then decision 'Confirm change?' [confirm] -> ':Confirm change;' / [cancel before saving — AF-01] -> 'Keep current Product Goal unchanged' | no (cancel now possible after revising, as the YAML implies) | MODEL CORRECTION |
| EX-01 / BR-PRODUCT-ONE-GOAL | Reject the revision from the former Product Owner | cause in label (rule 3); cause is already in guard [accountability lost — EX-01] | Reject Product Goal revision | yes | EDITORIAL |
| NF1, NF2, NF4, POST2 | Open the current Product Goal and choose to edit it / Display the current goal text / Validate the revised Product Goal / Save the revised Product Goal / Record the change in project activity history | article / extra words removed (label rule 1) | same without articles | yes | EDITORIAL |
| decision | $question_x('Still the Product Owner?') | flow enters from same lane | $question | yes | EDITORIAL |
| Leader edit (post-agent) | (agent label) | Label shortened further after the agent pass to meet the 2–7 word / 2-line target; see auto label table. | see auto label table | yes | EDITORIAL |

Final nodes: F1 = revised Product Goal saved and recorded (POST1, POST2); F2 = Product Goal unchanged (EX-01 rejection and AF-01 cancellation merged).

Ghi chú: BR-PRODUCT-ONE-GOAL also traced on save.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the current Product Goal and choose to edit it | Choose to edit Product Goal |
| NF2 | Display the current goal text | Display current goal text |
| NF3 | Revise the Product Goal and confirm the change | Revise Product Goal / Confirm change |
| NF4 | Validate the revised Product Goal / Save the revised Product Goal | Validate revised Product Goal / Save revised Product Goal |
| POST2 | Record the change in project activity history | Record change in project activity history |
| EX-01 | Reject the revision from the former Product Owner | Reject Product Goal revision |
| AF-01.1 | Keep the current Product Goal unchanged | Keep current Product Goal unchanged |

</details>

### UC-15.1 View Product Backlog Item (`UC-BACKLOG-ITEM-VIEW`) — READY FOR PEER REVIEW

Kích thước 523×472 px · 10.5 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Report that the selected item is no longer available | 'Report …' not described by UC (rule 10); item unavailable = data unavailable -> policy (c) | no action: guard [no longer available — EX-01] goes straight to F2 | no (invented response removed) | NEEDS CLARIFICATION |
| NF1, NF2 | Select a Product Backlog Item / Retrieve the item's current information | article / extra words removed (label rule 1) | Select Product Backlog Item / Retrieve current item information | yes | EDITORIAL |
| NF3 / POST1 | Display the item details and related Sprint information | article / extra words removed (label rule 1) | Display item details and related Sprint information | yes | EDITORIAL |
| structure | main flow after endif | layout pattern | main flow in then, EX-01 sideways to final | yes | EDITORIAL |

Final nodes: F1 = item details displayed (POST1); F2 = item no longer available, nothing displayed (EX-01, no response in UC).

NEEDS CLARIFICATION — EX-01: What does the User see when the selected item is no longer available? Đề xuất cho spec: "EX-01: The selected item is no longer available; the system informs the User that the item is no longer available."

Ghi chú: EX-01 classified as (c) data unavailable; if the BA sees it as a state rejection, it would become ':Reject item view;' instead.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a Product Backlog Item | Select Product Backlog Item |
| NF2 | Retrieve the item's current information | Retrieve current item information |
| NF3 | Display the item details and related Sprint information | Display item details and related Sprint information |
| EX-01 | Report that the selected item is no longer available | — |

</details>

### UC-15.2 Create Product Backlog Item (`UC-BACKLOG-ITEM-CREATE`) — READY FOR PEER REVIEW

Kích thước 917×914 px · 7.1 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 / AF-01 | EX-01 title check only on complete-item path; draft path stored without check | YAML revised: EX-01 'applies to complete items and to drafts'; old manifest observation now resolved | NF3 and AF-01 merge -> 'Validate new item' -> 'Title present?' [title missing — EX-01] Reject; then 'Draft item?' selects Store new item (NF4) / Store item not ready for Sprint planning (AF-01.1) | no (draft path now validated, per current YAML) | MODEL CORRECTION |
| EX-01 | Reject the item without identifying information | cause in label (rule 3) | Reject item creation (guard [title missing — EX-01]) | yes | EDITORIAL |
| AF-01.1 | Store the item without marking it ready for Sprint planning | long / 3 lines | Store item not ready for Sprint planning | yes | EDITORIAL |
| NF1-NF4, AF-01, POST2 | Choose to create a Product Backlog Item / Request the title, description, acceptance criteria, and item type / Provide the required information and confirm creation / Save the incomplete information as a draft / Store the new item in the Product Backlog / Record the creation in item activity history | article / extra words removed (label rule 1); 3-line boxes | Choose to create Product Backlog Item / Request title, description, acceptance criteria, item type / Provide required information and confirm creation / Save incomplete information as draft / Store new item in Product Backlog / Record creation in item activity history | yes | EDITORIAL |
| header | no Final nodes comment | 2 finals | F1/F2 added | yes | EDITORIAL |

Final nodes: F1 = item stored (complete or draft) and recorded (POST1, POST2); F2 = item creation rejected, nothing stored (EX-01).

Ghi chú: Old manifest note about EX-01 on drafts is stale; YAML now answers it.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Choose to create a Product Backlog Item | Choose to create Product Backlog Item |
| NF2 | Request the title, description, acceptance criteria, and item type | Request title, description, acceptance criteria, item type |
| NF3 | Provide the required information and confirm creation | Provide required information and confirm creation |
| AF-01 | Save the incomplete information as a draft | Save incomplete information as draft |
| NF4 | Validate the new item / Store the new item in the Product Backlog | Validate new item / Store new item in Product Backlog |
| AF-01.1 | Store the item without marking it ready for Sprint planning | Store item not ready for Sprint planning |
| POST2 | Record the creation in item activity history | Record creation in item activity history |
| EX-01 | Reject the item without identifying information | Reject item creation |

</details>

### UC-15.3 Update Product Backlog Item (`UC-BACKLOG-ITEM-UPDATE`) — READY FOR PEER REVIEW

Kích thước 599×828 px · 9.8 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the update because the item was changed concurrently | cause in label (rule 3) | Reject item update (guard [changed by another User — EX-01]) | yes | EDITORIAL |
| AF-01.1 | Limit changes that would invalidate active Sprint planning | long | Limit changes invalidating active Sprint planning | yes | EDITORIAL |
| NF1-NF4, POST2 | Open an existing Product Backlog Item for editing / Display the editable item values / Revise the desired values and submit the item / Validate the changes / Save the changes / Record the update in item activity history | article / extra words removed (label rule 1) | Open Product Backlog Item for editing / Display editable item values / Revise values and submit item / Validate changes / Save changes / Record update in item activity history | yes | EDITORIAL |
| guards | Item in the active Sprint? / [not in the active Sprint] / [in the active Sprint — AF-01] | article / extra words removed (label rule 1) | Item in active Sprint? / [not in active Sprint] / [in active Sprint — AF-01] | yes | EDITORIAL |
| structure | main flow after endif; $question_x on same-lane decision | layout pattern | main flow in then, EX-01 sideways; $question | yes | EDITORIAL |
| header | no Final nodes comment | 2 finals | F1/F2 added | yes | EDITORIAL |

Final nodes: F1 = changes saved and recorded (POST1, POST2); F2 = update rejected, item unchanged (EX-01).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open an existing Product Backlog Item for editing | Open Product Backlog Item for editing |
| NF2 | Display the editable item values | Display editable item values |
| AF-01.1 | Limit changes that would invalidate active Sprint planning | Limit changes invalidating active Sprint planning |
| NF3 | Revise the desired values and submit the item | Revise values and submit item |
| NF4 | Validate the changes / Save the changes | Validate changes / Save changes |
| POST2 | Record the update in item activity history | Record update in item activity history |
| EX-01 | Reject the update because the item was changed concurrently | Reject item update |

</details>

### UC-15.4 Remove Product Backlog Item (`UC-BACKLOG-ITEM-REMOVE`) — READY FOR PEER REVIEW

Kích thước 954×754 px · 6.9 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | 'Item in the active Sprint?' check with note 'contradicts a precondition' | stale: YAML no longer has that precondition; EX-01 is a real state rejection (rule 9 'item locked in the active Sprint') | 'Item locked in active Sprint?' [locked in active Sprint — EX-01] -> Reject item removal | yes | EDITORIAL |
| EX-01 | Reject the removal of the locked item | cause in label | Reject item removal | yes | EDITORIAL |
| NF1, NF2, NF4, AF-01.1 | Select a Product Backlog Item and request removal / Display the impact and request confirmation / Remove the item and record the action / Leave the Product Backlog Item unchanged | article / extra words removed (label rule 1) | Select Product Backlog Item and request removal / Display impact and request confirmation / Remove item and record removal / Leave Product Backlog Item unchanged | yes | EDITORIAL |

Final nodes: F1 = item removed and recorded (POST1, POST2); F2 = item unchanged (AF-01 cancellation and EX-01 rejection merged).

Ghi chú: Manifest observation about precondition conflict is stale and can be dropped.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a Product Backlog Item and request removal | Select Product Backlog Item and request removal |
| NF2 | Display the impact and request confirmation | Display impact and request confirmation |
| NF3 | Confirm removal | Confirm removal |
| NF4 | Remove the item and record the action | Remove item and record removal |
| AF-01.1 | Leave the Product Backlog Item unchanged | Leave Product Backlog Item unchanged |
| EX-01 | Reject the removal of the locked item | Reject item removal |

</details>

### UC-16 Order Product Backlog (`UC-BACKLOG-ORDER`) — READY FOR PEER REVIEW

Kích thước 620×942 px · 8.6 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the order because it cannot be saved completely and uniquely | persistence failure: 'Reject' not allowed (rule 9), cause in label; policy (c) | no action: guard [cannot be saved — EX-01] goes straight to F2 | no (invented rejection removed) | NEEDS CLARIFICATION |
| NF4 / POST1 | Save the new order placed after the EX-01 check in main flow after endif | postcondition only where it holds | Save new order + Display updated Product Backlog inside then-branch [can be saved] | yes | EDITORIAL |
| AF-01.1 | Refresh the current order of the Product Backlog | article / extra words removed (label rule 1) | Refresh current Product Backlog order (kept on one line so the loop return edge clears the guard) | yes | EDITORIAL |
| NF1-NF3, AF-01.2 | Open the ordered Product Backlog / Display all available items in their current order / Change the relative order of one or more items / Reapply the intended changes / Validate the new order | article / extra words removed (label rule 1) | Open ordered Product Backlog / Display available items in current order / Change relative order of one or more items / Reapply intended changes / Validate new order | yes | EDITORIAL |
| header | no Final nodes comment | 2 finals | F1/F2 added | yes | EDITORIAL |

Final nodes: F1 = new order saved and displayed (POST1); F2 = new order not saved, previous order kept (EX-01, no response in UC).

NEEDS CLARIFICATION — EX-01: What does the Product Owner see when a complete and unique order cannot be saved? Đề xuất cho spec: "EX-01: The system cannot save a complete and unique order for all backlog items; the previous order is kept and the system informs the Product Owner that the new order could not be saved."

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the ordered Product Backlog | Open ordered Product Backlog |
| NF2 | Display all available items in their current order | Display available items in current order |
| NF3 | Change the relative order of one or more items | Change relative order of one or more items |
| NF4 | Validate the new order / Save the new order | Validate new order / Save new order |
| AF-01.1 | Refresh the current order of the Product Backlog | Refresh current Product Backlog order |
| AF-01.2 | Reapply the intended changes | Reapply intended changes |
| NF5 | Display the updated Product Backlog | Display updated Product Backlog |
| EX-01 | Reject the order because it cannot be saved completely and uniquely | — |

</details>

### UC-17 Refine Backlog Item (`UC-BACKLOG-ITEM-REFINE`) — READY FOR PEER REVIEW

Kích thước 1070×1059 px · 6.1 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the decomposition of the item in the active Sprint; stop | YAML revised: 'the system rejects the decomposition and refinement continues without splitting the item' -> the flow must continue to NF5-NF6, not end | 'Reject item decomposition' merges back before NF5 (Confirm refined scope) | no (diagram ended the UC; YAML now continues) | MODEL CORRECTION |
| EX-01 | Item check 'Selected into an active Sprint?' | shorter | 'Item in active Sprint?' [not in Sprint] / [in active Sprint — EX-01] | yes | EDITORIAL |
| AF-01.1 | Define smaller independent backlog items with the Developer | article / extra words removed (label rule 1) | Define smaller independent items with Developer | yes | EDITORIAL |
| NF1-NF6, AF-01.2 | Select an item that requires refinement / Display the item's current details and estimate / Clarify the expected outcome and acceptance criteria / Add implementation-relevant clarification and propose decomposition when needed / Confirm the refined scope and description / Save the refined item and record the participants / Preserve traceability to the original item | article / extra words removed (label rule 1); 3-line box | Select item that requires refinement / Display current item details and estimate / Clarify expected outcome and acceptance criteria / Add implementation clarification and propose decomposition if needed / Confirm refined scope and description / Save refined item and record participants / Preserve traceability to original item | yes | EDITORIAL |

Final nodes: F1 = single final: refined item saved and participants recorded (POST1, POST2); the EX-01 path also reaches it.

Ghi chú: Old manifest observation about EX-01 ending the UC is resolved by the revised YAML. Lanes: PO steps 'Acting as the Product Owner' in PO lane, NF4 in Developer lane.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select an item that requires refinement | Select item that requires refinement |
| NF2 | Display the item's current details and estimate | Display current item details and estimate |
| NF3 | Clarify the expected outcome and acceptance criteria | Clarify expected outcome and acceptance criteria |
| NF4 | Add implementation-relevant clarification and propose decomposition when needed | Add implementation clarification and propose decomposition if needed |
| AF-01.1 | Define smaller independent backlog items with the Developer | Define smaller independent items with Developer |
| AF-01.2 | Preserve traceability to the original item | Preserve traceability to original item |
| EX-01 | Reject the decomposition of the item in the active Sprint | Reject item decomposition |
| NF5 | Confirm the refined scope and description | Confirm refined scope and description |
| NF6 | Save the refined item and record the participants | Save refined item and record participants |

</details>

### UC-18 Estimate Backlog Item (`UC-BACKLOG-ITEM-ESTIMATE`) — READY FOR PEER REVIEW

Kích thước 975×1095 px · 6.7 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-01.2 | Return the item for further refinement | YAML revised: 'The system marks the item as requiring further refinement' (System actor now explicit; old manifest observation resolved) | Mark item as requiring further refinement (System lane, BR-BACKLOG-ITEM-READY) | no (new YAML wording) | MODEL CORRECTION |
| AF-01.1 | Leave the estimate unset for this item | extra words | Leave estimate unset | yes | EDITORIAL |
| EX-01 | Reject the estimate because the item was removed or is in a completed Sprint | cause in label (rule 3); guard was vague [unavailable — EX-01] | Reject estimate; guard [removed or in completed Sprint — EX-01] | yes | EDITORIAL |
| NF1-NF5, POST2 | Select a refined Product Backlog Item / Display the item's details and current estimate / Clarify the expected outcome / Provide the agreed estimate / Validate the estimate / Record the estimate / Record the estimate change in item activity history | article / extra words removed (label rule 1) | Select refined Product Backlog Item / Display item details and current estimate / Clarify expected outcome / Provide agreed estimate / Validate estimate / Record estimate / Record estimate change in item activity history | yes | EDITORIAL |
| layout | 5.4 pt (1220 px wide): AF-01 branch beside the whole validation subtree | legibility | AF-01 sideways with stop; validation + EX-01 below the merge -> 975 px, 6.7 pt | yes (layout only) | EDITORIAL |
| header | no Final nodes comment | 3 finals | F1/F2/F3 added | yes | EDITORIAL |

Final nodes: F1 = estimate left unset and item marked as requiring further refinement (AF-01); F2 = agreed estimate recorded (POST1, POST2); F3 = estimate rejected, item unchanged (EX-01).

Ghi chú: Now >= 6 pt; was needs-manual-review only because of size. NF3 'when requested' kept as decision in the PO lane.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a refined Product Backlog Item | Select refined Product Backlog Item |
| NF2 | Display the item's details and current estimate | Display item details and current estimate |
| NF3 | Clarify the expected outcome | Clarify expected outcome |
| NF4 | Provide the agreed estimate | Provide agreed estimate |
| AF-01.1 | Leave the estimate unset for this item | Leave estimate unset |
| AF-01.2 | Return the item for further refinement | Mark item as requiring further refinement |
| NF5 | Validate the estimate / Record the estimate | Validate estimate / Record estimate |
| POST2 | Record the estimate change in item activity history | Record estimate change in item activity history |
| EX-01 | Reject the estimate because the item was removed or is in a completed Sprint | Reject estimate |

</details>

### UC-19 Plan Sprint (`UC-SPRINT-PLAN`) — READY FOR PEER REVIEW

Kích thước 864×1022 px · 7.6 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject saving the Sprint because its date range conflicts with another Sprint | cause in label (rule 3) | Reject Draft Sprint creation; guard [conflicts with another Sprint — EX-01] | yes | EDITORIAL |
| NF1 / BR-SPRINT-DATE-RANGE | BR-SPRINT-DATE-RANGE listed in header but not traced | BR trace | traced on NF1 (date range proposed) | yes | EDITORIAL |
| NF1-NF6, AF-01 | Start Sprint planning and propose the Sprint Goal and date range / Display the ordered Product Backlog Items that are ready for selection / Propose backlog items that support the Sprint Goal / Identify the missing readiness information / Refine the item or remove it from the Sprint selection with the Developer / Confirm the Sprint Goal and selected items with the Developer / Create the Draft Sprint and its initial Sprint Backlog | article / extra words removed (label rule 1) | Start Sprint planning and propose Sprint Goal and date range / Display ordered Product Backlog Items ready for selection / Propose backlog items supporting Sprint Goal / Identify missing readiness information / Refine item or remove it from Sprint selection with Developer / Confirm Sprint Goal and selected items with Developer / Create Draft Sprint and initial Sprint Backlog | yes | EDITORIAL |
| structure | main flow after endif | layout pattern | NF6 in then, EX-01 sideways | yes | EDITORIAL |
| header | no Final nodes comment | 2 finals | F1/F2 added | yes | EDITORIAL |
| Leader edit (post-agent) | (agent label) | Label shortened further after the agent pass to meet the 2–7 word / 2-line target; see auto label table. | see auto label table | yes | EDITORIAL |

Final nodes: F1 = Draft Sprint and initial Sprint Backlog created (POST1, POST2); F2 = Sprint not saved, date range conflict (EX-01).

Ghi chú: EX-01 has no BR (BR-SPRINT-DATE-RANGE covers end>start and <=1 month, not overlap); kept as UC-stated state rejection.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Start Sprint planning and propose the Sprint Goal and date range | Propose Sprint Goal and date range |
| NF2 | Display the ordered Product Backlog Items that are ready for selection | Display ordered Product Backlog Items ready for selection |
| NF3 | Propose backlog items that support the Sprint Goal | Propose backlog items supporting Sprint Goal |
| NF4 | Review capacity, estimates and item readiness | Review capacity, estimates and item readiness |
| AF-01.1 | Identify the missing readiness information | Identify missing readiness information |
| AF-01.2 | Refine the item or remove it from the Sprint selection with the Developer | Refine or deselect item with Developers |
| NF5 | Confirm the Sprint Goal and selected items with the Developer | Confirm Sprint Goal and selected items with Developer |
| NF6 | Create the Draft Sprint and its initial Sprint Backlog | Create Draft Sprint and initial Sprint Backlog |
| EX-01 | Reject saving the Sprint because its date range conflicts with another Sprint | Reject Draft Sprint creation |

</details>

### UC-20 Start Sprint (`UC-SPRINT-START`) — READY FOR PEER REVIEW

Kích thước 848×1301 px · 6.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-02 | (missing) | validate: 'alternative flow AF-02 is not represented'; YAML added AF-02 (revalidation in AF-01 fails) | inner loop after 'Revalidate Sprint before activation': while 'Revalidation failed?' [fails — AF-02] -> 'Report violated constraint' (AF-02.1, explicitly stated) -> PO 'Update selected backlog items again' (AF-02.2); exit [passes] | no (new flow added) | MODEL CORRECTION |
| EX-01 | 'Another Sprint active?' with note 'contradicts a precondition' | stale: precondition removed; EX-01 is a real state rejection under BR-SPRINT-ONE-ACTIVE | kept as check; label 'Reject Sprint start' | yes | EDITORIAL |
| EX-01 | Reject the start because another Sprint is already active | cause in label | Reject Sprint start | yes | EDITORIAL |
| NF1-NF5, AF-01, OTHER | Request to start the Draft Sprint / Validate the Sprint Goal, dates, selected work and active-Sprint constraint / Confirm that the selected work is understood and executable / Update the selected backlog items / Revalidate the Sprint before activation / Mark the Sprint active and open its Sprint Board / Record the Sprint start time in the activity history | article / extra words removed (label rule 1) | Request to start Draft Sprint / Validate Sprint Goal, dates, selected work and active-Sprint constraint / Confirm selected work is understood and executable / Update selected backlog items / Revalidate Sprint before activation / Mark Sprint active and open its Sprint Board / Record Sprint start time in activity history | yes | EDITORIAL |
| header | no Final nodes comment | 2 finals | F1/F2 + AF-02 note added | yes | EDITORIAL |

Final nodes: F1 = start rejected, Sprint stays Draft (EX-01); F2 = Sprint active, Sprint Board open, start time recorded (POST1, POST2).

Ghi chú: AF-02 'Sprint remains in Draft status' is an outcome, not drawn as action (header note). The inner loop returns to the revalidation decision without redrawing the revalidation action (same convention as UC-PROJECT-UPDATE AF-01). Old manifest note 'AF-01.2 failure not modelled' is now answered by AF-02. Main-flow-in-then pattern produced crossings (first then-node in Developer lane), so EX-01 keeps the sideways-stop pattern.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Request to start the Draft Sprint | Request to start Draft Sprint |
| NF2 | Validate the Sprint Goal, dates, selected work and active-Sprint constraint | Validate Sprint Goal, dates, selected work and active-Sprint constraint |
| EX-01 | Reject the start because another Sprint is already active | Reject Sprint start |
| NF3 | Confirm that the selected work is understood and executable | Confirm selected work is understood and executable |
| AF-01.1 | Update the selected backlog items | Update selected backlog items |
| AF-01.2 | Revalidate the Sprint before activation | Revalidate Sprint before activation |
| AF-02.1 | — | Report violated constraint |
| AF-02.2 | — | Update selected backlog items again |
| NF4 | Confirm Sprint activation | Confirm Sprint activation |
| NF5 | Mark the Sprint active and open its Sprint Board | Mark Sprint active and open its Sprint Board |
| OTHER | Record the Sprint start time in the activity history | Record Sprint start time in activity history |

</details>

### UC-21 Complete Sprint (`UC-SPRINT-COMPLETE`) — READY FOR PEER REVIEW

Kích thước 892×1218 px · 6.7 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the completion because the Sprint state has changed | cause in label | Reject Sprint completion; guard [state changed — EX-01] | yes | EDITORIAL |
| NF3 | Review the final work status and confirm that task data is current (one long line, twice) | drove width 1197 px -> 5.5 pt | Review final work status and confirm / task data is current (2 lines, both occurrences) | yes | EDITORIAL |
| AF-01 guard | [correction required — AF-01] | crossed by loop return edge after the body labels were shortened | [correction — AF-01] | yes | EDITORIAL |
| NF1, NF2, NF4-NF6, AF-01 | Request to complete the active Sprint / Complete the Sprint and return incomplete items to the Product Backlog / Record the Sprint result for reporting / Update the affected items / Repeat the completion request | article / extra words removed (label rule 1) | Request to complete active Sprint / Complete Sprint and return incomplete items to Product Backlog / Record Sprint result for reporting / Update affected items / Repeat completion request | yes | EDITORIAL |
| header | no Final nodes comment | 2 finals | F1/F2 added | yes | EDITORIAL |
| Leader edit (post-agent) | (agent label) | Label shortened further after the agent pass to meet the 2–7 word / 2-line target; see auto label table. | see auto label table | yes | EDITORIAL |

Final nodes: F1 = completion rejected, Sprint unchanged (EX-01); F2 = Sprint completed, incomplete items returned, result recorded (POST1-POST3).

Ghi chú: Now >= 6 pt (was 5.5). NF2/NF3 still drawn twice inside the AF-01 loop because AF-01.2 re-performs NF1 and 'repeat while' is not allowed; semantics unchanged.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Request to complete the active Sprint | Request to complete active Sprint |
| NF2 | Display completed and incomplete Sprint work / Display completed and incomplete Sprint work | Display completed and incomplete Sprint work / Display completed and incomplete Sprint work |
| NF3 | Review the final work status and confirm that task data is current / Review the final work status and confirm that task data is current | Review work status and confirm task data / Review work status and confirm task data |
| AF-01.1 | Update the affected items | Update affected items |
| AF-01.2 | Repeat the completion request | Repeat completion request |
| NF4 | Confirm Sprint completion | Confirm Sprint completion |
| EX-01 | Reject the completion because the Sprint state has changed | Reject Sprint completion |
| NF5 | Complete the Sprint and return incomplete items to the Product Backlog | Complete Sprint and return incomplete items to Product Backlog |
| NF6 | Record the Sprint result for reporting | Record Sprint result for reporting |

</details>

### UC-22 Cancel Sprint (`UC-SPRINT-CANCEL`) — READY FOR PEER REVIEW

Kích thước 1023×864 px · 6.4 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | System check 'Sprint still active?' right after NF1, before NF2 (note: 'contradicts a precondition') | YAML: 'completed or cancelled BEFORE THE CANCELLATION IS CONFIRMED' -> state can change while PO decides; check belongs after NF3; precondition note stale | check moved after 'Confirm cancellation' (NF3), before NF4 | no (timing of the check changed) | MODEL CORRECTION |
| EX-01 | Reject the cancellation because the Sprint is no longer active | cause in label | Reject Sprint cancellation; guard [completed or cancelled — EX-01] | yes | EDITORIAL |
| NF4 | Cancel the Sprint and return incomplete items to the Product Backlog (3 lines) | two actions in one box; width | Cancel active Sprint (POST1) + Return incomplete items to Product Backlog (POST2, BR-SPRINT-INCOMPLETE-RETURN-BACKLOG) | yes | EDITORIAL |
| AF-01.1 | action 'Cancel the confirmation' in PO lane | actor choice is the decision outcome (brief: confirm/cancel are decisions); removing it keeps diagram >= 6 pt | drawn by guard [continue Sprint — AF-01]; header note; AF-01.2 'Leave Sprint unchanged' kept | yes | EDITORIAL |
| NF1, NF2, NF5 | Request Sprint cancellation and provide a reason / Display the impact on selected and completed work / Record the cancellation reason and timestamp | article / extra words removed (label rule 1) | Request Sprint cancellation and provide reason / Display impact on selected and completed work / Record cancellation reason and timestamp | yes | EDITORIAL |

Final nodes: F1 = Sprint cancelled, items returned, reason/timestamp recorded (POST1, POST2); F2 = Sprint unchanged (EX-01 rejection and AF-01 continuation merged).

Ghi chú: 'Cancel Sprint' alone equals the UC name and fails validate (title in diagram), hence 'Cancel active Sprint'.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Request Sprint cancellation and provide a reason | Request Sprint cancellation and provide reason |
| NF2 | Display the impact on selected and completed work | Display impact on selected and completed work |
| NF3 | Confirm the cancellation | Confirm cancellation |
| NF4 | Cancel the Sprint and return incomplete items to the Product Backlog | Cancel active Sprint / Return incomplete items to Product Backlog |
| NF5 | Record the cancellation reason and timestamp | Record cancellation reason and timestamp |
| EX-01 | Reject the cancellation because the Sprint is no longer active | Reject Sprint cancellation |
| AF-01.2 | Leave the Sprint unchanged | Leave Sprint unchanged |
| AF-01.1 | Cancel the confirmation | — |

</details>

### UC-23 Review Sprint Board (`UC-SPRINT-BOARD-REVIEW`) — READY FOR PEER REVIEW

Kích thước 812×757 px · 8.1 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1 | Open the Sprint Board | article | Open Sprint Board | yes | EDITORIAL |
| NF2 | Load the active Sprint and its work items | article | Load active Sprint and its work items | yes | EDITORIAL |
| NF3 | Group the items by their current workflow status | articles/pronoun | Group items by current workflow status | yes | EDITORIAL |
| EX-01 | Report that the Sprint Board cannot be loaded at this time | Technical/data-unavailable failure with no response in UC; policy (c) forbids an invented Report action | removed; guard [unavailable — EX-01] goes to shared final F2 | no (invented action removed) | MODEL CORRECTION |
| EX-01 | separate final for EX-01 | EX-01 and AF-01 share the outcome 'current board not shown, no data changed' | merged into F2 with AF-01 | yes | MODEL CORRECTION |
| NF4 path | shared final with AF-01 | POST1 holds only on NF4 path; restructured main flow into then-branch with own final F1 | F1 = board displayed | yes | MODEL CORRECTION |
| AF-01 | manifest observation 'AF-01 contradicts a precondition' | Stale: the only precondition is active membership; AF-01 is consistent | kept AF-01 branch as drawn | yes | EDITORIAL |
| AF-01.2 guard | [not available] | complementary guard | kept | yes | EDITORIAL |

Final nodes: F1 = current Sprint Board displayed (POST1); F2 = current board not displayed, no data changed (AF-01 no active Sprint, EX-01 data unavailable).

NEEDS CLARIFICATION — EX-01: What does the User see when Sprint data is temporarily unavailable? Đề xuất cho spec: "EX-01: The board cannot be loaded because Sprint data is temporarily unavailable; the system informs the User that the Sprint Board is temporarily unavailable."

Ghi chú: EX-01 now ends silently per exception policy (c); clarification recorded.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the Sprint Board | Open Sprint Board |
| NF2 | Load the active Sprint and its work items | Load active Sprint and its work items |
| NF3 | Group the items by their current workflow status | Group items by current workflow status |
| NF4 | Display item priority, assignee, estimate and status | Display item priority, assignee, estimate and status |
| AF-01.1 | Display that no Sprint is active | Display that no Sprint is active |
| AF-01.2 | Offer access to previous Sprint information | Offer access to previous Sprint information |
| EX-01 | Report that the Sprint Board cannot be loaded at this time | — |

</details>

### UC-24.1 View Sprint Task (`UC-SPRINT-TASK-VIEW`) — READY FOR PEER REVIEW

Kích thước 488×453 px · 10.5 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1 | Select a Sprint Task | article | Select Sprint Task | yes | EDITORIAL |
| NF2 | Retrieve the task details, assignment, dependencies and activity summary | article | Retrieve task details, assignment, dependencies and activity summary | yes | EDITORIAL |
| NF3 | Display the Sprint Task | article | Display Sprint Task | yes | EDITORIAL |
| EX-01 | Report that the selected Sprint Task is no longer available | Action + cause in one box; 'Report …' is not described by the YAML (rule 10) | guard [no longer available — EX-01] → Activity Final, no action (policy c, same reading as UC-15.1) | yes (outcome: task not displayed) | MODEL CORRECTION |
| EX-01 decision | Task available? | clarify concurrency meaning | Task still available? | yes | EDITORIAL |
| structure | exception in else above a bypass | layout pattern: main flow in then-branch | main flow in then, EX-01 in else with own final | yes | EDITORIAL |

Final nodes: F1 = Sprint Task displayed (POST1); F2 = task not displayed, no longer available (EX-01).

NEEDS CLARIFICATION — EX-01: Does 'no longer available' mean the task was removed (state rejection) or that its data temporarily cannot be retrieved? Đề xuất cho spec: "EX-01: The selected Sprint Task has been removed; the system informs the User that the task is no longer available."

Ghi chú: Leader changed EX-01 to policy (c) for consistency with UC-15.1; the BA must state whether EX-01 is a removal (would become 'Reject …') or a retrieval failure.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a Sprint Task | Select Sprint Task |
| NF2 | Retrieve the task details, assignment, dependencies and activity summary | Retrieve task details, assignment, dependencies and activity summary |
| NF3 | Display the Sprint Task | Display Sprint Task |
| EX-01 | Report that the selected Sprint Task is no longer available | — |

</details>

### UC-24.2 Create Sprint Task (`UC-SPRINT-TASK-CREATE`) — READY FOR PEER REVIEW

Kích thước 728×913 px · 8.9 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-01 (new in YAML) | (missing) | validate reported AF-01 not represented | while [invalid — AF-01]: Identify missing or invalid task information (AF-01.1) -> Developer: Correct and resubmit information (AF-01.2); exit [valid] | n/a (new flow) | MODEL CORRECTION |
| NF4 | Validate the Sprint Task | validation object is the submitted information | Validate task information | yes | EDITORIAL |
| NF1/NF2/NF3 | Choose to create a task for a Sprint Backlog Item / Request the task title... / Provide the task information... | articles | Choose to create task for Sprint Backlog Item / Request task title and initial work details / Provide task information and confirm creation | yes | EDITORIAL |
| EX-01 decision | Does the related Product Backlog Item still belong to the active Sprint? | 3-line question | Backlog Item still in active Sprint?; guards [still in Sprint] / [no longer in active Sprint — EX-01] | yes | EDITORIAL |
| EX-01 | Reject the task creation | article; add BR that forbids it | Reject Sprint Task creation [EX-01, BR-SPRINT-TASK-ACTIVE-SPRINT, GUIDE-7.3] | yes | EDITORIAL |
| NF4/POST | Store the Sprint Task for the selected Product Backlog Item / Record the creation in work item activity | articles | Store Sprint Task for selected Product Backlog Item / Record creation in work item activity | yes | EDITORIAL |
| manifest obs. | 'outcome when task information is invalid is not specified' | Stale: AF-01 now specifies it | resolved by AF-01 loop | yes | EDITORIAL |
| header | no Final nodes line | two finals need explanation | added | yes | EDITORIAL |

Final nodes: F1 = Sprint Task created and recorded (postconditions met); F2 = creation rejected, no task created (EX-01).

Ghi chú: Loop guard shortened to [invalid — AF-01] (question carries 'missing or invalid') to keep the return edge clear of the label; loop exit crossing the body lines is the known PlantUML limitation.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Choose to create a task for a Sprint Backlog Item | Choose to create task for Sprint Backlog Item |
| NF2 | Request the task title and initial work details | Request task title and initial work details |
| NF3 | Provide the task information and confirm creation | Provide task information and confirm creation |
| NF4 | Validate the Sprint Task / Store the Sprint Task for the selected Product Backlog Item | Validate task information / Store Sprint Task for selected Product Backlog Item |
| AF-01.1 | — | Identify missing or invalid task information |
| AF-01.2 | — | Correct and resubmit information |
| POST2 | Record the creation in work item activity | Record creation in work item activity |
| EX-01 | Reject the task creation | Reject Sprint Task creation |

</details>

### UC-24.3 Update Sprint Task (`UC-SPRINT-TASK-UPDATE`) — READY FOR PEER REVIEW

Kích thước 895×811 px · 7.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the update because the task is no longer in the active Sprint | action + cause in one box | guard [no longer in active Sprint — EX-01] + Reject Sprint Task update | yes | EDITORIAL |
| EX-01 decision | $question_x("Task still in the active Sprint?") | _x used although flow enters from same lane | $question("Task still in active Sprint?") | yes | EDITORIAL |
| NF1-NF4, AF-01.1 | Open a Sprint Task..., Display the editable..., Update the desired values and submit the task, Validate the changes, Save the changes, Record the update..., Discard the unsaved task changes | articles / vague object | Open Sprint Task for editing, Display editable task information, Update desired values and submit task, Validate task changes, Save task changes, Record update in work item activity, Discard unsaved task changes | yes | EDITORIAL |
| final | \|DEV\| before stop | shared 'task unchanged' final placed in actor lane | \|SYS\| before stop (merge diamond still drawn in Developer lane by PlantUML) | yes | EDITORIAL |

Final nodes: F1 = changes saved and recorded (postconditions met); F2 = task unchanged (EX-01 rejected, AF-01 cancelled).

Ghi chú: Merge node for F2 is placed by PlantUML in the Developer lane; not semantically wrong.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open a Sprint Task for editing | Open Sprint Task for editing |
| NF2 | Display the editable task information | Display editable task information |
| NF3 | Update the desired values and submit the task | Update desired values and submit task |
| NF4 | Validate the changes / Save the changes | Validate task changes / Save task changes |
| POST2 | Record the update in work item activity | Record update in work item activity |
| EX-01 | Reject the update because the task is no longer in the active Sprint | Reject Sprint Task update |
| AF-01.1 | Discard the unsaved task changes | Discard unsaved task changes |

</details>

### UC-24.4 Assign Sprint Task (`UC-SPRINT-TASK-ASSIGN`) — READY FOR PEER REVIEW

Kích thước 899×680 px · 7.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the assignment to the inactive member | cause in box | guard [assignee no longer active — EX-01] + Reject task assignment | yes | EDITORIAL |
| structure | EX-01 in else above, main flow after endif | layout pattern | main flow in then-branch, EX-01 in else | yes | EDITORIAL |
| NF1/NF3/NF4/AF-01.1 | Open the task assignment control / Select an assignee and confirm the assignment / Save the assignment and record the change / Mark the Sprint Task as unassigned | articles | Open task assignment control / Select assignee and confirm assignment / Save assignment and record change / Mark Sprint Task as unassigned | yes | EDITORIAL |
| header | no Final nodes line | three finals with different outcomes need explanation | added | yes | EDITORIAL |

Final nodes: F1 = assignment saved and recorded (postconditions met); F2 = assignment rejected, unchanged (EX-01); F3 = assignment cleared, task unassigned (AF-01).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the task assignment control | Open task assignment control |
| NF2 | Display eligible Developers | Display eligible Developers |
| NF3 | Select an assignee and confirm the assignment | Select assignee and confirm assignment |
| NF4 | Save the assignment and record the change | Save assignment and record change |
| EX-01 | Reject the assignment to the inactive member | Reject task assignment |
| AF-01.1 | Mark the Sprint Task as unassigned | Mark Sprint Task as unassigned |

</details>

### UC-24.5 Delete Sprint Task (`UC-SPRINT-TASK-DELETE`) — READY FOR PEER REVIEW

Kích thước 1076×884 px · 6.1 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-02 (new in YAML) | (missing; confirmation had no decline path) | validate reported AF-02 not represented | Developer decision Confirm deletion? [confirm] -> Confirm deletion (NF3); [cancel — AF-02] -> System: Leave Sprint Task unchanged (AF-02.1) -> shared F2 | n/a (new flow) | MODEL CORRECTION |
| EX-01 | Reject the deletion of the started task | cause in box | Reject Sprint Task deletion (guard [in execution — EX-01]) | yes | EDITORIAL |
| EX-01 decision | Task already in execution? | polarity | Task execution started? | yes | EDITORIAL |
| AF-01 decision | Other tasks depend on it? [no dependent tasks] | short complementary guard | Dependent tasks exist? [none] | yes | EDITORIAL |
| AF-01.1 | Require the dependencies to be removed before deletion | 3 lines, too wide (pt 5.0) | Require dependency removal first | yes ('first' = before deletion) | EDITORIAL |
| NF1/NF2/NF4 | Select a Sprint Task and request deletion / Display the dependency impact... / Delete the task and record the action | articles | Select Sprint Task and request deletion / Display dependency impact and ask for confirmation / Delete task and record action | yes | EDITORIAL |
| manifest obs. | 'EX-01 contradicts a precondition' / 'no decline path' | Stale: preconditions no longer require an unstarted task; AF-02 now provides the decline path | EX-01 drawn as a normal state rejection | yes | EDITORIAL |

Final nodes: F1 = task deleted and recorded (postconditions met); F2 = task unchanged (AF-02 cancelled, AF-01 dependencies must be removed first, EX-01 rejected).

Ghi chú: Width driven by three nested side branches; labels wrapped to reach 6.1 pt.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a Sprint Task and request deletion | Select Sprint Task and request deletion |
| NF2 | Display the dependency impact and ask for confirmation | Display dependency impact and ask for confirmation |
| NF3 | Confirm deletion | Confirm deletion |
| NF4 | Delete the task and record the action | Delete task and record action |
| AF-02.1 | — | Leave Sprint Task unchanged |
| AF-01.1 | Require the dependencies to be removed before deletion | Require dependency removal first |
| EX-01 | Reject the deletion of the started task | Reject Sprint Task deletion |

</details>

### UC-24.6 Add Task Dependency (`UC-TASK-DEPENDENCY-ADD`) — READY FOR PEER REVIEW

Kích thước 805×717 px · 8.1 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the dependency that would create a cycle | cause in box | guard [direct or indirect cycle — EX-01] + Reject task dependency | yes | EDITORIAL |
| EX-02 | Reject the dependency of the task on itself | cause in box | guard [same task — EX-02] + Reject task dependency | yes | EDITORIAL |
| NF1-NF4 | Open a Sprint Task and choose to add a dependency / Display eligible tasks in the same project / Select the dependency target and confirm the relationship / Validate the dependency / Store the dependency | articles | Open Sprint Task and choose to add dependency / Display eligible tasks in same project / Select dependency target and confirm relationship / Validate task dependency / Store task dependency | yes | EDITORIAL |

Final nodes: F1 = dependency stored (postconditions met); F2 = dependency rejected, nothing stored (EX-01, EX-02).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open a Sprint Task and choose to add a dependency | Open Sprint Task and choose to add dependency |
| NF2 | Display eligible tasks in the same project | Display eligible tasks in same project |
| NF3 | Select the dependency target and confirm the relationship | Select dependency target and confirm relationship |
| NF4 | Validate the dependency / Store the dependency | Validate task dependency / Store task dependency |
| EX-01 | Reject the dependency that would create a cycle | Reject task dependency |
| EX-02 | Reject the dependency of the task on itself | Reject task dependency |

</details>

### UC-24.7 Remove Task Dependency (`UC-TASK-DEPENDENCY-REMOVE`) — READY FOR PEER REVIEW

Kích thước 931×806 px · 7.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Report that the dependency was already removed | Report action not described by UC; concurrent removal by another User is a state rejection, policy (b) | Reject dependency removal (guard [already removed — EX-01]) | yes | EDITORIAL |
| NF1/NF2/NF3/NF5/AF-01.1 | Open a Sprint Task and select an existing dependency / Request removal of the dependency / Request confirmation and display the affected tasks / Remove the relationship and record the change / Leave the dependency unchanged | articles | Open Sprint Task and select existing dependency / Request dependency removal / Request confirmation and display affected tasks / Remove relationship and record change / Leave dependency unchanged | yes | EDITORIAL |
| final | \|DEV\| before stop | shared final in actor lane | \|SYS\| before stop | yes | EDITORIAL |

Final nodes: F1 = dependency removed and recorded (postconditions met); F2 = no removal by this use case (EX-01 rejected, AF-01 cancelled).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open a Sprint Task and select an existing dependency | Open Sprint Task and select existing dependency |
| NF2 | Request removal of the dependency | Request dependency removal |
| NF3 | Request confirmation and display the affected tasks | Request confirmation and display affected tasks |
| NF4 | Confirm removal | Confirm removal |
| NF5 | Remove the relationship and record the change | Remove relationship and record change |
| EX-01 | Report that the dependency was already removed | Reject dependency removal |
| AF-01.1 | Leave the dependency unchanged | Leave dependency unchanged |

</details>

### UC-25 Claim Sprint Task (`UC-SPRINT-TASK-CLAIM`) — READY FOR PEER REVIEW

Kích thước 552×502 px · 10.5 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| whole diagram | (no source; previously BLOCKED: AF-01 referred to a non-existent confirmation step) | YAML revised: AF list now empty, NF1-NF4 + EX-01 consistent with preconditions and BRs | new source created: NF1 (Developer) -> NF2 Verify task is active and still unassigned -> decision Task still unassigned? -> NF3 Assign task to Developer -> NF4 Update Sprint Board and record assignment; [claimed by another Developer — EX-01] -> Reject task claim | n/a (new diagram) | MODEL CORRECTION |
| NF2 'active' part | Verify task is active and still unassigned | UC defines no outcome when the task is not active (precondition guarantees it); no branch drawn | kept as one verification action; only EX-01 branches | yes | NEEDS CLARIFICATION |

Final nodes: F1 = task assigned to the Developer and recorded (postconditions met); F2 = claim rejected, another Developer claimed it first (EX-01).

NEEDS CLARIFICATION — NF2: What happens if NF2 finds the task is no longer active (e.g. removed from the Sprint between selection and claim)? Đề xuất cho spec: "EX-02: The task is no longer active in the Sprint; the system rejects the claim."

Ghi chú: Unblocked: the current YAML is consistent and complete enough to draw. Developer lane (trigger + BR-SPRINT-TASK-DEVELOPER). Previously BLOCKED; PR #8 (commit 8d5ecf2) resolved the YAML, so the diagram is now drawn.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | — | Open unassigned task and choose to claim it |
| NF2 | — | Verify task is active and still unassigned |
| NF3 | — | Assign task to Developer |
| NF4 | — | Update Sprint Board and record assignment |
| EX-01 | — | Reject task claim |

</details>

### UC-26 Update Work Item Status (`UC-WORK-ITEM-STATUS-UPDATE`) — READY FOR PEER REVIEW

Kích thước 821×791 px · 8.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-01.3 (new in YAML) | (loop returned to the condition without re-validation) | AF-01.3 'validates the requested transition again' not traced | loop body ends with System: Validate requested transition again [AF-01.3, BR-WORK-ITEM-STATUS] | n/a (new step) | MODEL CORRECTION |
| EX-01 | Reject the change to the unavailable status | cause in box | guard [no longer available — EX-01] + Reject status change [EX-01, BR-WORK-ITEM-STATUS, GUIDE-7.3] | yes | EDITORIAL |
| structure | EX-01 in else above, main flow after endif | layout pattern | main flow in then-branch | yes | EDITORIAL |
| NF1/NF2/NF3/NF4/AF-01.1/AF-01.2 | Select a new status or move the card... / Validate the requested transition... / Identify the missing information / Complete the information or choose another status / Update the work item status / Refresh the Sprint Board and record the change | articles | Select new status or move card to another workflow column / Validate requested transition and actor permission / Identify missing information / Complete information or choose another status / Update work item status / Refresh Sprint Board and record change | yes | EDITORIAL |
| manifest obs. | 'YAML does not say whether NF2 validation is repeated' | Stale: AF-01.3 now says it is | resolved | yes | EDITORIAL |
| header | no Final nodes line | two finals | added | yes | EDITORIAL |
| Leader edit (post-agent) | (agent label) | Label shortened further after the agent pass to meet the 2–7 word / 2-line target; see auto label table. | see auto label table | yes | EDITORIAL |

Final nodes: F1 = status updated, board refreshed, change recorded (postconditions met); F2 = status change rejected, status unchanged (EX-01).

Ghi chú: Loop exit crossing the body edges is the known PlantUML limitation.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a new status or move the card to another workflow column | Select new status or move card |
| NF2 | Validate the requested transition and actor permission | Validate requested transition and actor permission |
| AF-01.1 | Identify the missing information | Identify missing information |
| AF-01.2 | Complete the information or choose another status | Complete information or choose another status |
| AF-01.3 | — | Validate requested transition again |
| NF3 | Update the work item status | Update work item status |
| NF4 | Refresh the Sprint Board and record the change | Refresh Sprint Board and record change |
| EX-01 | Reject the change to the unavailable status | Reject status change |

</details>

### UC-27.1 View Subtasks (`UC-SUBTASKS-VIEW`) — READY FOR PEER REVIEW

Kích thước 519×450 px · 10.5 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1/NF2/AF-01.1 | Open a Sprint Task's subtask section / Retrieve the existing subtasks / Display the existing subtasks / Display an empty subtask list | articles | Open Sprint Task's subtask section / Retrieve existing subtasks / Display existing subtasks / Display empty subtask list | yes | EDITORIAL |

Final nodes: single final (both paths display the current subtask state, POST1).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open a Sprint Task's subtask section | Open Sprint Task's subtask section |
| NF2 | Retrieve the existing subtasks / Display the existing subtasks | Retrieve existing subtasks / Display existing subtasks |
| AF-01.1 | Display an empty subtask list | Display empty subtask list |

</details>

### UC-27.2 Create Subtask (`UC-SUBTASK-CREATE`) — READY FOR PEER REVIEW

Kích thước 637×653 px · 10.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the subtask below another subtask | cause in box | guard [parent is a subtask — EX-01] + Reject subtask creation | yes | EDITORIAL |
| EX-01 decision | Parent is itself a subtask? [Sprint Task] | question polarity did not match then-guard | Parent is a Sprint Task? [Sprint Task] | yes | EDITORIAL |
| structure | EX-01 in else above, main flow after endif | layout pattern | main flow in then-branch | yes | EDITORIAL |
| NF1-NF4 | Open a Sprint Task and choose to add a subtask / Request the subtask's work details... / Provide the information... / Validate the subtask / Store and display the new subtask | articles | Open Sprint Task and choose to add subtask / Request subtask's work details and optional assignee / Provide information and confirm creation / Validate subtask / Store and display new subtask | yes | EDITORIAL |
| header | no Final nodes line | two finals | added | yes | EDITORIAL |

Final nodes: F1 = subtask created, parent progress recalculated (postconditions met); F2 = creation rejected (EX-01).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open a Sprint Task and choose to add a subtask | Open Sprint Task and choose to add subtask |
| NF2 | Request the subtask's work details and optional assignee | Request subtask's work details and optional assignee |
| NF3 | Provide the information and confirm creation | Provide information and confirm creation |
| NF4 | Validate the subtask / Store and display the new subtask | Validate subtask / Store and display new subtask |
| POST2 | Recalculate parent-task progress | Recalculate parent-task progress |
| EX-01 | Reject the subtask below another subtask | Reject subtask creation |

</details>

### UC-27.3 Update Subtask (`UC-SUBTASK-UPDATE`) — READY FOR PEER REVIEW

Kích thước 941×935 px · 7.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the update because the parent task left the active Sprint | cause in box | guard [no longer in active Sprint — EX-01] + Reject subtask update | yes | EDITORIAL |
| EX-01 decision | $question_x("Parent still in the active Sprint?") | _x used although flow enters from same lane | $question("Parent still in active Sprint?") | yes | EDITORIAL |
| NF1-NF4, AF-01.1 | Open a subtask for editing / Display its current editable values / Revise the information and submit the subtask / Validate the changes / Save the changes / Keep the subtask unchanged | articles, vague pronoun/object | Open subtask for editing / Display current editable values / Revise information and submit subtask / Validate subtask changes / Save subtask changes / Keep subtask unchanged | yes | EDITORIAL |
| final | \|DEV\| before stop | shared final in actor lane | \|SYS\| before stop | yes | EDITORIAL |

Final nodes: F1 = changes saved (postconditions met); F2 = subtask unchanged (EX-01 rejected, AF-01 cancelled).

Ghi chú: POST2 'when relevant' kept as decision Parent progress affected?

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open a subtask for editing | Open subtask for editing |
| NF2 | Display its current editable values | Display current editable values |
| NF3 | Revise the information and submit the subtask | Revise information and submit subtask |
| NF4 | Validate the changes / Save the changes | Validate subtask changes / Save subtask changes |
| POST2 | Recalculate parent-task progress | Recalculate parent-task progress |
| EX-01 | Reject the update because the parent task left the active Sprint | Reject subtask update |
| AF-01.1 | Keep the subtask unchanged | Keep subtask unchanged |

</details>

### UC-27.4 Complete Subtask (`UC-SUBTASK-COMPLETE`) — READY FOR PEER REVIEW

Kích thước 903×567 px · 7.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| whole diagram | (no source; previously BLOCKED: AF-01 restore conflicted with precondition 'subtask is not already complete') | YAML revised: precondition removed, AF-01 now has validation step AF-01.1; spec consistent | new source created: Developer decision Requested status change? [mark complete] NF1 / [restore to incomplete — AF-01]; merge -> Validate requested status change [NF2, AF-01.1] -> Sprint still active? -> Record requested status and recalculate parent-task progress [NF3, AF-01.2, POST1, POST2]; [Sprint completed — EX-01] -> Reject subtask status change | n/a (new diagram) | MODEL CORRECTION |
| NF3 / AF-01.2 | (two YAML steps) | identical System behaviour for the requested status; drawing them separately would need a second decision on the same choice | one shared action 'Record requested status and recalculate parent-task progress' (explained in header) | yes | EDITORIAL |

Final nodes: F1 = subtask has requested completion status, parent progress recalculated (postconditions met); F2 = status change rejected, subtask unchanged (EX-01).

Ghi chú: Unblocked: current YAML consistent. EX-01 treated as state rejection (policy b) with BR-SPRINT-TASK-ACTIVE-SPRINT. Previously BLOCKED; PR #8 (commit 8d5ecf2) resolved the YAML, so the diagram is now drawn.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | — | Select incomplete subtask and mark it complete |
| AF-01 | — | Restore completed subtask to incomplete |
| NF2 | — | Validate requested status change |
| NF3 | — | Record requested status and recalculate parent-task progress |
| EX-01 | — | Reject subtask status change |

</details>

### UC-27.5 Delete Subtask (`UC-SUBTASK-DELETE`) — READY FOR PEER REVIEW

Kích thước 936×729 px · 7.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Reject the deletion because the subtask was completed or the Sprint ended | cause in box, 4 lines | guard [completed or Sprint ended — EX-01] + Reject subtask deletion | yes | EDITORIAL |
| NF1/NF4/AF-01.1 | Select an incomplete subtask and request deletion / Remove the subtask and recalculate parent-task progress / Leave the subtask unchanged | articles | Select incomplete subtask and request deletion / Remove subtask and recalculate parent-task progress / Leave subtask unchanged | yes | EDITORIAL |
| final | \|DEV\| before stop | shared final in actor lane | \|SYS\| before stop | yes | EDITORIAL |

Final nodes: F1 = subtask removed, parent progress recalculated (postconditions met); F2 = subtask unchanged (EX-01 rejected, AF-01 cancelled).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select an incomplete subtask and request deletion | Select incomplete subtask and request deletion |
| NF2 | Request confirmation | Request confirmation |
| NF3 | Confirm deletion | Confirm deletion |
| NF4 | Remove the subtask and recalculate parent-task progress | Remove subtask and recalculate parent-task progress |
| EX-01 | Reject the deletion because the subtask was completed or the Sprint ended | Reject subtask deletion |
| AF-01.1 | Leave the subtask unchanged | Leave subtask unchanged |

</details>

### UC-28 Comment on Work Item (`UC-WORK-ITEM-COMMENT`) — READY FOR PEER REVIEW

Kích thước 850×1254 px · 6.5 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1-NF6 | long labels with articles | rule 1/2 | Open work item and enter comment; Validate comment and referenced members; Submit comment; Save comment and record it in activity history; Create in-app notifications for relevant members; Request email delivery for eligible members | yes | EDITORIAL |
| AF-01 | empty content handled as a branch | AF-01.1 says the system asks for content, then the actor re-enters it | loop 'Comment has no content?' [empty — AF-01]: Ask actor to enter comment content → Enter comment content | yes | EDITORIAL |
| EX-01 | no explicit response | work item removed = state rejection (policy b) | guard [removed — EX-01] + Reject comment [GUIDE-7.3] | yes | EDITORIAL |
| EX-02 | — | response explicit in YAML (policy a) | Email Service: Return delivery result; [not delivered — EX-02] Record failed email delivery | yes | EDITORIAL |

Final nodes: F1 = comment saved, postconditions met (EX-02 does not change this outcome, BR-NOTIFICATION-DELIVERY-INDEPENDENT); F2 = comment rejected, work item removed (EX-01).

Ghi chú: 6.5 pt; loop-body label kept on one line to keep the return edge off the guard text.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open a work item and enter a comment / Enter the comment content | Open work item and enter comment / Enter comment content |
| NF2 | Validate the comment and referenced members | Validate comment and referenced members |
| AF-01.1 | Ask the actor to enter content | Ask actor to enter comment content |
| NF3 | Submit the comment | Submit comment |
| NF4 | Save the comment and record it in activity history | Save comment and record it in activity history |
| NF5 | Create in-app notifications for relevant members / Request email delivery for eligible members | Create in-app notifications for relevant members / Request email delivery for eligible members |
| NF6 | Return the email delivery result | Return delivery result |
| EX-02 | Record the failed delivery and keep the saved comment | Record failed email delivery |
| EX-01 | Reject the comment because the work item was removed | Reject comment |

</details>

### UC-29 Review Work Item Activity (`UC-WORK-ITEM-ACTIVITY-REVIEW`) — READY FOR PEER REVIEW

Kích thước 707×646 px · 9.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1-NF4 | long labels | rule 1/2 | Request work item activity history; Retrieve entries in reverse chronological order; Display events with actor, time and change summary; Review activity history | yes | EDITORIAL |
| AF-01 | — | creation-only history | [creation only — AF-01] Display creation event only | yes | EDITORIAL |
| EX-01 | explicit 'report' action | retrieval failure, no response in YAML (policy c) | [cannot be retrieved — EX-01] → final, no action | yes (outcome: history not displayed) | MODEL CORRECTION |

Final nodes: F1 = activity history reviewed (NF3 or AF-01, then NF4); F2 = history not retrieved, nothing displayed (EX-01).

NEEDS CLARIFICATION — EX-01: Is the User informed when activity data cannot be retrieved? Đề xuất cho spec: "EX-01: Activity data cannot be retrieved; the system informs the User that the activity history is temporarily unavailable."

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Request the activity history for a work item | Request work item activity history |
| NF2 | Retrieve the activity entries in reverse chronological order | Retrieve entries in reverse chronological order |
| NF3 | Display each event with its actor, time and change summary | Display events with actor, time and change summary |
| AF-01.1 | Display only the creation event | Display creation event only |
| NF4 | Review the displayed history | Review activity history |
| EX-01 | Report that the activity history cannot be retrieved | — |

</details>

### UC-30 Review Notifications (`UC-NOTIFICATIONS-REVIEW`) — READY FOR PEER REVIEW

Kích thước 1089×1026 px · 6.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1-NF3, AF-01 | long labels | rule 1/2 | Open notification center; Display notifications and email preference, newest first; Select a notification; Mark as read and display project context; Mark all visible notifications as read | yes | EDITORIAL |
| EX-01 / BR-PROJECT-MEMBER-ACCESS | — | permission refusal (policy b) | [inaccessible — EX-01] Deny access to related item | yes | EDITORIAL |
| AF-02, EX-03 | cause inside the action | condition belongs in guards (rule 3) | Check verified email when enabling (AF-02.1) → 'Change permitted?' [enabling, not verified — EX-03] Reject preference change | yes | EDITORIAL |
| EX-02 | both branches of 'Preference saved?' merged with no action between | degenerate decision; save failure has no described response (policy c) | [not saved — EX-02] → own final, no action | yes (previous preference remains) | MODEL CORRECTION |

Final nodes: F1 = preference not saved, previous preference remains (EX-02); F2 = shared final for all other paths.

NEEDS CLARIFICATION — EX-02: Is the User informed that the email delivery preference could not be saved? Đề xuất cho spec: "EX-02: The email delivery preference cannot be saved; the previous preference remains unchanged and the system informs the User that the change was not saved."

Ghi chú: 6.0 pt — right at the threshold; columns narrowed to 3-line labels.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the notification center | Open notification center |
| NF2 | Display the actor's notifications and email delivery preference in reverse chronological order | Display notifications and email preference, newest first |
| NF3 | Select a notification to review | Select a notification |
| NF4 | Mark it as read and display its related project context | Mark as read and display project context |
| EX-01 | Report that the related project item is no longer accessible | Deny access to related item |
| AF-01.1 | Mark all visible notifications as read | Mark all visible notifications as read |
| AF-02.1 | Verify that the actor has a verified email address when email delivery is enabled | Check verified email when enabling |
| AF-02.2 | Save the updated email delivery preference | Save email delivery preference |
| EX-03 | Reject the change and keep the previous preference | Reject preference change |
| EX-02 | Keep the previous preference and report the failure | — |

</details>

### UC-31 Monitor Sprint Progress (`UC-SPRINT-PROGRESS-MONITOR`) — READY FOR PEER REVIEW

Kích thước 588×792 px · 10.3 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| NF1-NF4 | long labels | rule 1/2 | Open Sprint progress view; Aggregate work item status and estimates; Calculate completion, remaining work, overdue items and member workload; Display Sprint indicators and charts | yes | EDITORIAL |
| AF-01 | — | missing estimates | [estimates missing — AF-01] Label estimate-based measures as incomplete | yes | EDITORIAL |
| EX-01 | 'contradicts a precondition' defensive Reject | no active Sprint is a data state with no described response (policy c) | [no active Sprint — EX-01] → final, no action | yes (nothing displayed) | MODEL CORRECTION |

Final nodes: F1 = Sprint indicators displayed (also after AF-01); F2 = no active Sprint, no progress calculated (EX-01, BR-PROGRESS-ACTIVE-SPRINT).

NEEDS CLARIFICATION — EX-01: What does the User see when the selected project has no active Sprint? Đề xuất cho spec: "EX-01: No active Sprint exists for the selected project; the system informs the User that there is no active Sprint to monitor."

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the active Sprint progress view | Open Sprint progress view |
| NF2 | Aggregate current work item status and estimate data | Aggregate work item status and estimates |
| NF3 | Calculate completion, remaining work, overdue items and member workload | Calculate completion, remaining work, overdue items and member workload |
| AF-01.1 | Label estimate-based measures as incomplete | Label estimate-based measures as incomplete |
| NF4 | Display the resulting Sprint indicators and charts | Display Sprint indicators and charts |
| EX-01 | Report that no active Sprint exists for the project | — |

</details>

### UC-32.1 Search and View User Accounts (`UC-USER-ACCOUNTS-SEARCH`) — READY FOR PEER REVIEW

Kích thước 687×948 px · 8.6 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| AF-01.2 | (not drawn; AF-01 ended the use case) | YAML now says the administrator may change the criteria and search again. | loop: while "No matching account?" [no match — AF-01] -> Report no matching account -> decision "Search again?" ([no — AF-01] -> F1 / [search again — AF-01] -> Change search criteria and search again) -> back | no (new flow from YAML) | MODEL CORRECTION |
| EX-01 | Report that account administration data is temporarily unavailable [EX-01, GUIDE-7.3] | Data unavailable with no described response: no action (policy c). | no action: [temporarily unavailable — EX-01] -> F3 | yes | MODEL CORRECTION |
| AF-01.1 | Report that no matching account was found | Article/length. | Report no matching account | yes | EDITORIAL |
| Labels | Select an account; Display its administrative status and relevant account metadata | Articles. | Select account; Display administrative status and relevant account metadata | yes | EDITORIAL |

Final nodes: F1 = search ended without a matching account (AF-01); F2 = selected account displayed (POST1); F3 = data unavailable, nothing displayed (EX-01)..

NEEDS CLARIFICATION — EX-01: Is the administrator told that account administration data is unavailable? Đề xuất cho spec: "EX-01: Account administration data is temporarily unavailable; the system informs the System Administrator that accounts cannot be searched at the moment."

Ghi chú: The loop exit "[no — AF-01]" reflects "may" in AF-01.2. EX-01 is checked once after the first search (YAML does not place it). Old manifest observation obsolete.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open user account administration and enter search criteria | Open user account administration and enter search criteria |
| AF-01.1 | Report that no matching account was found | Report no matching account |
| AF-01.2 | — | Change search criteria and search again |
| NF2 | Display matching User accounts | Display matching User accounts |
| NF3 | Select an account | Select account |
| NF4 | Display its administrative status and relevant account metadata | Display administrative status and relevant account metadata |
| EX-01 | Report that account administration data is temporarily unavailable | — |

</details>

### UC-32.2 Suspend User Account (`UC-USER-ACCOUNT-SUSPEND`) — READY FOR PEER REVIEW

Kích thước 942×757 px · 7.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01, EX-02 (manifest observation) | "EX-01 and EX-02 contradict a precondition"; header cited "precondition 3" | Preconditions no longer contain a protected-account clause; EX-01/EX-02 are ordinary business checks (BRs). Header rationale corrected. | one decision [current owner — EX-01 or last administrator — EX-02] (both are target-account protections with the same rejection) | yes | EDITORIAL |
| EX-01, EX-02 | Reject the suspension of the protected account | Cause in the box. | Reject suspension | yes | EDITORIAL |
| AF-01.1 | Leave the account active | Agent removed it as an outcome; leader restored it: the YAML lists it as a System step (same convention as UC-10/11/24.5) | kept as action: 'Leave account active' (AF-01.1 is an explicit System step of the YAML) | yes | EDITORIAL |
| Labels | Select a/an ... account; Provide a reason ...; ... the account and record the audit event | Articles. | ... and request suspension; Provide reason and confirm suspension; Suspend account and record audit event; TRIGGER traced on NF1 | yes | EDITORIAL |

Final nodes: F1 = account suspended, audit recorded (POST1, POST2); F2 = account unchanged (EX-01, EX-02, AF-01)..

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select an active User account and request suspension | Select active User account and request suspension |
| NF2 | Display the impact and request a reason and confirmation | Display impact and request reason and confirmation |
| NF3 | Provide a reason and confirm suspension | Provide reason and confirm suspension |
| NF4 | Suspend the account and record the audit event | Suspend account and record audit event |
| AF-01.1 | Leave the account active | Leave account active |
| EX-01 | Reject the suspension of the protected account | Reject suspension |

</details>

### UC-32.3 Reactivate User Account (`UC-USER-ACCOUNT-REACTIVATE`) — READY FOR PEER REVIEW

Kích thước 958×729 px · 6.8 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | decision "Account deleted?" right after NF1, before NF2 (defensive precondition check) | YAML: the account is deleted before the reactivation is confirmed -> the check belongs after the confirmation (NF3), before NF4. | after "Confirm reactivation": decision "Account still exists?" [deleted — EX-01] -> Reject reactivation | no (moved to the point the YAML describes) | MODEL CORRECTION |
| AF-01.1 | Leave the account suspended | Agent removed it as an outcome; leader restored it: the YAML lists it as a System step (same convention as UC-10/11/24.5) | kept as action: 'Leave account suspended' (AF-01.1 is an explicit System step of the YAML) | yes | EDITORIAL |
| Labels | Select a suspended User account ...; Display the account status ...; Reactivate the account and record the audit event; Reject the reactivation of the deleted account | Articles; cause in box. | Select suspended User account and request reactivation; Display account status and request confirmation; Reactivate account and record audit event; Reject reactivation | yes | EDITORIAL |

Final nodes: F1 = account reactivated, audit recorded (POST1, POST2); F2 = account not reactivated (AF-01 stays suspended, EX-01 deleted)..

Ghi chú: Old manifest observation (EX-01 contradicts precondition) is obsolete with the timing in EX-01.

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a suspended User account and request reactivation | Select suspended User account and request reactivation |
| NF2 | Display the account status and request confirmation | Display account status and request confirmation |
| NF3 | Confirm reactivation | Confirm reactivation |
| NF4 | Reactivate the account and record the audit event | Reactivate account and record audit event |
| EX-01 | Reject the reactivation of the deleted account | Reject reactivation |
| AF-01.1 | Leave the account suspended | Leave account suspended |

</details>

### UC-32.4 Delete User Account (`UC-USER-ACCOUNT-DELETE`) — READY FOR PEER REVIEW

Kích thước 930×757 px · 7.0 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01, EX-02 (manifest observation) | "EX-01 and EX-02 contradict a precondition"; header cited "precondition 3" | Preconditions no longer contain a protected-account clause; EX-01/EX-02 are ordinary business checks (BRs). Header rationale corrected. | one decision [current owner — EX-01 or last administrator — EX-02] (both are target-account protections with the same rejection) | yes | EDITORIAL |
| EX-01, EX-02 | Reject the deletion of the protected account | Cause in the box. | Reject deletion | yes | EDITORIAL |
| AF-01.1 | Leave the account unchanged | Agent removed it as an outcome; leader restored it: the YAML lists it as a System step (same convention as UC-10/11/24.5) | kept as action: 'Leave account unchanged' (AF-01.1 is an explicit System step of the YAML) | yes | EDITORIAL |
| Labels | Select a/an ... account; Provide a reason ...; ... the account and record the audit event | Articles. | ... and request deletion; Provide reason and confirm deletion; Delete account and record audit event; TRIGGER traced on NF1 | yes | EDITORIAL |

Final nodes: F1 = account deleted, audit recorded (POST1, POST2); F2 = account unchanged (EX-01, EX-02, AF-01)..

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Select a User account and request deletion | Select User account and request deletion |
| NF2 | Display ownership, membership and administrative impact | Display ownership, membership and administrative impact |
| NF3 | Provide a reason and confirm deletion | Provide reason and confirm deletion |
| NF4 | Delete the account and record the audit event | Delete account and record audit event |
| AF-01.1 | Leave the account unchanged | Leave account unchanged |
| EX-01 | Reject the deletion of the protected account | Reject deletion |

</details>

### UC-33 Review System Audit Log (`UC-SYSTEM-AUDIT-LOG-REVIEW`) — READY FOR PEER REVIEW

Kích thước 708×776 px · 9.2 pt ở A4 · layout issues: none.

| UC step/BR | Current element | Problem | Proposed element | Same meaning? | Class |
|---|---|---|---|---|---|
| EX-01 | Report that the audit store is temporarily unavailable [EX-01, GUIDE-7.3] | Store unavailable with no described response: no action (policy c). | no action: [temporarily unavailable — EX-01] -> F3 | yes | MODEL CORRECTION |
| Finals | F2 merged NF5 and AF-01 ("review completed") | Different outcomes (events reviewed vs none matched; POST1 does not really hold on AF-01). | F1 reviewed (POST1), F2 no match reported (AF-01) | yes | EDITORIAL |
| Labels | Open the system audit log; Display matching events and their recorded details; Review the results; Report that no matching events were found | Articles. | Open system audit log; Display matching events and recorded details; Review results; Report no matching events | yes | EDITORIAL |

Final nodes: F1 = matching events displayed and reviewed (POST1); F2 = no matching events reported (AF-01); F3 = audit store unavailable (EX-01)..

NEEDS CLARIFICATION — EX-01: Is the administrator informed that the audit store is unavailable? Đề xuất cho spec: "EX-01: The audit store is temporarily unavailable; the system informs the System Administrator that audit events cannot be displayed at the moment."

Ghi chú: BR-SYSADMIN-NO-PROJECT-AUTO-ACCESS does not affect the flow and is not traced to an action (header only).

<details><summary>Nhãn action trước → sau (trích tự động từ source)</summary>

| Ref | Trước | Sau |
|---|---|---|
| NF1 | Open the system audit log | Open system audit log |
| NF2 | Display recent audit events | Display recent audit events |
| NF3 | Filter events by time, actor, event type or target | Filter events by time, actor, event type or target |
| NF4 | Display matching events and their recorded details | Display matching events and recorded details |
| NF5 | Review the results | Review results |
| AF-01.1 | Report that no matching events were found | Report no matching events |
| EX-01 | Report that the audit store is temporarily unavailable | — |

</details>

## 5. UC từng bị BLOCKED — kiểm tra lại

UC-25 `UC-SPRINT-TASK-CLAIM` và UC-27.4 `UC-SUBTASK-COMPLETE` bị BLOCKED ở audit 2026-10-03. YAML hiện tại (sau PR #8, commit `8d5ecf2`) đã nhất quán với precondition và BR, đủ để vẽ, nên cả hai được vẽ mới và **không còn BLOCKED**. Số UC bị chặn hiện tại: **0**. UC-25 vẫn có một câu hỏi NEEDS CLARIFICATION (NF2: task không còn active).

## 6. Danh sách NEEDS CLARIFICATION gửi BA

| UC | Ref | Câu hỏi | Câu đề xuất cho spec |
|---|---|---|---|
| UC-01 | EX-01 | Is the Guest informed that the verification message could not be delivered, and how is verification requested again? | EX-01: The Email Service cannot deliver the verification message; the account remains pending, and the system informs the Guest that the message could not be sent and that verification can be requested again. |
| UC-01 | EX-02 | Is the Guest informed when the Identity Provider returns no valid verified identity? | EX-02: The Identity Provider does not return a valid verified identity; registration is cancelled and the system informs the Guest that Google registration could not be completed. |
| UC-01 | EX-03 | Is the Guest informed when account data cannot be persisted? | EX-03: Account data cannot be persisted, so no User account is created; the system informs the Guest that registration could not be completed and can be tried again later. |
| UC-02 | EX-03 | Is the User informed when the Identity Provider is unavailable or rejects authentication? | EX-03: The Identity Provider is unavailable or rejects authentication; no session is created and the system informs the User that Google log-in could not be completed. |
| UC-05.1 | EX-01 | Is the User told that the profile is temporarily unavailable? | EX-01: The profile information is temporarily unavailable; the system informs the User that the profile cannot be displayed at the moment. |
| UC-15.1 | EX-01 | What does the User see when the selected item is no longer available? | EX-01: The selected item is no longer available; the system informs the User that the item is no longer available. |
| UC-16 | EX-01 | What does the Product Owner see when a complete and unique order cannot be saved? | EX-01: The system cannot save a complete and unique order for all backlog items; the previous order is kept and the system informs the Product Owner that the new order could not be saved. |
| UC-23 | EX-01 | What does the User see when Sprint data is temporarily unavailable? | EX-01: The board cannot be loaded because Sprint data is temporarily unavailable; the system informs the User that the Sprint Board is temporarily unavailable. |
| UC-24.1 | EX-01 | Does 'no longer available' mean the task was removed (state rejection) or that its data temporarily cannot be retrieved? | EX-01: The selected Sprint Task has been removed; the system informs the User that the task is no longer available. |
| UC-25 | NF2 | What happens if NF2 finds the task is no longer active (e.g. removed from the Sprint between selection and claim)? | EX-02: The task is no longer active in the Sprint; the system rejects the claim. |
| UC-29 | EX-01 | Is the User informed when activity data cannot be retrieved? | EX-01: Activity data cannot be retrieved; the system informs the User that the activity history is temporarily unavailable. |
| UC-30 | EX-02 | Is the User informed that the email delivery preference could not be saved? | EX-02: The email delivery preference cannot be saved; the previous preference remains unchanged and the system informs the User that the change was not saved. |
| UC-31 | EX-01 | What does the User see when the selected project has no active Sprint? | EX-01: No active Sprint exists for the selected project; the system informs the User that there is no active Sprint to monitor. |
| UC-32.1 | EX-01 | Is the administrator told that account administration data is unavailable? | EX-01: Account administration data is temporarily unavailable; the system informs the System Administrator that accounts cannot be searched at the moment. |
| UC-33 | EX-01 | Is the administrator informed that the audit store is unavailable? | EX-01: The audit store is temporarily unavailable; the system informs the System Administrator that audit events cannot be displayed at the moment. |

Ngoài ra: UC-01 POST1 trên nhánh Google chỉ được trace ở comment đầu file (quy ước vẽ, không cần sửa spec).

## 7. Điểm cần peer reviewer chú ý

UC-01, UC-02, UC-04 vẫn dưới 6 pt ở A4 (4.3 / 5.0 / 4.7 pt) dù nhãn đã rút gọn: cần quyết định cho cả trang, chấp nhận, hoặc đề nghị BA tách UC. UC-02 giữ hai cặp final cùng kết cục (F1/F4, F2/F5) vì gộp lại làm sơ đồ xuống 3.7 pt; quyết định "Log-in option?" nằm ở lane System vì chuyển sang lane User gây cắt đường. UC-27.4 dùng chung một bước xác thực và một bước ghi nhận cho hoàn thành (NF2-NF4) và mở lại (AF-01); trạng thái yêu cầu là quyết định của Developer. UC-24.1 và UC-15.1 cùng đọc "no longer available" là dữ liệu không lấy được (chính sách c); nếu BA nói là đã bị xoá thì đổi thành `Reject …`. UC-30 đạt đúng 6.0 pt.

Báo cáo nghiệm thu cũ `docs/activity-diagram-binh-acceptance-report.md` mô tả UC-28 → UC-31 theo phiên bản trước; phiên bản mới nằm trong báo cáo này.

## 8. Kiểm tra đã chạy

Render từng key (không render hàng loạt): `python3 scripts/activity_diagrams.py render --key <KEY> --plantuml-jar tools/plantuml.jar` cho 45 key → 45/45 OK. Kiểm tra: `python3 scripts/activity_diagrams.py validate` → 0 error, 0 warning; `python3 cli.py validate` → 55 UC OK; `python3 -m unittest discover -s tests` → 18 tests OK; so khớp source ↔ SVG (mọi nhãn trong source có trong SVG) → 0 lệch; kiểm tra lane theo actor của bước YAML → 0 lỗi thật (1 cảnh báo giả ở UC-32.1 AF-01.2 do heuristic đọc "The System Administrator" thành "The system"). Visual QA: xem PNG của cả 45 sơ đồ và một tài liệu Word A4 (lề 2.25 cm, 45 trang) xuất PDF.

Manifest được tạo lại từ YAML + quyết định review; 10 entry loại trừ và phần header giống từng byte so với trước. `output/activity-diagrams/by-id/` không nằm trong git (`.gitignore: output/*`); bản xuất này được làm mới bằng cách sao nguyên byte SVG theo manifest cho 45 UC trong phạm vi (43 cập nhật, 2 mới: UC-25, UC-27.4), không đụng 10 file UC-06 → UC-13.

Bằng chứng 10 UC loại trừ không đổi: md5 của 30 file (10 `.puml`, 10 `.svg`, 10 bản `by-id`) trước và sau khi chép giống hệt; cả 20 file trong `diagrams/activity/project-membership/` có blob trùng với commit `7c08559`; `_shared/activity-style.puml`, `data/`, `scripts/` không đổi.
