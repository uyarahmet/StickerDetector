import cv2
import numpy as np

print("Package Imported")


''' CHAPTER #1 TAKEAWAY DEMOS

img = cv2.imread('Resources/gogh.jpeg')

cv2.imshow("Output", img)
cv2.waitKey(0)

*************CHAPTER 1 END****************
''''

''' CHAPTER #2 BASIC FUNCTIONS

img = cv2.imread('Resources/gogh.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # opens in different color and imgGray is a new image..
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)
 
************EXAMPLE 1 - Blurring *******************

img = cv2.imread('Resources/gogh.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # opens in different color and imgGray is a new image..
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) # could've been 3-3, 5-5
imgCanny = cv2.Canny(img, 100, 100) # makes the img canny
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0) # 0 delay means infinite

************EXAMPLE 2 - Dialation *******************

kernel = np.ones((5,5), np.uint8)
img = cv2.imread('Resources/gogh.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # opens in different color and imgGray is a new image..
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) # could've been 3-3, 5-5
imgCanny = cv2.Canny(img, 100, 100) # makes the img canny
imgDialation = cv2.dilate(imgCanny, kernel) # read the docs
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialated Image", imgDialation) # Please read this from the docs
cv2.waitKey(0) # 0 delay means infinite

************EXAMPLE 3 - Erosion ********************

kernel = np.ones((5,5), np.uint8)
img = cv2.imread('Resources/gogh.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # opens in different color and imgGray is a new image..
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) # could've been 3-3, 5-5
imgCanny = cv2.Canny(img, 100, 100) # makes the img canny
imgDialation = cv2.dilate(imgCanny, kernel) # read the docs
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialated Image", imgDialation) # Please read this from the docs
cv2.imshow("Eroded Image", imgEroded) # Please read this from the docs
cv2.waitKey(0) # 0 delay means infinite

CHAPTER 2 KEY QUESTIONS : WHAT IS KERNEL IN OPENCV

CHAPTER 2 END ***************************************
'''



'''CHAPTER #3 START **********************************




CHAPTER #3 END ***************************
'''









