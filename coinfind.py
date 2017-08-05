import cv2
import numpy as np
from matplotlib import pyplot

img = cv2.imread('imgs/01.jpg',0)

def processImage(img):
    # blur to reduce noise
    img = cv2.GaussianBlur(img,(1,1),0)

    # canny edge detection on img
    canny_img = cv2.Canny(img,100,170)

    return canny_img

def boundingCircle(canny_img):
    # morph
    kernel = np.ones((3, 3), np.uint8)
    close_circle = cv2.morphologyEx(canny_img,cv2.MORPH_CLOSE,kernel, iterations=5)

    # fill bounds
    bounding_img = close_circle.copy()

    bounding_circles, hierarchy = cv2.findContours(bounding_img, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)


    # convert back to color
    colored_img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR) 

    return bounding_circles, colored_img


def detectCoins(bounding_circles, colored_img):
    
    count = 0
    for circle in bounding_circles:
        area = cv2.contourArea(circle)

        if 10000 < area and area < 40000:
            count += 1
 
        ellipse = cv2.fitEllipse(circle)
        cv2.ellipse(colored_img, ellipse, (0,0,255),3)

    print("# of coins: " + str(count))

def display(canny_img, colored_img):
    cv2.imshow('original', canny_img)
    cv2.waitKey(0)
    cv2.imshow('draw bounding circles on coins', colored_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    canny_img = processImage(img)
    bounding_circles, colored_img = boundingCircle(canny_img)
    detectCoins(bounding_circles, colored_img)
    display(canny_img, colored_img)

main() 
