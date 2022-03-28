#include "StickerDetection.h"


std::tuple<bool, int, int, int, int> StickerDetection::stickerDetectionRealTime(cv::Mat imFromFile)
{
    found = 0;
    stickerColorMask = blurAndExtractSpecificColor(9, imFromFile, COLOR_BGR2HSV); // ATTENTION, the parameters here is BGR

    if (found == 0) {
        cv::Mat matImageGray;
        cvtColor(imFromFile, matImageGray, COLOR_BGR2GRAY);
        cv::Mat cannyMorphed = enhanceContrastApplyCannyConnectBrokenLines(matImageGray, true);

        if (!stickerColorMask.empty()) {
            found = detectEllipses(cannyMorphed, 1, imFromFile.cols, imFromFile.rows, stickerColorMask);
        }
    }

    if (found)
    {
        result = std::make_tuple(found, hitPointFast.x, hitPointFast.y, hitSizeFast, hitSizeFast);        
    }
    else {
        result = std::make_tuple(found, 0, 0, 0, 0);
    }

    return result;
}

std::tuple<bool, int, int, int, int> StickerDetection::stickerDetectionAccurateOneTime(cv::Mat imFromFile)
{
    found = 0;
    //cv::Mat matImage;
    //matImage = imFromFile;
    
    float imWidth = imFromFile.cols;
    float imHeight = imFromFile.rows;

    int blurKernelSize = 9;  //TODOG hyper-parameter
    cv::Mat stickerColorMask;
    stickerColorMask = blurAndExtractSpecificColor(blurKernelSize, imFromFile, COLOR_BGR2HSV); // 
 //   stickerColorMask = blurAndExtractSpecificColor(blurKernelSize, imFromFile, COLOR_RGB2HSV); // ATTENTION: cvMatFromUIIMage returns RGB

            /** Perform closing operation on mask image to get rid of the white sticker label text */
        // in the center of the stickers
    int morphSize = 5;
    cv::Mat elementMorph = getStructuringElement(cv::MORPH_RECT, cv::Size(2 * morphSize + 1, 2 * morphSize + 1), cv::Point(morphSize, morphSize));
    // Apply the specified morphology operation
    morphologyEx(stickerColorMask, stickerColorMask, cv::MORPH_CLOSE, elementMorph);

    /** Enhance contrast and perform Canny edge detection and close broken lines */
    // Convert color image to gray image
    cv::Mat matImageGray;
    cvtColor(imFromFile, matImageGray, COLOR_BGR2GRAY);
    cv::Mat cannyMorphed;
    cannyMorphed = enhanceContrastApplyCannyConnectBrokenLines(matImageGray, false);


    /** Find contours and iterate over sticker candidates */
    // Find contours in the Canny output with connected broken lines
    std::vector<std::vector<cv::Point> > contours;
    cv::findContours(cannyMorphed, contours, RETR_LIST, CHAIN_APPROX_NONE);

    // Iterate over the contours and find sticker candidates
    for (size_t i = 0; i < contours.size(); i++)
    {
        /** Filter out too small and too big contours */
        // Check for number of pixels making up the contour
        size_t count = contours[i].size();

        int periMin, periMax;
        if (imWidth == 1080)
        {
            periMin = 85;
            periMax = 1100;
        }
        else
        {
            periMin = 210;
            periMax = 1800;
        }

        cv::RotatedRect box = filterSizeShapeCircularity(contours[i] , count , periMin , periMax);
        if (box.size.height == 0 && box.size.width == 0)
            continue;

        // At this point we found a potential candidate
        // Retrieve center position and the longest side
        cv::Point2f point = box.center;
        float sizeSticker = MAX(box.size.width, box.size.height);

        if (checkOverlayOfMaskAndContour(matImageGray, contours[i] , stickerColorMask))
        {
            found = 1;
            hitPointHighRes.x = point.x;
            hitPointHighRes.y = point.y;
            hitSizeHighRes = sizeSticker;
        }
    }    
    if (found)
    {
        result = std::make_tuple(found, hitPointHighRes.x, hitPointHighRes.y, hitSizeHighRes, hitSizeHighRes);
    }
    else {
        result = std::make_tuple(found, 0, 0, 0, 0);
    }

    return result;
}

cv::Mat StickerDetection::blurAndExtractSpecificColor(int blurKernelSize, cv::Mat matImage, int converionType)
{
    /** Threshold image according to sticker color (sea foam green) */
    cv::GaussianBlur(matImage, matImage, cv::Size(blurKernelSize, blurKernelSize), 0);

    // Convert RGB image to HSV color format
    cv::Mat hsv;
    cv::cvtColor(matImage, hsv, converionType);


    // Set lower and upper HSV thresholds depending on sticker color
    // Note: In OpenCV for HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].
    // In GIMP for HSV, Hue range is [0,360], Saturation range is [0,100] and Value range is [0,100].
    cv::Scalar greenLower(H_MIN, S_MIN, V_MIN);
    cv::Scalar greenUpper(H_MAX, S_MAX, V_MAX);


    // Extract sticker color depending on the threshold above
    cv::Mat stickerColorMask;
    cv::inRange(hsv, greenLower, greenUpper, stickerColorMask);

    return stickerColorMask;

}

