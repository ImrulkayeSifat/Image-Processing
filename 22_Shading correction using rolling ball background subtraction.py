#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:56:59 2022

@author: timjim
"""

import cv2
import numpy as np

img = cv2.imread("images/Ti_powder.tif", 1)

lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab_img)


clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
clahe_img = clahe.apply(l)
CLAHE_img = cv2.merge((clahe_img,a,b))

corrected_image = cv2.cvtColor(CLAHE_img, cv2.COLOR_LAB2BGR)

cv2.imshow("Original image", img)
cv2.imshow("Corrected image", corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
from cv2_rolling_ball import subtract_background_rolling_ball
from matplotlib import pyplot as plt

img = cv2.imread("images/Ti_powder.tif", 0)

radius=20
final_img, background = subtract_background_rolling_ball(img, radius, light_background=True,
                                     use_paraboloid=False, do_presmooth=True)


#optionally perform CLAHE to equalize histogram for better segmentation
#otherwise the image may appear washedout. 

clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
clahe_img = clahe.apply(final_img)

#cv2.imshow("Original image", img)
cv2.imshow("Background image", background)
cv2.imshow("AFter background subtraction", final_img)
cv2.imshow("After CLAHE", clahe_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
