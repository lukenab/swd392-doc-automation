# Hướng dẫn vẽ Activity Diagram cho cả nhóm (SWD392)

Đây là hướng dẫn thao tác chung trước khi vẽ hoặc review một Activity Diagram. Mục tiêu là cả 4 thành viên vẽ ra
sơ đồ cùng ngữ nghĩa, cùng format và cùng cách kiểm tra. Nguồn nghiệp vụ vẫn là YAML/Business Rules của từng UC;
template chỉ chuẩn hóa cấu trúc và trình bày, không thay thế Use Case Specification.

- Bản gốc tiếng Anh là `docs/activity-diagram-guideline.md`. Nếu hai tài liệu khác nhau, bản gốc thắng. Hãy báo
  cho leader để sửa lại file này.
- Mỗi quy tắc có một nhãn để biết nó bắt buộc tới đâu:

| Nhãn | Ý nghĩa |
|---|---|
| **[UML]** | Ngữ nghĩa UML 2.5.1. Sai là sơ đồ sai. |
| **[TEAM]** | Quy ước của nhóm. UML không bắt buộc, nhưng cả nhóm phải theo để thống nhất. |
| **[TRÌNH BÀY]** | Lựa chọn để dễ đọc khi in vào báo cáo Word A4. Được phép lệch nếu có lý do. |

## 1. Phạm vi và phân công

- Mỗi **concrete Use Case** có đúng một Activity Diagram. Use case cha trừu tượng `Manage …` không vẽ.
- Use case con như UC-09.2, UC-24.6, UC-27.2 có sơ đồ riêng. Tổng cộng có 55 sơ đồ.

| Người vẽ | Use Case |
|---|---|
| Trần Công Luận | UC-01–04, UC-05.1–05.3, UC-32.1–32.4, UC-33 |
| Nguyễn An Bình | UC-06–08, UC-09.1–09.3, UC-10–13, UC-28–31 |
| Nguyễn Quốc Khánh | UC-14.1–14.3, UC-15.1–15.4, UC-16–22 |
| Nguyễn Tấn Trung | UC-23, UC-24.1–24.7, UC-25–26, UC-27.1–27.5 |

Danh sách chính xác (display ID ↔ semantic key ↔ đường dẫn file) nằm trong `diagrams/activity/manifest.yml`.
Luôn tìm file theo **semantic key** trong manifest, không đoán từ mã UC.

## 2. Đọc gì trước khi vẽ

### 2.1 Thứ tự đọc

1. File YAML của UC: `data/use_cases/<domain>/UC-<KEY>.yml`. Mở file và kiểm tra trường `key:` bên trong.
2. Trigger và preconditions.
3. Normal flow (NF1, NF2, …).
4. Alternative flows (AF-01, …) và từng bước của chúng (AF-01.1, …).
5. Exceptions (EX-01, …).
6. Postconditions.
7. Các Business Rule được tham chiếu, trong `data/business_rules.yml`.

### 2.2 Thứ tự ưu tiên khi các nguồn khác nhau

1. YAML của UC.
2. Business Rules.
3. Định nghĩa actor/group.
4. Các tài liệu đã duyệt.

Sơ đồ cũ (kể cả của người khác) **không bao giờ** là nguồn chuẩn.

### 2.3 Khi spec có vấn đề

- **Spec mâu thuẫn**, ví dụ AF cần bắt đầu từ một trạng thái mà precondition đã loại trừ: không vẽ. Ghi
  `BLOCKED — REQUIREMENT CONFLICT` cùng câu hỏi cho BA vào manifest.
- **Spec thiếu thông tin** để vẽ: ghi `BLOCKED — INSUFFICIENT SPECIFICATION`.
- **Không tự bịa luồng** để «chữa» spec. Không sửa YAML hay Business Rule chỉ để sơ đồ hợp lệ.
- Một EX/AF mô tả trạng thái bị precondition loại trừ, nhưng System **phát hiện được**: vẽ thành bước kiểm tra
  phòng thủ của System và ghi observation.

