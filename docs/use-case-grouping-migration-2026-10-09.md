# Cây Use Case và mapping mã — 09/10/2026

## Phương án đã chốt

- Không tạo Manage Account Access. UC01–04 Register Account, Log In, Log Out và Forgot Password vẫn độc lập.
- 9 nhóm tổng hợp, 13 UC độc lập, 54 UC cụ thể; danh mục YAML gồm 63 mục.
- Nhóm chỉ tổ chức tài liệu và đánh số (`abstract: true`, `grouping_only: true`), không tự động là UML generalization/include và không áp đặt quyền hoặc điều kiện cho con.
- Mỗi UC cụ thể vẫn có actor, preconditions, flows và outcomes riêng. Semantic key giữ nguyên, trừ UC-SUBTASK-COMPLETE được nhập vào UC-WORK-ITEM-STATUS-UPDATE.
- UC-07 cũ View Project Dashboard đổi tên hiển thị thành View Project Overview; semantic key UC-PROJECT-DASHBOARD-VIEW giữ nguyên.
- Update Work Item Status bao gồm complete/reopen subtask, cập nhật tiến độ task cha, kiểm tra active Sprint trước khi lưu; không tự động hoàn thành task cha.
- BR-WORK-ITEM-STATUS được làm rõ: workflow status cho task/selected PBI, completion state cho subtask.

## Cây đã cập nhật

- **UC-01 — Register Account**
- **UC-02 — Log In**
- **UC-03 — Log Out**
- **UC-04 — Forgot Password**
- **UC-05 — Manage Personal Profile** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-05.1 — View Personal Profile**
  - **UC-05.2 — Update Personal Profile**
  - **UC-05.3 — Change Password**
- **UC-06 — Manage Projects** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-06.1 — Create Project**
  - **UC-06.2 — View Project Overview**
  - **UC-06.3 — Update Project Information**
  - **UC-06.4 — Archive Project**
  - **UC-06.5 — Transfer Project Ownership**
- **UC-07 — Manage Project Members** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-07.1 — View Project Members**
  - **UC-07.2 — Add Project Member**
  - **UC-07.3 — Remove Project Member**
  - **UC-07.4 — Leave Project**
- **UC-08 — Assign Scrum Accountability**
- **UC-09 — Manage Product Goal** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-09.1 — View Product Goal**
  - **UC-09.2 — Set Product Goal**
  - **UC-09.3 — Update Product Goal**
- **UC-10 — Manage Product Backlog** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-10.1 — View Product Backlog Item**
  - **UC-10.2 — Create Product Backlog Item**
  - **UC-10.3 — Update Product Backlog Item**
  - **UC-10.4 — Remove Product Backlog Item**
  - **UC-10.5 — Order Product Backlog**
  - **UC-10.6 — Refine Backlog Item**
- **UC-11 — Estimate Backlog Item**
- **UC-12 — Manage Sprints** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-12.1 — Plan Sprint**
  - **UC-12.2 — Start Sprint**
  - **UC-12.3 — Complete Sprint**
  - **UC-12.4 — Cancel Sprint**
- **UC-13 — Review Sprint Board**
- **UC-14 — Manage Sprint Tasks** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-14.1 — View Sprint Task**
  - **UC-14.2 — Create Sprint Task**
  - **UC-14.3 — Update Sprint Task**
  - **UC-14.4 — Assign Sprint Task**
  - **UC-14.5 — Delete Sprint Task**
  - **UC-14.6 — Add Task Dependency**
  - **UC-14.7 — Remove Task Dependency**
  - **UC-14.8 — Claim Sprint Task**
- **UC-15 — Update Work Item Status**
- **UC-16 — Manage Subtasks** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-16.1 — View Subtasks**
  - **UC-16.2 — Create Subtask**
  - **UC-16.3 — Update Subtask**
  - **UC-16.4 — Delete Subtask**
- **UC-17 — Comment on Work Item**
- **UC-18 — Review Work Item Activity**
- **UC-19 — Review Notifications**
- **UC-20 — Monitor Sprint Progress**
- **UC-21 — Manage User Accounts** (nhóm tổng hợp, không có specification/AD riêng)
  - **UC-21.1 — Search and View User Accounts**
  - **UC-21.2 — Suspend User Account**
  - **UC-21.3 — Reactivate User Account**
  - **UC-21.4 — Delete User Account**
- **UC-22 — Review System Audit Log**

