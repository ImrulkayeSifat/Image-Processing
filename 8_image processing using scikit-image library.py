#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:00:39 2022

@author: timjim
"""

import matplotlib.pyplot as plt

from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread("images/Osteosarcoma_01.tif", as_gray=True)

#Rescale, resize image by a given factor. While rescaling image
#gaussian smoothing can performed to avoid anti aliasing artifacts.
img_rescaled = rescale(img, 1.0 / 4.0, anti_aliasing=False)

#Resize, resize image to given dimensions (shape)
img_resized = resize(img, (200, 200),anti_aliasing=True)  #Check dimensions in variable explorer

#Downscale, downsample using local mean of elements of each block defined by user
img_downscaled = downscale_local_mean(img, (4, 3))

plt.imshow(img_downscaled)



#A quick look at a few skimage functions
from skimage import io
from skimage.filters import gaussian, sobel
img = io.imread("images/Osteosarcoma_01_25Sigma_noise.tif")
plt.imshow(img)
gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)
plt.imshow(gaussian_using_skimage)

img_gray = io.imread("images/Osteosarcoma_01.tif", as_gray=True)
sobel_img = sobel(img_gray)  #Works only on 2D (gray) images
plt.imshow(sobel_img, cmap='gray')