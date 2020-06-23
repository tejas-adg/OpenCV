import os, sys, cv2
sys.path.append(os.getcwd()[:os.getcwd().find(os.path.basename(os.getcwd())) - 1])
from Modified_Functions import Get_Image, Show_image, Get_Resized_Image

img = Get_Image()

# Another way to reduce an image is to use functions on the X-axis and Y-axis
# Here, the fx and fy fulfil the purpose and we are reducing them by 50% or 0.5
half_img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
Show_image("Half", half_img)

img = Get_Resized_Image()
interopolated_img = cv2.resize(img, (900, 900), interpolation = cv2.INTER_NEAREST)
Show_image("Interpolation", interopolated_img)
