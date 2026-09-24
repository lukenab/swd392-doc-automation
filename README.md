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
│   ├── groups.yml          # Danh sách business domain
│   ├── actors.yml          # Danh sách actor
│   ├── business_rules.yml  # Danh sách business rule
│   └── use_cases/          # Use Case được chia theo domain
│       ├── <domain-folder>/
│       │   └── UC-<DOMAIN>-<ACTION>.yml
│       └── ...
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
| `py cli.py build --use-case UC-<DOMAIN>-<ACTION>` | Chỉ sinh một Use Case theo semantic key |

Kết quả được đặt trong `output/`:

| File | Nội dung |
|---|---|
| `use-case-list.md` | Bảng tổng hợp Use Case |
| `use-case-descriptions.md` | Mô tả chi tiết để review trên GitHub |
| `use-case-descriptions.docx` | Bảng Word để đưa vào báo cáo |
| `use-case-diagram.puml` | Source Use Case Diagram |
| `id-mapping.md` | Mapping semantic key với ID được sinh tự động |

Nếu Word đang mở, hãy đóng `use-case-descriptions.docx` trước khi chạy `build`.

## Thêm hoặc sửa Use Case

### 1. Chọn domain

- Domain phải được khai báo trong `data/groups.yml`.
- Mỗi domain có một `folder` tương ứng.
- File Use Case phải nằm trong đúng folder của domain.

### 2. Tạo file YAML

Sao chép một file có sẵn trong `data/use_cases/` vào folder cần sử dụng.

Tên file phải trùng với semantic key:

```text
UC-<DOMAIN>-<ACTION>.yml
```

```text
Key:      UC-<DOMAIN>-<ACTION>
Group:    <DOMAIN_KEY>
File:     data/use_cases/<domain-folder>/UC-<DOMAIN>-<ACTION>.yml
```

Quy tắc đặt tên:

- Sử dụng chữ in hoa và dấu gạch ngang.
- Sử dụng phần mở rộng `.yml`.
- Không sử dụng khoảng trắng.
- Không sử dụng generated ID như `UC-05.yml`.

### 3. Cập nhật nội dung

- `key`: định danh ổn định của Use Case.
- `group`: domain chứa Use Case.
- `order`: vị trí của Use Case bên trong domain.
- Các trường còn lại: nội dung dùng để generate tài liệu.

```yaml
key: UC-<DOMAIN>-<ACTION>
group: <DOMAIN_KEY>
order: 100
name: <Use Case Name>
summary: <Short description>
created_by: <Author Name>
date_created: <YYYY-MM-DD>
primary_actor: <Primary Actor>
secondary_actors: []
trigger: <Event that starts the use case>
description: <Use case description>
preconditions:
  - <Precondition>
postconditions:
  - <Postcondition>
normal_flow:
  - actor: <Actor Name>
    action: <Actor action>
  - actor: System
    action: <System response>
alternative_flows: []
exceptions: []
priority: <Must Have | Should Have | Could Have | Won't Have>
frequency_of_use: <Frequency>
business_rules: []
other_information: ""
assumptions: []
```

Các giá trị tham chiếu phải tồn tại trước:

- Actor trong `data/actors.yml`.
- Business Rule trong `data/business_rules.yml`.
- Domain trong `data/groups.yml`.

### 4. Kiểm tra và generate

Sau mỗi thay đổi, chạy:

```powershell
py cli.py validate
py cli.py build
```

### Quy tắc sắp xếp

- Nên đặt `order` cách nhau 100 trong từng domain.
- Hai Use Case thuộc hai domain khác nhau có thể cùng `order: 100`.
- Để chèn giữa `100` và `200`, sử dụng `order: 150`.
- Không cần thay đổi semantic key khi thay đổi `order`.

CLI sắp xếp theo `group.order`, sau đó theo `order`. Trong DOCX, trường
`UC ID and Name` vẫn có dạng `UC-05 - <Use Case Name>`.

### Tạo domain mới

Khi nhóm chốt domain, thêm một entry có `key`, `name`, `folder`, `order` vào
`data/groups.yml` và tạo folder tương ứng dưới `data/use_cases/`.

```yaml
groups:
  - key: <DOMAIN_KEY>
    name: <Domain Name>
    folder: <domain-folder>
    order: 100
```

Business Rule cũng phải có `group` và `order`.

Thứ tự của UC và BR được quản lý độc lập. Vì vậy, một UC và một BR trong cùng
domain đều có thể sử dụng `order: 100`.

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
