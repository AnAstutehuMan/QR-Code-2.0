import base64
import math
import os
import shutil
import time

import qrcode
from PIL import Image

filename = "test.png"
readablefile = open(filename, "rb")
convfile = base64.b64encode(readablefile.read())

# Convert Base64 to QR Code
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(convfile)  # encoded is the data from Base64
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qr.png')

input("Done")