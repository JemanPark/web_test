import qrcode

qr_data = "www.google.com"
qr_img = qrcode.make(qr_data)

save_path = "qr_sample.png"
qr_img.save(save_path)

# print("hello")
