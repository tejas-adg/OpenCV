import cv2
import numpy as np
import os

# Reading the image using imread() function
img = cv2.imread("road.jpg")

# Printing the shape of the image
print(f"The shape of the image is given as (<height>, <width>, <depth>)\n{img.shape}")
print(f"The type is: {type(img.shape)}")
print(f"The depth shows how each pixel is stored, usually it is in BGR (Blue, Green, Red) format.\nSo Three layers to an image.")

# Selecting the Height, Width, Depth
h, w, r = img.shape


# Selecting a Pixel randomly