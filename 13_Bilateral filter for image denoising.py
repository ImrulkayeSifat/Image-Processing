#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 02:35:02 2022

@author: timjim
"""

import cv2

img_gaussian_noise = cv2.imread('images/Osteosarcoma_01_25Sigma_noise.tif', 0)
img_salt_pepper_noise = cv2.imread('images/Osteosarcoma_01_8bit_salt_pepper.tif', 0)

img = img_gaussian_noise
cv2.imshow("Original", img)

bilateral_using_cv2 = cv2.bilateralFilter(img, 5, 20, 100, borderType=cv2.BORDER_CONSTANT)
cv2.imshow("cv2 bilateral", bilateral_using_cv2)


from skimage.restoration import denoise_bilateral
bilateral_using_skimage = denoise_bilateral(img, sigma_color=0.05, sigma_spatial=15, multichannel=False)
cv2.imshow("Using skimage bilateral", bilateral_using_skimage)