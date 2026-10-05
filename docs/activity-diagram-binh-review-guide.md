# Hướng dẫn trình bày và review Activity Diagram — phạm vi Nguyễn An Bình

Tài liệu này áp dụng cho 14 Activity Diagram được giao cho Nguyễn An Bình (UC-06, 07, 08, 09.1, 09.2, 09.3,
10, 11, 12, 13, 28, 29, 30, 31). Nó bổ sung, không thay thế, `docs/activity-diagram-guideline.md`. Khi hai tài
liệu khác nhau, guideline chung thắng; tài liệu này chỉ cụ thể hóa cách áp dụng cho 14 UC trên.

Báo cáo kết quả review và nghiệm thu của 14 UC nằm ở `docs/activity-diagram-binh-acceptance-report.md`.

Mỗi quy tắc dưới đây được gắn một nhãn để biết nó có tính bắt buộc đến đâu:

| Nhãn | Ý nghĩa |
|---|---|
| **[UML]** | Ngữ nghĩa UML 2.5.1. Vi phạm làm diagram sai về mặt ngôn ngữ mô hình. |
| **[TEAM]** | Quy ước của nhóm (guideline chung, mục được trích). Không phải yêu cầu của UML. |
| **[TRÌNH BÀY]** | Lựa chọn trình bày để diagram dễ đọc trong báo cáo Word A4. Có thể lệch nếu có lý do. |

## 1. Đặc điểm trình bày rút ra từ 14 hình tham chiếu

### 1.1 Nguồn và cách dùng

Người dùng cung cấp 14 ảnh PNG Activity Diagram của Nguyễn Tấn Trung (UC-23, 24.1–24.7, 26, 27.1–27.5). Các
ảnh này là bản vẽ riêng của Trung, khác với bản SVG cùng mã UC trong repo (bản repo dùng shared style). Ảnh là
PNG nên không có PlantUML/XML nhúng để đối chiếu; mọi nhận xét dưới đây dựa trên hình hiển thị thực tế.

Các ảnh chỉ được dùng làm **bằng chứng về trình bày**. Không có action, condition, exception, actor hay Business
Rule nào của UC-23 → UC-27.5 được chép sang 14 UC của Bình.

### 1.2 Phân loại 14 hình

