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
    final = detectormethod(file)
    if(final[0] == 1):
        img = cv2.imread(file, cv2.IMREAD_COLOR)
        cv2.circle(img, (int(final[3] + final[1]/2), int(final[4] + final[1]/2)), int(final[1]/2), (0, 255, 0), 10)
        cv2.circle(img, (int(final[3] + final[1]/2), int(final[4] + final[1]/2)), 1, (0, 0, 255), 30)
        cv2.rectangle(img, (final[3],final[4]), (final[3] + final[2], final[4] + final[1]), (0, 0, 255),10)
        path = 'Output/'
        cv2.imwrite(os.path.join(path, str(file[10:23])), img)
