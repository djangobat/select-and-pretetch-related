# Ví dụ sử dụng Django Filter

Xem chi tiết bài viết tại [Tối ưu hóa queryset với select_related và prefetch_related ]()


## Cài đặt

Đầu tiên, tải repository về máy tính:

```bash
git clone https://github.com/djangobat/select-and-pretetch-related.git
```

Cài đặt requirements:

```bash
cd select-and-pretetch-related
pip install -r requirements.txt
```

Tạo database:

```bash
python manage.py makemigrations books
python manage.py migrate
```

Thuực hiện debug:

```bash
python manage.py run_debugger
```
