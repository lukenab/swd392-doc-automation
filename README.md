# SWD392 Documentation Automation

**Author:** Nguyễn An Bình

CLI tool dùng YAML làm dữ liệu nguồn để quản lý Use Case của **Project Management
System**. Công cụ kiểm tra dữ liệu và tự động sinh tài liệu Markdown, Word và
PlantUML.

> Chỉ chỉnh sửa dữ liệu trong `data/`. Không chỉnh sửa trực tiếp file trong
> `output/` vì chúng sẽ bị ghi đè khi chạy lại công cụ.

## Cài đặt nhanh

Yêu cầu: Python 3.10 trở lên và `pip`.

```powershell
git clone <repository-url>
cd swd392-doc-automation
py -m pip install -r requirements.txt
py cli.py validate
py cli.py build
```

Nếu sử dụng môi trường ảo:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Cấu trúc chính

```text
swd392-doc-automation/
├── data/
│   ├── actors.yml          # Danh sách actor
│   ├── business_rules.yml  # Danh sách business rule
│   └── use_cases/          # Mỗi Use Case là một file YAML
├── output/                 # Tài liệu được sinh tự động
├── tests/                  # Unit test
├── usecase_tool/           # Mã nguồn xử lý
├── cli.py                  # Điểm chạy CLI
└── requirements.txt        # Thư viện Python
```

## Các lệnh CLI

| Lệnh | Chức năng |
|---|---|
| `py cli.py validate` | Kiểm tra toàn bộ dữ liệu |
| `py cli.py list` | Hiển thị danh sách Use Case |
| `py cli.py build` | Sinh tất cả định dạng |
| `py cli.py build --format markdown` | Chỉ sinh Markdown |
| `py cli.py build --format docx` | Chỉ sinh Word |
| `py cli.py build --format plantuml` | Chỉ sinh PlantUML |
| `py cli.py build --use-case UC-04` | Chỉ sinh một Use Case |

Kết quả được đặt trong `output/`:

| File | Nội dung |
|---|---|
| `use-case-list.md` | Bảng tổng hợp Use Case |
| `use-case-descriptions.md` | Mô tả chi tiết để review trên GitHub |
| `use-case-descriptions.docx` | Bảng Word để đưa vào báo cáo |
| `use-case-diagram.puml` | Source Use Case Diagram |

Nếu Word đang mở, hãy đóng `use-case-descriptions.docx` trước khi chạy `build`.

## Thêm hoặc sửa Use Case

Sao chép một file mẫu trong `data/use_cases/`, đổi ID và cập nhật nội dung. Ví dụ:

```yaml
id: UC-09
name: Archive Project
summary: Archive a project while preserving its history.
created_by: Tran Cong Luan
date_created: 2026-09-24
primary_actor: Project Manager
secondary_actors: []
trigger: The Project Manager selects Archive Project.
description: This use case archives an active project.
preconditions:
  - The project exists and is active.
postconditions:
  - The project becomes archived.
normal_flow:
  - actor: Project Manager
    action: Confirms the archive operation.
  - actor: System
    action: Archives the project.
alternative_flows: []
exceptions: []
priority: Should Have
frequency_of_use: Rare
business_rules: []
other_information: ""
assumptions: []
```

Actor phải tồn tại trong `data/actors.yml`; Business Rule phải tồn tại trong
`data/business_rules.yml`. Sau mỗi thay đổi, chạy:

```powershell
py cli.py validate
py cli.py build
```

## Quy trình làm việc nhóm

1. Tạo branch riêng và sửa các file YAML được giao.
2. Chạy `py cli.py validate`.
3. Commit, push và tạo Pull Request.
4. Thành viên khác review nghiệp vụ và câu chữ.
5. Leader merge rồi chạy `py cli.py build` để cập nhật tài liệu.

Để chạy unit test:

```powershell
py -m unittest discover -s tests -v
```

YAML là **nguồn dữ liệu chính thức**. Word, Markdown và PlantUML chỉ là các định
dạng đầu ra được sinh tự động.
