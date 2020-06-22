import cv2
import numpy as np
from Modified_Functions import Get_Resized_Image, Show_image

img = Get_Resized_Image()
Show_image("Image before drawing", img)

# We will now be drawing basic shapes on images
# This is an inplace operation so be careful when implementing it
# The rectangle function takes many parameters, we are using five of them:
#   1. The image array
#   2. The rectangle's top-left coordinates
#   3. The rectangle's bottom-right coordinates
#   4. The color of the rectangle's line
#   5. The thickness of the rectangle's line 
cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 2)
Show_image("Image after drawing", img)

# Taking the shapes 
h, w, _ = img.shape
# The similar procedure to draw a circle
Show_image("Circle", cv2.circle(img, (w // 2, h // 2), 100, (0, 255, 0), 2))

# Putting text on images
# We shall use the putText method with the following parameters in the saem order
#   1. Image
#   2. The text
#   3. The bottom-left coordinates, from where the text should start
#   4. The Font from cv2
#   5. Font Size
#   6. Color of the text (in BGR format)
#   7. Line width
cv2.putText(img, "Hello World!", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
Show_image("Image after adding text", img)