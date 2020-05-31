# import the necessary packages
from transform import four_point_transform
#from pyimagesearch.transform import four_point_transform
import numpy as np
import argparse
import cv2

### https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image file")
ap.add_argument("-c", "--coords", help="comma separated list of source points")
args = vars(ap.parse_args())

# load the image and grab the source coordinates (i.e. the list
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]), dtype="float32")

# apply the four point transform to obtain a "birds eye view" of the image
warped = four_point_transform(image, pts)

# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)

# for image "getperspective_transform_01.jpg":
# offsets from top-left (75, 255):  tl=(0, 0) tr=(300, -129) br=(426, 23) bl=(121, 213)
# run from command-line:
# python transform_example.py --image getperspective_transform_01.jpg --coords "[(75, 255), (375, 126), (501, 278), (196, 468)]"
