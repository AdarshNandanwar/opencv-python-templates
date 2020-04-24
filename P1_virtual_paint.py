import cv2
import numpy as np

# WEBCAM
frameWidth = 640
frameHeight = 480
# WEBCAM
cap = cv2.VideoCapture(0)
# set width
cap.set(3, frameWidth)
# set height
cap.set(4, frameHeight)
# set brightness
cap.set(10, 70)

myColors = [[20, 41, 129, 34, 255, 255],
            [44, 19, 0, 95, 166, 255],
            [157, 84, 166, 179, 185, 255]]
# BGR, Not RGB
myColorValues = [[0, 255, 255],
                 [229, 255, 104],
                 [255, 153, 255]]

# [x, y, colorId]
myPoints = []

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    # RETR_EXTERNAL good for outer corners, CHAIN_APPROX_NONE to get all boundary points
    # CHAIN_APPROX_NONE gives only corner points
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # Getting corner points, 0.02*peri is threshold
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break