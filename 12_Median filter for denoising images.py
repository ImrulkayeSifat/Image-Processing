#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 02:13:34 2022

@author: timjim
"""

import cv2
from skimage.filters import median

img_gaussian_noise = cv2.imread('images/Osteosarcoma_01_25Sigma_noise.tif', 0)
img_salt_pepper_noise = cv2.imread('images/Osteosarcoma_01_8bit_salt_pepper.tif', 0)

img = img_salt_pepper_noise
median_using_cv2 = cv2.medianBlur(img, 3)
cv2.imshow("cv2 median", median_using_cv2)

from skimage.morphology import disk  
#Disk creates a circular structuring element, similar to a mask with specific radius
median_using_skimage = median(img, disk(3), mode='constant', cval=0.0)


cv2.imshow("Original", img)

cv2.imshow("Using skimage median", median_using_skimage)

cv2.waitKey(0)          
cv2.destroyAllWindows() 