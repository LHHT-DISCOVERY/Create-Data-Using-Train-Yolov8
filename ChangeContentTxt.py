import os

folder_path = "C:\Downloads\coco128\coco128\labels\_train2017"  # Thay thế bằng đường dẫn đến thư mục chứa các tệp tin

# Lặp qua từng tệp tin trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # Chỉ thay thế các tệp tin có phần mở rộng .txt
        file_path = os.path.join(folder_path, filename)

        # Đọc nội dung của tệp tin
        with open(file_path, "r") as file:
            content = file.read()

        # Thực hiện thay thế phần nội dung
        content = content.replace("2 ", "3 ")

        # Ghi nội dung đã thay thế vào tệp tin
        with open(file_path, "w") as file:
            file.write(content)


#  0 : car -> 4
#  1 : máy -> 0
#  2 : tải -> 1
#  3 : bus

# 0 : car
# 1 : máy
# 2 : đạp
# 3 : truck  ko cần đổi
# 4 : bus