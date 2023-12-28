# RealEstase Website Django

## Mô tả

Xây dựng một website django quản lí các bài post đăng bất động sản. User sẽ có admin và user đăng bài. Cả user và admin đều phải có lưu thông tin đăng nhập(id user tự generate, user_name, password), phone, email, và link url ảnh profile. ( Admin có quyền kiểm duyệt bài đăng và cho phép đăng(chuyển status bài đăng của user đăng bài sang status). User đăng bài có quyền xem lại bài đăng của mình, xóa sửa bài đăng. Mỗi bài đăng(post) sẽ bao gồm những thông tin như sau(id bài viết tự generate), id_user(đăng bài foreign key của user), user_name đăng bài, tên danh mục(foreign key từ bảng danh mục), title bài viết, body bài viết, link url của ảnh, giá cả, creationtime, publishedtime, status(mặc định khi được tạo sẽ là pending, sau khi được admin duyệt thì mới chuyển sang active), area(diện tích), bedroom(số lượng phòng ngủ), toilet(số lượng toilet), furniture,facade(Số lượng), house_direction(4 hướng đông tây nam bắc), way(độ rộng của đường), pacony_direction(4 hướng đông tây nam bắc), floor(bao nhiêu tầng). Mỗi bài viết sẽ thuộc duy nhất 1 danh mục.

### Chức năng cần có:

- [x] Tạo người dùng, thêm xóa sửa thông tin của người dùng
- [ ] Thêm, xóa, sửa bài post
- [ ] Lọc tìm kiếm bài post

## Cài đặt
- Nếu máy chưa có git vui lòng cài đặt git
- Chọn thư mục để lưu dự án. Nhấn chuột phải chọn Git Bash
- Clone project về máy bằng dòng lệnh sau: git clone https://github.com/Shylinn/django_project.git
- Activate venv(Môi trường ảo) bằng cách run file activate trong thư mục venv/Scripts/activate
- Khởi chạy dự án bằng câu lệnh: python manage.py runserver


