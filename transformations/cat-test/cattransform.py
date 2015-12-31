import sys
from PIL import Image

img = Image.open(sys.argv[1])
width, height = img.size
print(width)
print(height)
img.show()

#img.transform((width, height), Image.PERSPECTIVE, (1,2,0,0,4,0,0,1/100), Image.BICUBIC).save(sys.argv[2])
