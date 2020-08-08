'''
Description: 
Version: 1.0
Autor: wxchen
Date: 2020-08-06 11:48:33
LastEditTime: 2020-08-06 16:54:38
'''
import sys
import cv2
import numpy as np
import imutils

img = cv2.imread("/home/wxchen/datasets/switch/sw1.jpg")
if img is None:
    sys.exit("Could not read the image.")
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)
print(img.shape)

img_gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gary = cv2.medianBlur(img_gary, 3)
img_bin = cv2.adaptiveThreshold(img_gary,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
edged = cv2.Canny(img_gary, 25, 125)


# cnts = cv2.findContours(img_gary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

cnts = cv2.findContours(edged.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.drawContours(img_gary, cnts, -1, (255,0,0), 1)

# i = 0
# max = 0
# for i in range(len(cnts)):


# approx = cv2.approxPolyDP(cnts[1], 3, True)
# cv2.polylines(img_gary, [approx], True, (255, 0, 0), 2)

# cv2.imshow("edged", edged)
cv2.imshow("cnts", img_gary)
if cv2.waitKey(0) == ord("x"):
    cv2.destroyAllWindows()
