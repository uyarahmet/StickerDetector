import numpy as np
import cv2
from detector import detectormethod

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    input = detectormethod(frame)
    mask = input[5]
    #frame = cv2.resize(frame, (1000, 750))
    cv2.imshow('mask', mask)
    if (input[0] == 1):
        print("Detected!")
        cv2.circle(frame, (int(input[3] + input[1] / 2), int(input[4] + input[1] / 2)), int(input[1] / 2),
                   (0, 255, 0), 10)
        cv2.circle(frame, (int(input[3] + input[1] / 2), int(input[4] + input[1] / 2)), 1, (0, 0, 255), 30)
        cv2.rectangle(frame, (input[3], input[4]), (input[3] + input[2], input[4] + input[1]), (0, 0, 255), 10)

    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
