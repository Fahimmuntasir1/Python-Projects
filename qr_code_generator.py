# # A simple black and white QR code generator program
# import qrcode
#
# img = qrcode.make("https://fahimmuntasir1.netlify.app/")
# img.save("portfolio.png")

# Simple QrCode generator with some changes

import qrcode

# What is including in qrcode
data = "https://youtube.com/"

# Create a QR code

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=3
)
# Add data into qr varriable
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(
    fill_color = "red",
    back_color = "white"
)
img.save("youtube.png")