## Mapping mã cũ → mới

Mã cũ là snapshot repo ngay trước lần cập nhật này, không phải toàn bộ lịch sử đánh số. Dùng semantic key để đối chiếu; một mã cũ có thể nay thuộc một nhóm khác. UC-27.4 cũ và UC-26 cũ cùng ánh xạ vào UC-15 mới.

| Mã cũ | Mã mới | Semantic key cũ | Tên hiện tại / đích | Thay đổi |
|---|---|---|---|---|
| UC-01 | UC-01 | `UC-ACCOUNT-REGISTER` | Register Account | Giữ mã |
| UC-02 | UC-02 | `UC-SIGN-IN` | Log In | Giữ mã |
| UC-03 | UC-03 | `UC-SIGN-OUT` | Log Out | Giữ mã |
| UC-04 | UC-04 | `UC-PASSWORD-RESET` | Forgot Password | Giữ mã |
| UC-05 | UC-05 | `UC-PROFILE-MANAGE` | Manage Personal Profile | Giữ mã |
| UC-05.1 | UC-05.1 | `UC-PROFILE-VIEW` | View Personal Profile | Giữ mã |
| UC-05.2 | UC-05.2 | `UC-PROFILE-UPDATE` | Update Personal Profile | Giữ mã |
| UC-05.3 | UC-05.3 | `UC-PASSWORD-CHANGE` | Change Password | Giữ mã |
| UC-06 | UC-06.1 | `UC-PROJECT-CREATE` | Create Project | Đổi mã theo cây mới |
| UC-07 | UC-06.2 | `UC-PROJECT-DASHBOARD-VIEW` | View Project Overview | Đổi mã theo cây mới |
| UC-08 | UC-06.3 | `UC-PROJECT-UPDATE` | Update Project Information | Đổi mã theo cây mới |
| UC-09 | UC-07 | `UC-PROJECT-MEMBERS-MANAGE` | Manage Project Members | Đổi mã theo cây mới |
| UC-09.1 | UC-07.1 | `UC-PROJECT-MEMBERS-VIEW` | View Project Members | Đổi mã theo cây mới |
| UC-09.2 | UC-07.2 | `UC-PROJECT-MEMBER-ADD` | Add Project Member | Đổi mã theo cây mới |
| UC-09.3 | UC-07.3 | `UC-PROJECT-MEMBER-REMOVE` | Remove Project Member | Đổi mã theo cây mới |
| UC-10 | UC-08 | `UC-SCRUM-ACCOUNTABILITY-ASSIGN` | Assign Scrum Accountability | Đổi mã theo cây mới |
| UC-11 | UC-06.4 | `UC-PROJECT-ARCHIVE` | Archive Project | Đổi mã theo cây mới |
| UC-12 | UC-06.5 | `UC-PROJECT-OWNERSHIP-TRANSFER` | Transfer Project Ownership | Đổi mã theo cây mới |
| UC-13 | UC-07.4 | `UC-PROJECT-LEAVE` | Leave Project | Đổi mã theo cây mới |
| UC-14 | UC-09 | `UC-PRODUCT-GOAL-MANAGE` | Manage Product Goal | Đổi mã theo cây mới |
| UC-14.1 | UC-09.1 | `UC-PRODUCT-GOAL-VIEW` | View Product Goal | Đổi mã theo cây mới |
| UC-14.2 | UC-09.2 | `UC-PRODUCT-GOAL-SET` | Set Product Goal | Đổi mã theo cây mới |
| UC-14.3 | UC-09.3 | `UC-PRODUCT-GOAL-UPDATE` | Update Product Goal | Đổi mã theo cây mới |
| UC-15 | UC-10 | `UC-BACKLOG-ITEMS-MANAGE` | Manage Product Backlog | Đổi mã theo cây mới |
| UC-15.1 | UC-10.1 | `UC-BACKLOG-ITEM-VIEW` | View Product Backlog Item | Đổi mã theo cây mới |
| UC-15.2 | UC-10.2 | `UC-BACKLOG-ITEM-CREATE` | Create Product Backlog Item | Đổi mã theo cây mới |
| UC-15.3 | UC-10.3 | `UC-BACKLOG-ITEM-UPDATE` | Update Product Backlog Item | Đổi mã theo cây mới |
| UC-15.4 | UC-10.4 | `UC-BACKLOG-ITEM-REMOVE` | Remove Product Backlog Item | Đổi mã theo cây mới |
| UC-16 | UC-10.5 | `UC-BACKLOG-ORDER` | Order Product Backlog | Đổi mã theo cây mới |
| UC-17 | UC-10.6 | `UC-BACKLOG-ITEM-REFINE` | Refine Backlog Item | Đổi mã theo cây mới |
| UC-18 | UC-11 | `UC-BACKLOG-ITEM-ESTIMATE` | Estimate Backlog Item | Đổi mã theo cây mới |
| UC-19 | UC-12.1 | `UC-SPRINT-PLAN` | Plan Sprint | Đổi mã theo cây mới |
| UC-20 | UC-12.2 | `UC-SPRINT-START` | Start Sprint | Đổi mã theo cây mới |
| UC-21 | UC-12.3 | `UC-SPRINT-COMPLETE` | Complete Sprint | Đổi mã theo cây mới |
| UC-22 | UC-12.4 | `UC-SPRINT-CANCEL` | Cancel Sprint | Đổi mã theo cây mới |
| UC-23 | UC-13 | `UC-SPRINT-BOARD-REVIEW` | Review Sprint Board | Đổi mã theo cây mới |
| UC-24 | UC-14 | `UC-SPRINT-TASKS-MANAGE` | Manage Sprint Tasks | Đổi mã theo cây mới |
| UC-24.1 | UC-14.1 | `UC-SPRINT-TASK-VIEW` | View Sprint Task | Đổi mã theo cây mới |
| UC-24.2 | UC-14.2 | `UC-SPRINT-TASK-CREATE` | Create Sprint Task | Đổi mã theo cây mới |
| UC-24.3 | UC-14.3 | `UC-SPRINT-TASK-UPDATE` | Update Sprint Task | Đổi mã theo cây mới |
| UC-24.4 | UC-14.4 | `UC-SPRINT-TASK-ASSIGN` | Assign Sprint Task | Đổi mã theo cây mới |
| UC-24.5 | UC-14.5 | `UC-SPRINT-TASK-DELETE` | Delete Sprint Task | Đổi mã theo cây mới |
| UC-24.6 | UC-14.6 | `UC-TASK-DEPENDENCY-ADD` | Add Task Dependency | Đổi mã theo cây mới |
| UC-24.7 | UC-14.7 | `UC-TASK-DEPENDENCY-REMOVE` | Remove Task Dependency | Đổi mã theo cây mới |
| UC-25 | UC-14.8 | `UC-SPRINT-TASK-CLAIM` | Claim Sprint Task | Đổi mã theo cây mới |
| UC-26 | UC-15 | `UC-WORK-ITEM-STATUS-UPDATE` | Update Work Item Status | Đổi mã theo cây mới |
| UC-27 | UC-16 | `UC-SUBTASKS-MANAGE` | Manage Subtasks | Đổi mã theo cây mới |
| UC-27.1 | UC-16.1 | `UC-SUBTASKS-VIEW` | View Subtasks | Đổi mã theo cây mới |
| UC-27.2 | UC-16.2 | `UC-SUBTASK-CREATE` | Create Subtask | Đổi mã theo cây mới |
| UC-27.3 | UC-16.3 | `UC-SUBTASK-UPDATE` | Update Subtask | Đổi mã theo cây mới |
| UC-27.4 | UC-15 | `UC-SUBTASK-COMPLETE` | Update Work Item Status | Gộp vào Update Work Item Status; lưu YAML cũ trong archive |
| UC-27.5 | UC-16.4 | `UC-SUBTASK-DELETE` | Delete Subtask | Đổi mã theo cây mới |
| UC-28 | UC-17 | `UC-WORK-ITEM-COMMENT` | Comment on Work Item | Đổi mã theo cây mới |
| UC-29 | UC-18 | `UC-WORK-ITEM-ACTIVITY-REVIEW` | Review Work Item Activity | Đổi mã theo cây mới |
| UC-30 | UC-19 | `UC-NOTIFICATIONS-REVIEW` | Review Notifications | Đổi mã theo cây mới |
| UC-31 | UC-20 | `UC-SPRINT-PROGRESS-MONITOR` | Monitor Sprint Progress | Đổi mã theo cây mới |
| UC-32 | UC-21 | `UC-USER-ACCOUNTS-MANAGE` | Manage User Accounts | Đổi mã theo cây mới |
| UC-32.1 | UC-21.1 | `UC-USER-ACCOUNTS-SEARCH` | Search and View User Accounts | Đổi mã theo cây mới |
| UC-32.2 | UC-21.2 | `UC-USER-ACCOUNT-SUSPEND` | Suspend User Account | Đổi mã theo cây mới |
| UC-32.3 | UC-21.3 | `UC-USER-ACCOUNT-REACTIVATE` | Reactivate User Account | Đổi mã theo cây mới |
| UC-32.4 | UC-21.4 | `UC-USER-ACCOUNT-DELETE` | Delete User Account | Đổi mã theo cây mới |
| UC-33 | UC-22 | `UC-SYSTEM-AUDIT-LOG-REVIEW` | Review System Audit Log | Đổi mã theo cây mới |
| — | UC-06 | `UC-PROJECTS-MANAGE` | Manage Projects | Nhóm tổng hợp mới |
| — | UC-12 | `UC-SPRINTS-MANAGE` | Manage Sprints | Nhóm tổng hợp mới |