| Hình | UC (semantic key) | Phân loại | Lý do cụ thể |
|---|---|---|---|
| `d15aa01b` | UC-24.1 View Sprint Task (`UC-SPRINT-TASK-VIEW`) | **Phù hợp làm tham chiếu trình bày** | Hai lane gọn; luồng chính đi thẳng từ trên xuống; một decision, hai guard nằm ngang hai bên diamond; hai nhánh hội tụ về một final ở đáy; khoảng trắng đều. Lưu ý nhỏ: lane «Project Member» không phải tên partition hợp lệ theo guideline §6 (nội dung, không phải trình bày). |
| `6743714f` | UC-27.1 View Subtasks (`UC-SUBTASKS-VIEW`) | **Phù hợp làm tham chiếu trình bày** | Bố cục hai lane cân đối; action có padding rộng; guard ngắn, có mã AF; hai nhánh hội tụ về một final. Chữ guard dùng font monospace khác font action — không lấy đặc điểm này. |
| `7c63eec5` | UC-23 Review Sprint Board (`UC-SPRINT-BOARD-REVIEW`) | **Phù hợp nhưng có lưu ý** | Lấy được: luồng chính thẳng, nhánh exception ra ngang, một final ở đáy. Lưu ý: guard «[Sprint data available]» bị đường nối cắt qua; có bước «Retrieve Sprint data» không có trong YAML; lane «Project Member» không hợp lệ. |
| `e1375e6a` | UC-24.3 Update Sprint Task (`UC-SPRINT-TASK-UPDATE`) | **Phù hợp nhưng có lưu ý** | Lấy được: tỉ lệ dọc vừa A4, nhánh hội tụ gọn. Lưu ý: decision «cancel/submit» là lựa chọn của Developer nhưng nằm trong lane System; «Check Sprint Task status» là bước thêm. |
| `f8c81b7c` | UC-24.6 Add Task Dependency (`UC-TASK-DEPENDENCY-ADD`) | **Phù hợp nhưng có lưu ý** | Lấy được: action ngắn, ngắt dòng 2 dòng, ba nhánh hội tụ một final. Lưu ý: guard «[same task» và «[different task]» bị đường nối cắt chữ. |
| `4714e49e` | UC-27.5 Delete Subtask (`UC-SUBTASK-DELETE`) | **Phù hợp nhưng có lưu ý** | Lấy được: hai decision xếp dọc, nhánh hội tụ một final. Lưu ý: decision confirm/cancel (lựa chọn của Developer) đặt trong lane System; guard «[confirm deletion]» bị đường nối cắt. |
| `dd0edcb2` | UC-24.2 Create Sprint Task (`UC-SPRINT-TASK-CREATE`) | **Không phù hợp** | Vòng lặp quay về thẳng action «Validate Sprint Task request» (action có 2 cạnh vào = implicit join theo UML, không phải merge); có note «PBI: product backlog item» trong diagram; chữ quá nhỏ khi thu về A4. |
| `3c8f488c` | UC-24.4 Assign Sprint Task (`UC-SPRINT-TASK-ASSIGN`) | **Không phù hợp** | Hai cạnh đi thẳng vào action «Record change in activity history» (implicit join); «Mark Sprint Task as unassigned» là việc của System nhưng nằm trong lane Developer; nhánh exception «Display error…» dùng chữ chung chung. |
| `6583a8f7` | UC-24.5 Delete Sprint Task (`UC-SPRINT-TASK-DELETE`) | **Không phù hợp** | Action exception «Display error: Task already entered execution» không có cạnh ra (ngõ cụt, UC không kết thúc); đường «Cancel deletion» chạy ngang qua lane. |
| `a6fe3b5c` | UC-24.7 Remove Task Dependency (`UC-TASK-DEPENDENCY-REMOVE`) | **Không phù hợp** | Guard «[confirms removal]» và «[cancels removal (AF-01)]» bị đường nối gạch ngang chữ; viền giữa hai lane dày gấp đôi, không nhất quán. |
| `6b925143` | UC-26 Update Work Item Status (`UC-WORK-ITEM-STATUS-UPDATE`) | **Không phù hợp** | Cạnh quay lại đi thẳng vào action «Validate requested transition…» (implicit join); một nhánh ra của decision lồng không có guard; guard «[invalid request]» chung chung; thiếu nhánh EX-01 của YAML. |
| `598bfaed` | UC-27.2 Create Subtask (`UC-SUBTASK-CREATE`) | **Không phù hợp** | Nhánh EX-01 đi thẳng vào final, không có action nêu kết quả (kết thúc im lặng); final đặt ở lane bên trái với cạnh quay ngược từ phải. |
| `bca21d45` | UC-27.3 Update Subtask (`UC-SUBTASK-UPDATE`) | **Không phù hợp** | Các action của Developer («Revise Subtask Information», «Submit Subtask») nằm trong lane System — sai partition. |
| `79cbca81` | UC-27.4 Complete Subtask (`UC-SUBTASK-COMPLETE`) | **Không phù hợp** | Action «Display Sprint Completed Error» là ngõ cụt (không có cạnh tới final); diagram bắt đầu bằng một decision ngay sau Initial Node. Repo (`diagrams/activity/manifest.yml`, audit 2026-10-03) đánh dấu UC-27.4 là **BLOCKED — REQUIREMENT CONFLICT** vì AF-01 «restore a completed subtask» mâu thuẫn với precondition cũ «The subtask is not already complete». PR #8 đã bỏ precondition đó khỏi YAML, nhưng entry manifest vẫn ghi BLOCKED. Vì vậy hình này không được dùng làm mẫu, kể cả về trình bày. Việc cập nhật UC-27.4 thuộc phạm vi của Trung. |

### 1.3 Đặc điểm được giữ lại (chỉ trình bày)

| # | Đặc điểm quan sát được | Hình minh họa | Nhãn |
|---|---|---|---|
| P1 | Luồng chính đi từ trên xuống, nằm gần trục giữa của lane System. | 24.1, 27.1, 23 | [TRÌNH BÀY] — trùng guideline §7.1 [TEAM] |
| P2 | Nhánh exception/alternative rời diamond theo hướng ngang, guard đặt cạnh diamond, sát cạnh ra của nó. | 24.1, 27.1, 24.6 | [TRÌNH BÀY] |
| P3 | Action có padding rộng, chữ ngắt 2–3 dòng (khoảng 15–35 ký tự mỗi dòng). | 24.1, 27.1, 24.3 | [TRÌNH BÀY] — trùng guideline §8 |
| P4 | Ít lane nhất có thể (thường hai: actor và System). | tất cả | [TEAM] guideline §6 |
| P5 | Guard ngắn, có mã AF/EX trong ngoặc vuông. | 24.1, 27.1, 24.5 | [TEAM] guideline §7.2–7.3 |
| P6 | Các nhánh cùng kết quả hội tụ về một Activity Final ở đáy diagram. | 24.1, 27.1, 24.6 | [TEAM] guideline §5 |
| P7 | Khung ngoài và viền lane nét đậm, liên tục. | tất cả | [TRÌNH BÀY] — renderer đã thêm khung |
| P8 | Tỉ lệ dọc, đọc được khi thu về khổ A4. | 24.1, 27.1, 24.3 | [TEAM] guideline §8 |

## 2. Mẫu trình bày cho 14 UC của Bình

```plantuml
@startuml UC-<SEMANTIC-KEY>
' UC-xx - <Name> | semantic key: UC-<SEMANTIC-KEY>
' Source: data/use_cases/<domain>/UC-<SEMANTIC-KEY>.yml
' Business Rules: <keys>
' Trace comments ' [ref] name the YAML element behind the next action.
' No title: the Word caption supplies it.
' Final nodes: F1 = <outcome, POST refs>; F2 = <outcome, AF/EX refs>.
!include ../../_shared/activity-style.puml
|OWN| $lane_title("Project Owner")      ' hoặc |USR| $lane_title("User")
|SYS| $lane_title("System")

|OWN|
start
' [NF1]
:<Verb + object, 2–3 dòng>;
|SYS|
' [NF2]
:<System action>;
' Exception ra ngang, luồng chính đi xuống, cả hai nhánh kết thúc riêng:
if ($question("<Condition>?")) then ($guard_left("[<normal guard>]"))
  ' [NF3, POST1]
  :<Main-flow action>;
  stop
else ($guard_right("[<exception guard>", "— EX-01]"))
  ' [EX-01, GUIDE-7.3]
  :Reject/Report <outcome>;
  stop
endif
@enduml
```

Những điểm chính của mẫu:

- Header comment có dòng `Final nodes:` giải thích từng final khi có hơn một final [TEAM §5].
- Mỗi action có trace comment trước nó [TEAM §9.1].
- Exception kết thúc bằng một action System nêu kết quả, rồi mới tới final [TEAM §5, §7.3].
- Khi một nhánh kết thúc mà nhánh kia đi tiếp, dùng dạng `if … then (normal) … else (exception) … stop endif`.
  Shared style bật `useVerticalIf`, nên nhánh khác rỗng sẽ được vẽ ngay dưới diamond còn nhánh rỗng vòng sang
  phải [TRÌNH BÀY]. Khi cần nhánh exception nằm ngang, đặt phần còn lại của luồng chính vào `then` (ví dụ UC-10,
  UC-28 sau sửa).

## 3. Những đặc điểm KHÔNG được sao chép

| # | Đặc điểm trong hình tham chiếu | Lý do không dùng | Nhãn |
|---|---|---|---|
| N1 | Font sans-serif cho action và font monospace cho guard. | Guideline §8 quy định Times New Roman cho toàn bộ diagram. Đổi font cần sửa shared style và ảnh hưởng 41 diagram còn lại (xem mục 4.9). | [TEAM] |
| N2 | Nhiều cạnh đi thẳng vào một action (24.2, 24.4, 26). | Theo UML, action có nhiều cạnh vào là implicit join (chờ tất cả token), không phải merge. Phải dùng merge node. | [UML] |
| N3 | Action exception không có cạnh ra (24.5, 27.4). | Một node không có cạnh ra làm token dừng ở đó; activity không đạt final. Mỗi nhánh phải tới một final. | [UML] |
| N4 | Exception đi thẳng vào final mà không có action kết quả (24.2, 27.2). | Guideline §5 cấm kết thúc im lặng ngay sau decision. | [TEAM] |
| N5 | Action của actor nằm trong lane System, hoặc ngược lại (24.4, 27.3); decision do actor chọn đặt trong lane System (24.3, 27.5). | Partition phải thể hiện đúng trách nhiệm. | [UML] partition = trách nhiệm; [TEAM §6] |
| N6 | Guard bị đường nối cắt chữ (23, 24.6, 24.7, 27.5). | Guideline §8: guard không chạm đường và viền node. | [TRÌNH BÀY] |
| N7 | Bước kiểm tra/lấy dữ liệu không có trong YAML («Retrieve Sprint data», «Check Sprint Task status», «Check task status and dependencies»). | Không được thêm bước không có nguồn. | [TEAM §7.3] |
| N8 | Lane «Project Member». | Không có trong danh sách partition hợp lệ ở guideline §6 (dùng «User» hoặc vai trò cụ thể). | [TEAM] |
| N9 | Note trong diagram (24.2). | Không cần thiết; giải thích nằm ở caption hoặc trong báo cáo. | [TRÌNH BÀY] |
| N10 | Action viết hoa từng chữ («Display Invalidation Error»). | Guideline dùng câu thường dạng động từ + tân ngữ. | [TRÌNH BÀY] |

## 4. Quy tắc trình bày cụ thể

### 4.1 Font và cỡ chữ [TEAM §8]

- Toàn bộ diagram dùng Times New Roman do shared style cung cấp. Không đặt `skinparam` font trong file UC.
- Lane title 18 px đậm; action 16 px; decision 15 px; guard 14 px.
- Ngưỡng đọc được [TEAM]: chữ guard sau khi co diagram vào vùng 16,5 × 20,5 cm phải đạt khoảng 6 pt.
  Công thức: `10,5 pt × min(1, 623,6 / width_px, 774,8 / height_px)`. 6 pt là khuyến nghị của nhóm, UML không quy định.

### 4.2 Kích thước và khoảng cách [TRÌNH BÀY]

- Ngắt chữ action ở 15–35 ký tự mỗi dòng, tối đa 5 dòng. Khi diagram bị giới hạn bởi chiều rộng, ngắt hẹp hơn.
- Không chèn khoảng trắng hay action đệm để căn chỉnh. Các helper `$question`, `$guard_left`, `$guard_right`
  chỉ thêm padding vô hình.
- Dùng `$question_x` chỉ khi luồng đi vào decision từ partition khác. Khi vào trong cùng partition, dùng
  `$question` để không tạo khoảng trống thừa (UC-10 sau sửa).

### 4.3 Swimlane

- [UML] Partition thể hiện trách nhiệm. Action của actor nằm ở lane actor, action của hệ thống nằm ở lane System.
- [TEAM §6] Thứ tự: primary actor, System, rồi service bên ngoài. Với 14 UC của Bình:
  - «Project Owner» cho UC-08, 09.2, 09.3, 10, 11, 12.
  - «User» cho UC-06, 07, 09.1, 13, 28, 29, 30, 31.
  - «Email Service» chỉ có ở UC-28.
- [TEAM] Khai báo lane với alias trước `start`. Khai báo lại lane ở đầu nhánh `else`, vì nhánh `else` kế thừa
  partition của cuối nhánh `then`.

### 4.4 Action [TEAM §5, §9.1]

- Viết dạng động từ + tân ngữ, câu thường.
- Mỗi action có trace comment tới NF/AF/EX/POST/BR/GUIDE-7.3.
- Không dùng action chung chung (Validate, Persist, Display error, Notify, Retry, Record change) khi không có
  nguồn YAML cụ thể.
- Không vẽ Log In hay kiểm tra precondition thành action.

### 4.5 Decision và guard

- [UML] Mỗi cạnh ra của decision có guard. Các guard loại trừ nhau và phủ hết các trường hợp.
- [TEAM §7.4] Decision là một câu hỏi ngắn. Guard trong ngoặc vuông, có mã AF/EX khi nhánh thuộc AF/EX.
- [TEAM] Decision do actor lựa chọn nằm trong lane actor (UC-10 «Confirm the replacement?», UC-11 «Confirm
  archival?», UC-13 «Leave anyway?», UC-30 «Review a notification?»).
- [TRÌNH BÀY] Nhánh ở partition khác rời diamond theo hướng ngang. Nếu nhánh `then` bắt đầu ở partition khác, nhãn
  của nó sẽ bị đường nối cắt, nên đặt action đầu tiên của nhánh `then` cùng partition với diamond.
- [TRÌNH BÀY] Kiểm tra guard có nằm cạnh đúng cạnh ra không. Ví dụ, ở UC-28 trước khi sửa, nhãn «[none eligible]»
  nằm bên phải trong khi cạnh của nó đi sang trái.

### 4.6 Vòng lặp [TEAM §7.5]

- Dùng `while (...) is ([guard]) … endwhile ([guard])`. Không dùng `repeat while`, vì kiểu này mất nhãn khi
  decision dạng diamond.
- Giới hạn đã biết [TRÌNH BÀY]: khi thân vòng lặp đi sang lane actor (UC-06, 08, 12, 28), PlantUML vẽ cạnh thoát
  cắt qua hai cạnh của thân vòng lặp. Đây là giới hạn của layout engine, không phải lỗi ngữ nghĩa. Reviewer ghi
  nhận và không yêu cầu sửa.

### 4.7 Mũi tên [TRÌNH BÀY]

- Renderer đổi mũi tên đặc của PlantUML sang mũi tên hở (UML style). Mọi đường có cùng độ dày 1,4 px.
- Không có cạnh đi ngược lên trên, trừ cạnh quay lại của vòng lặp.

### 4.8 Final node

- [UML 15.7.3] Một activity có thể có nhiều Activity Final. Final đầu tiên được chạm sẽ kết thúc toàn bộ
  activity. Final có thể có nhiều cạnh vào. UML **không** yêu cầu chỉ có một final.
- [UML 15.7.16] Flow Final chỉ kết thúc một luồng, các luồng song song khác vẫn chạy. Không UC nào của Bình có
  luồng song song, nên không dùng Flow Final.
- [TEAM §5]:
  - Các nhánh cùng kết quả dùng chung một final qua merge node.
  - Final riêng chỉ dùng cho kết quả khác nhau và được giải thích trong header comment.
  - Khi các kết quả khác nhau đan xen trên nhánh lồng nhau, dùng một final chung (UC-30).
  - Ngoại lệ có giải thích: UC-13 và UC-10 giữ hai final cùng kết quả, vì gộp lại sẽ phải vẽ lại NF5 (và bước
    kiểm tra EX-01 ở UC-10).
- [TEAM] Không bao giờ gộp làm sai kết quả, và không tạo «error ending» không có trong spec.
- [TRÌNH BÀY] Đặt `|LANE|` trước `stop` để final nằm đúng lane.

### 4.9 Đề xuất về shared style

Không cần sửa `diagrams/activity/_shared/activity-style.puml` cho 14 UC này. Mọi điều chỉnh đều nằm trong file
`.puml` của từng UC (ngắt dòng, cấu trúc if/else, `$question` thay `$question_x`).

Font sans-serif của hình tham chiếu **không** được đề xuất. Nếu nhóm muốn đổi font, phạm vi ảnh hưởng gồm cả 55
diagram:

- Tất cả 53 SVG hiện có phải render lại.
- Kích thước diagram sẽ thay đổi, nên mọi giá trị pt trong báo cáo phải đo lại.
- Guideline §8 phải sửa.

Leader cần quyết định riêng nếu muốn đổi.

## 5. Kiểm tra SVG sau khi render và sau khi chèn vào Word A4

1. Render: `py scripts/activity_diagrams.py render --key <KEY>`. Lệnh in kích thước SVG và báo lỗi layout
   (`layout_issues`: chữ bị đường cắt, chữ chồng lên action).
2. Mở SVG (trình duyệt) ở 100 %. Kiểm tra:
   - Không có chữ bị cắt hay chồng lên nhau, không có đường nối chồng lên nhau.
   - Guard nằm cạnh đúng cạnh ra của nó.
   - Final nằm đúng lane.
   - Không có title trong diagram.
   - Font thống nhất.
3. Tính cỡ chữ guard hiệu dụng theo mục 4.1. Dưới khoảng 6 pt thì đánh dấu `needs-manual-review`.
4. Chèn vào Word, thực hiện từng bước:
   - Insert → Pictures → chọn SVG; Word giữ ảnh vector.
   - Đặt chiều rộng ≤ 16,5 cm và chiều cao ≤ 20,5 cm, giữ khóa tỉ lệ.
   - Thêm caption «Figure n. UC-xx <Name>».
5. Xuất PDF hoặc in thử ở 100 %. Đọc được mọi guard ở khoảng cách đọc bình thường, không phóng to, thì đạt.
6. Lần review này đã kiểm tra như sau:
   - Chèn 14 SVG (kèm PNG fallback) vào một file `.docx` A4, lề 2,25 cm.
   - Chuyển sang PDF bằng LibreOffice và xem lại ảnh trang ở 110–200 dpi.
   - Mỗi diagram nằm gọn một trang, không bị cắt.

## 6. Checklist peer review và leader acceptance

### 6.1 Peer reviewer

- [ ] Display ID ↔ semantic key ↔ YAML ↔ `.puml` ↔ SVG khớp với `diagrams/activity/manifest.yml`.
- [ ] Bảng A: trigger, mọi NF, AF, EX, POST và BR ảnh hưởng luồng đều có node/nhánh tương ứng hoặc lý do không vẽ.
- [ ] Bảng B: mọi action/decision/guard/final có nguồn. Không còn UNSUPPORTED/CONFLICT/UNCLEAR chưa giải thích.
- [ ] Lane đúng trách nhiệm; decision do actor chọn nằm ở lane actor.
- [ ] Thứ tự bước đúng YAML; AF quay về đúng bước; exception có action kết quả.
- [ ] Mọi nhánh đến được final đúng kết quả; final cùng kết quả đã gộp hoặc có giải thích.
- [ ] Không có Log In/precondition vẽ thành action; không có action đệm.
- [ ] SVG: không cắt chữ, guard đọc được ở A4 (≈ 6 pt), không có đường chồng lên nhau, không có title.
- [ ] `py scripts/activity_diagrams.py validate` không báo lỗi cho UC đang review.

### 6.2 Leader

- [ ] Peer review đã xong, mọi comment đã có trả lời.
- [ ] Manifest `final_status` và `observations` phản ánh trạng thái thật (xem các mục cần cập nhật trong báo cáo
  nghiệm thu).
- [ ] Đã chèn thử vào báo cáo Word và đọc được.
- [ ] Chỉ sau các bước trên mới chuyển trạng thái Jira sang Accepted. Báo cáo của Claude không bao giờ ghi
  ACCEPTED.

## 7. Ví dụ truy vết đầy đủ — UC-09.2 Add Project Member

Các file liên quan:

- YAML: `data/use_cases/project-membership/UC-PROJECT-MEMBER-ADD.yml`
- Nguồn: `diagrams/activity/project-membership/source/UC-PROJECT-MEMBER-ADD.puml`
- SVG: `diagrams/activity/project-membership/svg/UC-PROJECT-MEMBER-ADD.svg`

Diagram có hai partition, «Project Owner» và «System», kích thước 916 × 827 px, guard ≈ 7,1 pt ở A4.

### 7.1 Bảng A — UC Spec → Diagram

| UC source | Nội dung trong spec | Node/nhánh trên diagram | Kết quả |
|---|---|---|---|
| TRIGGER | «The Project Owner chooses to add a member to the project.» | «Open project membership management and choose to add a member» (Project Owner), bước đầu sau Initial Node | Đạt |
| PRE1–PRE3 | «The actor is the current Project Owner.»; «The project is active.»; «The target User account is active.» | Không vẽ thành action. PRE1 thể hiện qua partition «Project Owner». | Đạt |
| NF1 (User) | «Opens project membership management and chooses to add a member.» | «Open project membership management and choose to add a member» (Project Owner) | Đạt |
| NF2 (System) | «Requests an existing User account.» | «Request an existing User account» (System) | Đạt |
| NF3 (User) | «Selects the User and confirms the addition.» | «Select the User and confirm the addition» (Project Owner) | Đạt |
| NF4 (System) | «Verifies that the User is active and is not already a member.» | «Verify that the User is active and is not already a member» (System), rồi hai decision «Already a member?» và «Account still active?» | Đạt |
| NF5 (System) | «Creates the membership and refreshes the member list.» | «Create the membership and refresh the member list» (System) | Đạt |
| AF-01 condition | «The selected User is already a project member.» | [already a member — AF-01] tại «Already a member?» | Đạt |
| AF-01.1 | «The system reports that no new membership is required.» | «Report that no new membership is required» (System) | Đạt |
| EX-01 | «The selected User account becomes inactive before confirmation.» | [became inactive — EX-01] tại «Account still active?»; «Reject the addition of the inactive account» (System) | Đạt |
| POST1 | «The target User becomes an active Project Member.» | «Create the membership and refresh the member list» | Đạt |
| POST2 | «The membership change is recorded in project activity history.» | «Record the membership change in project activity history» | Đạt |
| BR-ACTIVE-USER-REQUIRED | «Only an active authenticated User can create or access a project.» | Trace ở NF4 «Verify that the User is active…»; nhánh EX-01 | Đạt |
| BR-PROJECT-OWNER-ADMINISTRATION | «Only the Project Owner may … manage project membership …» | Partition «Project Owner» (PRE1) | Đạt |

### 7.2 Bảng B — Diagram → UC Spec

| Action/decision/guard/end node | Nguồn YAML/BR chính xác | Kết luận |
|---|---|---|
| Action «Open project membership management and choose to add a member» (Project Owner) | NF1 | EXPLICIT |
| Action «Request an existing User account» (System) | NF2 | EXPLICIT |
| Action «Select the User and confirm the addition» (Project Owner) | NF3 | EXPLICIT |
| Action «Verify that the User is active and is not already a member» (System) | NF4; BR-ACTIVE-USER-REQUIRED | EXPLICIT |
| Decision «Already a member?» | AF-01 condition | NECESSARY UML REPRESENTATION |
| Guard [not a member] | Phủ định của AF-01 | NECESSARY UML REPRESENTATION |
| Decision «Account still active?» | EX-01 | NECESSARY UML REPRESENTATION |
| Guard [active] | Phủ định của EX-01 | NECESSARY UML REPRESENTATION |
| Action «Create the membership and refresh the member list» | NF5; POST1 | EXPLICIT |
| Action «Record the membership change in project activity history» | POST2 | EXPLICIT (postcondition) |
| Activity Final F1 | Kết quả: membership được tạo (POST1, POST2) | NECESSARY UML REPRESENTATION |
| Guard [became inactive — EX-01] | EX-01 | NECESSARY UML REPRESENTATION |
| Action «Reject the addition of the inactive account» | EX-01; GUIDE-7.3 | JUSTIFIED DERIVATION — YAML không nêu kết quả của EX-01 |
| Guard [already a member — AF-01] | AF-01 condition | NECESSARY UML REPRESENTATION |
| Action «Report that no new membership is required» | AF-01.1 | EXPLICIT |
| Activity Final F2 (qua merge) | Kết quả: không thay đổi membership (AF-01, EX-01) | NECESSARY UML REPRESENTATION |

### 7.3 Kiểm tra bổ sung

- **Thứ tự bước:** NF4 kiểm tra cả hai điều kiện trong một bước. Diagram tách thành hai decision liên tiếp
  («Already a member?» trước, «Account still active?» sau). Thứ tự này không làm đổi kết quả, vì hai điều kiện
  độc lập và mỗi điều kiện dẫn tới một kết quả riêng.
- **End node:**
  - F1 và F2 là hai kết quả khác nhau: có tạo membership và không đổi gì.
  - AF-01 và EX-01 cùng kết quả nên đã gộp qua một merge node vào F2.
  - Đúng UML (nhiều final là hợp lệ) và đúng quy ước nhóm (cùng kết quả thì gộp).
- **Precondition:** không có action Log In hay «check Project Owner».
- **Reachability:** mọi nhánh đều tới một final; không có action nào có hai cạnh vào.
- **Kết luận:** READY FOR PEER REVIEW.