## 3. Chuẩn bị công cụ và quy trình

### 3.1 Công cụ

- Java (JRE) để chạy PlantUML.
- `tools/plantuml.jar`, bản 1.2024.7 trở lên. File này không commit, tự tải về.
- Python 3.

**Không** vẽ bằng draw.io, Visual Paradigm hay PlantUML online. Format chung chỉ có khi render bằng pipeline của
repo.

### 3.2 Các bước từ YAML tới Jira

1. Tạo nhánh riêng từ `develop`, ví dụ `docs/activity-<tên>`.
2. Đọc YAML theo mục 2.
3. Copy **file template duy nhất** ở mục 5 vào `diagrams/activity/<domain>/source/UC-<KEY>.puml`.
4. Vẽ từng bước. Mỗi action có trace comment.
5. Render:
   `py scripts/activity_diagrams.py render --key UC-<KEY> --plantuml-jar tools/plantuml.jar`
6. Kiểm tra:
   `py scripts/activity_diagrams.py validate`
   Không được còn lỗi nào thuộc UC của mình.
7. Mở SVG xem bằng mắt và tính cỡ chữ (mục 8).
8. Commit **chỉ** file `.puml` và `.svg` (không commit PNG), tạo PR, rồi chuyển Jira sang `In Review`.

## 4. Đặt tên và thư mục [TEAM]

```text
diagrams/activity/
├── manifest.yml                       một entry cho mỗi concrete UC
├── _shared/activity-style.puml        style dùng chung — KHÔNG tự sửa
└── <domain>/
    ├── source/UC-<SEMANTIC-KEY>.puml  file nguồn
    └── svg/UC-<SEMANTIC-KEY>.svg      file đưa vào báo cáo
```

- Domain: `account-authentication`, `project-membership`, `product-backlog`, `sprint-management`, `sprint-work`,
  `collaboration-notification`, `scrum-reporting`, `system-administration`.
- Tên file dùng semantic key, ví dụ `UC-SPRINT-TASK-CREATE.puml`, không dùng `UC-24.2.puml`. Display ID chỉ xuất
  hiện trong header comment, manifest và caption.
- Nếu `_shared/activity-style.puml` cần thay đổi, báo leader. File này ảnh hưởng cả 55 sơ đồ.

## 5. Một file template `.puml` cho cả nhóm [TEAM]

**Chỉ copy file** `.claude/skills/activity-diagram/templates/activity-template.puml` làm điểm xuất phát. Đây là
template PlantUML dùng chung cho mọi thành viên, kể cả người không dùng Claude. File
`diagrams/activity/_shared/activity-style.puml` là style được `!include`, **không** phải sơ đồ để copy. Không tạo
thêm một bản template khác trong tài liệu hoặc thư mục cá nhân.

Template chứa ví dụ minh họa cho NF, AF lặp và EX; chúng **không** phải các bước mặc định của mọi UC. Trước khi
render, thay display ID, semantic key, domain, Business Rules, lane và toàn bộ action/guard theo spec của UC; **xóa**
khối AF/EX hoặc action minh họa nếu spec không có. Không được giữ lại placeholder hoặc copy logic của UC-24.2.

Quy trình dùng template cho một UC:

1. Tìm đúng entry trong `diagrams/activity/manifest.yml`; mở YAML của semantic key đó và các Business Rules được
   tham chiếu.
2. Lập ánh xạ `TRIGGER / NF / AF / EX / POST / BR → action, decision, guard hoặc final`. Với chiều ngược lại,
   mỗi node/nhánh phải chỉ ra được nguồn; precondition không tự trở thành action.
3. Copy template vào đúng đường dẫn `source/` trong manifest. Giữ `!include ../../_shared/activity-style.puml`,
   header comment và cách khai báo lane; đổi alias/tên actor cho đúng UC.
