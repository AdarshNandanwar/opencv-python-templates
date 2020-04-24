import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# Color whole img
# img[:] = 255, 0, 0

# Color part of img
# img[200:300, 100:200] = 255, 0, 0

# Line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Hollow Rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# Filled Rectangle
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

# Circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# Text
cv2.putText(img, " OPEN CV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow("Image", img)
cv2.waitKey(0)