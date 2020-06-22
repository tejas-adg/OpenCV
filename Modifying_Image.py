import cv2
import numpy as np
from Modified_Functions import Get_Image, Show_image

img = Get_Image()

# If we try to view the image as is, in most cases, we shall see that our monitor is not big enough 
# So, let us focus on a part of the image this is called region-of-interest (ROI)
roi = img[100 : 500, 200 : 700]

# Show the image
#Show_image("ROI", roi)

# Resizing the image
# The resize() function takes two parameters: the image and the new dimenstions
resized_img = cv2.resize(img, (800, 800))

# Show the image
#Show_image("Resized Image", resized_img)

# We see the image was disoriented, now we shall fix it by using the ratio
h, w, _ = img.shape
resized_img_ratio = cv2.resize(img, (800, int(h * (800 / w))))
#Show_image("Resized with ratio", resized_img_ratio)

# Above, we calculated the ratio of the width (800 / w) to the resized height (800) and multiplied it

# Now we shall see how to rotate the image
# First, we have to calculate the center of the image
center = (w // 2, h // 2)

# Generating the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
print(rotation_matrix)
print(type(rotation_matrix))

# Performing the affine transformation
rotated_image = cv2.warpAffine(img, rotation_matrix, (w, h))
Show_image("Rotated Image", rotated_image)