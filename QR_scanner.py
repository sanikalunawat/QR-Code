import cv2

img = cv2.imread("Generated_QR.png")
detector = cv2.QRCodeDetector()

data, box, straight_qrcode = detector.detectAndDecode(img)
print(data)
