# ---------------------------------------------------------------------------
# This program detects ekare's stickers in a given input file from Resources
# and writes to a file inside the Output folder using the detector_method
#
# (C) 2022 Ahmet Uyar, Derin Berktay, Özgür Güler, VA, United States
#  email: auyar19@ku.edu.tr, bberktay19@ku.edu.tr, oguler@ekareinc.com
#
# ---------------------------------------------------------------------------
from webcam_detection import *
// openCV-test.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include "StickerDetection.h"
#include <iostream>
#include <tuple>

using namespace cv;
using namespace std;

int main(int argc, char ** argv)
{
	Mat image;
	namedWindow("Display window");
	VideoCapture cap(0);

	if (!cap.isOpened())

	{

		cout << "cannot open camera";

	}
	StickerDetection skdect;
	std::tuple<bool, int, int, int, int> detection_result;
	while (true)
	{
		cap >> image;
		imshow("Display window", image);
		bool m_found = false;
		int m_px, m_py, m_width, m_height;

		if (image.empty())
		{
			cout << "could not open or find the image" << std::endl;
			return -1;
		}


		//if use real time detection algoirthm, call the function of stickerDetectionRealTime
		// detection_result = skdect.stickerDetectionRealTime(image);

		//if use accurate detection algoirthm, call the function of stickerDetectionAccurateOneTime
		detection_result = skdect.stickerDetectionAccurateOneTime(image);

		m_found = std::get<0>(detection_result);
		m_px = std::get<1>(detection_result);
		m_py = std::get<2>(detection_result);
		m_width = std::get<3>(detection_result);
		m_height = std::get<4>(detection_result);


		if (m_found)
		{
			int px = m_px - m_width / 2;
			int py = m_py - m_height / 2;
			int rectWidth = m_width;
			int rectHeight = m_height;

			Rect Rec(px, py, rectWidth, rectHeight);
			rectangle(image, Rec, Scalar(255), FILLED, 4);

			/*bool isSuccess = imwrite(outfolder + filename + "rect.jpg", image); //write the image to a file as JPEG 

			if (isSuccess == false)
			{
				cout << "Failed to save the stickerColorMask image " << endl;
			}*/

		}

		cout << "Is found? " << m_found << " "
			<< "x coordinate: " << m_px << " "
			<< "y coordinate: " << m_py << " "
			<< "rect width: " << m_width << " "
			<< "rect height: " << m_height << " " << endl;
		waitKey(25);
	}
}

