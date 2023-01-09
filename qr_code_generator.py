import qrcode

img = qrcode.make("https://fahimmuntasir1.netlify.app/")
img.save("portfolio.png")
