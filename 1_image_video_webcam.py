import cv2
print("Package Imported")


# # IMAGE
# img = cv2.imread("Resources/lena.jpg")
#
# cv2.imshow("Output", img)
#
# # To add delay in ms, 0 is infinite
# cv2.waitKey(0)


# # VIDEO
# cap = cv2.VideoCapture("Resources/test_video.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

frameWidth = 640
frameHeight = 480
# WEBCAM
cap = cv2.VideoCapture(0)
# set width
cap.set(3, frameWidth)
# set height
cap.set(4, frameHeight)
# set brightness
cap.set(10, 130)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break