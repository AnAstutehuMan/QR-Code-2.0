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
from PIL import Image, ImageTk

rootdir = os.path.dirname(os.path.realpath(__file__))
fs = False

def reSize(path):
    newImg = Image.open(os.path.join(rootdir,path))
    width = 150
    ratio = width/float(newImg.size[0])
    height = int(float(newImg.size[1])*ratio)

    lbl.configure(text="Resizing the Image...")

    newImg = newImg.resize((width, height))
    newImg.convert('RGB').save(os.path.join(rootdir, 'resized/' + path))

    # Convert Image to Base64
    readablefile = open(os.path.join(rootdir, 'resized/' + path), "rb")
    convFile = base64.b64encode(readablefile.read())

    lbl.configure(text="Converting the Image to QR...")

    base64ToQR(convFile, path)


def base64ToQR(convFile, path):
    qr = qrcode.QRCode(
        version=20,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=5,
    )

    # Encoded is the data from Base64 (convFile is `str`)
    qr.add_data(convFile)

    print('Creating Image Ver: ' + str(qr.version))

    qr.make(fit=True)
    newImageToGenerate = qr.make_image(fill_color="black", back_color="white")

    newImageToGenerate.save(os.path.join(rootdir, 'qr/QR - ' + path))

    qr = Image.open(os.path.join(rootdir, 'qr/QR - ' + path))
    qrrender = ImageTk.PhotoImage(qr)
    img.config(image = qrrender)
    img.image = qrrender

def tooglefull():
    if not fs:
        window.attributes("-fullscreen", True)
        fs = True
    elif fs:
        window.attributes("-fullscreen", False)
        fs = False
window = tkinter.Tk()
window.title("QR Image")
window.geometry("500x250")
lbl = tkinter.Label(window, text="Enter the Image path:  ")
lbl.config(width = 25)
lbl.grid(column=0, row=0)

fileName = tkinter.Entry(window, width=10)
fileName.config(width = 25)
fileName.grid(column=1, row=0)


def clicked():
    path = fileName.get()
    print(path)
    lbl.configure(text="Processing the Image...")
    reSize(path)
    lbl.configure(text="Enter the Image path :  ")
    print("Entered the Path!")



btn1 = tkinter.Button(window, text="Submit", command=clicked)
btn1.config(width = 10)
btn1.grid(column=2, row=0)

btn1 = tkinter.Button(window, text="FullScreen", command=tooglefull)
btn1.config(width = 10)
btn1.grid(column=3, row=0)

img = tkinter.Label(window)
img.place(x = 20, y = 50)

window.mainloop()
