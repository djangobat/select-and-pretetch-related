# select_related và prefetch_related

Xem chi tiết bài viết tại [Tối ưu hóa queryset với select_related và prefetch_related ](https://djangobat.com/blog/toi-uu-hoa-queryset-voi-select_related-va-prefetch_related/)


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
python manage.py makemigrations blog
python manage.py migrate
```

Thêm dữ liệu vào:

```bash
python manage.py load_items
```

Chạy debugger:

```bash
python manage.py run_debugger
```
