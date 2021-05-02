<<<<<<< HEAD
import cv2 as cv
import mediapipe as mp
import bodydetection as bfd

cap = cv.VideoCapture(0)
detector = bfd.bodyDetector()

while True:
    isTrue , img = cap.read()
    img = detector.findBody(img)

    cv.imshow("body", img)

    if cv.waitKey(1) & 0xFF == ord('f'):
        break 
=======
import cv2 as cv
import mediapipe as mp
import bodydetection as bfd

cap = cv.VideoCapture(0)
detector = bfd.bodyDetector()

while True:
    isTrue , img = cap.read()
    img = detector.findBody(img)

    cv.imshow("body", img)

    if cv.waitKey(1) & 0xFF == ord('f'):
        break 
>>>>>>> 4548fc9d6af6359635c79b43d52e09c24cc37d08
