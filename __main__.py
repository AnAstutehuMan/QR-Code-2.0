import time
import math
import qrcode
import os
import shutil
import base64
from PIL import Image     

filename = "test.jpg"
readablefile = open(filename, "rb")
encoded = base64.b64encode(readablefile.read())

print(encoded)
input()