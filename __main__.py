import pytesseract
import os
import shutil
import base64
from PIL import Image     

filename = "test.jpg"
shutil.copyfile(filename,'copy-'+filename)
covfile = 'copy-'+filename
prefilename, preext = os.path.splitext(covfile)
postfile = os.rename(covfile,prefilename+'.txt')
postfile = open(postfile)
encoded = base64.b64encode(postfile.read())

print(encoded)
input()