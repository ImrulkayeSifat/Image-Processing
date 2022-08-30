#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:58:36 2022

@author: timjim
"""

from skimage import io, filters, feature
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np


img = cv2.imread('images/sandstone.tif', 0)

#Canny
canny_edge = cv2.Canny(img, 50, 80)  #Supply Thresholds 1 and 2 

#Autocanny
sigma = 0.3
median = np.median(img)

# apply automatic Canny edge detection using the computed median
lower = int(max(0, (1.0 - sigma) * median)) 
#Lower threshold is sigma % lower than median
#If the value is below 0 then take 0 as the value

upper = int(min(255, (1.0 + sigma) * median)) 
#Upper threshold is sigma% higher than median
#If the value is larger than 255 then take 255 a the value

auto_canny = cv2.Canny(img, lower, upper)


cv2.imshow("Canny", canny_edge)
cv2.imshow("Auto Canny", auto_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()