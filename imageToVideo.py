import os

import cv2

video_path = 'C:\Downloads\data_video\_dtr.mp4'  # đường dẫn tới video
image_folder = 'C:\Downloads\data2'  # đường dẫn tới thư mục lưu các ảnh

# tạo thư mục lưu các ảnh nếu chưa tồn tại
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# mở video
cap = cv2.VideoCapture(video_path)

# đếm số ảnh được tạo ra
count = 0
count_image = 272

# lặp qua từng khung hình trong video
while cap.isOpened():
    # đọc khung hình tiếp theo
    ret, frame = cap.read()

    # kiểm tra xem video có hết khung hình hay không
    if ret == False:
        break

    # lưu ảnh vào thư mục
    if count % 40 == 0:
        # tạo tên file cho ảnh
        image_name = str(count_image) + '.jpg'
        cv2.imwrite(os.path.join(image_folder, image_name), frame)
        count_image += 1

    # tăng biến đếm
    count += 1

# giải phóng các tài nguyên và đóng video
cap.release()
cv2.destroyAllWindows()
