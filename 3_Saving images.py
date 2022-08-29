#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:39:26 2022

@author: timjim
"""

"""
Saving images to local drive 
"""

#Read an image
from skimage import io
img = io.imread("images/Osteosarcoma_01.tif")

#e.g. let us apply gaussian smoothing
from skimage import filters
gaussian_img = filters.gaussian(img, sigma=1)

#Save image using skimage
#Best way as it converts float images to RGB and scales them accordingly
io.imsave("images/export/saved_using_skimage.jpg", gaussian_img)

#Will succeed writing an image but rounds off float
#final image may not look good if saving float 
#so first convert float to 8 bit
from skimage import img_as_ubyte
gaussian_img_8bit = img_as_ubyte(gaussian_img);
io.imsave("images/export/saved_using_skimage_byte.tif",gaussian_img_8bit)

#save image using opencv
import cv2
cv2.imwrite("images/export/saved_using_opencv.jpg", gaussian_img_8bit)

#convert images from BGR to RGB when necessary.

gaussian_img_8bit_RGB = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)
cv2.imwrite("images/export/saved_using_opencv3.jpg", gaussian_img_8bit_RGB)


#############################################################################
#Save using Matplotlib
from matplotlib import pyplot as plt
plt.imsave("images/export/saved_using_pyplot.jpg", gaussian_img)
#For gray images you can define a colormap using cmap

#########################################################################
#Saving images into tiff files..
#USe tifffile library: pip install tifffile
#First convert images to 8 bit and then use tifffile
import tifffile
tifffile.imwrite("images/export/saved_using_tifffile.tiff", gaussian_img_8bit)

#Can also use skimage but image needs to be converted to 8 bit integer first. 
io.imsave("images/export/saved_using_skimage.tif", gaussian_img_8bit)