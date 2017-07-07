import cv2
import numpy as np
from matplotlib import pyplot


img = cv2.imread('imgs/01.jpg',0)

# blur to reduce noise
img = cv2.GaussianBlur(img,(5,5),0)

# canny edge detection on img
cannyImg = cv2.Canny(img,100,170)

#morph
kernel = np.ones((3, 3), np.uint8)
close = cv2.morphologyEx(cannyImg,cv2.MORPH_CLOSE,kernel, iterations=5)

cv2.imshow("canny edged image",close)
cv2.waitKey(0)
cv2.destroyAllWindows() 
