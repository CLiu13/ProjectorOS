from transfunction import transfunction
from PIL import Image
import sys

img=Image.open(sys.argv[1])
newimg=transfunction.project(img, 0.5)
newimg.save(sys.argv[2])
