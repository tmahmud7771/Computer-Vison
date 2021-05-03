<<<<<<< HEAD
import cv2 as cv
import mediapipe as mp
import FaceAndHandDetectionModule as bfd

cap = cv.VideoCapture(0)
detector = bfd.

while True:
    isTrue , img = cap.read()

    cv.imshow("body", img)

    if cv.waitKey(1) & 0xFF == ord('f'):f
        break 
=======
import cv2 as cv
import mediapipe as mp
import FaceAndHandDetectionModule as bfd

cap = cv.VideoCapture(0)
detector = bfd.

while True:
    isTrue , img = cap.read()

    cv.imshow("body", img)

    if cv.waitKey(1) & 0xFF == ord('f'):f
        break 
