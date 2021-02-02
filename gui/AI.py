import cv2
import numpy as np
import math
global cap
cap = cv2.VideoCapture(0)
def update():
    su=0
    try:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        kernel = np.ones((3, 3), np.uint8)
        x=100
        y=100
        h=200
        w=200
        roi = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        mask = cv2.dilate(mask, kernel, iterations=4)
        mask = cv2.GaussianBlur(mask, (5, 5), 100)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        hull = cv2.convexHull(cnt)
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)
        arearatio = ((areahull - areacnt) / areacnt) * 100
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)
        l = 0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            pt = (100, 180)
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            s = (a + b + c) / 2
            ar = math.sqrt(s * (s - a) * (s - b) * (s - c))
            d = (2 * ar) / a
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
            if angle <= 90 and d > 30:
                l += 1
                cv2.circle(roi, far, 3, [255, 0, 0], -1)
            cv2.line(roi, start, end, [0, 255, 0], 2)
        l += 1
        font = cv2.FONT_HERSHEY_SIMPLEX
        if l == 1:
            if areacnt < 2000:
                pass
            else:
                if arearatio < 12:
                    pass
                    cv2.putText(frame, 'moving hand', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                else:
                    su = 1
                    cv2.putText(frame, 'option 1', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 2:
            su = 2
            cv2.putText(frame, 'option 2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 3:
            su = 3
            cv2.putText(frame, 'option 3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 4:
            su = 4
            cv2.putText(frame, 'option 4', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 5:
            su = 5
            cv2.putText(frame, 'Deselect All', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        else:
            pass
        cv2.imshow('frame', frame)
    except:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    return su
