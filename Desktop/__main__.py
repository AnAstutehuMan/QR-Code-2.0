import base64
import math
import os
import shutil
import time
import tkinter

import PIL
import qrcode
import qrcode.image.svg
from PIL import Image


def reSize(fileName):
    newImg = Image.open(fileName)
    width = 150
    ratio = width/float(newImg.size[0])
    height = int(float(newImg.size[1])*ratio)

    print(ratio)

    newImg = newImg.resize((width, height))
    newImg.convert('RGB').save('Resized/'+fileName)

    # Convert Image to Base64
    readablefile = open('Resized/' + fileName, "rb")
    convFile = base64.b64encode(readablefile.read())

    base64ToQR(convFile, fileName)  



def base64ToQR(convFile, fileName):
    qr = qrcode.QRCode(
        version = 40,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 5,
    )

    qr.add_data(convFile)  # Encoded is the data from Base64 (convFile is `str`)

    print('Creating Image Ver: ' + str(qr.version))

    qr.make(fit=True)
    newImageToGenerate = qr.make_image(fill_color="black", back_color="white")

    newImageToGenerate.save('QR/QR - ' + fileName)


reSize('test.jpg')
