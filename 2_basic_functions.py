import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
# uint8 is unsigned integer of 8 bits
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 7,7 is kernel size. Must be odd number.
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# Outline.
imgCanny = cv2.Canny(img, 100, 100)
# increases thickness of the outline
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# Opposite of dialation
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Grey Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)