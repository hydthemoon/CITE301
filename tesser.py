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

shutil.rmtree('C:/cited3_tesseract', ignore_errors = True)
os.mkdir('C:/cited3_tesseract')

filename = "C:/cited3_img/frame0.jpg"
image = cv2.imread(filename)

cv2.imshow('original', image)
image = get_grayscale(image)
cv2.imshow('grayscle', image)
image = thresholding(image)
cv2.imshow('threshold', image)
image = opening(image)
cv2.imshow('erosion', image)
image = canny(image)
cv2.imshow('canny', image)
cv2.waitKey(0)
text = pytesseract.image_to_string(image, lang = "eng")

f_txt = open("C:/cited3_tesseract/frame0.txt", 'w')
f_txt.write(text)
f_txt.close()