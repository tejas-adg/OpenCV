import cv2
import numpy as np
import os

# Reading the image using imread() function
img = cv2.imread("road.jpg")

# Printing the shape of the image
print(f"The shape of the image is given as (<height>, <width>, <depth>)\n{img.shape}\n")
print(f"The type is: {type(img.shape)}\n")
print(f"The depth shows how each pixel is stored, usually it is in BGR (Blue, Green, Red) format.\nSo Three layers to an image.\n")

# Selecting the Height, Width, Depth
h, w, r = img.shape
print(f"The Height, Width and Depth extracted\nHeight : {h}\nWidth : {w}\nDepth : {r}\n\n")

# Selecting a Pixel randomly
rand_pixel = img[100, 100]
print(f"A pixel at h = 100 and w = 100 : {rand_pixel}\n")
print(f"The type is: {type(rand_pixel)}\n")

# Extracting the Blue, Green and Red pixel values
b, g, r = rand_pixel
print(f"The individual colors extracted\nBlue = {b}\nGreen = {g}\nRed = {r}\n\n")

# Showing the image in a window
# "Image" is the name of the window's title bar
# img is the image read using the imread() function
cv2.imshow("Image", img)

# Waiting for a key press, otherwise it will close the window
# without us being able to see the image.
# The 0 passed means that the program has to wait indefinitely for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()