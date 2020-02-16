import base64
import math
import os
import shutil
import time

import PIL
import qrcode
import qrcode.image.svg 
from PIL import Image

filename = "test.jpg"

newimg = Image.open(filename)
newimg.resize(Image.NEAREST())
newimg.save('new-'+filename)

readablefile = open('new'+filename, "rb")
convfile = base64.b64encode(readablefile.read())

# Convert Base64 to QR Code
qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=5,
)
qr.add_data(convfile)  # encoded is the data from Base64
print("starting")
print('creating image | ver : '+str(qr.version))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qr.jpg')



input("Done")
