# ---------------------------------------------------------------------------
# This program detects ekare's stickers in a given input file from Resources
# and writes to a file inside the Output folder using the detector_method
#
# (C) 2022 Ahmet Uyar, Derin Berktay, Özgür Güler, VA, United States
#  email: auyar19@ku.edu.tr, bberktay19@ku.edu.tr, oguler@ekareinc.com
#
# ---------------------------------------------------------------------------
import cv2
import numpy as np
import os
import glob
def detectormethod(unchanged_img):
    '''
    :param img: file that was cv2.imreaded
    :return: void, writes on images
    the detector function takes a file as an input, then detects ekare's sticker and then returns its the coordinates of the
    top left corner of the square that encapsulates the circle, its width and height, and a binary value indicating whether
    or not any circle has been detected in the first place.
    '''

    width = 1000
    height = (width * unchanged_img.shape[0]) / unchanged_img.shape[1]  # (w2 * h1 / w1) = h2
    dsize = (width, int(height))
    img = cv2.resize(unchanged_img, dsize)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    min_distance_between_circles = 300
    param1 = 50
    param2 = 30
    minimum_radius = 1
    maximum_radius = 450

    lower = np.array([85, 128, 102])
    upper = np.array([179, 255, 255])
    mask = cv2.inRange(imgHSV, lower, upper)
    detected_circles = cv2.HoughCircles(mask,
                                        cv2.HOUGH_GRADIENT, 1, min_distance_between_circles, param1=param1, param2=param2, minRadius=minimum_radius,
                                        maxRadius=maximum_radius)
    # Logic for detected_circles:
    # Parameter 1: the image that will be scanned.
    # Parameter 2: defines the method that will be used to detect the circles on the image. Currently,
    # the only implementable method is cv2.HOUGH_GRADIENT.
    # Parameter 3: the inverse ratio of the accumulator resolution to the image resolution.
    # Parameter 4: The minimum distance in between the centers of the detected circles.
    # Parameter 5: Gradient value used to handle the edge detection.
    # Parameter 6:Accumulator threshold value for the cv2.HOUGH_GRADIENT method. The smaller the threshold is, the more
    # circles will be detected (including false circles). The larger the threshold is, the more circles will potentially
    # be returned.
    # Parameter 7: The program will scan for circles with a minimum radius of parameter 7.
    # Parameter 8: The program will scan for circles with a maximum radius of parameter 8.
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:  # X,Y coordinates of the center with radius
            a, b, r = pt[0], pt[1], pt[2]
            print(f'X = {a}, Y = {b}, Radius = {r}')  # assign x, y, r
        found = 1
        height = r*2
        width = r*2
        positionx = a - r
        positiony = b - r
        path = 'Output/'
        final = [found, height, width, positionx, positiony, img, mask] # final[5] = image, final[6] = mask // for debug
        return final
    else :
        path = 'Output/'
        final = [0, 0, 0, 0, 0, mask]
        return final
