import qrcode

def gen_code(site):
    img = qrcode.make(site)
    img.save("QR.png")

gen_code("https://github.com/olkhovichs")