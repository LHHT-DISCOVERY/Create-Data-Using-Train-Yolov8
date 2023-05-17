import os

folder_path = "C:\Downloads\Vehicle Detection.v2-raw.yolov8\_train\labels"  # Thay thế bằng đường dẫn đến thư mục chứa các tệp tin

# Lặp qua từng tệp tin trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # Chỉ thay thế các tệp tin có phần mở rộng .txt
        file_path = os.path.join(folder_path, filename)

        # Đọc nội dung của tệp tin
        with open(file_path, "r") as file:
            content = file.read()

        # Thực hiện thay thế phần nội dung
        content = content.replace("2 ", "1 ")

        # Ghi nội dung đã thay thế vào tệp tin
        with open(file_path, "w") as file:
            file.write(content)
