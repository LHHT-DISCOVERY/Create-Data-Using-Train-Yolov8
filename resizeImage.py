import os

from PIL import Image

# đường dẫn tới thư mục chứa các ảnh cần thay đổi kích thước
input_folder = 'C:\Downloads\gggg'

# đường dẫn tới thư mục chứa các ảnh đã thay đổi kích thước
output_folder = 'C:\Downloads\data_r'

# kích thước mới của ảnh
new_size = (640, 640)

# lặp qua từng ảnh trong thư mục
for filename in os.listdir(input_folder):
    # đường dẫn đầy đủ tới ảnh
    input_path = os.path.join(input_folder, filename)
    image = Image.open(input_path)
    if image.mode == "P" or image.mode == "RGBA":
        continue

    # nếu tệp đang xét không phải là tệp ảnh thì bỏ qua
    if not input_path.endswith('.jpg') and not input_path.endswith('.jpeg') and not input_path.endswith('.png'):
        continue

    # mở ảnh và thay đổi kích thước
    img = Image.open(input_path)
    img = img.resize(new_size)

    # tạo tên file mới và lưu ảnh vào thư mục đầu ra
    output_path = os.path.join(output_folder, filename)
    img.save(output_path)
