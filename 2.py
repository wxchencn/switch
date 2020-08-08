'''
Description: 
Version: 1.0
Autor: wxchen
Date: 2020-08-06 17:10:54
LastEditTime: 2020-08-06 21:45:58
'''

import sys
import cv2
import numpy as np
import imutils

img = cv2.imread("/home/wxchen/datasets/switch/sw1.jpg",0)
image = cv2.imread("/home/wxchen/datasets/switch/sw1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image = cv2.pyrDown(image)
image = cv2.pyrDown(image)
H,S,V = cv2.split(image)
if img is None:
    sys.exit("Could not read the image.")
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)
print(img.shape)

img_bin = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
img_bin = cv2.medianBlur(img_bin, 3)
edged = cv2.Canny(img, 10, 50,apertureSize=3)
lines = cv2.HoughLinesP(edged, 1, np.pi/180, 30)


# result = S.copy()
# edged = cv2.Canny(result, 1, 50,apertureSize=3)
# lines = cv2.HoughLinesP(edged, 1, np.pi/180, 30)
result = img.copy()
for line in lines:
    
    x1,y1,x2,y2 = line[0]
    cv2.line(result, (x1,y1),(x2,y2),(255,0,0),2)
#	rho, theta = line[0]

	# if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #垂直直线
    #             #该直线与第一行的交点
	# 	pt1 = (int(rho/np.cos(theta)),0)
	# 	#该直线与最后一行的焦点
	# 	pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)),result.shape[0])
	# 	#绘制一条白线
	# 	cv2.line( result, pt1, pt2, (255))
	# else: #水平直线
	# 	# 该直线与第一列的交点
	# 	pt1 = (0,int(rho/np.sin(theta)))
	# 	#该直线与最后一列的交点
	# 	pt2 = (result.shape[1], int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))
	# 	#绘制一条直线
	# 	cv2.line(result, pt1, pt2, (255), 1)


cv2.imshow("img", result)
if cv2.waitKey(0) == ord("x"):
    cv2.destroyAllWindows()