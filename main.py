# ---------------------------------------------------------------------------
# This program detects ekare's stickers in a given input file from Resources
# and writes to a file inside the Output folder using the detector_method
#
# (C) 2022 Ahmet Uyar, Derin Berktay, Özgür Güler, VA, United States
#  email: auyar19@ku.edu.tr, bberktay19@ku.edu.tr, oguler@ekareinc.com
#
# ---------------------------------------------------------------------------
from detector import *
import glob

def main():
    files = glob.glob('Resources/*.jpeg',
                       recursive = True)
    for file in files: # from IMG_0049 to IMG_102
        detector_method(file)

if __name__ == '__main__':
    main()