4. Thay toàn bộ bước minh họa bằng nội dung của UC. Chỉ giữ decision/loop/exception có căn cứ. Nếu AF yêu cầu sửa
   và gửi lại, sau bước gửi lại phải **thực hiện lại bước validate** trước khi kiểm tra guard; không quay thẳng về
   decision trên kết quả validate cũ.
5. Đặt final theo **kết quả** của từng nhánh. Nhánh loại trừ nhau có thể nối qua merge; không dùng fork/join để
   gộp success với rejection, và không bắt buộc mọi kết quả khác nhau phải về cùng một final.
6. Render, chạy validator, mở SVG kiểm tra bằng mắt và đối chiếu hai chiều theo mục 9 trước khi đưa vào PR/Jira.

`UC-24.2 – Create Sprint Task` chỉ có thể tham khảo bố cục hai lane, **không** dùng làm template nghiệp vụ: YAML
hiện có AF-01 nhưng sơ đồ tham khảo chưa phản ánh đầy đủ AF này. Khi có khác biệt, YAML/BR thắng.

### 5.1 Quy ước trong file nguồn [TEAM]

- Header comment ở đầu file, chứa display ID, tên, semantic key, đường dẫn YAML và Business Rules.
- Khi sơ đồ có **hơn một** Activity Final, thêm dòng `' Final nodes:` giải thích kết quả của từng final.
- Không dùng `title`, `caption`, `header`, `footer`, `legend`, `note`. Caption nằm trong Word.
- Không dùng `skinparam` hay đổi font trong file UC. Mọi style lấy từ `!include`.
- Trước **mỗi** action có một trace comment, ví dụ `' [NF4, POST1, BR-…]`. Các tham chiếu hợp lệ:
  - `NFn`, `PREn`, `POSTn`, `TRIGGER`
  - `AF-xx` (cả AF), `AF-xx.n` (một bước của AF), `EX-xx`
  - Business Rule key của UC
  - `OTHER` (lấy từ other_information)
  - `GUIDE-7.3`: action reject/report được thêm vì YAML nêu exception nhưng không nêu kết quả.

## 6. Quy tắc vẽ

### 6.1 Phần tử UML và quy ước kiểm tra

- [TEAM] Vẽ **một** Initial Node và ít nhất một Activity Final cho mỗi sơ đồ UC. Đây là chuẩn của nhóm,
  không phải giới hạn số lượng node mà UML áp đặt.
- [UML] Control flow có hướng.
- [UML] Dùng Decision node khi luồng rẽ nhánh.
- [UML] Dùng Merge node khi các nhánh loại trừ nhau nhập lại. **Không** cho hai đường đi thẳng vào cùng một
  action: theo UML, action có nhiều đường vào là *implicit join*, tức phải chờ đủ mọi đường, không phải merge.
- [UML] Fork/Join chỉ dùng khi thật sự chạy song song. Hiện chưa UC nào cần.
- [TEAM] Mọi nhánh của UC phải có lối kết thúc được thể hiện rõ. Action cuối không nối tới final hoặc bước tiếp
  theo là đường treo cần sửa; reviewer phải lần theo **từng guard**, kể cả AF/EX.

### 6.2 Swimlane (partition)

- [UML] Partition thể hiện **trách nhiệm**: việc actor làm nằm ở lane actor, việc hệ thống làm nằm ở lane
  System.
- [TEAM] Chỉ dùng các tên lane sau:

| Lane | Dùng khi |
|---|---|
| `Guest` | Người chưa đăng nhập (đăng ký, đăng nhập, quên mật khẩu). |
| `User` | Thành viên/tài khoản bất kỳ, không cần vai trò dự án. |
| `Project Owner` | Bước cần vai trò Project Owner. |
| `Product Owner` / `Developer` | YAML ghi «Acting as the Product Owner/Developer», hoặc BR yêu cầu vai trò đó. |
| `System Administrator` | Quản trị hệ thống. |
| `System` | Hệ thống Project Management. Sơ đồ nào cũng có. |
| `Email Service`, `Identity Provider` | Service bên ngoài có tham gia luồng. |

