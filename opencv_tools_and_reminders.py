import cv2
import numpy as np

print("Package Imported")


''' CHAPTER #1 TAKEAWAY DEMOS

img = cv2.imread('Resources/gogh.jpeg')

cv2.imshow("Output", img)
cv2.waitKey(0)

*************CHAPTER 1 END****************
'''

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

img = cv2.imread('Resources/gogh.jpeg')
print(img.shape)
imgResize = cv2.resize(img, (1000,500)) # resize function: width, height
print(imgResize.shape)
imgCropped = img [0:200, 200:500] # height, width

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)

resizing and cropping was learned from this chapter

CHAPTER #3 END ***************************
'''

''' Chapter 4 Start

****************EXAMPLE 1*************

img = np.zeros((512,512,3), np.uint8)
print(img)
cv2.imshow("Image", img)
cv2.waitkey(0)

****************EXAMPLE 2*************

img = np.zeros((512,512,3), np.uint8)
img[:] = 255, 0, 0 # blue
cv2.imshow("Image", img) # full blue 
img[200:300, 100:300] = 255, 0, 0 # height, width

***********EXAMPLE 3 IMPORTANT! ******

cv2.line(img, (0,0), (300,300), (0, 255, 0), 3) # target, start, end, color, thickness
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3) # target, start, end, color, thickness

cv2.circle(img, (400,50), 30, (255, 255, 0), 5) # IMPORTANT!
cv2.text

Chapter 4 End
'''








