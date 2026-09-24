# PMS Use Case CLI

Đây là dự án mẫu dùng Python để quản lý Use Case của **Project Management System** bằng YAML. Công cụ kiểm tra tính đồng bộ của dữ liệu và tự động sinh:

- Bảng danh sách Use Case bằng Markdown.
- Toàn bộ Use Case Description bằng Markdown.
- Các bảng Use Case Description trong file Word.
- Source Use Case Diagram bằng PlantUML.

Mục tiêu của công cụ là giúp nhóm chỉ sửa dữ liệu ở một nơi. Các file trong `output/` là kết quả được sinh tự động và không nên chỉnh sửa trực tiếp.

## 1. Cấu trúc dự án

```text
pms-usecase-cli/
├── data/
│   ├── actors.yml
│   ├── business_rules.yml
│   └── use_cases/
│       ├── UC-01-create-project.yml
│       ├── UC-02-manage-project-members.yml
│       └── ...
├── output/
├── tests/
├── usecase_tool/
│   ├── generator.py
│   ├── loader.py
│   └── validator.py
├── cli.py
├── requirements.txt
└── README.md
```

Các thư mục quan trọng:

- `data/`: dữ liệu nguồn được phép chỉnh sửa.
- `data/use_cases/`: mỗi Use Case nằm trong một file YAML riêng.
- `usecase_tool/`: source code của chương trình.
- `output/`: tài liệu được tạo tự động.
- `tests/`: kiểm thử các quy tắc validation.

## 2. Yêu cầu môi trường

- Python 3.10 trở lên.
- `pip` để cài thư viện.
- PlantUML chỉ cần thiết nếu muốn chuyển file `.puml` thành ảnh.

Kiểm tra Python:

```powershell
python --version
```

Nếu Windows không nhận lệnh `python`, thử:

```powershell
py --version
```

## 3. Cài đặt trên Windows PowerShell

Di chuyển vào thư mục dự án:

```powershell
cd pms-usecase-cli
```

Tạo môi trường ảo:

```powershell
python -m venv .venv
```

Kích hoạt môi trường:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell chặn script kích hoạt, có thể dùng Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Cài thư viện:

```powershell
python -m pip install -r requirements.txt
```

Nếu lệnh tạo môi trường ảo báo lỗi `ensurepip`, có thể chạy trực tiếp bằng Python Launcher:

```powershell
py -m pip install -r requirements.txt
py cli.py validate
```

## 4. Chạy thử

### Kiểm tra dữ liệu

```powershell
python cli.py validate
```

Kết quả hợp lệ:

```text
Validation completed: 8 use case(s), 0 errors.
  [OK] UC-01 - Create Project
  [OK] UC-02 - Manage Project Members
  ...
```

### Xem danh sách Use Case

```powershell
python cli.py list
```

### Sinh toàn bộ tài liệu

```powershell
python cli.py build
```

Kết quả được đặt trong `output/`:

```text
output/
├── use-case-list.md
├── use-case-descriptions.md
├── use-case-descriptions.docx
└── use-case-diagram.puml
```

### Chỉ sinh Markdown

```powershell
python cli.py build --format markdown
```

### Chỉ sinh Word

```powershell
python cli.py build --format docx
```

### Chỉ sinh PlantUML

```powershell
python cli.py build --format plantuml
```

### Chỉ sinh một Use Case

```powershell
python cli.py build --use-case UC-04
```

## 5. Cách thêm một Use Case

Sao chép một file trong `data/use_cases/`, sau đó đổi tên và cập nhật nội dung. Ví dụ:

```text
data/use_cases/UC-09-archive-project.yml
```

Cấu trúc cơ bản:

```yaml
id: UC-09
name: Archive Project
summary: Archive an active project while preserving its history.
created_by: Tran Cong Luan
date_created: 2026-09-24
primary_actor: Project Manager
secondary_actors: []
trigger: The Project Manager selects Archive Project.
description: This use case archives an active project.
preconditions:
  - The project exists and is active.
postconditions:
  - The project becomes archived and read-only.
normal_flow:
  - actor: Project Manager
    action: Selects Archive Project.
  - actor: System
    action: Requests confirmation.
  - actor: Project Manager
    action: Confirms the archive operation.
  - actor: System
    action: Archives the project.
alternative_flows: []
exceptions: []
priority: Should Have
frequency_of_use: Rare
business_rules:
  - BR-08
other_information: ""
assumptions: []
```

