#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 03:01:26 2022

@author: timjim
"""

import cv2
from skimage import io, img_as_float
from skimage.restoration import denoise_tv_chambolle
from matplotlib import pyplot as plt

img = img_as_float(io.imread('images/Osteosarcoma_01_25Sigma_noise.tif', as_gray=True))


plt.hist(img.flat, bins=100, range=(0,1))  #.flat returns the flattened numpy array (1D)


denoise_img = denoise_tv_chambolle(img, weight=0.1, eps=0.0002, n_iter_max=200, multichannel=False)


plt.hist(denoise_img.flat, bins=100, range=(0,1))

cv2.imshow("Original", img)
cv2.imshow("TV Filtered", denoise_img)
cv2.waitKey(0)          
cv2.destroyAllWindows() 