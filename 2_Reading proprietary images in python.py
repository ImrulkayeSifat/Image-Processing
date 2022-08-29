#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 22:58:12 2022

@author: timjim
"""

####Tiff files.... especially multidimensional tiff files####

import tifffile
#RGB images
img = tifffile.imread("images/Osteosarcoma_01.tif")

import numpy as np
print(np.shape(img))

#3D image
img1 = tifffile.imread("images/Osteosarcoma_01_8bit_salt_pepper.tif")
print(np.shape(img1))

#Time series images
img2 = tifffile.imread("images/scratch_time_series.tif")
print(np.shape(img2))

####reading czi files####


import czifile

img = czifile.imread('images/Osteosarcoma_01.czi')
#img = czifile.imread('images/Scratch_Assay_400_289.czi')


print(img.shape)  #7 dimensions
#Time series, scenes, channels, y, x, z, RGB

#Let us extract only relevant pixels, all channels in x and y

img1=img[0, 0, :, :, :, 0]
print(img1.shape)

#Next, let us extract each channel image.
img2=img1[0,:,:]  #First channel, Red
img3=img1[1,:,:] #Second channel, Green
img4=img1[2,:,:] #Third channel, Blue DAPI

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img2, cmap='hot')
ax1.title.set_text('1st channel')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img3, cmap='hot')
ax2.title.set_text('2nd channel')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img4, cmap='hot')
ax3.title.set_text('3rd channel')
plt.show()


from apeer_ometiff_library import io  #Use apeer.com free platform for image processing in the cloud

(pic2, omexml) = io.read_ometiff("images/Osteosarcoma_01_8bit.ome.tiff")  #Unwrap image and embedded xml metadata
print (pic2.shape)   #to verify the shape of the array
print(pic2)

print(omexml)

#Let us extract only relevant pixels, all channels in x and y
img1=img[0, 0, :, :, :, 0]
print(img1.shape)
#Next, let us extract each channel image.
img2=img1[0,:,:]  #First channel, Red
img3=img1[1,:,:] #Second channel, Green
img4=img1[2,:,:] #Third channel, Blue

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img2, cmap='hot')
ax1.title.set_text('1st channel')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img3, cmap='hot')
ax2.title.set_text('2nd channel')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img4, cmap='hot')
ax3.title.set_text('3rd channel')
plt.show()