Sau khi thêm hoặc sửa file, luôn chạy:

```powershell
python cli.py validate
python cli.py build
```

## 6. Các kiểm tra được thực hiện

Công cụ hiện kiểm tra:

- Use Case ID phải có dạng `UC-01`, `UC-02`, ...
- Không được trùng Use Case ID.
- Các trường bắt buộc không được để trống.
- Primary Actor và Secondary Actors phải tồn tại trong `actors.yml`.
- Actor trong Normal Flow phải hợp lệ hoặc là `System`.
- Business Rule phải tồn tại trong `business_rules.yml`.
- Priority phải thuộc `Must Have`, `Should Have`, `Could Have` hoặc `Won't Have`.
- Normal Flow phải có `actor` và `action`.
- Những trường dạng danh sách phải được viết dưới dạng YAML list.

Ví dụ lỗi:

```text
[ERROR] UC-04: unknown primary actor 'Manager'.
[ERROR] UC-04: unknown Business Rule 'BR-99'.
```

## 7. Quản lý Actor và Business Rule

Actor chỉ được định nghĩa một lần trong:

```text
data/actors.yml
```

Business Rule chỉ được định nghĩa một lần trong:

```text
data/business_rules.yml
```

Use Case chỉ tham chiếu bằng tên Actor và Business Rule ID. Cách này giúp tránh việc cùng một actor bị viết thành `Project Manager`, `Manager` và `Project Admin` ở nhiều tài liệu khác nhau.

## 8. Quy trình làm việc nhóm

Mỗi thành viên nên phụ trách một nhóm file Use Case:

1. Tạo branch riêng.
2. Sửa các file YAML được giao.
3. Chạy `python cli.py validate`.
4. Commit và tạo Pull Request.
5. Một thành viên khác kiểm tra nghiệp vụ và câu chữ.
6. Leader merge Pull Request.
7. Leader chạy `python cli.py build` để tạo lại toàn bộ tài liệu.

Không sửa trực tiếp các file trong `output/`. Nếu bảng Word sai, hãy sửa file YAML tương ứng rồi chạy lại lệnh `build`.

## 9. Đưa nội dung vào Google Docs

Quy trình đơn giản:

1. Chạy `python cli.py build --format docx`.
2. Mở `output/use-case-descriptions.docx`.
3. Sao chép toàn bộ phần Use Case Descriptions vào Course Project Report.
4. Khi dữ liệu thay đổi, sửa YAML và generate lại.
5. Thay toàn bộ phần Use Case cũ bằng bản mới; không sửa riêng từng bảng trong Google Docs.

Nếu nhóm muốn đồng bộ hoàn toàn tự động với Google Docs thì cần thêm Google Docs API. Phần này chưa cần thiết cho phiên bản đầu tiên của CLI.

## 10. Sinh ảnh Use Case Diagram

Lệnh `build` tạo file:

```text
output/use-case-diagram.puml
```

Nếu đã cài PlantUML:

```powershell
plantuml output/use-case-diagram.puml
```

PlantUML sẽ tạo ảnh Use Case Diagram từ cùng dữ liệu actor và Use Case. Diagram này thể hiện actor nào liên kết với Use Case nào, nhưng chưa tự động tạo quan hệ `include`, `extend` hoặc actor generalization.

## 11. Chạy kiểm thử

```powershell
python -m unittest discover -s tests -v
```

Các test mẫu kiểm tra dữ liệu hợp lệ, actor không tồn tại và Business Rule không tồn tại.

## 12. Nguyên tắc nguồn dữ liệu duy nhất

```text
data/*.yml             Được chỉnh sửa
output/*.md            Được sinh tự động
output/*.docx          Được sinh tự động
output/*.puml          Được sinh tự động
```

Nếu có khác biệt giữa YAML và Word, YAML được xem là dữ liệu chính thức. Word chỉ là định dạng trình bày để đưa vào báo cáo.
