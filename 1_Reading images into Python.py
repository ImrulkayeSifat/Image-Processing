# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

######### scikit-image #########

from skimage import io

img = io.imread("images/Osteosarcoma_01.tif")
print(img.shape)  #y,x,c

#x = Width = 1376
#y = Height = 1104
#Channels = 3 (RGB)

#Some image processing tasks in skimage require floating point image
#with values between 0 and 1

from skimage import img_as_float
img2 = img_as_float(img)

import numpy as np
img3 = img.astype(np.float)
#avoid using astype as it violates assumptions about dtype range.
#for example float should range from 0 to 1 (or -1 to 1) but if you use 
#astype to convert to float, the values do not lie between 0 and 1. 

#Convert back to 8 bit
from skimage import img_as_ubyte
img_8bit = img_as_ubyte(img2)

######### Using openCV #########

import cv2

grey_img = cv2.imread("images/Osteosarcoma_01.tif", 0)
color_img = cv2.imread("images/Osteosarcoma_01.tif", 1)

#images opened using cv2 are numpy arrays
print(type(grey_img)) 
print(type(color_img)) 

#Big difference between skimage imread and opencv is that 
#opencv reads images as BGR instead of RGB.

img_opencv = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB) #Should be same as skimage image