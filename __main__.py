import base64
import math
import os
import shutil
import time

import qrcode
from PIL import Image

# Convert File to Base64
filename = "test.jpg"
readablefile = open(filename, "rb")
encoded = base64.b64encode(readablefile.read())
qrCode = qrcode.make(encoded)

# print(encoded)
# input()

# Convert Base64 to QR Code
qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encoded)  # encoded is the data from Base64
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
