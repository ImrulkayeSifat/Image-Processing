#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:02:32 2022

@author: timjim
"""

import cv2
img = cv2.imread("images/my_plot.jpg", 1) 

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("original pic", img)
cv2.imshow("resized pic", resized)
cv2.waitKey(0)          
cv2.destroyAllWindows() 


import cv2

grey_img = cv2.imread("images/my_plot.jpg", 0) 
img = cv2.imread("images/my_plot.jpg", 1)   #Color is BGR not RGB

print(img.shape)     
print("Top left", img[0,0])    #Top left pixel
print("Top right", img[0, 432])  # Top right
print("Bottom Left", img[430, 0]) # Bottom left
print("Bottom right", img[430, 1150])  # Bottom right


cv2.imshow("color pic", img)
cv2.waitKey(0)          
cv2.destroyAllWindows() 



#Split and merging channels
#Show individual color channels in the image
blue = img[:, :, 0]   #Show only blue pic. (BGR so B=0)
green = img[:, :, 1]  #Show only green pixels
red = img[:, :, 2]  #red only


cv2.imshow("red pic", red)
cv2.waitKey(0)          
cv2.destroyAllWindows() 


#Or split all channels at once

b,g,r = cv2.split(img)

cv2.imshow("green pic", g)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

img_merged = cv2.merge((b,g,r))

cv2.imshow("merged pic", img_merged)
cv2.waitKey(0)          
cv2.destroyAllWindows() 



import cv2

img = cv2.imread("images/Osteosarcoma_01.tif", 0)
edges = cv2.Canny(img,100,200)   #Image, min and max values

cv2.imshow("Original Image", img)
cv2.imshow("Canny", edges)

cv2.waitKey(0)          
cv2.destroyAllWindows() 