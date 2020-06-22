import cv2
from Modified_Functions import Get_Image, Show_image, Get_Resized_Image

img = Get_Image()

half_img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
Show_image("Half", half_img)

img = Get_Resized_Image()
interopolated_img = cv2.resize(img, (900, 900), interpolation = cv2.INTER_NEAREST)
Show_image("Interpolation", interopolated_img)