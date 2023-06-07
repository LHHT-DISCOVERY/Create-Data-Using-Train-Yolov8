from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


# from reportlab.pdfgen import canvas


def bienBanNopPhat(info, image_path, output_file_path):
    # Tạo đối tượng Canvas với kích thước trang letter
    c = canvas.Canvas(output_file_path, pagesize=letter)
    # dfmetrics.registerFont(TTFont('Arial Unicode', 'ArialUnicode.ttf'))

    # Chèn tiêu đề biên bản phạt
    c.setFont("Helvetica-Bold", 18)
    c.drawString(130, 750, "CONG HOA XA HOI CHU NGHIA VIET NAM")
    c.drawString(200, 730, "DOC LAP - TU DO - HANH PHUC")
    c.drawString(230, 700, "BIEN BAN PHAT TIEN")

    # Chèn thông tin người vi phạm
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 650, "Ho va Ten : {}".format(info['name']))
    c.drawString(50, 620, "Dia Chi Thuong Tru : {}".format(info['address']))
    c.drawString(50, 590, "NGAY VI PHAM : {}".format(info['date']))

    # Chèn ảnh vi phạm
    c.drawString(50, 570,
                 "Hinh Anh Vi Pham Tu He Thong Giam Sat Giao Thong TP DA NANG NGAY ( {}".format(info['date']) + " )")
    c.drawImage(image_path, 50, 420, width=3 * inch, height=2 * inch)
    c.drawImage(image_path, 300, 420, width=3 * inch, height=2 * inch)

    # Chèn nội dung biên bản phạt
    c.setFont("Helvetica", 12)
    c.drawString(50, 400, "NOI DUNG BIEN BAN PHAT NGUOI :")
    c.drawString(50, 380, "- LOI VI PHAM : {}".format(info['violation']))
    c.drawString(50, 360, "- LOI KHAC (NEU CO) : {}".format(info['violationOther']))
    c.drawString(50, 340, "- MUC PHAT: {} VND".format(info['fine']))
    c.drawString(50, 320, "- HAN NOP PHAT : {}".format(info['deadline']))
    c.drawString(50, 300, "- Y KIEN CUA NGUOI DIEU KHIEN PHUONG TIEN : {}".format(info['opinion']))
    c.drawString(100, 250, " NGUOI VI PHAM")
    c.drawString(410, 250, " CAN BO GIAM SAT")

    c.drawString(130, 230, " KI TEN  ")
    c.drawString(440, 230, "  KI TEN ")

    # Lưu tệp tin PDF
    c.save()


# Thông tin biên bản phạt
penalty_info = {
    'name': '....................................................................................................................................',
    'address': '....................................................................................................................',
    'date': '2023-05-27',
    'violation': 'VUOT AU DI KHONG DUNG LAN XE QUI DINH',
    'violationOther': '....................................................................................................................',

    'fine': ".....................................................................",
    'deadline': '..................................................................',
    'opinion': ': ...................................................................'
}

# Đường dẫn đến file ảnh vi phạm
image_path = '_18.jpg'

# Đường dẫn đến file biên bản phạt mới
output_file_path = 'ticket/ticket.pdf'

# Gọi hàm để tạo biên bản phạt có chứa hình ảnh
bienBanNopPhat(penalty_info, image_path, output_file_path)
