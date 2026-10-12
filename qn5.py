import qrcode

message = input("Enter your name or a short message: ")

img = qrcode.make(message)
img.save("message_qr.png")

print("Message QR code saved as message_qr.png")

website = input("Enter your favorite website: ")

img2 = qrcode.make(website)
img2.save("website_qr.png")

print("Website QR code saved as website_qr.png")
