# COORDINATE SYSTEM
# -------->X
# |
# |
# |
# v
# Y

import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
print(img.shape)
# width, height
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)
# height first, then width
imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)