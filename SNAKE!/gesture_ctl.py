import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

UP_AREA = np.array([[160, 0], [1120, 0], [800, 360], [480, 360]])
DOWN_AREA = np.array([[160, 720], [1120, 720], [800, 360], [480, 360]])
LEFT_AREA = np.array([[0, 0], [160, 0], [480, 360], [160, 720], [0, 720]])
RIGHT_AREA = np.array([[1120, 0], [1280, 0], [1280, 720], [1120, 720], [800, 360]])

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.65, maxHands=6)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    cv2.polylines(img, [UP_AREA], True, (255, 255, 255))
    cv2.polylines(img, [DOWN_AREA], True, (255, 255, 255))
    cv2.polylines(img, [LEFT_AREA], True, (255, 255, 255))
    cv2.polylines(img, [RIGHT_AREA], True, (255, 255, 255))

    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[9]
        up = cv2.pointPolygonTest(UP_AREA, cursor, False)
        down = cv2.pointPolygonTest(DOWN_AREA, cursor, False)
        left = cv2.pointPolygonTest(LEFT_AREA, cursor, False)
        right = cv2.pointPolygonTest(RIGHT_AREA, cursor, False)

        if up == 1.0:
            print("up")
        if down == 1.0:
            print("down")
        if left == 1.0:
            print('left')
        if right == 1.0:
            print('right')

    cv2.imshow("im", img)
    cv2.waitKey(1)
