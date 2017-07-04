import cv2
import numpy as np
from matplotlib import pyplot


def nothing(x):
    pass

img = cv2.imread('imgs/01.jpg',0)

# blur to reduce noise
img = cv2.GaussianBlur(img,(5,5),0)

# canny edge detection on img
cannyImg = cv2.Canny(img,120,220)


cv2.imshow("canny edged image",cannyImg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
