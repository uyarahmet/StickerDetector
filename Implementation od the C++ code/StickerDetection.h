# ---------------------------------------------------------------------------
# This program detects ekare's stickers in a given input file from Resources
# and writes to a file inside the Output folder using the detector_method
#
# (C) 2022 Ahmet Uyar, Derin Berktay, Özgür Güler, VA, United States
#  email: auyar19@ku.edu.tr, bberktay19@ku.edu.tr, oguler@ekareinc.com
#
# ---------------------------------------------------------------------------
#pragma once
#define M_PI  3.14159
#define H_MIN	40
#define H_MAX	95
#define S_MIN	40
#define S_MAX	255
#define V_MIN	60
#define V_MAX	240

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <fstream>
#include <tuple> 


using namespace cv;
using namespace std;

// class for the sticker detection 
// with openCV library
/*
// Inputs and outputs
Input: image, 
Output: found (bool) height, width, position X, position W
1) std::tuple<bool, int, int, int, int> stickerDetectionRealTime(cv::Mat imFromFile);
2) std::tuple<bool, int, int, int, int> stickerDetectionAccurateOneTime(cv::Mat imFromFile);
return type:
std: tuple<bool, int, int, int, int>
in the return value, following parameters are included:
	bool found
	int coordinate_x
	int coordinate_y
	int rect_width
	int rect_height


*/


class StickerDetection
{	
	cv::Mat stickerColorMask;
public: 
	bool found = 0;
	String filename;
	cv::Point2f hitPointFast, hitPointHighRes;
	float hitSizeFast, hitSizeHighRes;
	std::tuple<bool, int, int, int, int> result; 
	
public: 
	std::tuple<bool, int, int, int, int> stickerDetectionRealTime(cv::Mat imFromFile);
	std::tuple<bool, int, int, int, int> stickerDetectionAccurateOneTime(cv::Mat imFromFile);
	cv::Mat blurAndExtractSpecificColor(int blurKernelSize, cv::Mat matImage, int converionType);
	cv::Mat enhanceContrastApplyCannyConnectBrokenLines(cv::Mat matImageGray, bool fast);
	int detectEllipses(cv::Mat im, double resizeFactor, double imWidth, double imHeight, cv::Mat mask);
	cv::RotatedRect filterSizeShapeCircularity(std::vector<cv::Point> contour, int count, int periMin, int periMax);
	bool checkOverlayOfMaskAndContour(cv::Mat matImageGray, std::vector<cv::Point> contour, cv::Mat stickerColorMask);
};

