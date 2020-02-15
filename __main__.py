import base64
import math
import os
import shutil
import time

import qrcode
from PIL import Image

filename = "test.jpg"
readablefile = open(filename, "rb")
encoded = base64.b64encode(readablefile.read())
qrCode = qrcode.make(encoded)

print(encoded)
input()
