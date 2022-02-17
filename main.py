from detector import *
import glob
files = glob.glob('Resources/*.jpeg',
                   recursive = True)
for file in files: # from IMG_0049 to IMG_102
    detectormethod(file)