- [TEAM] **Không** dùng `Project Member`, `Database`, `UI`, `Server` hay tên module nội bộ.
- [TEAM] Dùng ít lane nhất có thể, thường là hai. Thứ tự từ trái sang phải: actor chính, System, service ngoài.
- [TEAM] Khai báo mọi lane với alias trước `start`.
- [TEAM] Ở đầu nhánh `else`, khai báo lại lane, vì nhánh `else` kế thừa lane ở cuối nhánh `then`.
- [TEAM] Decision mà **actor** chọn (xác nhận/hủy, chọn chức năng) đặt trong lane của actor, không đặt trong lane
  System.

### 6.3 Action

- [TEAM] Viết dạng động từ + tân ngữ, câu thường: «Validate the comment», không viết «Validate Comment» hay
  «Comment validation».
- [TEAM] Bám chữ của YAML. Không thêm bước không có nguồn, như «Retrieve data», «Check status», «Load page».
- [TEAM] Không dùng action chung chung («Validate», «Display error», «Notify», «Retry», «Record change») khi không
  có câu YAML cụ thể đứng sau.
- [TEAM] **Không vẽ Log In** hay việc kiểm tra precondition thành action. Đăng nhập là precondition, chỉ có trong
  UC-SIGN-IN.
- [TEAM] Postcondition nên thể hiện ở action System cuối, ví dụ «Record the change in activity history» cho
  POST2.
- [TRÌNH BÀY] Ngắt dòng ở khoảng 15–35 ký tự, tối đa khoảng 5 dòng.

### 6.4 Decision và guard

- [UML] Mỗi đường ra của decision có guard trong `[ ]`. Các guard loại trừ nhau và phủ hết mọi trường hợp.
- [TEAM] Decision là một câu hỏi ngắn: «Work item still exists?».
- [TEAM] Guard có nghĩa, kèm mã AF/EX khi nhánh thuộc AF/EX: `[removed — EX-01]`, `[invalid — AF-01]`. Không dùng
  `yes`/`no`/`error` trơn.
- [TEAM] Luôn dùng helper:
  - `$question("…")` cho câu hỏi.
  - `$question_x("…")` **chỉ khi** luồng đi vào decision từ lane khác. Trong cùng lane mà dùng `_x` thì tạo
    khoảng trống thừa.
  - `$guard_left("[…]")` cho guard của nhánh `then`.
  - `$guard_right("[dòng 1", "dòng 2]")` cho nhánh `else`.
  - `$guard("[…]")` cho guard thoát vòng lặp.
  - Các helper này chỉ thêm khoảng trống vô hình, không đổi chữ.
- [TRÌNH BÀY] Sau khi render, kiểm tra từng guard **nằm sát đúng đường của nó**. Lỗi hay gặp: nhãn ở bên phải
  nhưng đường lại đi sang trái.
- [TRÌNH BÀY] Nếu action đầu tiên của nhánh `then` nằm ở lane khác với diamond, nhãn guard sẽ bị đường cắt. Đặt
  action đầu của nhánh `then` cùng lane với diamond, hoặc đảo nhánh.

### 6.5 Alternative flow

- [TEAM] Đặt decision đúng ở bước mà AF xảy ra.
- [TEAM] AF quay lại bước nó làm lại (dùng vòng lặp), hoặc nối tiếp ngay sau bước sinh ra nó.
- [TEAM] AF kiểu hủy hoặc kết thúc thì đi tới final.

### 6.6 Exception

- [TEAM] Guard ghi mã EX: `[account inactive — EX-01]`.
- [TEAM] Trước final phải có **một action System nêu kết quả**: «Reject …», «Report …», «Record …».
  - Nếu YAML có nêu kết quả, dùng đúng câu đó.
  - Nếu không, trace bằng `GUIDE-7.3`.
