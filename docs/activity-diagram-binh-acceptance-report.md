# Báo cáo peer review và nghiệm thu Activity Diagram — Nguyễn An Bình (14 UC)

Ngày: 2026-10-04 · Cơ sở: nhánh `develop` tại `ebcf9ad` (đã gồm PR #8 làm rõ UC spec và PR #9 audit Activity
Diagram) · Hướng dẫn áp dụng: `docs/activity-diagram-binh-review-guide.md` và `docs/activity-diagram-guideline.md`.

Báo cáo này **không** nghiệm thu thay leader. Verdict cao nhất là READY FOR PEER REVIEW; leader mới là người đổi
trạng thái Jira sang Accepted.

## 1. Xác nhận phạm vi theo `diagrams/activity/manifest.yml`

Mỗi file được tìm theo `key` trong manifest. File YAML được xác nhận bằng trường `key:` bên trong file, không chỉ
dựa vào tên file.

| Display ID | Semantic key | Tên | Assignee | YAML | Source | SVG |
|---|---|---|---|---|---|---|
| UC-06 | `UC-PROJECT-CREATE` | Create Project | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-CREATE.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-CREATE.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-CREATE.svg` |
| UC-07 | `UC-PROJECT-DASHBOARD-VIEW` | View Project Dashboard | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-DASHBOARD-VIEW.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-DASHBOARD-VIEW.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-DASHBOARD-VIEW.svg` |
| UC-08 | `UC-PROJECT-UPDATE` | Update Project Information | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-UPDATE.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-UPDATE.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-UPDATE.svg` |
| UC-09.1 | `UC-PROJECT-MEMBERS-VIEW` | View Project Members | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-MEMBERS-VIEW.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-MEMBERS-VIEW.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBERS-VIEW.svg` |
| UC-09.2 | `UC-PROJECT-MEMBER-ADD` | Add Project Member | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-ADD.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-ADD.svg` |
| UC-09.3 | `UC-PROJECT-MEMBER-REMOVE` | Remove Project Member | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-REMOVE.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-REMOVE.svg` |
| UC-10 | `UC-SCRUM-ACCOUNTABILITY-ASSIGN` | Assign Scrum Accountability | Nguyễn An Bình | `data/use_cases/project-membership/UC-SCRUM-ACCOUNTABILITY-ASSIGN.yml` | `diagrams/activity/project-membership/source/UC-SCRUM-ACCOUNTABILITY-ASSIGN.puml` | `diagrams/activity/project-membership/svg/UC-SCRUM-ACCOUNTABILITY-ASSIGN.svg` |
| UC-11 | `UC-PROJECT-ARCHIVE` | Archive Project | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-ARCHIVE.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-ARCHIVE.svg` |
| UC-12 | `UC-PROJECT-OWNERSHIP-TRANSFER` | Transfer Project Ownership | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-OWNERSHIP-TRANSFER.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-OWNERSHIP-TRANSFER.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-OWNERSHIP-TRANSFER.svg` |
| UC-13 | `UC-PROJECT-LEAVE` | Leave Project | Nguyễn An Bình | `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` | `diagrams/activity/project-membership/source/UC-PROJECT-LEAVE.puml` | `diagrams/activity/project-membership/svg/UC-PROJECT-LEAVE.svg` |
| UC-28 | `UC-WORK-ITEM-COMMENT` | Comment on Work Item | Nguyễn An Bình | `data/use_cases/collaboration-notification/UC-WORK-ITEM-COMMENT.yml` | `diagrams/activity/collaboration-notification/source/UC-WORK-ITEM-COMMENT.puml` | `diagrams/activity/collaboration-notification/svg/UC-WORK-ITEM-COMMENT.svg` |
| UC-29 | `UC-WORK-ITEM-ACTIVITY-REVIEW` | Review Work Item Activity | Nguyễn An Bình | `data/use_cases/collaboration-notification/UC-WORK-ITEM-ACTIVITY-REVIEW.yml` | `diagrams/activity/collaboration-notification/source/UC-WORK-ITEM-ACTIVITY-REVIEW.puml` | `diagrams/activity/collaboration-notification/svg/UC-WORK-ITEM-ACTIVITY-REVIEW.svg` |
| UC-30 | `UC-NOTIFICATIONS-REVIEW` | Review Notifications | Nguyễn An Bình | `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` | `diagrams/activity/collaboration-notification/source/UC-NOTIFICATIONS-REVIEW.puml` | `diagrams/activity/collaboration-notification/svg/UC-NOTIFICATIONS-REVIEW.svg` |
| UC-31 | `UC-SPRINT-PROGRESS-MONITOR` | Monitor Sprint Progress | Nguyễn An Bình | `data/use_cases/scrum-reporting/UC-SPRINT-PROGRESS-MONITOR.yml` | `diagrams/activity/scrum-reporting/source/UC-SPRINT-PROGRESS-MONITOR.puml` | `diagrams/activity/scrum-reporting/svg/UC-SPRINT-PROGRESS-MONITOR.svg` |

Kết quả: đủ 14 display ID, cả 14 entry có `assignee: Nguyễn An Bình`. Không có diagram nào của thành viên khác bị
sửa.

## 2. Thay đổi spec sau PR #8 ảnh hưởng tới 14 UC

| UC | Thay đổi trong YAML/BR (đã merge, không sửa ở đây) | Tác động lên diagram |
|---|---|---|
| UC-10 | Thêm AF-02 «The Project Owner does not confirm the Product Owner replacement» → «keeps the current Scrum accountabilities unchanged». BR-PRODUCT-OWNER-ACCOUNTABILITY-UNIQUE đổi thành «…replaces the previous one once the Project Owner confirms the replacement». | Diagram thiếu AF-02 → **đã sửa**. |
| UC-30 | Thêm EX-03 «Email delivery is enabled but the actor has no verified email address; the change is rejected and the previous preference remains unchanged». | Diagram thiếu EX-03 → **đã sửa**. |
| UC-09.3 | PRE3 đổi thành «The target User is an active Project Member». | EX-01 hết mâu thuẫn precondition; diagram giữ nguyên. |
| UC-11 | Bỏ precondition «no active Sprint». | EX-01 hết mâu thuẫn; diagram giữ nguyên. |
| UC-13 | Bỏ precondition «actor is not the current Project Owner». | EX-01 hết mâu thuẫn; diagram giữ nguyên. |
| UC-31 | Bỏ precondition «project has an active Sprint». | EX-01 hết mâu thuẫn; diagram giữ nguyên. |

## 3. Bảng nghiệm thu (14 UC)

