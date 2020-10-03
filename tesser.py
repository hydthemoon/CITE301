import os
import shutil
from PIL import Image
from pytesseract import *

## FILE 생성
shutil.rmtree('C:/cited3_tesseract', ignore_errors = True)
os.mkdir('C:/cited3_tesseract')

cnt = 0

filename = "C:/cited3_img/frame16.jpg"
image = Image.open(filename)
text = image_to_string(image, lang="eng")

with open("sample.txt", "w") as f:
    f.write(text)


cnt = 0

