#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 02:49:01 2022

@author: timjim
"""

import cv2
import numpy as np
from skimage import io, img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma

img_gaussian_noise = img_as_float(io.imread('images/Osteosarcoma_01_25Sigma_noise.tif', as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread('images/Osteosarcoma_01_8bit_salt_pepper.tif', as_gray=True))

img = img_gaussian_noise

sigma_est = np.mean(estimate_sigma(img, multichannel=True))


denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True,
                               patch_size=5, patch_distance=3, multichannel=False)



cv2.imshow("Original", img)
cv2.imshow("NLM Filtered", denoise_img)
cv2.waitKey(0)          
cv2.destroyAllWindows() 