- [TEAM] Không để exception kết thúc im lặng, tức đi thẳng từ decision vào final.
- [TEAM] Không tạo exception mới, kể cả lỗi validate, khi YAML/BR không mô tả. Ghi vào observation trong
  manifest.

### 6.7 Vòng lặp

- [TEAM] Dùng `while (…) is ([guard lặp]) … endwhile ([guard thoát])`. Cả hai guard phải có nhãn.
- [TEAM] Sau `Correct and resubmit …` phải quay về bước **Validate …** rồi mới xét lại điều kiện hợp lệ.
  Nếu dùng `while`, đặt action validate lại **trong thân vòng lặp**, trước `endwhile`. Không dùng kết quả
  kiểm tra cũ cho lần gửi lại; soát cả luồng mũi tên trên SVG, không chỉ đọc mã PlantUML.
- [TEAM] Không dùng `repeat … repeat while`: với decision hình thoi, PlantUML làm mất nhãn guard.
- [TEAM] Không vẽ lại toàn bộ luồng thành công sau khi thử lại.
- [TRÌNH BÀY] Giới hạn đã biết: khi thân vòng lặp đi sang lane actor, đường thoát sẽ cắt qua hai đường của thân
  vòng lặp. Đây là giới hạn của PlantUML, chấp nhận được.

### 6.8 Final node

- [UML] Một activity **được phép** có nhiều Activity Final. Final đầu tiên được chạm sẽ kết thúc toàn bộ
  activity. UML **không** yêu cầu chỉ có một final.
- [UML] Flow Final chỉ kết thúc một luồng, các luồng song song khác vẫn chạy. Hiện không UC nào cần.
- [TEAM] Các nhánh **cùng kết quả** dùng chung một final qua merge node. Hủy, bị từ chối, hay không có dữ liệu
  đều tính là cùng kết quả khi UC kết thúc không đạt postcondition và không thay đổi dữ liệu.
- [TEAM] Final riêng chỉ dành cho **kết quả khác nhau**, và mỗi final được giải thích trong `' Final nodes:`.
- [TEAM] Khi các kết quả khác nhau đan xen trên nhánh lồng nhau, dùng **một** final chung. Action cuối của mỗi
  nhánh nêu kết quả của nhánh đó.
- [TEAM] Được giữ hai final cùng kết quả **chỉ khi** gộp lại sẽ phải vẽ một bước hai lần. Phải ghi lý do trong
  header (đã dùng ở UC-10 và UC-13).
- [TEAM] Không gộp làm sai kết quả. Không tạo «error ending» không có trong spec.
- [UML] Fork/Join đồng bộ các luồng **song song**; Merge nối các nhánh **loại trừ nhau**. Không dùng Fork/Join
  chỉ để kéo các nhánh AF/EX về một Activity Final.
- [TRÌNH BÀY] Đặt `|LANE|` ngay trước `stop` để final nằm đúng lane.

### 6.9 Trình bày chung

Phần lớn đã có sẵn trong shared style. Không tự chỉnh.

| Thành phần | Chuẩn |
|---|---|
| Hướng | Luồng chính từ trên xuống, nằm gần giữa lane System; lane xếp trái → phải |
| Font | Times New Roman cho mọi chữ |
| Cỡ chữ | Tên lane 18 px đậm; action 16 px; decision 15 px; guard 14 px |
| Hình | Action bo góc; decision và merge hình thoi; không gradient, không bóng |
| Đường | Đen hoặc xám đậm, cùng độ dày; mũi tên hở (renderer tự đổi) |
| Khung | Khung ngoài đầy đủ và đường kẻ dưới tên lane (renderer tự thêm) |
| Tiêu đề | Không có tiêu đề trong sơ đồ |
| Khổ | Dọc. Khổ ngang là ngoại lệ, phải ghi vào manifest |

### 6.10 Bẫy PlantUML đã biết [TRÌNH BÀY]

