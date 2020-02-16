import base64
import math
import os
import shutil
import time

import PIL
import qrcode
import qrcode.image.svg
from PIL import Image

filename = "test.png"

# Resize Image
newimg = Image.open(filename)
newimg = newimg.resize((50, 50))
newimg.convert('RGB').save('resized/' + filename)

# Convert Image to Base64
readablefile = open('resized/' + filename, "rb")
convfile = base64.b64encode(readablefile.read())

# Convert Base64 to QR Code
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)

qr.add_data(convfile)  # encoded is the data from Base64
print("Starting")
print('Creating image | ver: ' + str(qr.version))
qr.make(fit=True)

# Save the QR Code to Path
img = qr.make_image(fill_color="black", back_color="white")
img.save('QR/' + filename)

print("Done")