| UC | YAML → AD | AD → YAML | UML | SVG/A4 | Verdict | Jira comment |
|---|---|---|---|---|---|---|
| UC-06 | 17 mục, thiếu 0. Đủ: trigger, NF1–NF6, AF-01 (2 bước), EX-01, POST1–3, 2 BR | 17 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt (2 final khác kết quả) | 807×1031 px, ≈ 7.9 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-06 Create Project — READY FOR PEER REVIEW**<br>Khớp: trigger, NF1–NF6, AF-01 (vòng sửa thông tin), EX-01 (không lưu được dữ liệu), POST1–POST3; BR-PROJECT-ONE-OWNER trace ở NF5; BR-ACTIVE-USER-REQUIRED là precondition.<br>Lỗi: không có lỗi nghiệp vụ. Ghi nhận: cạnh thoát vòng lặp AF-01 cắt thân vòng lặp (giới hạn PlantUML `while`).<br>Điều kiện nghiệm thu: peer reviewer xác nhận Bảng A/B; chèn thử SVG vào Word ở 16,5 cm.<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-CREATE.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-CREATE.svg` |
| UC-07 | 13 mục, thiếu 0. Đủ: trigger, NF1–NF4, AF-01, EX-01, POST1–2, 2 BR | 14 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt | 585×796 px, ≈ 10.2 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-07 View Project Dashboard — READY FOR PEER REVIEW**<br>Khớp: NF1–NF4, AF-01 (dashboard read-only khi archived, BR-PROJECT-ARCHIVED-READ-ONLY), EX-01 (dự án/membership không còn → «Deny access…», BR-PROJECT-MEMBER-ACCESS).<br>Lỗi: không có.<br>Điều kiện nghiệm thu: peer reviewer xác nhận Bảng A/B.<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-DASHBOARD-VIEW.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-DASHBOARD-VIEW.svg` |
| UC-08 | 15 mục, thiếu 0. Đủ: trigger, NF1–NF5, AF-01 (2 bước), EX-01, POST1–2; 2 BR là precondition/partition | 18 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 0 | Đạt | 690×1090 px, ≈ 7.5 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-08 Update Project Information — READY FOR PEER REVIEW**<br>Khớp: NF1–NF5 (NF4 tách Validate/Save), AF-01 (vòng sửa giá trị sai), EX-01 (ownership đổi trước khi lưu → reject), POST2 (ghi activity history).<br>Lỗi: không có. Ghi nhận: đường thoát vòng AF-01 cắt thân vòng lặp (giới hạn PlantUML).<br>Điều kiện nghiệm thu: peer reviewer xác nhận việc tách NF4.<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-UPDATE.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-UPDATE.svg` |
| UC-09.1 | 10 mục, thiếu 0. Đủ: trigger, NF1–NF3, AF-01, EX-01, POST1; BR qua PRE1 | 13 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt | 717×719 px, ≈ 9.1 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-09.1 View Project Members — READY FOR PEER REVIEW**<br>Khớp: NF1–NF3, AF-01 (chỉ hiển thị Project Owner), EX-01 (membership tạm thời không có → report), POST1.<br>Lỗi: không có.<br>Điều kiện nghiệm thu: peer reviewer xác nhận Bảng A/B.<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-MEMBERS-VIEW.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBERS-VIEW.svg` |
| UC-09.2 | 14 mục, thiếu 0. Đủ: trigger, NF1–NF5, AF-01, EX-01, POST1–2, 2 BR | 16 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt | 916×827 px, ≈ 7.1 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-09.2 Add Project Member — READY FOR PEER REVIEW**<br>Khớp: NF1–NF5, AF-01 (đã là thành viên → report), EX-01 (tài khoản inactive trước khi xác nhận → reject), POST1–POST2.<br>Lỗi: không có.<br>Điều kiện nghiệm thu: peer reviewer xác nhận việc tách NF4 thành hai decision.<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-ADD.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-ADD.svg` |
| UC-09.3 | 14 mục, thiếu 0. Đủ: trigger, NF1–NF5, AF-01, EX-01, POST1–2, 2 BR | 15 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 2 | Đạt | 983×815 px, ≈ 6.7 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-09.3 Remove Project Member — READY FOR PEER REVIEW**<br>Khớp: NF1–NF5, AF-01 (còn việc dở → yêu cầu reassign, kết thúc), EX-01 (owner tự xóa mình → reject, BR-PROJECT-ONE-OWNER), POST1–POST2.<br>Lỗi: không có. Sau PR #8, EX-01 không còn mâu thuẫn PRE3; observation cũ trong manifest cần gỡ.<br>Điều kiện nghiệm thu: reviewer đồng ý AF-01 là nhánh kết thúc; leader cập nhật observation trong manifest.<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-REMOVE.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-REMOVE.svg` |
| UC-10 | 18 mục, thiếu 0. Đủ: trigger, NF1–NF5, AF-01 (2 bước), AF-02 (mới), EX-01, POST1–2, 3 BR | 23 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 2 | Đạt (3 final, F1/F3 cùng kết quả có giải thích) | 867×1137 px, ≈ 7.2 pt; layout check: sạch; Word A4: vừa 1 trang (trước: 656×1150, 7.1 pt) | **READY FOR PEER REVIEW** | **[AD peer review] UC-10 Assign Scrum Accountability — READY FOR PEER REVIEW**<br>Khớp: NF1–NF5, AF-01 (yêu cầu xác nhận → chuyển PO), AF-02 MỚI (không xác nhận → giữ nguyên accountability), EX-01 (thành viên rời trước khi lưu → reject), POST1–POST2, BR-PRODUCT-OWNER-ACCOUNTABILITY-UNIQUE.<br>Đã sửa: diagram trên develop thiếu AF-02 (validator lỗi «AF-02 is not represented»); đã thêm decision «Confirm the replacement?» ở lane Project Owner. EX-01 chuyển sang nhánh ngang nên hết chữ bị đường cắt.<br>Điều kiện nghiệm thu: reviewer chấp nhận hai final cùng kết quả (F1 AF-02, F3 EX-01) như ngoại lệ UC-13; leader gỡ hai observation cũ trong manifest.<br>Files: `diagrams/activity/project-membership/source/UC-SCRUM-ACCOUNTABILITY-ASSIGN.puml`, `diagrams/activity/project-membership/svg/UC-SCRUM-ACCOUNTABILITY-ASSIGN.svg` |
| UC-11 | 14 mục, thiếu 0. Đủ: trigger, NF1–NF5, AF-01, EX-01, POST1–2, 2 BR | 15 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt | 1062×796 px, ≈ 6.2 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-11 Archive Project — READY FOR PEER REVIEW**<br>Khớp: NF1–NF5, AF-01 (hủy xác nhận → giữ nguyên active), EX-01 (còn Sprint đang chạy → reject), POST1–POST2, BR-PROJECT-ARCHIVED-READ-ONLY.<br>Lỗi: không có. Sau PR #8, EX-01 không còn mâu thuẫn precondition; cần gỡ observation cũ trong manifest.<br>Điều kiện nghiệm thu: chèn Word ở 16,5 cm (6,2 pt, sát ngưỡng 6 pt).<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-ARCHIVE.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-ARCHIVE.svg` |
| UC-12 | 18 mục, thiếu 0. Đủ: trigger, NF1–NF5, AF-01 (2 bước), EX-01, POST1–3, 4 BR | 16 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt | 731×973 px, ≈ 8.4 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-12 Transfer Project Ownership — READY FOR PEER REVIEW**<br>Khớp: NF1–NF5, AF-01 (thành viên không còn active → chọn người khác), EX-01 (ownership đổi đồng thời → reject), POST1/POST3 ở NF5, BR-PROJECT-ONE-OWNER.<br>Lỗi: không có. Ghi nhận: vòng AF-01 cắt đường (giới hạn PlantUML).<br>Điều kiện nghiệm thu: peer reviewer xác nhận Bảng A/B.<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-OWNERSHIP-TRANSFER.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-OWNERSHIP-TRANSFER.svg` |
| UC-13 | 16 mục, thiếu 0. Đủ: trigger, NF1–NF5, AF-01 (2 bước), EX-01, POST1–3, 2 BR | 20 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt (ngoại lệ 2 final cùng kết quả có giải thích) | 935×1090 px, ≈ 7.0 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-13 Leave Project — READY FOR PEER REVIEW**<br>Khớp: NF1–NF5, AF-01 (còn task dở → cảnh báo, xác nhận hoặc hủy), EX-01 (owner chưa chuyển quyền → reject, BR-PROJECT-OWNER-TRANSFER-BEFORE-LEAVE), POST1–POST3.<br>Lỗi: không có. Sau PR #8, EX-01 không còn mâu thuẫn precondition.<br>Điều kiện nghiệm thu: reviewer xác nhận ngoại lệ hai final cùng kết quả (đã giải thích trong header).<br>Files: `diagrams/activity/project-membership/source/UC-PROJECT-LEAVE.puml`, `diagrams/activity/project-membership/svg/UC-PROJECT-LEAVE.svg` |
| UC-28 | 18 mục, thiếu 0. Đủ: trigger, NF1–NF6, AF-01, EX-01, EX-02, POST1–2, 4 BR | 22 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 2 | Đạt (2 final khác kết quả) | 787×1310 px, ≈ 6.2 pt; layout check: sạch; Word A4: vừa 1 trang (trước: 826×1532, 5.3 pt) | **READY FOR PEER REVIEW** | **[AD peer review] UC-28 Comment on Work Item — READY FOR PEER REVIEW**<br>Khớp: NF1–NF6, AF-01 (comment rỗng → nhập lại), EX-01 (work item bị xóa → reject), EX-02 (gửi email thất bại → ghi nhận, comment vẫn lưu), POST1–POST2, 4 BR.<br>Đã sửa: nhãn «[none eligible]» đặt sai phía cạnh và chữ chỉ 5,3 pt. Đã bỏ decision này (YAML không mô tả trường hợp không ai đủ điều kiện), đưa EX-01 sang nhánh ngang; giờ ≈ 6,2 pt.<br>Điều kiện nghiệm thu: reviewer đồng ý bỏ nhánh «none eligible»; leader đổi manifest final_status từ needs-manual-review sang ready-for-peer-review.<br>Files: `diagrams/activity/collaboration-notification/source/UC-WORK-ITEM-COMMENT.puml`, `diagrams/activity/collaboration-notification/svg/UC-WORK-ITEM-COMMENT.svg` |
| UC-29 | 12 mục, thiếu 0. Đủ: trigger, NF1–NF4, AF-01, EX-01, POST1, 2 BR | 14 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt | 679×762 px, ≈ 9.6 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-29 Review Work Item Activity — READY FOR PEER REVIEW**<br>Khớp: NF1–NF4, AF-01 (chỉ có sự kiện tạo), EX-01 (không lấy được dữ liệu → report), POST1, BR-ACTIVITY-IMMUTABLE.<br>Lỗi: không có.<br>Điều kiện nghiệm thu: peer reviewer xác nhận Bảng A/B.<br>Files: `diagrams/activity/collaboration-notification/source/UC-WORK-ITEM-ACTIVITY-REVIEW.puml`, `diagrams/activity/collaboration-notification/svg/UC-WORK-ITEM-ACTIVITY-REVIEW.svg` |
| UC-30 | 20 mục, thiếu 0. Đủ: trigger, NF1–NF4, AF-01, AF-02 (2 bước), EX-01, EX-02, EX-03 (mới), POST1–3, 3 BR | 26 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 4 | Đạt (1 final chung, quy ước P2) | 1067×1267 px, ≈ 6.1 pt; layout check: sạch; Word A4: vừa 1 trang (trước: 1427×1114, 4.6 pt) | **READY FOR PEER REVIEW** | **[AD peer review] UC-30 Review Notifications — READY FOR PEER REVIEW**<br>Khớp: NF1–NF4, AF-01 (đánh dấu tất cả đã đọc), AF-02 (bật/tắt email: kiểm tra email đã xác thực, lưu), EX-01, EX-02, EX-03 MỚI (bật email nhưng chưa có email xác thực → reject, giữ preference cũ), POST1–POST3.<br>Đã sửa: thiếu EX-03 (validator lỗi «EX-03 is not represented»); chữ guard 4,6 pt → ≈ 6,1 pt nhờ bỏ decision «Enabling email delivery?» và ngắt chữ hẹp.<br>Điều kiện nghiệm thu: reviewer chấp nhận decision «Requested action?» ở lane System (observation); leader đổi manifest final_status sang ready-for-peer-review và cập nhật observations (AF-02.1 failure path đã có EX-03).<br>Files: `diagrams/activity/collaboration-notification/source/UC-NOTIFICATIONS-REVIEW.puml`, `diagrams/activity/collaboration-notification/svg/UC-NOTIFICATIONS-REVIEW.svg` |
| UC-31 | 13 mục, thiếu 0. Đủ: trigger, NF1–NF4, AF-01 (2 bước), EX-01, POST1, 2 BR | 14 node; UNSUPPORTED/CONFLICT/UNCLEAR: 0; JUSTIFIED: 1 | Đạt | 581×916 px, ≈ 8.9 pt; layout check: sạch; Word A4: vừa 1 trang | **READY FOR PEER REVIEW** | **[AD peer review] UC-31 Monitor Sprint Progress — READY FOR PEER REVIEW**<br>Khớp: NF1–NF4, AF-01 (thiếu estimate → gắn nhãn, vẫn hiển thị số đếm), EX-01 (không có Sprint đang chạy → report, BR-PROGRESS-ACTIVE-SPRINT), POST1.<br>Lỗi: không có. Sau PR #8, EX-01 không còn mâu thuẫn precondition; cần gỡ observation cũ trong manifest.<br>Điều kiện nghiệm thu: peer reviewer xác nhận Bảng A/B.<br>Files: `diagrams/activity/scrum-reporting/source/UC-SPRINT-PROGRESS-MONITOR.puml`, `diagrams/activity/scrum-reporting/svg/UC-SPRINT-PROGRESS-MONITOR.svg` |

Tổng: 14 READY FOR PEER REVIEW · 0 REQUEST CHANGES · 0 BLOCKED — REQUIREMENT CONFLICT · 0 BLOCKED — INSUFFICIENT
SPECIFICATION. Ba UC đã được sửa trong lần này (UC-10, UC-28, UC-30). Bảy UC chỉ được thêm dòng comment
`Final nodes:` vào header; SVG của chúng được render lại và giống hệt bản cũ từng byte.

## 4. Chi tiết từng UC

### UC-06 — Create Project (`UC-PROJECT-CREATE`)

YAML `data/use_cases/project-membership/UC-PROJECT-CREATE.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-CREATE.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-CREATE.svg` · Lane: User, System · Final: 2 · 807×1031 px ≈ 7.9 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Chỉ thêm comment `Final nodes:` vào header `.puml`; SVG render lại giống hệt từng byte.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Lane: User (người tạo chưa có vai trò dự án) và System. Đúng guideline §6.
- Thứ tự: NF1→NF6 đúng YAML. AF-01 là vòng `while` quay về kiểm tra sau khi User sửa (AF-01.2 «submits it again»).
- EX-01 kiểm tra sau NF5. Action «Reject the project creation…» là GUIDE-7.3 vì YAML không nêu kết quả.
- End node: F1 (EX-01, không tạo dự án) và F2 (tạo xong) là hai kết quả khác nhau → hai final hợp lệ. Header đã bổ sung dòng `Final nodes:`.
- Không có action từ precondition (Log In, kiểm tra active). Không thiếu bước/postcondition.
- Giới hạn layout đã biết: cạnh thoát của vòng lặp AF-01 cắt hai cạnh thân vòng lặp (PlantUML `while` khi thân vòng lặp sang lane User).

#### Bảng A — UC Spec → Diagram (UC-06)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The User chooses to create a new project.» | «Start project creation» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE2 | «The User is authenticated.»; «The User account is active.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Starts project creation.» | «Start project creation» (User) | Đạt |
| NF2 (System) | «Requests the project name, description, and planned dates.» | «Request the project name, description, and planned dates» (System) | Đạt |
| NF3 (User) | «Provides the required project information and confirms creation.» | «Provide the required project information and confirm creation» (User) | Đạt |
| NF4 (System) | «Validates the submitted information.» | «Validate the submitted information» (System) | Đạt |
| NF5 (System) | «Creates the project and assigns ownership to the User.» | «Create the project and assign ownership to the User» (System) | Đạt |
| NF6 (System) | «Initializes the Product Backlog and default Sprint Board.» | «Initialize the Product Backlog and default Sprint Board» (System) | Đạt |
| AF-01 condition | «Required project information is missing or invalid.» | [invalid — AF-01] tại «Information missing or invalid?» | Đạt |
| AF-01.1 | «The system identifies the invalid information.» | «Identify the invalid information» (System) | Đạt |
| AF-01.2 | «The User corrects the information and submits it again.» | «Correct the information and submit it again» (User) | Đạt |
| EX-01 | «The project cannot be created because project data cannot be persisted.» | [not persisted — EX-01] tại «Project data persisted?»; «Reject the project creation because the data cannot be persisted» (System) | Đạt |
| POST1 | «A new active project is created.» | «Create the project and assign ownership to the User» (System) | Đạt |
| POST2 | «The creator becomes the sole Project Owner.» | «Create the project and assign ownership to the User» (System) | Đạt |
| POST3 | «An empty Product Backlog and default Sprint Board are initialized.» | «Initialize the Product Backlog and default Sprint Board» (System) | Đạt |
| BR-ACTIVE-USER-REQUIRED | «Only an active authenticated User can create or access a project.» | Không vẽ: bảo đảm bởi PRE1–PRE2 (User authenticated, active); BR không tạo nhánh trong luồng. | Đạt |
| BR-PROJECT-ONE-OWNER | «Every active project must have exactly one Project Owner.» | «Create the project and assign ownership to the User» (System) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-06)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Start project creation» (User) | NF1 «Starts project creation.» | EXPLICIT |
| Action «Request the project name, description, and planned dates» (System) | NF2 «Requests the project name, description, and planned dates.» | EXPLICIT |
| Action «Provide the required project information and confirm creation» (User) | NF3 «Provides the required project information and confirms creation.» | EXPLICIT |
| Action «Validate the submitted information» (System) | NF4 «Validates the submitted information.» | EXPLICIT |
| Loop decision «Information missing or invalid?» (System) | AF-01 «Required project information is missing or invalid.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [invalid — AF-01] | AF-01 «Required project information is missing or invalid.» | NECESSARY UML REPRESENTATION |
| Action «Identify the invalid information» (System) | AF-01.1 «The system identifies the invalid information.» | EXPLICIT |
| Action «Correct the information and submit it again» (User) | AF-01.2 «The User corrects the information and submits it again.» | EXPLICIT |
| Guard [valid] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Create the project and assign ownership to the User» (System) | NF5 «Creates the project and assigns ownership to the User.»; POST1 «A new active project is created.»; POST2 «The creator becomes the sole Project Owner.»; BR-PROJECT-ONE-OWNER | EXPLICIT |
| Decision «Project data persisted?» (System) | EX-01 «The project cannot be created because project data cannot be persisted.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [persisted] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [not persisted — EX-01] | EX-01 «The project cannot be created because project data cannot be persisted.» | NECESSARY UML REPRESENTATION |
| Action «Reject the project creation because the data cannot be persisted» (System) | EX-01 «The project cannot be created because project data cannot be persisted.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F1 (sau [not persisted — EX-01]) | Kết quả: không tạo dự án (EX-01) | NECESSARY UML REPRESENTATION |
| Action «Initialize the Product Backlog and default Sprint Board» (System) | NF6 «Initializes the Product Backlog and default Sprint Board.»; POST3 «An empty Product Backlog and default Sprint Board are initialized.» | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: dự án được tạo và khởi tạo (POST1–POST3) | NECESSARY UML REPRESENTATION |

### UC-07 — View Project Dashboard (`UC-PROJECT-DASHBOARD-VIEW`)

YAML `data/use_cases/project-membership/UC-PROJECT-DASHBOARD-VIEW.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-DASHBOARD-VIEW.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-DASHBOARD-VIEW.svg` · Lane: User, System · Final: 2 · 585×796 px ≈ 10.2 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Chỉ thêm comment `Final nodes:`; SVG giống hệt.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Lane: User (Project Member không cần vai trò riêng) và System.
- Thứ tự: NF1 → NF2 (kiểm tra membership) → EX-01 → NF3 → AF-01/NF4. EX-01 đặt ngay sau NF2 vì NF2 là bước kiểm tra membership.
- AF-01 (archived) và NF4 là hai cách hiển thị cùng một kết quả nên hội tụ vào một final. EX-01 là kết quả khác nên có final riêng. Header đã bổ sung `Final nodes:`.
- POST2 «No project data is modified» được thỏa vì không có action nào sửa dữ liệu.
- Không có action từ precondition.

#### Bảng A — UC Spec → Diagram (UC-07)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Member selects a project from the list of participating projects.» | «Select a project» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE2 | «The actor is authenticated.»; «The actor is an active member of the selected project.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Selects a project.» | «Select a project» (User) | Đạt |
| NF2 (System) | «Verifies the actor's active project membership.» | «Verify the actor's active project membership» (System) | Đạt |
| NF3 (System) | «Retrieves project information, member count, and current Sprint summary.» | «Retrieve project information, member count, and current Sprint summary» (System) | Đạt |
| NF4 (System) | «Displays the project dashboard.» | «Display the project dashboard» (System) | Đạt |
| AF-01 condition | «The project is archived.» | [archived — AF-01] tại «Project archived?» | Đạt |
| AF-01.1 | «The system displays the dashboard in read-only mode.» | «Display the dashboard in read-only mode» (System) | Đạt |
| EX-01 | «The project no longer exists or the actor's membership has been removed.» | [project or membership removed — EX-01] tại «Project and membership exist?»; «Deny access to the project dashboard for this actor» (System) | Đạt |
| POST1 | «The current project overview is displayed.» | «Display the project dashboard» (System) | Đạt |
| POST2 | «No project data is modified.» | Không cần node: không có action nào sửa dữ liệu dự án. | Đạt |
| BR-PROJECT-MEMBER-ACCESS | «Project information is available only to active members of that project.» | «Verify the actor's active project membership» (System) | Đạt |
| BR-PROJECT-ARCHIVED-READ-ONLY | «An archived project and its contained work are read-only.» | «Display the dashboard in read-only mode» (System) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-07)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Select a project» (User) | NF1 «Selects a project.» | EXPLICIT |
| Action «Verify the actor's active project membership» (System) | NF2 «Verifies the actor's active project membership.»; BR-PROJECT-MEMBER-ACCESS | EXPLICIT |
| Decision «Project and membership exist?» (System) | EX-01 «The project no longer exists or the actor's membership has been removed.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [exist] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [project or membership removed — EX-01] | EX-01 «The project no longer exists or the actor's membership has been removed.» | NECESSARY UML REPRESENTATION |
| Action «Deny access to the project dashboard for this actor» (System) | EX-01 «The project no longer exists or the actor's membership has been removed.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F1 (sau [project or membership removed — EX-01]) | Kết quả: không hiển thị dashboard (EX-01) | NECESSARY UML REPRESENTATION |
| Action «Retrieve project information, member count, and current Sprint summary» (System) | NF3 «Retrieves project information, member count, and current Sprint summary.» | EXPLICIT |
| Decision «Project archived?» (System) | AF-01 «The project is archived.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [active] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Display the project dashboard» (System) | NF4 «Displays the project dashboard.»; POST1 «The current project overview is displayed.» | EXPLICIT |
| Guard [archived — AF-01] | AF-01 «The project is archived.» | NECESSARY UML REPRESENTATION |
| Action «Display the dashboard in read-only mode» (System) | AF-01.1 «The system displays the dashboard in read-only mode.»; BR-PROJECT-ARCHIVED-READ-ONLY | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: dashboard được hiển thị, read-only nếu archived (POST1, POST2) | NECESSARY UML REPRESENTATION |

### UC-08 — Update Project Information (`UC-PROJECT-UPDATE`)

YAML `data/use_cases/project-membership/UC-PROJECT-UPDATE.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-UPDATE.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-UPDATE.svg` · Lane: Project Owner, System · Final: 2 · 690×1090 px ≈ 7.5 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Chỉ thêm comment `Final nodes:`; SVG giống hệt.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Lane: Project Owner và System (BR-PROJECT-OWNER-ADMINISTRATION).
- NF4 «Validates and saves» được tách thành «Validate…» (trước vòng AF-01) và «Save…» (sau khi kiểm tra EX-01). Cả hai trace NF4.
- EX-01 «Ownership changes before the update is saved» được kiểm tra ngay trước Save. Action reject là EXPLICIT vì YAML có «the operation is rejected».
- POST2 được thể hiện bằng action «Record the change in project activity history».
- End node: F1 (EX-01, không đổi) và F2 (đã cập nhật) khác kết quả. Header đã bổ sung `Final nodes:`.
- Giới hạn layout đã biết: vòng lặp AF-01 có hai chỗ cắt đường (PlantUML `while`).

#### Bảng A — UC Spec → Diagram (UC-08)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Owner chooses to edit project information.» | «Request to update project information» (Project Owner) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE3 | «The actor is authenticated.»; «The actor is the current Project Owner.»; «The project is active.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Requests to update project information.» | «Request to update project information» (Project Owner) | Đạt |
| NF2 (System) | «Presents the current project information.» | «Present the current project information» (System) | Đạt |
| NF3 (User) | «Changes the permitted values and submits the update.» | «Change the permitted values and submit the update» (Project Owner) | Đạt |
| NF4 (System) | «Validates and saves the updated information.» | «Validate the updated information» (System); «Save the updated information» (System) | Đạt |
| NF5 (System) | «Confirms the successful update.» | «Confirm the successful update» (System) | Đạt |
| AF-01 condition | «One or more submitted values are invalid.» | [invalid — AF-01] tại «Submitted values invalid?» | Đạt |
| AF-01.1 | «The system rejects the update and identifies the invalid values.» | «Reject the update and identify the invalid values» (System) | Đạt |
| AF-01.2 | «The Project Owner corrects and resubmits the information.» | «Correct and resubmit the information» (Project Owner) | Đạt |
| EX-01 | «Ownership changes before the update is saved, so the operation is rejected.» | [ownership changed — EX-01] tại «Ownership unchanged?»; «Reject the update because ownership changed» (System) | Đạt |
| POST1 | «Valid project information is updated.» | «Save the updated information» (System) | Đạt |
| POST2 | «The change is recorded in project activity history.» | «Record the change in project activity history» (System) | Đạt |
| BR-PROJECT-OWNER-ADMINISTRATION | «Only the Project Owner may update project information, manage project membership, assign Scrum accountabilities, transfer project ownership, or archive the project.» | Thể hiện bằng partition «Project Owner»; điều kiện là PRE2, không vẽ thành bước kiểm tra. | Đạt |
| BR-PROJECT-ARCHIVED-READ-ONLY | «An archived project and its contained work are read-only.» | Không vẽ: PRE3 «The project is active» đã loại trường hợp archived. | Đạt |

#### Bảng B — Diagram → UC Spec (UC-08)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Request to update project information» (Project Owner) | NF1 «Requests to update project information.» | EXPLICIT |
| Action «Present the current project information» (System) | NF2 «Presents the current project information.» | EXPLICIT |
| Action «Change the permitted values and submit the update» (Project Owner) | NF3 «Changes the permitted values and submits the update.» | EXPLICIT |
| Action «Validate the updated information» (System) | NF4 «Validates and saves the updated information.» | EXPLICIT |
| Loop decision «Submitted values invalid?» (System) | AF-01 «One or more submitted values are invalid.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [invalid — AF-01] | AF-01 «One or more submitted values are invalid.» | NECESSARY UML REPRESENTATION |
| Action «Reject the update and identify the invalid values» (System) | AF-01.1 «The system rejects the update and identifies the invalid values.» | EXPLICIT |
| Action «Correct and resubmit the information» (Project Owner) | AF-01.2 «The Project Owner corrects and resubmits the information.» | EXPLICIT |
| Guard [valid] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Decision «Ownership unchanged?» (System) | EX-01 «Ownership changes before the update is saved, so the operation is rejected.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [unchanged] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [ownership changed — EX-01] | EX-01 «Ownership changes before the update is saved, so the operation is rejected.» | NECESSARY UML REPRESENTATION |
| Action «Reject the update because ownership changed» (System) | EX-01 «Ownership changes before the update is saved, so the operation is rejected.» | EXPLICIT — EX-01 nêu rõ «the operation is rejected». |
| Activity Final F1 (sau [ownership changed — EX-01]) | Kết quả: cập nhật bị từ chối, thông tin không đổi (EX-01) | NECESSARY UML REPRESENTATION |
| Action «Save the updated information» (System) | NF4 «Validates and saves the updated information.»; POST1 «Valid project information is updated.» | EXPLICIT |
| Action «Record the change in project activity history» (System) | POST2 «The change is recorded in project activity history.» | EXPLICIT |
| Action «Confirm the successful update» (System) | NF5 «Confirms the successful update.» | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: thông tin được cập nhật và ghi lịch sử (POST1, POST2) | NECESSARY UML REPRESENTATION |

### UC-09.1 — View Project Members (`UC-PROJECT-MEMBERS-VIEW`)

YAML `data/use_cases/project-membership/UC-PROJECT-MEMBERS-VIEW.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-MEMBERS-VIEW.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBERS-VIEW.svg` · Lane: User, System · Final: 2 · 717×719 px ≈ 9.1 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Chỉ thêm comment `Final nodes:`; SVG giống hệt.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Lane: User và System.
- EX-01 (dữ liệu tạm thời không có) được kiểm tra ngay sau NF2. AF-01 (chỉ có Project Owner) rẽ nhánh trước NF3.
- NF3 và AF-01.1 cùng kết quả «danh sách được hiển thị» nên hội tụ một final. EX-01 có final riêng. Header đã bổ sung `Final nodes:`.
- Không có action từ precondition.

#### Bảng A — UC Spec → Diagram (UC-09.1)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «A Project Member opens the project member list.» | «Open the project member list» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE2 | «The User is an active member of the project.»; «The project is accessible.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Opens the project member list.» | «Open the project member list» (User) | Đạt |
| NF2 (System) | «Retrieves active members and their project-scoped assignments.» | «Retrieve active members and their project-scoped assignments» (System) | Đạt |
| NF3 (System) | «Displays the member list.» | «Display the member list» (System) | Đạt |
| AF-01 condition | «The project has no members other than its Project Owner.» | [Project Owner only — AF-01] tại «Other members?» | Đạt |
| AF-01.1 | «The system displays only the Project Owner.» | «Display only the Project Owner» (System) | Đạt |
| EX-01 | «Membership information is temporarily unavailable.» | [unavailable — EX-01] tại «Membership information available?»; «Report that membership information is temporarily unavailable» (System) | Đạt |
| POST1 | «Current project membership information is displayed without modification.» | «Display the member list» (System) | Đạt |
| BR-PROJECT-MEMBER-ACCESS | «Project information is available only to active members of that project.» | Không vẽ: PRE1 «active member»; BR không tạo nhánh. | Đạt |

#### Bảng B — Diagram → UC Spec (UC-09.1)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Open the project member list» (User) | NF1 «Opens the project member list.» | EXPLICIT |
| Action «Retrieve active members and their project-scoped assignments» (System) | NF2 «Retrieves active members and their project-scoped assignments.» | EXPLICIT |
| Decision «Membership information available?» (System) | EX-01 «Membership information is temporarily unavailable.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [available] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [unavailable — EX-01] | EX-01 «Membership information is temporarily unavailable.» | NECESSARY UML REPRESENTATION |
| Action «Report that membership information is temporarily unavailable» (System) | EX-01 «Membership information is temporarily unavailable.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F1 (sau [unavailable — EX-01]) | Kết quả: không hiển thị danh sách (EX-01) | NECESSARY UML REPRESENTATION |
| Decision «Other members?» (System) | AF-01 «The project has no members other than its Project Owner.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [other members] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Display the member list» (System) | NF3 «Displays the member list.»; POST1 «Current project membership information is displayed without modification.» | EXPLICIT |
| Guard [Project Owner only — AF-01] | AF-01 «The project has no members other than its Project Owner.» | NECESSARY UML REPRESENTATION |
| Action «Display only the Project Owner» (System) | AF-01.1 «The system displays only the Project Owner.» | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: danh sách thành viên được hiển thị (POST1) | NECESSARY UML REPRESENTATION |

### UC-09.2 — Add Project Member (`UC-PROJECT-MEMBER-ADD`)

YAML `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-ADD.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-ADD.svg` · Lane: Project Owner, System · Final: 2 · 916×827 px ≈ 7.1 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Không đổi (`.puml` và SVG giữ nguyên).

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Xem ví dụ đầy đủ ở guide mục 7.
- NF4 được tách thành hai decision độc lập; thứ tự không đổi kết quả.
- F1 (tạo membership) và F2 (không đổi; AF-01 và EX-01 gộp qua merge) đã có giải thích trong header.

#### Bảng A — UC Spec → Diagram (UC-09.2)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Owner chooses to add a member to the project.» | «Open project membership management and choose to add a member» (Project Owner) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE3 | «The actor is the current Project Owner.»; «The project is active.»; «The target User account is active.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Opens project membership management and chooses to add a member.» | «Open project membership management and choose to add a member» (Project Owner) | Đạt |
| NF2 (System) | «Requests an existing User account.» | «Request an existing User account» (System) | Đạt |
| NF3 (User) | «Selects the User and confirms the addition.» | «Select the User and confirm the addition» (Project Owner) | Đạt |
| NF4 (System) | «Verifies that the User is active and is not already a member.» | «Verify that the User is active and is not already a member» (System) | Đạt |
| NF5 (System) | «Creates the membership and refreshes the member list.» | «Create the membership and refresh the member list» (System) | Đạt |
| AF-01 condition | «The selected User is already a project member.» | [already a member — AF-01] tại «Already a member?» | Đạt |
| AF-01.1 | «The system reports that no new membership is required.» | «Report that no new membership is required» (System) | Đạt |
| EX-01 | «The selected User account becomes inactive before confirmation.» | [became inactive — EX-01] tại «Account still active?»; «Reject the addition of the inactive account» (System) | Đạt |
| POST1 | «The target User becomes an active Project Member.» | «Create the membership and refresh the member list» (System) | Đạt |
| POST2 | «The membership change is recorded in project activity history.» | «Record the membership change in project activity history» (System) | Đạt |
| BR-ACTIVE-USER-REQUIRED | «Only an active authenticated User can create or access a project.» | «Verify that the User is active and is not already a member» (System) | Đạt |
| BR-PROJECT-OWNER-ADMINISTRATION | «Only the Project Owner may update project information, manage project membership, assign Scrum accountabilities, transfer project ownership, or archive the project.» | Thể hiện bằng partition «Project Owner» (PRE1). | Đạt |

#### Bảng B — Diagram → UC Spec (UC-09.2)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Open project membership management and choose to add a member» (Project Owner) | NF1 «Opens project membership management and chooses to add a member.» | EXPLICIT |
| Action «Request an existing User account» (System) | NF2 «Requests an existing User account.» | EXPLICIT |
| Action «Select the User and confirm the addition» (Project Owner) | NF3 «Selects the User and confirms the addition.» | EXPLICIT |
| Action «Verify that the User is active and is not already a member» (System) | NF4 «Verifies that the User is active and is not already a member.»; BR-ACTIVE-USER-REQUIRED | EXPLICIT |
| Decision «Already a member?» (System) | AF-01 «The selected User is already a project member.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [not a member] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Decision «Account still active?» (System) | EX-01 «The selected User account becomes inactive before confirmation.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [active] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Action «Create the membership and refresh the member list» (System) | NF5 «Creates the membership and refreshes the member list.»; POST1 «The target User becomes an active Project Member.» | EXPLICIT |
| Action «Record the membership change in project activity history» (System) | POST2 «The membership change is recorded in project activity history.» | EXPLICIT |
| Activity Final F1 (sau [not a member] > [active]) | Kết quả: membership được tạo (POST1, POST2) | NECESSARY UML REPRESENTATION |
| Guard [became inactive — EX-01] | EX-01 «The selected User account becomes inactive before confirmation.» | NECESSARY UML REPRESENTATION |
| Action «Reject the addition of the inactive account» (System) | EX-01 «The selected User account becomes inactive before confirmation.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Guard [already a member — AF-01] | AF-01 «The selected User is already a project member.» | NECESSARY UML REPRESENTATION |
| Action «Report that no new membership is required» (System) | AF-01.1 «The system reports that no new membership is required.» | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: không thay đổi membership (AF-01, EX-01) | NECESSARY UML REPRESENTATION |

### UC-09.3 — Remove Project Member (`UC-PROJECT-MEMBER-REMOVE`)

YAML `data/use_cases/project-membership/UC-PROJECT-MEMBER-REMOVE.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-REMOVE.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-REMOVE.svg` · Lane: Project Owner, System · Final: 2 · 983×815 px ≈ 6.7 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Không đổi.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Sau PR #8, PRE3 là «The target User is an active Project Member», nên EX-01 (Project Owner tự xóa mình) không còn mâu thuẫn precondition. Diagram đã vẽ EX-01 thành bước kiểm tra ngay sau NF1, không cần sửa.
- Observation cũ trong manifest («contradicts a precondition») đã lỗi thời; xem mục 7 về đề xuất cập nhật manifest.
- AF-01: YAML chỉ ghi «requires the work to be reassigned before removal». Diagram kết thúc UC sau bước này (JUSTIFIED DERIVATION). Reviewer cần xác nhận cách hiểu này.
- F1 (đã xóa) và F2 (không đổi; AF-01 và EX-01 gộp) có giải thích trong header.

#### Bảng A — UC Spec → Diagram (UC-09.3)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Owner chooses to remove a member from the project.» | «Select a project member and request removal» (Project Owner) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE3 | «The actor is the current Project Owner.»; «The project is active.»; «The target User is an active Project Member.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Selects a project member and requests removal.» | «Select a project member and request removal» (Project Owner) | Đạt |
| NF2 (System) | «Displays the member's active assignments and asks for confirmation.» | «Display the member's active assignments and ask for confirmation» (System) | Đạt |
| NF3 (User) | «Confirms removal after active work has been reassigned or cleared.» | «Confirm the removal» (Project Owner) | Đạt |
| NF4 (System) | «Removes Scrum accountabilities and project membership.» | «Remove Scrum accountabilities and project membership» (System) | Đạt |
| NF5 (System) | «Records the removal and refreshes the member list.» | «Record the removal and refresh the member list» (System) | Đạt |
| AF-01 condition | «The target member owns unfinished Sprint work.» | [owns unfinished work — AF-01] tại «Unfinished Sprint work?» | Đạt |
| AF-01.1 | «The system requires the work to be reassigned before removal.» | «Require the work to be reassigned before removal» (System) | Đạt |
| EX-01 | «The Project Owner attempts to remove their own membership.» | [own membership — EX-01] tại «Own membership selected?»; «Reject the removal of the Project Owner's own membership» (System) | Đạt |
| POST1 | «The target User no longer has access through project membership.» | «Remove Scrum accountabilities and project membership» (System) | Đạt |
| POST2 | «The removal is recorded in project activity history.» | «Record the removal and refresh the member list» (System) | Đạt |
| BR-PROJECT-ONE-OWNER | «Every active project must have exactly one Project Owner.» | «Reject the removal of the Project Owner's own membership» (System) | Đạt |
| BR-PROJECT-OWNER-ADMINISTRATION | «Only the Project Owner may update project information, manage project membership, assign Scrum accountabilities, transfer project ownership, or archive the project.» | Thể hiện bằng partition «Project Owner» (PRE1). | Đạt |

#### Bảng B — Diagram → UC Spec (UC-09.3)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Select a project member and request removal» (Project Owner) | NF1 «Selects a project member and requests removal.» | EXPLICIT |
| Decision «Own membership selected?» (System) | EX-01 «The Project Owner attempts to remove their own membership.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [another member] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Action «Display the member's active assignments and ask for confirmation» (System) | NF2 «Displays the member's active assignments and asks for confirmation.» | EXPLICIT |
| Decision «Unfinished Sprint work?» (System) | AF-01 «The target member owns unfinished Sprint work.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [none] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Confirm the removal» (Project Owner) | NF3 «Confirms removal after active work has been reassigned or cleared.» | EXPLICIT |
| Action «Remove Scrum accountabilities and project membership» (System) | NF4 «Removes Scrum accountabilities and project membership.»; POST1 «The target User no longer has access through project membership.» | EXPLICIT |
| Action «Record the removal and refresh the member list» (System) | NF5 «Records the removal and refreshes the member list.»; POST2 «The removal is recorded in project activity history.» | EXPLICIT |
| Activity Final F1 (sau [another member] > [none]) | Kết quả: thành viên bị xóa (POST1, POST2) | NECESSARY UML REPRESENTATION |
| Guard [owns unfinished work — AF-01] | AF-01 «The target member owns unfinished Sprint work.» | NECESSARY UML REPRESENTATION — AF-01 kết thúc UC (JUSTIFIED DERIVATION: YAML không nói UC tiếp tục sau khi yêu cầu reassign). |
| Action «Require the work to be reassigned before removal» (System) | AF-01.1 «The system requires the work to be reassigned before removal.» | EXPLICIT |
| Guard [own membership — EX-01] | EX-01 «The Project Owner attempts to remove their own membership.» | NECESSARY UML REPRESENTATION |
| Action «Reject the removal of the Project Owner's own membership» (System) | EX-01 «The Project Owner attempts to remove their own membership.»; BR-PROJECT-ONE-OWNER; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F2 (sau luồng chính) | Kết quả: membership không đổi (AF-01, EX-01) | NECESSARY UML REPRESENTATION |

### UC-10 — Assign Scrum Accountability (`UC-SCRUM-ACCOUNTABILITY-ASSIGN`)

YAML `data/use_cases/project-membership/UC-SCRUM-ACCOUNTABILITY-ASSIGN.yml` · Source `diagrams/activity/project-membership/source/UC-SCRUM-ACCOUNTABILITY-ASSIGN.puml` · SVG `diagrams/activity/project-membership/svg/UC-SCRUM-ACCOUNTABILITY-ASSIGN.svg` · Lane: Project Owner, System · Final: 3 · 867×1137 px ≈ 7.2 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Sửa `.puml` (thêm AF-02, cấu trúc lại nhánh EX-01, header `Final nodes:`) và render lại SVG.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- **Lỗi đã sửa (bằng chứng):** PR #8 thêm AF-02 «The Project Owner does not confirm the Product Owner replacement → keeps the current Scrum accountabilities unchanged». Diagram trên develop thiếu AF-02, và validator báo `alternative flow AF-02 is not represented`.
- Sau sửa: decision «Confirm the replacement?» nằm ở lane Project Owner. [confirm — AF-01] → «Confirm the replacement» → «Transfer the Product Owner accountability». [not confirmed — AF-02] → «Keep the current Scrum accountabilities unchanged» → final.
- BR-PRODUCT-OWNER-ACCOUNTABILITY-UNIQUE (đã sửa ở PR #8: thay thế sau khi Project Owner xác nhận) giờ khớp cả AF-01 và AF-02. Hai observation cũ trong manifest đã lỗi thời.
- End node: F1 (AF-02) và F3 (EX-01) cùng kết quả «accountability không đổi» nhưng giữ riêng. AF-02 phải bỏ qua bước kiểm tra EX-01 và NF5, mà nhánh AF-01 dùng chung với luồng chính; gộp lại sẽ phải vẽ lại hai bước đó. Đây là cùng ngoại lệ đã chấp nhận ở UC-13 và đã ghi trong header.
- Trình bày: EX-01 chuyển sang dạng `then` (luồng chính) / `else` (exception ngang). Nhờ đó hết lỗi chữ «[left or removed» bị đường cắt, và chiều cao giảm từ 1336 xuống 1137 px.
- «Confirm the replacement» trace AF-01 (JUSTIFIED DERIVATION, suy từ «after confirmation»), không trace AF-01.2 vì AF-01.2 là bước của System.

#### Bảng A — UC Spec → Diagram (UC-10)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Owner chooses to assign a Scrum accountability to a project member.» | «Select an active project member» (Project Owner) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE3 | «The actor is the current Project Owner.»; «The target User is an active member of the project.»; «The project is active.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Selects an active project member.» | «Select an active project member» (Project Owner) | Đạt |
| NF2 (System) | «Displays the member's current Scrum accountability.» | «Display the member's current Scrum accountability» (System) | Đạt |
| NF3 (User) | «Selects Product Owner or Developer.» | «Select Product Owner or Developer» (Project Owner) | Đạt |
| NF4 (System) | «Validates the assignment against project constraints.» | «Validate the assignment against project constraints» (System) | Đạt |
| NF5 (System) | «Saves and confirms the project-scoped accountability.» | «Save and confirm the project-scoped accountability» (System) | Đạt |
| AF-01 condition | «Assigning Product Owner would leave the project with conflicting accountability assignments.» | [conflicting assignment — AF-01] tại «Conflicting Product Owner?»; [confirm — AF-01] tại «Confirm the replacement?» | Đạt |
| AF-01.1 | «The system requests confirmation of the replacement.» | «Request confirmation of the replacement» (System) | Đạt |
| AF-01.2 | «The system transfers Product Owner accountability after confirmation.» | «Transfer the Product Owner accountability» (System) | Đạt |
| AF-02 condition | «The Project Owner does not confirm the Product Owner replacement.» | [not confirmed — AF-02] tại «Confirm the replacement?» | Đạt |
| AF-02.1 | «The system keeps the current Scrum accountabilities unchanged.» | «Keep the current Scrum accountabilities unchanged» (System) | Đạt |
| EX-01 | «The target member leaves or is removed before the assignment is saved.» | [left or removed — EX-01] tại «Member still in the project?»; «Reject the assignment for the departed member» (System) | Đạt |
| POST1 | «The selected Scrum accountability is assigned within the project.» | «Save and confirm the project-scoped accountability» (System) | Đạt |
| POST2 | «The accountability change is recorded in activity history.» | «Record the accountability change in activity history» (System) | Đạt |
| BR-SCRUM-ACCOUNTABILITY-PROJECT-SCOPED | «A Scrum accountability is assigned to an active member within one project and does not apply to other projects.» | «Validate the assignment against project constraints» (System) | Đạt |
| BR-PROJECT-OWNER-ADMINISTRATION | «Only the Project Owner may update project information, manage project membership, assign Scrum accountabilities, transfer project ownership, or archive the project.» | Thể hiện bằng partition «Project Owner» (PRE1). | Đạt |
| BR-PRODUCT-OWNER-ACCOUNTABILITY-UNIQUE | «A project has at most one active Product Owner accountability at a time; assigning a new Product Owner replaces the previous one once the Project Owner confirms the replacement.» | «Transfer the Product Owner accountability» (System); «Keep the current Scrum accountabilities unchanged» (System) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-10)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Select an active project member» (Project Owner) | NF1 «Selects an active project member.» | EXPLICIT |
| Action «Display the member's current Scrum accountability» (System) | NF2 «Displays the member's current Scrum accountability.» | EXPLICIT |
| Action «Select Product Owner or Developer» (Project Owner) | NF3 «Selects Product Owner or Developer.» | EXPLICIT |
| Action «Validate the assignment against project constraints» (System) | NF4 «Validates the assignment against project constraints.»; BR-SCRUM-ACCOUNTABILITY-PROJECT-SCOPED | EXPLICIT |
| Decision «Conflicting Product Owner?» (System) | AF-01 «Assigning Product Owner would leave the project with conflicting accountability assignments.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [no conflict] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Guard [conflicting assignment — AF-01] | AF-01 «Assigning Product Owner would leave the project with conflicting accountability assignments.» | NECESSARY UML REPRESENTATION |
| Action «Request confirmation of the replacement» (System) | AF-01.1 «The system requests confirmation of the replacement.» | EXPLICIT |
| Decision «Confirm the replacement?» (Project Owner) | AF-01 «Assigning Product Owner would leave the project with conflicting accountability assignments.»; AF-02 «The Project Owner does not confirm the Product Owner replacement.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01, AF-02 |
| Guard [confirm — AF-01] | AF-01 «Assigning Product Owner would leave the project with conflicting accountability assignments.» | NECESSARY UML REPRESENTATION |
| Action «Confirm the replacement» (Project Owner) | AF-01.2 «The system transfers Product Owner accountability after confirmation.»; AF-02 «The Project Owner does not confirm the Product Owner replacement.» | JUSTIFIED DERIVATION — AF-01.2 «…after confirmation» và AF-02 «does not confirm» ngụ ý Project Owner xác nhận; YAML không có bước actor riêng. |
| Action «Transfer the Product Owner accountability» (System) | AF-01.2 «The system transfers Product Owner accountability after confirmation.»; BR-PRODUCT-OWNER-ACCOUNTABILITY-UNIQUE | EXPLICIT |
| Guard [not confirmed — AF-02] | AF-02 «The Project Owner does not confirm the Product Owner replacement.» | NECESSARY UML REPRESENTATION |
| Action «Keep the current Scrum accountabilities unchanged» (System) | AF-02.1 «The system keeps the current Scrum accountabilities unchanged.»; BR-PRODUCT-OWNER-ACCOUNTABILITY-UNIQUE | EXPLICIT |
| Activity Final F1 (sau [conflicting assignment — AF-01] > [not confirmed — AF-02]) | Kết quả: accountability không đổi (AF-02) | NECESSARY UML REPRESENTATION |
| Decision «Member still in the project?» (System) | EX-01 «The target member leaves or is removed before the assignment is saved.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [still a member] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Action «Save and confirm the project-scoped accountability» (System) | NF5 «Saves and confirms the project-scoped accountability.»; POST1 «The selected Scrum accountability is assigned within the project.» | EXPLICIT |
| Action «Record the accountability change in activity history» (System) | POST2 «The accountability change is recorded in activity history.» | EXPLICIT |
| Activity Final F2 (sau [still a member]) | Kết quả: accountability được lưu (POST1, POST2) | NECESSARY UML REPRESENTATION |
| Guard [left or removed — EX-01] | EX-01 «The target member leaves or is removed before the assignment is saved.» | NECESSARY UML REPRESENTATION |
| Action «Reject the assignment for the departed member» (System) | EX-01 «The target member leaves or is removed before the assignment is saved.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F3 (sau [left or removed — EX-01]) | Kết quả: accountability không đổi (EX-01) | NECESSARY UML REPRESENTATION |

### UC-11 — Archive Project (`UC-PROJECT-ARCHIVE`)

YAML `data/use_cases/project-membership/UC-PROJECT-ARCHIVE.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-ARCHIVE.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-ARCHIVE.svg` · Lane: Project Owner, System · Final: 2 · 1062×796 px ≈ 6.2 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Không đổi.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Sau PR #8, precondition «no active Sprint» đã bị bỏ, nên EX-01 (có Sprint đang chạy) khớp NF2 «Checks that the project has no active Sprint». Diagram không cần sửa; observation cũ trong manifest đã lỗi thời.
- Decision «Confirm archival?» nằm ở lane Project Owner (lựa chọn của actor).
- F1 (đã archive) và F2 (giữ nguyên; AF-01 và EX-01 gộp) có giải thích trong header.
- Cỡ chữ 6,2 pt, sát ngưỡng nhưng đạt.

#### Bảng A — UC Spec → Diagram (UC-11)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Owner chooses to archive the project.» | «Request project archival» (Project Owner) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE2 | «The actor is the current Project Owner.»; «The project is active.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Requests project archival.» | «Request project archival» (Project Owner) | Đạt |
| NF2 (System) | «Checks that the project has no active Sprint.» | «Check that the project has no active Sprint» (System) | Đạt |
| NF3 (System) | «Summarizes the effects of archival and requests confirmation.» | «Summarize the effects of archival and request confirmation» (System) | Đạt |
| NF4 (User) | «Confirms archival.» | «Confirm archival» (Project Owner) | Đạt |
| NF5 (System) | «Marks the project and its contained work as read-only.» | «Mark the project and its contained work as read-only» (System) | Đạt |
| AF-01 condition | «The Project Owner cancels the confirmation.» | [cancel — AF-01] tại «Confirm archival?» | Đạt |
| AF-01.1 | «The system leaves the project active and unchanged.» | «Leave the project active and unchanged» (System) | Đạt |
| EX-01 | «The project has an active Sprint and cannot be archived.» | [active Sprint — EX-01] tại «Active Sprint?»; «Reject the archival because the project has an active Sprint» (System) | Đạt |
| POST1 | «The project is archived.» | «Mark the project and its contained work as read-only» (System) | Đạt |
| POST2 | «Project information remains available in read-only mode.» | «Mark the project and its contained work as read-only» (System) | Đạt |
| BR-PROJECT-OWNER-ADMINISTRATION | «Only the Project Owner may update project information, manage project membership, assign Scrum accountabilities, transfer project ownership, or archive the project.» | Thể hiện bằng partition «Project Owner» (PRE1). | Đạt |
| BR-PROJECT-ARCHIVED-READ-ONLY | «An archived project and its contained work are read-only.» | «Mark the project and its contained work as read-only» (System) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-11)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Request project archival» (Project Owner) | NF1 «Requests project archival.» | EXPLICIT |
| Action «Check that the project has no active Sprint» (System) | NF2 «Checks that the project has no active Sprint.» | EXPLICIT |
| Decision «Active Sprint?» (System) | EX-01 «The project has an active Sprint and cannot be archived.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [none] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Action «Summarize the effects of archival and request confirmation» (System) | NF3 «Summarizes the effects of archival and requests confirmation.» | EXPLICIT |
| Decision «Confirm archival?» (Project Owner) | AF-01 «The Project Owner cancels the confirmation.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [confirm] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Confirm archival» (Project Owner) | NF4 «Confirms archival.» | EXPLICIT |
| Action «Mark the project and its contained work as read-only» (System) | NF5 «Marks the project and its contained work as read-only.»; POST1 «The project is archived.»; POST2 «Project information remains available in read-only mode.»; BR-PROJECT-ARCHIVED-READ-ONLY | EXPLICIT |
| Activity Final F1 (sau [none] > [confirm]) | Kết quả: dự án được archive (POST1, POST2) | NECESSARY UML REPRESENTATION |
| Guard [cancel — AF-01] | AF-01 «The Project Owner cancels the confirmation.» | NECESSARY UML REPRESENTATION |
| Action «Leave the project active and unchanged» (System) | AF-01.1 «The system leaves the project active and unchanged.» | EXPLICIT |
| Guard [active Sprint — EX-01] | EX-01 «The project has an active Sprint and cannot be archived.» | NECESSARY UML REPRESENTATION |
| Action «Reject the archival because the project has an active Sprint» (System) | EX-01 «The project has an active Sprint and cannot be archived.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F2 (sau luồng chính) | Kết quả: dự án giữ nguyên active (AF-01, EX-01) | NECESSARY UML REPRESENTATION |

### UC-12 — Transfer Project Ownership (`UC-PROJECT-OWNERSHIP-TRANSFER`)

YAML `data/use_cases/project-membership/UC-PROJECT-OWNERSHIP-TRANSFER.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-OWNERSHIP-TRANSFER.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-OWNERSHIP-TRANSFER.svg` · Lane: Project Owner, System · Final: 2 · 731×973 px ≈ 8.4 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Chỉ thêm comment `Final nodes:`; SVG giống hệt.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Lane: Project Owner và System.
- AF-01 là vòng `while`: reject → chọn thành viên khác → quay lại kiểm tra (AF-01.2).
- EX-01 (ownership đổi đồng thời) kiểm tra trước NF5.
- POST2 và BR-SCRUM-ACCOUNTABILITY-PROJECT-SCOPED được thỏa vì không có action xóa membership hay đổi accountability.
- F1 (EX-01) và F2 (đã chuyển) khác kết quả. Header đã bổ sung `Final nodes:`.
- Giới hạn layout đã biết: vòng lặp AF-01 cắt đường.

#### Bảng A — UC Spec → Diagram (UC-12)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Owner chooses an active member as the new owner.» | «Select Transfer Project Ownership» (Project Owner) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE3 | «The actor is the current Project Owner.»; «The target User is an active Project Member.»; «The project is active.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Selects Transfer Project Ownership.» | «Select Transfer Project Ownership» (Project Owner) | Đạt |
| NF2 (System) | «Displays eligible active Project Members.» | «Display eligible active Project Members» (System) | Đạt |
| NF3 (User) | «Selects the new owner and confirms the transfer.» | «Select the new owner and confirm the transfer» (Project Owner) | Đạt |
| NF4 (System) | «Validates both memberships and the current ownership state.» | «Validate both memberships and the current ownership state» (System) | Đạt |
| NF5 (System) | «Transfers ownership atomically and records the change.» | «Transfer ownership atomically and record the change» (System) | Đạt |
| AF-01 condition | «The selected member is no longer active in the project.» | [inactive — AF-01] tại «Selected member inactive?» | Đạt |
| AF-01.1 | «The system rejects the transfer.» | «Reject the transfer to the inactive member» (System) | Đạt |
| AF-01.2 | «The Project Owner selects another eligible member.» | «Select another eligible member» (Project Owner) | Đạt |
| EX-01 | «Ownership changed concurrently before the transfer was committed.» | [changed concurrently — EX-01] tại «Ownership unchanged?»; «Reject the transfer because ownership changed concurrently» (System) | Đạt |
| POST1 | «The target member becomes the sole Project Owner.» | «Transfer ownership atomically and record the change» (System) | Đạt |
| POST2 | «The previous owner remains a Project Member unless that User later leaves.» | Không cần node: không có action nào xóa membership của owner cũ. | Đạt |
| POST3 | «The transfer is recorded in project and system audit history.» | «Transfer ownership atomically and record the change» (System) | Đạt |
| BR-PROJECT-ONE-OWNER | «Every active project must have exactly one Project Owner.» | «Transfer ownership atomically and record the change» (System) | Đạt |
| BR-PROJECT-OWNER-TRANSFER-BEFORE-LEAVE | «A Project Owner must transfer ownership before leaving the project.» | Không ảnh hưởng luồng của UC này (áp dụng cho UC-13 Leave Project). | Đạt |
| BR-PROJECT-OWNER-ADMINISTRATION | «Only the Project Owner may update project information, manage project membership, assign Scrum accountabilities, transfer project ownership, or archive the project.» | Thể hiện bằng partition «Project Owner» (PRE1). | Đạt |
| BR-SCRUM-ACCOUNTABILITY-PROJECT-SCOPED | «A Scrum accountability is assigned to an active member within one project and does not apply to other projects.» | Không cần node: other_information «new owner retains the member's existing Scrum accountability»; không có action đổi accountability. | Đạt |

#### Bảng B — Diagram → UC Spec (UC-12)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Select Transfer Project Ownership» (Project Owner) | NF1 «Selects Transfer Project Ownership.» | EXPLICIT |
| Action «Display eligible active Project Members» (System) | NF2 «Displays eligible active Project Members.» | EXPLICIT |
| Action «Select the new owner and confirm the transfer» (Project Owner) | NF3 «Selects the new owner and confirms the transfer.» | EXPLICIT |
| Action «Validate both memberships and the current ownership state» (System) | NF4 «Validates both memberships and the current ownership state.» | EXPLICIT |
| Loop decision «Selected member inactive?» (System) | AF-01 «The selected member is no longer active in the project.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [inactive — AF-01] | AF-01 «The selected member is no longer active in the project.» | NECESSARY UML REPRESENTATION |
| Action «Reject the transfer to the inactive member» (System) | AF-01.1 «The system rejects the transfer.» | EXPLICIT |
| Action «Select another eligible member» (Project Owner) | AF-01.2 «The Project Owner selects another eligible member.» | EXPLICIT |
| Guard [active] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Decision «Ownership unchanged?» (System) | EX-01 «Ownership changed concurrently before the transfer was committed.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [unchanged] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [changed concurrently — EX-01] | EX-01 «Ownership changed concurrently before the transfer was committed.» | NECESSARY UML REPRESENTATION |
| Action «Reject the transfer because ownership changed concurrently» (System) | EX-01 «Ownership changed concurrently before the transfer was committed.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F1 (sau [changed concurrently — EX-01]) | Kết quả: chuyển quyền bị từ chối, owner không đổi (EX-01) | NECESSARY UML REPRESENTATION |
| Action «Transfer ownership atomically and record the change» (System) | NF5 «Transfers ownership atomically and records the change.»; POST1 «The target member becomes the sole Project Owner.»; POST3 «The transfer is recorded in project and system audit history.»; BR-PROJECT-ONE-OWNER | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: quyền sở hữu được chuyển và ghi nhận (POST1–POST3) | NECESSARY UML REPRESENTATION |

### UC-13 — Leave Project (`UC-PROJECT-LEAVE`)

YAML `data/use_cases/project-membership/UC-PROJECT-LEAVE.yml` · Source `diagrams/activity/project-membership/source/UC-PROJECT-LEAVE.puml` · SVG `diagrams/activity/project-membership/svg/UC-PROJECT-LEAVE.svg` · Lane: User, System · Final: 3 · 935×1090 px ≈ 7.0 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Không đổi.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Sau PR #8, precondition «actor is not the current Project Owner» đã bị bỏ, nên EX-01 khớp. Observation cũ trong manifest đã lỗi thời.
- AF-01: cảnh báo, sau đó decision «Leave anyway?» ở lane User. [confirm] đi tới NF5 (thay cho NF3–NF4); [cancel] dẫn tới «Cancel the leave request».
- End node: F1 (EX-01) và F2 (hủy) cùng kết quả «membership không đổi» nhưng giữ riêng, vì gộp sẽ phải vẽ NF5 hai lần. Ngoại lệ này đã được chấp nhận ở audit và ghi trong header. F3 là kết quả đã rời dự án.

#### Bảng A — UC Spec → Diagram (UC-13)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Member chooses to leave the project.» | «Request to leave the project» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE2 | «The actor is an active member of the project.»; «The project is active.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Requests to leave the project.» | «Request to leave the project» (User) | Đạt |
| NF2 (System) | «Checks ownership and unfinished work constraints.» | «Check ownership and unfinished work constraints» (System) | Đạt |
| NF3 (System) | «Explains the effects of leaving and requests confirmation.» | «Explain the effects of leaving and request confirmation» (System) | Đạt |
| NF4 (User) | «Confirms leaving the project.» | «Confirm leaving the project» (User) | Đạt |
| NF5 (System) | «Removes active membership and project-scoped permissions.» | «Remove active membership and project-scoped permissions» (System) | Đạt |
| AF-01 condition | «The member owns unfinished Sprint Tasks.» | [owns tasks — AF-01] tại «Unfinished Sprint Tasks?»; [confirm — AF-01] tại «Leave anyway?»; [cancel — AF-01] tại «Leave anyway?» | Đạt |
| AF-01.1 | «The system warns that unfinished work will become unclaimed.» | «Warn that unfinished work will become unclaimed» (System) | Đạt |
| AF-01.2 | «The member confirms leaving or cancels the request.» | «Cancel the leave request» (User) | Đạt |
| EX-01 | «The current Project Owner attempts to leave before transferring ownership.» | [current owner — EX-01] tại «Current Project Owner?»; «Reject the request until ownership is transferred» (System) | Đạt |
| POST1 | «The actor is no longer a member of the project.» | «Remove active membership and project-scoped permissions» (System) | Đạt |
| POST2 | «Project-scoped access and Scrum accountability are removed.» | «Remove active membership and project-scoped permissions» (System) | Đạt |
| POST3 | «Historical contributions remain attributed to the actor.» | «Remove active membership and project-scoped permissions» (System) | Đạt |
| BR-PROJECT-OWNER-TRANSFER-BEFORE-LEAVE | «A Project Owner must transfer ownership before leaving the project.» | «Reject the request until ownership is transferred» (System) | Đạt |
| BR-PROJECT-MEMBER-ACCESS | «Project information is available only to active members of that project.» | Thể hiện gián tiếp: NF5 gỡ project-scoped permissions; điều kiện truy cập là PRE1. | Đạt |

#### Bảng B — Diagram → UC Spec (UC-13)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Request to leave the project» (User) | NF1 «Requests to leave the project.» | EXPLICIT |
| Action «Check ownership and unfinished work constraints» (System) | NF2 «Checks ownership and unfinished work constraints.» | EXPLICIT |
| Decision «Current Project Owner?» (System) | EX-01 «The current Project Owner attempts to leave before transferring ownership.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [not the owner] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [current owner — EX-01] | EX-01 «The current Project Owner attempts to leave before transferring ownership.» | NECESSARY UML REPRESENTATION |
| Action «Reject the request until ownership is transferred» (System) | EX-01 «The current Project Owner attempts to leave before transferring ownership.»; BR-PROJECT-OWNER-TRANSFER-BEFORE-LEAVE; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F1 (sau [current owner — EX-01]) | Kết quả: yêu cầu bị từ chối, membership không đổi (EX-01) | NECESSARY UML REPRESENTATION |
| Decision «Unfinished Sprint Tasks?» (System) | AF-01 «The member owns unfinished Sprint Tasks.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [none] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Explain the effects of leaving and request confirmation» (System) | NF3 «Explains the effects of leaving and requests confirmation.» | EXPLICIT |
| Action «Confirm leaving the project» (User) | NF4 «Confirms leaving the project.» | EXPLICIT |
| Guard [owns tasks — AF-01] | AF-01 «The member owns unfinished Sprint Tasks.» | NECESSARY UML REPRESENTATION |
| Action «Warn that unfinished work will become unclaimed» (System) | AF-01.1 «The system warns that unfinished work will become unclaimed.» | EXPLICIT |
| Decision «Leave anyway?» (User) | AF-01 «The member owns unfinished Sprint Tasks.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [confirm — AF-01] | AF-01 «The member owns unfinished Sprint Tasks.» | NECESSARY UML REPRESENTATION |
| Guard [cancel — AF-01] | AF-01 «The member owns unfinished Sprint Tasks.» | NECESSARY UML REPRESENTATION |
| Action «Cancel the leave request» (User) | AF-01.2 «The member confirms leaving or cancels the request.» | EXPLICIT |
| Activity Final F2 (sau [owns tasks — AF-01] > [cancel — AF-01]) | Kết quả: người dùng hủy, membership không đổi (AF-01.2) | NECESSARY UML REPRESENTATION |
| Action «Remove active membership and project-scoped permissions» (System) | NF5 «Removes active membership and project-scoped permissions.»; POST1 «The actor is no longer a member of the project.»; POST2 «Project-scoped access and Scrum accountability are removed.»; POST3 «Historical contributions remain attributed to the actor.» | EXPLICIT |
| Activity Final F3 (sau luồng chính) | Kết quả: đã rời dự án (POST1–POST3) | NECESSARY UML REPRESENTATION |

### UC-28 — Comment on Work Item (`UC-WORK-ITEM-COMMENT`)

YAML `data/use_cases/collaboration-notification/UC-WORK-ITEM-COMMENT.yml` · Source `diagrams/activity/collaboration-notification/source/UC-WORK-ITEM-COMMENT.puml` · SVG `diagrams/activity/collaboration-notification/svg/UC-WORK-ITEM-COMMENT.svg` · Lane: User, System, Email Service · Final: 2 · 787×1310 px ≈ 6.2 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Sửa `.puml` (EX-01 nhánh ngang, NF5 theo YAML, bỏ decision «Eligible email deliveries?», header `Final nodes:`) và render lại SVG.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- **Lỗi trình bày đã sửa (bằng chứng):**
- Trên develop, nhãn «[none eligible]» nằm bên phải diamond trong khi cạnh của nó đi sang trái, nên người đọc dễ gắn guard nhầm cạnh.
- Chữ guard chỉ ≈ 5,3 pt ở A4 (manifest: REQUEST CHANGES).
- Sau sửa:
- EX-01 chuyển sang nhánh ngang.
- NF5 vẽ đúng hai phần của YAML: «Create in-app notifications for relevant members» và «Request email delivery for eligible members».
- Bỏ decision «Eligible email deliveries?»: YAML không mô tả trường hợp không ai đủ điều kiện, và đây chính là decision có guard đặt sai phía. Đây là đơn giản hóa về phía spec (ít suy diễn hơn), đã ghi trong header.
- Kích thước 787 × 1310 px, ≈ 6,2 pt.
- EX-02 «Record the failed delivery and keep the saved comment» là EXPLICIT (YAML nêu rõ kết quả, BR-NOTIFICATION-DELIVERY-INDEPENDENT). Nhánh này hội tụ vào cùng final với nhánh gửi thành công, vì comment vẫn được lưu.
- AF-01: vòng `while` hỏi lại nội dung. «Enter the comment content» là JUSTIFIED DERIVATION (actor thực hiện lại NF1).
- Giới hạn layout đã biết: vòng lặp AF-01 cắt đường.

#### Bảng A — UC Spec → Diagram (UC-28)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Member needs to communicate about a work item.» | «Open a work item and enter a comment» (User), «Enter the comment content» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE2 | «The actor is an active member of the project.»; «The work item exists and is accessible to the actor.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Opens a work item and enters a comment.» | «Open a work item and enter a comment» (User); «Enter the comment content» (User) | Đạt |
| NF2 (System) | «Validates the comment and referenced members.» | «Validate the comment and referenced members» (System) | Đạt |
| NF3 (User) | «Submits the comment.» | «Submit the comment» (User) | Đạt |
| NF4 (System) | «Saves the comment and records it in activity history.» | «Save the comment and record it in activity history» (System) | Đạt |
| NF5 (System) | «Creates in-app notifications and requests email delivery for eligible mentioned or relevant members.» | «Create in-app notifications for relevant members» (System); «Request email delivery for eligible members» (System) | Đạt |
| NF6 (Email Service) | «Returns the email delivery result to the system.» | «Return the email delivery result» (Email Service) | Đạt |
| AF-01 condition | «The comment contains no content.» | [empty — AF-01] tại «Comment has no content?» | Đạt |
| AF-01.1 | «The system asks the actor to enter content.» | «Ask the actor to enter content» (System) | Đạt |
| EX-01 | «The work item is removed before the comment is submitted.» | [removed — EX-01] tại «Work item still exists?»; «Reject the comment because the work item was removed» (System) | Đạt |
| EX-02 | «An email notification cannot be delivered; the comment and in-app notification remain saved, and the failed delivery is recorded.» | [not delivered — EX-02] tại «Email delivered?»; «Record the failed delivery and keep the saved comment» (System) | Đạt |
| POST1 | «The comment is attached to the work item.» | «Save the comment and record it in activity history» (System) | Đạt |
| POST2 | «Relevant in-app notifications are created and eligible email deliveries are requested.» | «Create in-app notifications for relevant members» (System); «Request email delivery for eligible members» (System) | Đạt |
| BR-COMMENT-PROJECT-MEMBER | «Only an active Project Member can comment on a work item in that project.» | «Open a work item and enter a comment» (User); «Validate the comment and referenced members» (System) | Đạt |
| BR-ACTIVITY-IMMUTABLE | «Automatically recorded work item activity cannot be manually edited or deleted.» | «Save the comment and record it in activity history» (System) | Đạt |
| BR-NOTIFICATION-EMAIL-PREFERENCE | «An email notification is sent only to the intended recipient's verified email address when that User has enabled email delivery.» | «Request email delivery for eligible members» (System) | Đạt |
| BR-NOTIFICATION-DELIVERY-INDEPENDENT | «An email delivery failure must not roll back the originating project operation or remove the corresponding in-app notification.» | «Record the failed delivery and keep the saved comment» (System) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-28)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Open a work item and enter a comment» (User) | NF1 «Opens a work item and enters a comment.»; BR-COMMENT-PROJECT-MEMBER | EXPLICIT |
| Action «Validate the comment and referenced members» (System) | NF2 «Validates the comment and referenced members.»; BR-COMMENT-PROJECT-MEMBER | EXPLICIT |
| Loop decision «Comment has no content?» (System) | AF-01 «The comment contains no content.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [empty — AF-01] | AF-01 «The comment contains no content.» | NECESSARY UML REPRESENTATION |
| Action «Ask the actor to enter content» (System) | AF-01.1 «The system asks the actor to enter content.» | EXPLICIT |
| Action «Enter the comment content» (User) | NF1 «Opens a work item and enters a comment.» | JUSTIFIED DERIVATION — AF-01.1 yêu cầu actor nhập nội dung; actor thực hiện lại NF1 rồi quay lại kiểm tra (§7.5). |
| Guard [content present] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Submit the comment» (User) | NF3 «Submits the comment.» | EXPLICIT |
| Decision «Work item still exists?» (System) | EX-01 «The work item is removed before the comment is submitted.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [exists] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Action «Save the comment and record it in activity history» (System) | NF4 «Saves the comment and records it in activity history.»; POST1 «The comment is attached to the work item.»; BR-ACTIVITY-IMMUTABLE | EXPLICIT |
| Action «Create in-app notifications for relevant members» (System) | NF5 «Creates in-app notifications and requests email delivery for eligible mentioned or relevant members.»; POST2 «Relevant in-app notifications are created and eligible email deliveries are requested.» | EXPLICIT |
| Action «Request email delivery for eligible members» (System) | NF5 «Creates in-app notifications and requests email delivery for eligible mentioned or relevant members.»; POST2 «Relevant in-app notifications are created and eligible email deliveries are requested.»; BR-NOTIFICATION-EMAIL-PREFERENCE | EXPLICIT |
| Action «Return the email delivery result» (Email Service) | NF6 «Returns the email delivery result to the system.» | EXPLICIT |
| Decision «Email delivered?» (System) | EX-02 «An email notification cannot be delivered; the comment and in-app notification remain saved, and the failed delivery is recorded.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-02 |
| Guard [delivered] | Phủ định của EX-02 | NECESSARY UML REPRESENTATION |
| Guard [not delivered — EX-02] | EX-02 «An email notification cannot be delivered; the comment and in-app notification remain saved, and the failed delivery is recorded.» | NECESSARY UML REPRESENTATION |
| Action «Record the failed delivery and keep the saved comment» (System) | EX-02 «An email notification cannot be delivered; the comment and in-app notification remain saved, and the failed delivery is recorded.»; BR-NOTIFICATION-DELIVERY-INDEPENDENT | EXPLICIT — EX-02 nêu rõ kết quả. |
| Activity Final F1 (sau [exists]) | Kết quả: comment đã lưu (POST1, POST2; EX-02 không đổi kết quả này) | NECESSARY UML REPRESENTATION |
| Guard [removed — EX-01] | EX-01 «The work item is removed before the comment is submitted.» | NECESSARY UML REPRESENTATION |
| Action «Reject the comment because the work item was removed» (System) | EX-01 «The work item is removed before the comment is submitted.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F2 (sau [removed — EX-01]) | Kết quả: comment bị từ chối (EX-01) | NECESSARY UML REPRESENTATION |

### UC-29 — Review Work Item Activity (`UC-WORK-ITEM-ACTIVITY-REVIEW`)

YAML `data/use_cases/collaboration-notification/UC-WORK-ITEM-ACTIVITY-REVIEW.yml` · Source `diagrams/activity/collaboration-notification/source/UC-WORK-ITEM-ACTIVITY-REVIEW.puml` · SVG `diagrams/activity/collaboration-notification/svg/UC-WORK-ITEM-ACTIVITY-REVIEW.svg` · Lane: User, System · Final: 2 · 679×762 px ≈ 9.6 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Chỉ thêm comment `Final nodes:`; SVG giống hệt.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Lane: User và System.
- EX-01 kiểm tra ngay sau NF2. AF-01 (chỉ có sự kiện tạo) và NF3 cùng dẫn tới NF4 (User xem lịch sử).
- F1 (EX-01) và F2 (đã xem) khác kết quả. Header đã bổ sung `Final nodes:`.
- BR-ACTIVITY-IMMUTABLE: không có action sửa activity.

#### Bảng A — UC Spec → Diagram (UC-29)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Member opens a work item's activity history.» | «Request the activity history for a work item» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE2 | «The actor is an active member of the project.»; «The work item exists and is accessible to the actor.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Requests the activity history for a work item.» | «Request the activity history for a work item» (User) | Đạt |
| NF2 (System) | «Retrieves activity entries in reverse chronological order.» | «Retrieve the activity entries in reverse chronological order» (System) | Đạt |
| NF3 (System) | «Displays each event with its actor, time, and change summary.» | «Display each event with its actor, time and change summary» (System) | Đạt |
| NF4 (User) | «Reviews the displayed history.» | «Review the displayed history» (User) | Đạt |
| AF-01 condition | «No activity beyond item creation exists.» | [creation only — AF-01] tại «Activity beyond creation?» | Đạt |
| AF-01.1 | «The system displays only the creation event.» | «Display only the creation event» (System) | Đạt |
| EX-01 | «Activity data cannot be retrieved.» | [cannot be retrieved — EX-01] tại «Activity data retrieved?»; «Report that the activity history cannot be retrieved» (System) | Đạt |
| POST1 | «The actor has reviewed the current activity history without changing it.» | «Review the displayed history» (User) | Đạt |
| BR-PROJECT-MEMBER-ACCESS | «Project information is available only to active members of that project.» | «Request the activity history for a work item» (User) | Đạt |
| BR-ACTIVITY-IMMUTABLE | «Automatically recorded work item activity cannot be manually edited or deleted.» | «Review the displayed history» (User) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-29)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Request the activity history for a work item» (User) | NF1 «Requests the activity history for a work item.»; BR-PROJECT-MEMBER-ACCESS | EXPLICIT |
| Action «Retrieve the activity entries in reverse chronological order» (System) | NF2 «Retrieves activity entries in reverse chronological order.» | EXPLICIT |
| Decision «Activity data retrieved?» (System) | EX-01 «Activity data cannot be retrieved.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [retrieved] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [cannot be retrieved — EX-01] | EX-01 «Activity data cannot be retrieved.» | NECESSARY UML REPRESENTATION |
| Action «Report that the activity history cannot be retrieved» (System) | EX-01 «Activity data cannot be retrieved.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F1 (sau [cannot be retrieved — EX-01]) | Kết quả: không hiển thị lịch sử (EX-01) | NECESSARY UML REPRESENTATION |
| Decision «Activity beyond creation?» (System) | AF-01 «No activity beyond item creation exists.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [further activity] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Action «Display each event with its actor, time and change summary» (System) | NF3 «Displays each event with its actor, time, and change summary.» | EXPLICIT |
| Guard [creation only — AF-01] | AF-01 «No activity beyond item creation exists.» | NECESSARY UML REPRESENTATION |
| Action «Display only the creation event» (System) | AF-01.1 «The system displays only the creation event.» | EXPLICIT |
| Action «Review the displayed history» (User) | NF4 «Reviews the displayed history.»; POST1 «The actor has reviewed the current activity history without changing it.»; BR-ACTIVITY-IMMUTABLE | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: lịch sử đã được xem (POST1) | NECESSARY UML REPRESENTATION |

### UC-30 — Review Notifications (`UC-NOTIFICATIONS-REVIEW`)

YAML `data/use_cases/collaboration-notification/UC-NOTIFICATIONS-REVIEW.yml` · Source `diagrams/activity/collaboration-notification/source/UC-NOTIFICATIONS-REVIEW.puml` · SVG `diagrams/activity/collaboration-notification/svg/UC-NOTIFICATIONS-REVIEW.svg` · Lane: User, System · Final: 1 · 1067×1267 px ≈ 6.1 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Sửa `.puml` (thêm EX-03, gộp kiểm tra email vào AF-02.1 + «Change permitted?», ngắt dòng hẹp, header) và render lại SVG.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- **Lỗi đã sửa (bằng chứng):**
- PR #8 thêm EX-03 «Email delivery is enabled but the actor has no verified email address; the change is rejected and the previous preference remains unchanged». Diagram trên develop thiếu EX-03; validator báo `exception EX-03 is not represented`.
- Chữ guard chỉ ≈ 4,6 pt (manifest: REQUEST CHANGES).
- Sau sửa:
- AF-02.1 vẽ đúng chữ YAML «Verify that the actor has a verified email address when email delivery is enabled».
- Decision «Change permitted?» với guard [disabling, or verified] / [enabling, not verified — EX-03] → «Reject the change and keep the previous preference» (EXPLICIT).
- Decision «Enabling email delivery?» cũ và đường vòng [disabling] được thay bằng decision trên, nên bớt một cột.
- Ngắt chữ hẹp hơn; kích thước 1067 × 1267 px, ≈ 6,1 pt.
- Decision «Review a notification?» nằm ở lane User (lựa chọn của actor). «Requested action?» ở lane System là JUSTIFIED DERIVATION: YAML không xếp thứ tự NF3/AF-01/AF-02, nên System phân biệt yêu cầu. Observation này giữ nguyên.
- End node: một final chung, vì các kết quả đan xen trên nhánh lồng nhau (quy ước P2). Mọi postcondition đều là «may», nên không nhánh nào làm sai kết quả. Header đã cập nhật để nêu EX-03.
- Trình bày còn lại: merge cuối cùng vẽ trong lane User và có một đoạn gấp khúc ngắn (PlantUML đặt merge dưới decision đầu tiên). Không làm sai ngữ nghĩa.

#### Bảng A — UC Spec → Diagram (UC-30)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Member opens the notification center.» | «Open the notification center» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE1 | «The actor has an active system account.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Opens the notification center.» | «Open the notification center» (User) | Đạt |
| NF2 (System) | «Displays the actor's notifications and email delivery preference in reverse chronological order.» | «Display the actor's notifications and email delivery preference in reverse chronological order» (System) | Đạt |
| NF3 (User) | «Selects a notification to review.» | «Select a notification to review» (User) | Đạt |
| NF4 (System) | «Marks it as read and displays its related project context.» | «Mark it as read and display its related project context» (System) | Đạt |
| AF-01 condition | «The actor chooses to mark all notifications as read.» | [mark all — AF-01] tại «Requested action?» | Đạt |
| AF-01.1 | «The system marks all visible notifications as read.» | «Mark all visible notifications as read» (System) | Đạt |
| AF-02 condition | «The actor enables or disables email notification delivery.» | [change email delivery — AF-02] tại «Requested action?» | Đạt |
| AF-02.1 | «The system verifies that the actor has a verified email address when email delivery is enabled.» | «Verify that the actor has a verified email address when email delivery is enabled» (System) | Đạt |
| AF-02.2 | «The system saves the updated email delivery preference.» | «Save the updated email delivery preference» (System) | Đạt |
| EX-01 | «The related project item is no longer accessible to the actor.» | [inaccessible — EX-01] tại «Item accessible?»; «Report that the related project item is no longer accessible» (System) | Đạt |
| EX-02 | «The email delivery preference cannot be saved; the previous preference remains unchanged.» | [not saved — EX-02] tại «Preference saved?»; «Keep the previous preference and report the failure» (System) | Đạt |
| EX-03 | «Email delivery is enabled but the actor has no verified email address; the change is rejected and the previous preference remains unchanged.» | [enabling, not verified — EX-03] tại «Change permitted?»; «Reject the change and keep the previous preference» (System) | Đạt |
| POST1 | «Selected notifications may be marked as read.» | «Mark it as read and display its related project context» (System); «Mark all visible notifications as read» (System) | Đạt |
| POST2 | «The email delivery preference may be updated.» | «Save the updated email delivery preference» (System) | Đạt |
| POST3 | «No project work data is changed.» | «Mark it as read and display its related project context» (System); «Mark all visible notifications as read» (System) | Đạt |
| BR-NOTIFICATION-OWNER-ONLY | «A User can review only notifications addressed to that User.» | «Open the notification center» (User); «Display the actor's notifications and email delivery preference in reverse chronological order» (System) | Đạt |
| BR-PROJECT-MEMBER-ACCESS | «Project information is available only to active members of that project.» | «Report that the related project item is no longer accessible» (System) | Đạt |
| BR-NOTIFICATION-EMAIL-PREFERENCE | «An email notification is sent only to the intended recipient's verified email address when that User has enabled email delivery.» | «Verify that the actor has a verified email address when email delivery is enabled» (System); «Reject the change and keep the previous preference» (System) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-30)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Open the notification center» (User) | NF1 «Opens the notification center.»; BR-NOTIFICATION-OWNER-ONLY | EXPLICIT |
| Action «Display the actor's notifications and email delivery preference in reverse chronological order» (System) | NF2 «Displays the actor's notifications and email delivery preference in reverse chronological order.»; BR-NOTIFICATION-OWNER-ONLY | EXPLICIT |
| Decision «Review a notification?» (User) | NF3 «Selects a notification to review.»; AF-01 «The actor chooses to mark all notifications as read.»; AF-02 «The actor enables or disables email notification delivery.» | NECESSARY UML REPRESENTATION — lựa chọn của actor giữa NF3 và AF-01/AF-02, đặt trong partition User. |
| Guard [review] | NF3 «Selects a notification to review.» | NECESSARY UML REPRESENTATION |
| Action «Select a notification to review» (User) | NF3 «Selects a notification to review.» | EXPLICIT |
| Decision «Item accessible?» (System) | EX-01 «The related project item is no longer accessible to the actor.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [accessible] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Action «Mark it as read and display its related project context» (System) | NF4 «Marks it as read and displays its related project context.»; POST1 «Selected notifications may be marked as read.»; POST3 «No project work data is changed.» | EXPLICIT |
| Guard [inaccessible — EX-01] | EX-01 «The related project item is no longer accessible to the actor.» | NECESSARY UML REPRESENTATION |
| Action «Report that the related project item is no longer accessible» (System) | EX-01 «The related project item is no longer accessible to the actor.»; BR-PROJECT-MEMBER-ACCESS; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Guard [other request] | AF-01 «The actor chooses to mark all notifications as read.»; AF-02 «The actor enables or disables email notification delivery.» | NECESSARY UML REPRESENTATION — Phủ định của lựa chọn NF3 = AF-01 hoặc AF-02. |
| Decision «Requested action?» (System) | AF-01 «The actor chooses to mark all notifications as read.»; AF-02 «The actor enables or disables email notification delivery.» | JUSTIFIED DERIVATION — YAML không xếp thứ tự NF3/AF-01/AF-02; System phân biệt yêu cầu khác (mark all hoặc đổi email). Ghi observation. |
| Guard [mark all — AF-01] | AF-01 «The actor chooses to mark all notifications as read.» | NECESSARY UML REPRESENTATION |
| Action «Mark all visible notifications as read» (System) | AF-01.1 «The system marks all visible notifications as read.»; POST1 «Selected notifications may be marked as read.»; POST3 «No project work data is changed.» | EXPLICIT |
| Guard [change email delivery — AF-02] | AF-02 «The actor enables or disables email notification delivery.» | NECESSARY UML REPRESENTATION |
| Action «Verify that the actor has a verified email address when email delivery is enabled» (System) | AF-02.1 «The system verifies that the actor has a verified email address when email delivery is enabled.»; BR-NOTIFICATION-EMAIL-PREFERENCE | EXPLICIT |
| Decision «Change permitted?» (System) | EX-03 «Email delivery is enabled but the actor has no verified email address; the change is rejected and the previous preference remains unchanged.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-03 |
| Guard [disabling, or verified] | AF-02.1 «…verified email address when email delivery is enabled.»; phủ định của EX-03 | JUSTIFIED DERIVATION — AF-02.1 chỉ kiểm tra email khi bật; tắt email không cần kiểm tra. |
| Action «Save the updated email delivery preference» (System) | AF-02.2 «The system saves the updated email delivery preference.»; POST2 «The email delivery preference may be updated.» | EXPLICIT |
| Decision «Preference saved?» (System) | EX-02 «The email delivery preference cannot be saved; the previous preference remains unchanged.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-02 |
| Guard [saved] | Phủ định của EX-02 | NECESSARY UML REPRESENTATION |
| Guard [not saved — EX-02] | EX-02 «The email delivery preference cannot be saved; the previous preference remains unchanged.» | NECESSARY UML REPRESENTATION |
| Action «Keep the previous preference and report the failure» (System) | EX-02 «The email delivery preference cannot be saved; the previous preference remains unchanged.»; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — EX-02 nêu «previous preference remains unchanged» (EXPLICIT); phần «report the failure» theo §7.3. |
| Guard [enabling, not verified — EX-03] | EX-03 «Email delivery is enabled but the actor has no verified email address; the change is rejected and the previous preference remains unchanged.» | NECESSARY UML REPRESENTATION |
| Action «Reject the change and keep the previous preference» (System) | EX-03 «Email delivery is enabled but the actor has no verified email address; the change is rejected and the previous preference remains unchanged.»; BR-NOTIFICATION-EMAIL-PREFERENCE | EXPLICIT — EX-03 nêu rõ kết quả. |
| Activity Final F1 (sau luồng chính) | Kết quả: một final dùng chung cho mọi nhánh (POST1–POST3 đều là “may”); hành động cuối của từng nhánh nêu kết quả | NECESSARY UML REPRESENTATION |

### UC-31 — Monitor Sprint Progress (`UC-SPRINT-PROGRESS-MONITOR`)

YAML `data/use_cases/scrum-reporting/UC-SPRINT-PROGRESS-MONITOR.yml` · Source `diagrams/activity/scrum-reporting/source/UC-SPRINT-PROGRESS-MONITOR.puml` · SVG `diagrams/activity/scrum-reporting/svg/UC-SPRINT-PROGRESS-MONITOR.svg` · Lane: User, System · Final: 2 · 581×916 px ≈ 8.9 pt · **READY FOR PEER REVIEW**

Thay đổi lần này: Chỉ thêm comment `Final nodes:`; SVG giống hệt.

Kiểm tra lane, thứ tự, guard, reachability, end node, precondition:

- Sau PR #8, precondition «project has an active Sprint» đã bị bỏ, nên EX-01 (không có Sprint đang chạy) khớp BR-PROGRESS-ACTIVE-SPRINT. Diagram không cần sửa; observation cũ trong manifest đã lỗi thời.
- AF-01: gắn nhãn chỉ số ước lượng là chưa đủ, rồi vẫn hiển thị (AF-01.2 gộp vào NF4).
- F1 (EX-01) và F2 (đã hiển thị) khác kết quả. Header đã bổ sung `Final nodes:`.

#### Bảng A — UC Spec → Diagram (UC-31)

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Member opens Sprint progress reporting.» | «Open the active Sprint progress view» (User) (bước đầu tiên sau Initial Node) | Đạt |
| PRE1–PRE1 | «The actor is an active member of the project.» | Không vẽ thành action (precondition, kể cả đăng nhập) | Đạt |
| NF1 (User) | «Opens the active Sprint progress view.» | «Open the active Sprint progress view» (User) | Đạt |
| NF2 (System) | «Aggregates current work item status and estimate data.» | «Aggregate current work item status and estimate data» (System) | Đạt |
| NF3 (System) | «Calculates completion, remaining work, overdue items, and member workload.» | «Calculate completion, remaining work, overdue items and member workload» (System) | Đạt |
| NF4 (System) | «Displays the resulting Sprint indicators and charts.» | «Display the resulting Sprint indicators and charts» (System) | Đạt |
| AF-01 condition | «Some work items have no estimate.» | [estimates missing — AF-01] tại «All work items estimated?» | Đạt |
| AF-01.1 | «The system labels estimate-based measures as incomplete.» | «Label estimate-based measures as incomplete» (System) | Đạt |
| AF-01.2 | «The system still displays count-based progress.» | «Display the resulting Sprint indicators and charts» (System) | Đạt |
| EX-01 | «No active Sprint exists for the selected project.» | [no active Sprint — EX-01] tại «Active Sprint exists?»; «Report that no active Sprint exists for the project» (System) | Đạt |
| POST1 | «The actor sees a current progress snapshot without changing Sprint data.» | «Display the resulting Sprint indicators and charts» (System) | Đạt |
| BR-PROJECT-MEMBER-ACCESS | «Project information is available only to active members of that project.» | «Open the active Sprint progress view» (User) | Đạt |
| BR-PROGRESS-ACTIVE-SPRINT | «Sprint progress is calculated only for the project's active Sprint.» | «Report that no active Sprint exists for the project» (System) | Đạt |

#### Bảng B — Diagram → UC Spec (UC-31)

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Open the active Sprint progress view» (User) | NF1 «Opens the active Sprint progress view.»; BR-PROJECT-MEMBER-ACCESS | EXPLICIT |
| Decision «Active Sprint exists?» (System) | EX-01 «No active Sprint exists for the selected project.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của EX-01 |
| Guard [active Sprint] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Guard [no active Sprint — EX-01] | EX-01 «No active Sprint exists for the selected project.» | NECESSARY UML REPRESENTATION |
| Action «Report that no active Sprint exists for the project» (System) | EX-01 «No active Sprint exists for the selected project.»; BR-PROGRESS-ACTIVE-SPRINT; GUIDE-7.3 (hành động kết quả của exception) | JUSTIFIED DERIVATION — YAML nêu exception nhưng không nêu kết quả; §7.3 yêu cầu một action reject/report. |
| Activity Final F1 (sau [no active Sprint — EX-01]) | Kết quả: không tính tiến độ (EX-01) | NECESSARY UML REPRESENTATION |
| Action «Aggregate current work item status and estimate data» (System) | NF2 «Aggregates current work item status and estimate data.» | EXPLICIT |
| Action «Calculate completion, remaining work, overdue items and member workload» (System) | NF3 «Calculates completion, remaining work, overdue items, and member workload.» | EXPLICIT |
| Decision «All work items estimated?» (System) | AF-01 «Some work items have no estimate.» | NECESSARY UML REPRESENTATION — điểm rẽ nhánh của AF-01 |
| Guard [all estimated] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Guard [estimates missing — AF-01] | AF-01 «Some work items have no estimate.» | NECESSARY UML REPRESENTATION |
| Action «Label estimate-based measures as incomplete» (System) | AF-01.1 «The system labels estimate-based measures as incomplete.» | EXPLICIT |
| Action «Display the resulting Sprint indicators and charts» (System) | NF4 «Displays the resulting Sprint indicators and charts.»; AF-01.2 «The system still displays count-based progress.»; POST1 «The actor sees a current progress snapshot without changing Sprint data.» | EXPLICIT |
| Activity Final F2 (sau luồng chính) | Kết quả: chỉ số Sprint được hiển thị (POST1) | NECESSARY UML REPRESENTATION |

## 5. Kết quả kiểm tra

| Kiểm tra | Kết quả |
|---|---|
| `py scripts/activity_diagrams.py render` (UC-10, 28, 30 và 7 UC chỉ đổi comment) | 10 lần render, 0 lỗi. 7 SVG chỉ đổi comment giống hệt bản cũ từng byte. |
| `layout_issues` (chữ bị cắt hoặc chồng) cho 14 SVG | 0 vấn đề |
| `py scripts/activity_diagrams.py validate` | Develop trước khi sửa: 7 lỗi. Sau khi sửa: 5 lỗi, tất cả thuộc UC của thành viên khác (xem mục 6). Lỗi UC-10 AF-02 và UC-30 EX-03 đã hết. 0 warning. |
| `py cli.py validate` (YAML) | 62 use case, 0 lỗi |
| `python -m unittest discover -s tests` | 18 test, OK |
| Kiểm tra text SVG ↔ source (svgcheck) | 0 sai khác |
| Kiểm tra lane theo actor của bước YAML (lanecheck) | 0 vấn đề cho 14 UC |
| Chèn 14 SVG vào `.docx` A4 (lề 2,25 cm, rộng ≤ 16,5 cm), chuyển PDF, xem ảnh trang | 14 trang, mỗi diagram nằm gọn một trang, không bị cắt; guard của UC-10, 28, 30 đọc được ở 150–200 dpi |
| Xem trực tiếp PNG render của 14 SVG | Đã xem cả 14 (3 UC sửa: trước và sau) |

## 6. Việc ngoài phạm vi được phép sửa — cần leader quyết định

Yêu cầu lần này chỉ cho sửa `.puml` và SVG của 14 UC. Vì vậy các file dưới đây **không** bị sửa, nhưng đã lỗi thời
so với diagram hoặc spec mới.

**6.1 Đề xuất cập nhật `diagrams/activity/manifest.yml` (chỉ entry của Bình):**

- UC-28 `UC-WORK-ITEM-COMMENT`:
  - `final_status`/`visual_review_status`: `needs-manual-review` → `ready-for-peer-review`/`pass`
    (`audit_status` sẽ thành APPROVED).
  - Bỏ `review_notes` 5,3 pt.
  - Thêm observation: «NF5 requests email delivery only for eligible members; the YAML does not describe the case
    with no eligible member, so no separate branch is drawn.»
- UC-30 `UC-NOTIFICATIONS-REVIEW`:
  - Đổi trạng thái như UC-28; bỏ `review_notes` 4,6 pt.
  - Bỏ observation «AF-02.1 does not say what happens when the actor has no verified email address», vì EX-03 đã
    có.
  - Giữ observation về thứ tự NF3/AF-01/AF-02.
- UC-10 `UC-SCRUM-ACCOUNTABILITY-ASSIGN`:
  - Bỏ hai observation cũ (AF-01 không nói trường hợp không xác nhận; xung đột với BR). PR #8 đã giải quyết cả
    hai.
  - Thêm ghi chú: hai final cùng kết quả (AF-02, EX-01), theo ngoại lệ đã dùng ở UC-13.
- UC-09.3, UC-11, UC-13, UC-31: bỏ observation «contradicts a precondition», vì precondition liên quan đã được sửa
  ở PR #8.
- Mục `review_sections` → «End-node policy», điểm (4): thêm UC-10 cạnh UC-13.

**6.2 Tài liệu audit cũ:** `docs/activity-diagram-audit-report.md` và `docs/activity-diagram-traceability.md`
vẫn mô tả UC-10, UC-28, UC-30 theo cấu trúc cũ (không có AF-02/EX-03; có nhánh «none eligible»). Nên chạy lại phần
sinh báo cáo sau khi leader đồng ý cập nhật manifest.

**6.3 Lỗi validator của thành viên khác** (do PR #8 thêm AF/EX, không sửa ở đây):

| UC | Lỗi |
|---|---|
| UC-ACCOUNT-REGISTER | EX-04 is not represented |
| UC-PASSWORD-RESET | AF-03 is not represented |
| UC-SPRINT-START | AF-02 is not represented |
| UC-SPRINT-TASK-CREATE | AF-01 is not represented |
| UC-SPRINT-TASK-DELETE | AF-02 is not represented |

**6.4 UC-27.4** (của Trung): PR #8 đã bỏ precondition gây xung đột, nhưng manifest vẫn ghi BLOCKED — REQUIREMENT
CONFLICT. Trung cần audit lại.

**6.5 Shared style:** không cần sửa. Không đề xuất đổi font; phạm vi ảnh hưởng nếu đổi được ghi ở guide mục 4.9.

## 7. Câu hỏi cần người dùng/leader quyết định

1. UC-28: có đồng ý bỏ nhánh «no eligible email recipient» không? Nhánh này không có trong YAML, và bỏ nó giúp
   sửa lỗi guard đặt sai phía. Nếu nhóm muốn giữ, BA cần thêm một AF vào YAML.
2. UC-10: có chấp nhận hai Activity Final cùng kết quả (AF-02 và EX-01) như ngoại lệ đã dùng ở UC-13 không?
3. Có cho phép cập nhật entry manifest của Bình theo mục 6.1 trong một commit riêng không?
