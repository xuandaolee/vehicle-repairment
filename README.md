# Car Repair Center Management System

Hệ thống quản lý trung tâm sửa chữa ô tô được xây dựng bằng Flask, SQLAlchemy và MySQL với kiến trúc module hóa (Blueprints).

## Yêu cầu hệ thống

- Python 3.10+
- MySQL 8.0+

## Cài đặt

### 1. Clone repository

```bash
git clone <repository-url>
cd car-repair
```

### 2. Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv env
```

Kích hoạt môi trường ảo:

**Windows:**
```bash
env\Scripts\activate
```

**Linux/macOS:**
```bash
source env/bin/activate
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 4. Cấu hình database

Tạo file `.env` trong thư mục gốc với nội dung:

```env
SECRET_KEY=your_secret_key_here
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=car_repair_db
```

### 5. Khởi tạo database

Chạy file SQL để tạo database và các bảng ban đầu:

```bash
mysql -u root -p < database/schema.sql
```

Hoặc sử dụng MySQL Workbench để import file `database/schema.sql`.

## Chạy ứng dụng

Sử dụng script `run.py` ở thư mục gốc:

```bash
python run.py
```

Ứng dụng sẽ chạy tại: http://127.0.0.1:5000

## Tài khoản mặc định

| Username   | Password | Role       |
|------------|----------|------------|
| admin      | 123      | Admin      |
| reception  | 123      | Reception  |
| tech       | 123      | Technician |
| cashier    | 123      | Cashier    |

## Cấu trúc thư mục (Mới)

Dự án đã được tái cấu trúc theo mô hình package:

```
car-repair/
├── app/                    # Application Package
│   ├── __init__.py         # App factory, DB setup, Login Manager
│   ├── models.py           # SQLAlchemy Data Models
│   ├── dao/                # Data Access Objects (Tách biệt logic database)
│   ├── index.py            # Main Blueprint (Home, Login, Logout)
│   ├── admin.py            # Admin Blueprint
│   ├── reception.py        # Reception Blueprint
│   ├── technician.py       # Technician Blueprint
│   ├── cashier.py          # Cashier Blueprint
│   ├── static/             # Static assets (css, images)
│   └── templates/          # Jinja2 Templates (theo module)
├── database/
│   └── schema.sql          # Database schema gốc
├── run.py                  # Entry point để chạy ứng dụng
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
└── README.md               # Project documentation
```

## Tính năng chính

- **Kiến trúc Module hóa**: Sử dụng Flask Blueprints để phân chia logic theo chức năng (Admin, Reception, Technician, Cashier).
- **ORM**: Sử dụng Flask-SQLAlchemy thay vì raw SQL để tăng tính bảo mật và dễ bảo trì.
- **DAO Pattern**: Tách biệt lớp truy cập dữ liệu vào thư mục `app/dao/`.
- **Phân quyền**: Role-based Access Control (RBAC) với Flask-Login.

### Các Module:
- **Reception**: Tiếp nhận xe, tạo phiếu tiếp nhận.
- **Technician**: Quản lý sửa chữa, thêm vật tư/phụ tùng, cập nhật trạng thái.
- **Cashier**: Xem danh sách xe đã sửa xong, xuất hóa đơn, xử lý thanh toán.
- **Admin**: Dashboard thống kê doanh thu, tần suất xe, quản lý linh kiện.
