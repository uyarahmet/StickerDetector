import cv2
import numpy as np
import os

for i in range(49,103): # from IMG_0049 to IMG_102

    #img = cv2.imread('Resources/IMG_00' + str(i) +'.jpeg', cv2.IMREAD_COLOR) # Reading image

    if i >= 100:
        img = cv2.imread('Resources/IMG_0' + str(i) + '.jpeg', cv2.IMREAD_COLOR)  # Reading image
    else:
        img = cv2.imread('Resources/IMG_00' + str(i) + '.jpeg', cv2.IMREAD_COLOR)  # Reading image


    # Convert to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur using 3 * 3 kernel.

    gray_blurred = cv2.blur(gray, (3, 3))
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
                                        cv2.HOUGH_GRADIENT, 1, 20, minRadius=50, maxRadius=400) # Existing logic

    # Draw circles that are detected.
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]: # X,Y coordinates of the center with radius
            a, b, r = pt[0], pt[1], pt[2]
            print(f'X = {a}, Y = {b}, Radius = {r}') # assign x, y, r
            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 10)
            # Draw a small circle (of radius 1) to show the center (needed for later).
            cv2.circle(img, (a, b), 1, (0, 0, 255), 30)
        path = 'Output/'
        cv2.imwrite(os.path.join(path, 'img' + str(i) + '.jpeg'), img)
