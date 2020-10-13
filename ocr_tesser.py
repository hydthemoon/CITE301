import os
import shutil
import cv2
import pytesseract
import numpy as np

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def remove_noise(image):
    return cv2.medianBlur(image,5)
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
def canny(image):
    return cv2.Canny(image, 100, 200)
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags = cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

###     SETTING     ###
vid_target = "lyrics_coldplay_2"
start = 1
end = 200
###     SETTING end ###


i = start
while i <= end :
    filename = "C:/cited3_db/cited3_image_sample/{0}/frame{1}.jpg".format(vid_target, i)
    image = cv2.imread(filename)
    image = get_grayscale(image)
    image = thresholding(image)

### OCR-TESSERACT   ###
    text = pytesseract.image_to_string(image, lang = "eng").replace(" ", "")
### OCR end         ###

    if i == start:
        f_txt = open("C:/cited3_db/cited3_tesseract/{0}.txt".format(vid_target), 'w', -1, 'utf-8')
        f_txt.write("sample{0}\n".format(i))
        f_txt.write(text)
        f_txt.close()
    else :
        f_txt = open("C:/cited3_db/cited3_tesseract/{0}.txt".format(vid_target), 'a', -1, 'utf-8')
        f_txt.write("\nsample{0}\n".format(i))
        f_txt.write(text)
        f_txt.close()
    i += 1