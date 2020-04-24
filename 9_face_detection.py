import cv2

# haar cascade is not the most accurate, but it is very fast and thus can be used with camera
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/lena.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Scale Factor = 1.1, min neighbours = 4
# min neighbours is the min number of squares that must be near each other to classify it as a face
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)