cv::Mat StickerDetection::enhanceContrastApplyCannyConnectBrokenLines(cv::Mat matImageGray, bool fast)
{
    // Under flash light the contrast between sticker outer border (white) and innner ring (sea foam green) vanishes.
// Contrast in the brighter sections of the color range e.g. white, gray needs enhancement to increase the contrast
// Code snippet belows weighs the gray scale color range following this function: 1/x^4
    cv::Mat contrastEnhanced = cv::Mat::zeros(matImageGray.size(), matImageGray.type());
    for (int y = 0; y < matImageGray.rows; y++)
    {
        for (int x = 0; x < matImageGray.cols; x++)
        {
            contrastEnhanced.at<unsigned char>(y, x) =
                cv::saturate_cast<uchar>((float)matImageGray.at<unsigned char>(y, x) / (1.0 / (((float)matImageGray.at<unsigned char>(y, x) / 255.0) * ((float)matImageGray.at<unsigned char>(y, x) / 255.0) * ((float)matImageGray.at<unsigned char>(y, x) / 255.0) * ((float)matImageGray.at<unsigned char>(y, x) / 255.0))));
        }
    }

    // Perform Canny edege detection on the gray scale enhanced image
    cv::Mat cannyOutput;
    int thresh = 25; // TODO hyper parameter
    cv::Canny(contrastEnhanced, cannyOutput, thresh, thresh * 3, 3, true);

    // Connect broken lines using Closing (morphological operation)
    int morph_size;
    if (fast)
        morph_size = 1;
    else
        morph_size = 3;

    cv::Mat element = getStructuringElement(cv::MORPH_RECT, cv::Size(2 * morph_size + 1, 2 * morph_size + 1), cv::Point(morph_size, morph_size));

    // Apply the specified morphology operation
    cv::Mat cannyMorph = cv::Mat::zeros(matImageGray.size(), matImageGray.type());
    morphologyEx(cannyOutput, cannyMorph, cv::MORPH_CLOSE, element);

    return cannyMorph;
}

cv::RotatedRect StickerDetection::filterSizeShapeCircularity(std::vector<cv::Point> contour, int count, int periMin, int periMax)
{
    cv::RotatedRect failed;
    failed.size.height = 0;
    failed.size.width = 0;
    // Filter out too small or too big contours
    if (count < periMin || count > periMax)// Info ca. 560 pixel diameter at 5 cm => 560 * pi = 1759  (marker size 1 cm) || ca. 66 pixel diameter at 62 cm => 66 * pi = 207
    {
        return failed;
    }


    /** Filter out images taken from a very sharp angle i.e. sticker appears as a flattened ellipse */
    // Fit ellipse to the contour and ignore contours with ratio > 1.5
    cv::Mat pointsf;
    cv::Mat(contour).convertTo(pointsf, CV_32F);
    cv::RotatedRect box = fitEllipse(pointsf);

    if (MAX(box.size.width, box.size.height) > (MIN(box.size.width, box.size.height) * 1.5))
    {
        return failed;
    }

    /** Filter out non elliptic contours */
    // Ideally fitted ellipse and perimeter of the contour are the same to a certain extend, if not ignore.
    // Calculate perimeter of fitted ellipse and actual perimeter of contour and ignore ratios below and above a certaion threshold
    // Pperimeter of ellipse
    double a = MAX(box.size.width, box.size.height) / 2;
    double b = MIN(box.size.width, box.size.height) / 2;
    double p = M_PI * (3 * (a + b) - sqrt((3 * a + b) * (a + 3 * b)));

    double ratio = p / (double)count;

    if (ratio > 1.2 || ratio < 0.8)
    {

        return failed;
    }
    
    return box;
    
}

bool StickerDetection::checkOverlayOfMaskAndContour(cv::Mat matImageGray, std::vector<cv::Point> contour, cv::Mat stickerColorMask)
{
    /** Check if contour is filled with sticker color, reject otherwise */
// Overlay contour with sticker color mask to check size of overlap
// If ~100 % overlap than the sticker is found, not otherwise

// Fill current contour
    cv::Mat currentContourFilled(matImageGray.rows, matImageGray.cols, CV_8U, cv::Scalar(0));
    fillConvexPoly(currentContourFilled, contour, 1);

    // Copy only the values within the filled contour overlaid onto the color mask
    cv::Mat overlapFilledContourAndColorMask = cv::Mat(matImageGray.size(), CV_8UC1, double(0));
    stickerColorMask.copyTo(overlapFilledContourAndColorMask, currentContourFilled);

    // Calculate ratio between area of filled contour and contour overlaid onto mask
    float area = contourArea(contour);
    float sumMask = cv::sum(overlapFilledContourAndColorMask)[0] / 255;
    float overlapRatio = 0;
    if (area != 0 && sumMask != 0)
        overlapRatio = area / sumMask;
    return (overlapRatio > 0.9 && overlapRatio < 1.2);
}



int StickerDetection::detectEllipses(cv::Mat im, double resizeFactor, double imWidth, double imHeight, cv::Mat mask)
{
    int found = 0;
    std::vector<std::vector<cv::Point> > contours;
    cv::findContours(im, contours, RETR_LIST, CHAIN_APPROX_NONE);

    for (size_t i = 0; i < contours.size(); i++)
    {
        // check for number of pixels making up the contour
        // we are not interested in small contours
        size_t count = contours[i].size();
        int periMin = 50;
        int periMax = 800;
        cv::RotatedRect box = filterSizeShapeCircularity(contours[i], count, periMin, periMax);
        if (box.size.height == 0 && box.size.width == 0)
        {
            continue;
        }
        
        cv::Point2f point = box.center;
        float size = MAX(box.size.width, box.size.height);

            if (checkOverlayOfMaskAndContour(im, contours[i], mask))
            {
                found = 1;

                hitPointFast.x = round(point.x * resizeFactor);
                hitPointFast.y = round(point.y * resizeFactor);
                size *= resizeFactor;
                hitSizeFast = size;
            }
    }            
    return found;
}

