import base64
import math
import os
import shutil
import time
import tkinter
from pathlib import Path
import PIL
import qrcode
import qrcode.image.svg
from PIL import Image

def reSize(path):
    rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)),path)
    newImg = Image.open(rootdir)
    width = 150
    ratio = width/float(newImg.size[0])
    height = int(float(newImg.size[1])*ratio)

    print(ratio)

    newImg = newImg.resize((width, height))
    newImg.convert('RGB').save('resized/'+path)

    # Convert Image to Base64
    readablefile = open('resized/' + path, "rb")
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

    newImageToGenerate.save('qr/QR - ' + path)


window = tkinter.Tk()
window.title("QR Image")
window.geometry('250x250')
lbl = tkinter.Label(window, text="Enter the Image path:  ")
lbl.grid(column=0, row=0)

fileName = tkinter.Entry(window, width=10)
fileName.grid(column=1, row=0)


def clicked():
    path = fileName.get()
    print(path)
    lbl.configure(text="Converting the Image to QR")
    reSize(path)
    print("Entered the Path!")



btn1 = tkinter.Button(window, text="Submit", command=clicked)
btn1.grid(column=2, row=0)

window.mainloop()
