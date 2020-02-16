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


def reSize(path):
    newImg = Image.open(path)
    width = 150
    ratio = width/float(newImg.size[0])
    height = int(float(newImg.size[1])*ratio)

    print(ratio)

    newImg = newImg.resize((width, height))
    newImg.convert('RGB').save('Resized/'+path)

    # Convert Image to Base64
    readablefile = open('Resized/' + path, "rb")
    convFile = base64.b64encode(readablefile.read())

    base64ToQR(convFile, path)


def base64ToQR(convFile, path):
    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )

    # Encoded is the data from Base64 (convFile is `str`)
    qr.add_data(convFile)

    print('Creating Image Ver: ' + str(qr.version))

    qr.make(fit=True)
    newImageToGenerate = qr.make_image(fill_color="black", back_color="white")

    newImageToGenerate.save('QR/QR - ' + path)


window = Tk()
window.title("QR Image")
window.geometry('250x250')
lbl = Label(window, text="Enter the Image path:  ")
lbl.grid(column=0, row=0)

fileName = Entry(window, width=10)
fileName.grid(column=1, row=0)

path = str(fileName)
print(path)


def clicked(path):
    lbl.configure(text="Converting the Image to QR")
    reSize(path)
    print("Entered the Path!")


path = str(fileName)
print(path)

btn1 = Button(window, text="Submit", command=clicked)
btn1.grid(column=2, row=0)

btn2 = Button(window, text="Quit", command=window.destroy)
btn2.grid(column=3, row=0)

window.mainloop()
