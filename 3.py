'''
Description: 
Version: 1.0
Autor: wxchen
Date: 2020-08-26 09:10:46
LastEditTime: 2020-08-26 21:50:41
'''
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("/home/wxchen/Project/switch/images/1598411420.jpg")

img = cv.medianBlur(img, 5)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)

titles = ['Original Image', 'Adaptive Mean Thresholding']
images = [img, th2,]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


# fast

# # Initiate FAST object with default values
# fast = cv.FastFeatureDetector_create()
# # find and draw the keypoints
# kp = fast.detect(img,None)
# img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

# adaptive binary