| Bẫy | Cách xử lý |
|---|---|
| `repeat while` mất nhãn guard | Dùng `while … endwhile` |
| `elseif` vẽ ra hình lục giác; `switch`/`goto` không dùng được trong swimlane | Lồng nhiều decision 2 nhánh |
| Nhánh `else` kế thừa lane của nhánh `then` | Khai báo lại `\|LANE\|` ở đầu nhánh `else` |
| Shared style bật `useVerticalIf`: nhánh **khác rỗng** được vẽ ngay dưới diamond, nhánh rỗng vòng sang phải | Muốn exception nằm ngang thì đặt phần còn lại của luồng chính vào `then` và exception vào `else` (template mục 5, dạng B) |
| Final hoặc merge cuối bị vẽ vào lane actor | Đặt `\|SYS\|` ngay trước `stop`. Cách này không phải lúc nào cũng hiệu quả với merge; nếu còn lệch mà không sai ngữ nghĩa thì ghi nhận |
| Sơ đồ quá rộng (chữ nhỏ) | Ngắt chữ action hẹp hơn, bỏ decision dư, gộp các kiểm tra thuộc cùng một bước YAML |

## 7. Lỗi thường gặp — KHÔNG làm

| # | Lỗi | Tại sao sai |
|---|---|---|
| 1 | Hai hoặc nhiều đường đi thẳng vào một action (vòng lặp quay về thẳng action, hai nhánh nhập vào «Record change») | [UML] implicit join. Phải đi qua merge node. |
| 2 | Action exception không có đường ra (ngõ cụt) | [TEAM] nhánh EX chưa thể hiện kết quả kết thúc; nối tới bước tiếp theo hoặc final đúng kết quả. |
| 3 | Exception đi thẳng vào final mà không có action kết quả | [TEAM] kết thúc im lặng. |
| 4 | Action của actor nằm trong lane System, hoặc ngược lại; decision do actor chọn đặt trong lane System | [UML] partition sai trách nhiệm. |
| 5 | Thêm bước không có trong YAML («Retrieve Sprint data», «Check task status») | [TEAM] không có nguồn. |
| 6 | Nhánh có guard chung chung («[invalid request]») hoặc thiếu guard | [UML] mọi đường ra cần guard rõ nghĩa. |
| 7 | Thiếu một AF hoặc EX của YAML | [TEAM] `validate` sẽ báo lỗi. |
| 8 | Guard hoặc chữ bị đường nối cắt ngang | [TRÌNH BÀY] khó đọc khi in. |
| 9 | Font sans-serif hoặc monospace, cỡ chữ tự chỉnh, viết hoa từng chữ («Display Error Message») | [TEAM] lệch format chung. |
| 10 | Lane «Project Member», «Database», «UI» | [TEAM] không thuộc danh sách lane. |
| 11 | Có note, title hay legend trong sơ đồ | [TEAM] caption nằm ở Word. |
| 12 | Vẽ «Log In» trong UC khác | [TEAM] đăng nhập là precondition. |

## 8. Kiểm tra sau khi render và khi chèn Word A4

1. Lệnh `render` in kích thước SVG và báo lỗi layout (chữ bị đường cắt, chữ đè lên action). Phải sạch.
2. Mở SVG ở 100 % và kiểm tra:
   - Không có chữ bị cắt hay đè lên nhau.
   - Không có đường nối chồng lên nhau.
   - Guard nằm cạnh đúng đường của nó.
   - Final nằm đúng lane.
   - Không có tiêu đề.
3. Tính cỡ chữ guard khi in, khi sơ đồ được co vào vùng 16,5 × 20,5 cm:

   `cỡ chữ (pt) = 10,5 × min(1; 623,6 / rộng_px; 774,8 / cao_px)`

   Ngưỡng của nhóm là khoảng **6 pt**. Dưới mức đó thì sơ đồ là `needs-manual-review`: phải chỉnh lại, hoặc leader
   quyết định cho dùng cả trang.
