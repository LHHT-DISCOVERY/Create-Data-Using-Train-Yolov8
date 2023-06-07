import os
from PIL import Image

def batch_convert_png_to_jpg(input_folder, output_folder):
    # Tạo thư mục đầu ra nếu nó chưa tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lặp qua tất cả các tệp tin trong thư mục đầu vào
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            # Xác định đường dẫn đầy đủ của tệp tin PNG và tạo đường dẫn tương ứng cho tệp tin JPG
            png_path = os.path.join(input_folder, filename)
            jpg_filename = filename[:-4] + '.jpg'
            jpg_path = os.path.join(output_folder, jpg_filename)

            # Chuyển đổi ảnh PNG sang JPG
            image = Image.open(png_path)
            image.convert('RGB').save(jpg_path, 'JPEG')

# Đường dẫn đến thư mục chứa các tệp tin ảnh PNG
input_folder = 'C:\Downloads\data_r'

# Đường dẫn đến thư mục đầu ra cho các tệp tin ảnh JPG
output_folder = 'C:\Downloads\data'

# Chuyển đổi hoàn loạt ảnh từ PNG sang JPG
batch_convert_png_to_jpg(input_folder, output_folder)
