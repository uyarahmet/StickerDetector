import numpy as np
import cv2
from detector import detectormethod

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    input = detectormethod(frame)
    mask = None
    frame = cv2.resize(frame, (1000, 750))
    if (input[0] == 1):
        print("Detected!")
        mask = input[6]
        cv2.circle(frame, (int(input[3] + input[1] / 2), int(input[4] + input[1] / 2)), int(input[1] / 2),
                   (0, 255, 0), 10)
        cv2.circle(frame, (int(input[3] + input[1] / 2), int(input[4] + input[1] / 2)), 1, (0, 0, 255), 30)
        cv2.rectangle(frame, (input[3], input[4]), (input[3] + input[2], input[4] + input[1]), (0, 0, 255), 10)


    cv2.imshow('webcam', frame)
    if mask:
        cv2.imshow('mask', mask)


    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
