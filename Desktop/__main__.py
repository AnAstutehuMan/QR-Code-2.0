import base64
import math
import os
import shutil
import time
from tkinter import *
import PIL
import qrcode
import qrcode.image.svg 
from PIL import Image

main = Tk()

title = Label(main, text = "BASE-64 Image to QR")
title.grid()

fileselector = Entry(main)
fileselector.grid()

filename = "test.jpg"

def conv():
    width = 150
    newimg = Image.open(filename)
    ratio = width/float(newimg.size[0])
    height = int(float(newimg.size[1])*ratio)
    print(ratio)
    newimg = newimg.resize((width,height)).show()
    newimg.convert('RGB').save('resized/'+filename)

    # Convert Image to Base64
    readablefile = open('resized/' + filename, "rb")
    convfile = base64.b64encode(readablefile.read())

    # Convert Base64 to QR Code
    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(convfile)  # encoded is the data from Base64
    print("starting")
    print('creating image | ver : '+str(qr.version))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr/qr'+filename)



main.mainloop()
