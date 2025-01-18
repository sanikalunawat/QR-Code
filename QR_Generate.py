import qrcode
import numpy as np

data = "https://kjsce.somaiya.edu/en"

qr = qrcode.QRCode(version=1, box_size=10, border=4)   

qr.add_data(data)

qr.make()

print("The shape of the QR image:", np.array(qr.get_matrix()).shape)

img = qr.make_image(fill_color="black", back_color="white")

img.save("Generated_QR.png")







