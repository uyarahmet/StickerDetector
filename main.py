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
from detector import *
import glob
files = glob.glob('Resources/*.jpeg',
                   recursive = True)
for file in files:
    unchanged_img = cv2.imread(file, cv2.IMREAD_COLOR)
    width = 1000
    height = (width * unchanged_img.shape[0])/unchanged_img.shape[1] # (w2 * h1 / w1) = h2
    dsize = (width, int(height))
    img = cv2.resize(unchanged_img, dsize)
    final = detectormethod(img)
    if(final[0] == 1):
        new_img = img
        cv2.circle(new_img, (int(final[3] + final[1]/2), int(final[4] + final[1]/2)), int(final[1]/2), (0, 255, 0), 10)
        cv2.circle(new_img, (int(final[3] + final[1]/2), int(final[4] + final[1]/2)), 1, (0, 0, 255), 30)
        cv2.rectangle(new_img, (final[3],final[4]), (final[3] + final[2], final[4] + final[1]), (0, 0, 255),10)
        path = 'Output/'
        cv2.imwrite(os.path.join(path, str(file[10:23])), new_img)
