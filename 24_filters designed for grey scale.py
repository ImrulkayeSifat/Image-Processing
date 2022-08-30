#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 00:08:54 2022

@author: timjim
"""


from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage import filters
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

image = io.imread("images/monalisa.jpg")

try_to_apply_sobel = filters.sobel(image)


@adapt_rgb(each_channel)
def sobel_each(image):
    return filters.sobel(image)


@adapt_rgb(hsv_value)
def sobel_hsv(image):
    return filters.sobel(image)


each_channel_image = sobel_each(image)
hsv_value_image = sobel_hsv(image)

#Convert to grey if needed

sobel_grey = rgb2gray(hsv_value_image)

plt.imshow(sobel_grey)


import cv2

@adapt_rgb(each_channel)
def median_each(image, k):
    output_image = cv2.medianBlur(image, k)
    return (output_image)

median_using_cv2 = median_each(image, 3)
plt.imshow(median_using_cv2)


from skimage import exposure

@adapt_rgb(each_channel)
def eq_each(image):
    output_image = exposure.equalize_hist(image)
    return (output_image)

equ_RGB = eq_each(image)
plt.imshow(equ_RGB)


@adapt_rgb(hsv_value)
def eq_hsv(image):
    output_image = exposure.equalize_hist(image)
    return (output_image)

equ_hsv = eq_hsv(image)
plt.imshow(equ_hsv)


fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image)
ax1.title.set_text('Input Image')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(equ_RGB)
ax2.title.set_text('Equalized using RGB channels')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(equ_hsv)
ax3.title.set_text('Equalized using v channel in hsv')

plt.show()
