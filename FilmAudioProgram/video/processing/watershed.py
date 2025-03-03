'''
Created on May 11, 2015

@author: Mitali
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_LABEL_PIXEL,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


