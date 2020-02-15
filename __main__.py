import base64
import math
import os
import shutil
import time

import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    box_size=20,
    border=4
)

filename = "test.jpg"
readablefile = open(filename, "rb")
encoded = base64.b64encode(readablefile.read())

qrcode.make(encoded)

input()