4. Chèn vào Word:
   - Insert → Pictures → chọn SVG.
   - Rộng ≤ 16,5 cm, cao ≤ 20,5 cm, giữ tỉ lệ.
   - Caption: `Figure <n>. <Use Case Name> Activity Diagram (<UC ID>)`.
5. Xuất PDF hoặc in thử ở 100 %. Đọc được mọi guard mà không cần phóng to thì đạt.

## 9. Checklist

### 9.1 Người vẽ tự kiểm trước khi chuyển `In Review`

- [ ] Một sơ đồ cho một concrete UC; tên file là semantic key; nằm trong `source/` và `svg/`.
- [ ] Khớp YAML hiện tại: có trigger, mọi NF, mọi AF, mọi EX, postcondition, và BR ảnh hưởng tới luồng.
- [ ] Mọi action có trace comment. Không có action không có nguồn. Không có Log In hay kiểm tra precondition.
- [ ] Một Initial Node. Mọi nhánh tới được một final. Final cùng kết quả đã gộp hoặc có giải thích.
- [ ] Mọi decision có guard đầy đủ, loại trừ nhau. Vòng lặp quay về đúng bước.
- [ ] AF sửa/gửi lại đi qua validate mới rồi mới tới decision; không kiểm tra lại trên dữ liệu cũ.
- [ ] Mọi action và decision nằm đúng lane.
- [ ] Mọi exception có action nêu kết quả.
- [ ] Không có đường treo, chồng hay mơ hồ. Không có chữ bị cắt. Guard ≈ 6 pt trở lên ở A4.
- [ ] Không có tiêu đề hay note. Font và style lấy từ shared style.
- [ ] `py scripts/activity_diagrams.py validate` không báo lỗi cho UC này.

### 9.2 Peer reviewer

- [ ] Lập hai bảng đối chiếu:
  - **Bảng A — Spec → Diagram**: mỗi mục trigger, NF, AF, EX, POST, BR ứng với node hoặc nhánh nào.
  - **Bảng B — Diagram → Spec**: mỗi action, decision, guard, final lấy nguồn từ đâu. Kết luận là một trong:
    EXPLICIT, NECESSARY UML REPRESENTATION, JUSTIFIED DERIVATION, UNSUPPORTED, CONFLICT, UNCLEAR.
- [ ] Không còn UNSUPPORTED, CONFLICT hay UNCLEAR chưa được giải thích.
- [ ] Đã mở SVG thật và chèn thử vào Word. Không duyệt chỉ dựa trên file `.puml`.

Ví dụ hai bảng đầy đủ: `docs/activity-diagram-binh-acceptance-report.md` (hiện nằm trên nhánh `docs/activity-binh-review`).

### 9.3 Leader

- [ ] Peer review đã xong và mọi comment đã được trả lời.
- [ ] `final_status` và `observations` trong manifest đúng với thực tế.
- [ ] Chỉ leader chuyển Jira sang `Done`.

## 10. Jira

- Mỗi UC là một subtask: `To Do` → `In Progress` → `In Review` → (`Changes requested` → `In Progress`) → `Done`.
- Có thể đính kèm PNG preview trên Jira. Trên GitHub chỉ lưu `.puml` và `.svg`.
- `final_status: ready-for-peer-review` trong manifest chỉ có nghĩa là đã qua các bước kiểm tra tự động. Nó
  **không** thay cho peer review và leader.

Mẫu comment khi yêu cầu sửa:

```text
Changes requested

UC: <UC ID> — <Use Case Name>

Cần sửa:
1. <Lệch NF/AF/EX/postcondition/BR — ghi tên node và bước YAML>
2. <Sai node UML, guard, merge, lane hoặc đường nối>
3. <Lỗi trình bày hoặc không đọc được khi chèn Word>

Bằng chứng nghiệm thu:
- File .puml đã sửa
- File SVG đã render lại
- Kết quả validate
- Xác nhận đã đối chiếu với YAML hiện tại
```
