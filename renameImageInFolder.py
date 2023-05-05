import os
import shutil

folder_path = 'C:\Downloads\data'  # đường dẫn tới thư mục chứa các ảnh cần đổi tên
extension = '.jpg'  # đuôi mở rộng của các ảnh

# lấy danh sách các file ảnh trong thư mục
images = [f for f in os.listdir(folder_path) if f.endswith(extension)]

# sắp xếp các file ảnh theo thứ tự tên
images.sort()

# duyệt qua từng file ảnh và đổi tên
for i, image in enumerate(images):
    old_path = os.path.join(folder_path, image)
    new_path = os.path.join(folder_path, str(i) + extension)
    shutil.move(old_path, new_path)