## Phần đã đồng bộ

- YAML danh mục và specification nguồn, grouping validator, regression tests, README.
- Markdown Use Case List, Use Case Descriptions và ID Mapping trong output được sinh lại từ YAML.
- Manifest AD dùng ID/name/actor hiện tại cho danh mục; metadata render cũ được giữ để truy vết. Các nguồn/hình chưa được redraw không được coi là đã nghiệm thu theo catalog mới.
- UC-SUBTASK-COMPLETE được đưa khỏi danh mục active, không xóa mất nội dung cũ: `docs/archive/use-cases/2026-10-09/UC-SUBTASK-COMPLETE.yml`. Nguồn/hình AD cũ được giữ qua retired manifest entry để tham khảo, không dùng như diagram active.

## Chưa thực hiện trong lần này

- Không chỉnh hoặc sinh lại Word Iter1 hay DOCX output.
- Không vẽ lại hàng loạt UCD/AD hoặc đổi tên hàng loạt các hình trong output/activity-diagrams/by-id. Các hình đó vẫn theo snapshot cũ, xem README cảnh báo trong thư mục.
- Không chỉnh các báo cáo audit cũ thành kết luận nghiệm thu mới; chúng là lịch sử review theo phiên bản trước.
- Không commit hoặc push.

## Công việc đồng bộ diagram/Word tiếp theo

