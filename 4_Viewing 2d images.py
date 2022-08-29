#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:09:30 2022

@author: timjim
"""

from skimage import io
img = io.imread("images/Osteosarcoma_01.tif")

io.imshow(img)

#MATPLOTLIB.PYPLOT
import matplotlib.pyplot as plt
plt.imshow(img)  

#Colormaps...  https://matplotlib.org/tutorials/colors/colormaps.html
plt.imshow(img, cmap="hot")

img_gray = io.imread("images/Osteosarcoma_01.tif", as_gray=True)
plt.imshow(img_gray, cmap="hot")
plt.imshow(img_gray, cmap="jet")
plt.imshow(img_gray, cmap="Blues")


#Multiple plots using pyplot
fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray, cmap='hot')
ax1.title.set_text('1st')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_gray, cmap='jet')
ax2.title.set_text('2nd')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_gray, cmap='gray')
ax3.title.set_text('3rd')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_gray, cmap='nipy_spectral')
ax4.title.set_text('4th')
plt.show()

#Using opencv

import cv2

gray_img = cv2.imread("images/Osteosarcoma_01.tif", 0)
color_img = cv2.imread("images/Osteosarcoma_01.tif", 1)

cv2.imshow("pic from skimage import", img)  #Shows weird colors as R and B channels are swapped
cv2.imshow("color pic from opencv", color_img)
cv2.imshow("gray pic from opencv", gray_img)

# Maintain output window until 
# user presses a key or 1000 ms (1s)
cv2.waitKey(0)          

#destroys all windows created
cv2.destroyAllWindows() 