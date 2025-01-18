import qrcode
import tkinter as tk
from PIL import Image, ImageTk

def generate_qr_code():
    text = entry.get()  
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=7)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("generated_qr.png")  
    
    qr_image = Image.open("generated_qr.png")
    qr_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image

window = tk.Tk()
window.title("QR Code Generator")

# Box to enter text
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# button to generate QR
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# label to display QR image
qr_label = tk.Label(window)
qr_label.pack()

window.mainloop()