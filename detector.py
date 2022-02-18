# ---------------------------------------------------------------------------
# This program detects ekare's stickers in a given input file from Resources
# and writes to a file inside the Output folder.
#
# (C) 2022 Ahmet Uyar, Derin Berktay, Özgür Güler, VA, United States
#  email: auyar19@ku.edu.tr, bberktay19@ku.edu.tr, oguler@ekareinc.com
#
# ---------------------------------------------------------------------------
import cv2
import numpy as np
import os
import glob
def detectormethod(file):
    img = cv2.imread(file, cv2.IMREAD_COLOR)

    def empty(a):
        pass

    cv2.namedWindow("TrackBars")
    cv2.createTrackbar("Hue Min", "TrackBars", 85, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 128, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 102, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    # cv2.imshow("Origin " + str(i), mask)
    cv2.waitKey(1)

    detected_circles = cv2.HoughCircles(mask,
                                        cv2.HOUGH_GRADIENT, 1, 300, param1=50, param2=30, minRadius=1,
                                        maxRadius=400)  # Existing logic
    # Draw circles that are detected.
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:  # X,Y coordinates of the center with radius
            a, b, r = pt[0], pt[1], pt[2]
            print(f'X = {a}, Y = {b}, Radius = {r}')  # assign x, y, r
            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 10)
            # Draw a small circle (of radius 1) to show the center (needed for later).
            cv2.circle(img, (a, b), 1, (0, 0, 255), 30)
        # position = (10, 250)
        # cv2.rectangle(image, (x, x), (x + w, y + h), (0, 0, 0), -1)
        # cv2.putText(img, str(r*2), position, cv2.FONT_HERSHEY_COMPLEX_SMALL, 20, (0, 0, 255), 1)
        #x, y, w, h = 0, 0, 500, 250
        # Draw black background rectangle
        #cv2.rectangle(img, (x, x), (x + w, y + h), (0, 0, 0), -1)
        #cv2.putText(img, str(r * 2), (x + int(w / 10), 200), cv2.FONT_HERSHEY_SIMPLEX, 5,
        #            (255, 255, 255), 10)
        found = 1
        height = r*2
        width = r*2
        positionx = a - r
        positiony = b - r
        path = 'Output/'
        final = [found, height, width, positionx, positiony]
        file = open(os.path.join(path, str(file[10:18])+".txt"),"w")
        file.write(str(final))
        file.close()
    else :
        path = 'Output/'
        final = [0, 0, 0, 0, 0]
        file = open(os.path.join(path, str(file[10:18])+".txt"), "w")
        file.write(str(final))
        file.close()