1. Dùng YAML và mapping này để cập nhật tên, caption, ID, actor và các tham chiếu UC trong Word/UCD. Authentication là precondition cho UC được bảo vệ, không phải include Log In chỉ vì cần đăng nhập.
2. Rà nội dung/traceability các AD theo actor mới; ưu tiên UC-WORK-ITEM-STATUS-UPDATE vì đã tiếp nhận complete/reopen subtask và exception Sprint kết thúc.
3. Sửa PlantUML source trước, rồi render và review SVG; cập nhật catalog_sync_status/rendered_display_id/rendered_name trong manifest sau khi hoàn tất. Chỉ đổi tên file không chứng minh diagram đã khớp spec.
4. Khi tạo bộ by-id mới, dùng semantic key làm căn cứ và mapping catalog hiện tại; không trộn file cũ vào bộ mới.
5. Chỉ khôi phục trạng thái ready-for-peer-review/pass sau khi kiểm tra nguồn, traceability và hình thực tế; không xem thay đổi metadata là render thành công.

## Kiểm chứng lần cập nhật

- Validator catalog: 63 mục, 0 lỗi (9 nhóm tổng hợp, 54 UC cụ thể).
- Unit tests: 27/27 thành công, bao gồm cây đã chốt, auth độc lập,
  grouping-only không làm mất validation của UC cụ thể, nội dung merge subtask,
  manifest active/retired và Markdown generator.
- Markdown build thành công; không chạy build DOCX hoặc renderer.
- Có 52 AD cần source review theo manifest mới. Đây là trạng thái chưa đồng bộ
  diagram, không phải kết quả nghiệm thu UML hoặc traceability đạt.
- Chạy validator AD hiện chưa đạt: 101 lỗi, gồm cảnh báo chặn source review,
  header/ID nguồn còn theo catalog cũ và traceability của UC status mới.
  Không bỏ qua các lỗi này hoặc đặt pass chỉ để đạt kiểm tra; cần cập nhật source
  và hình trong đợt đồng bộ diagram tiếp theo.
