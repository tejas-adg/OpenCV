# This program can be used to study the effects of weights and gamma correction on images
# Use 'w' to increase the weight of first image and 's' to decrease
# Use 'e' to increase the weight of second image and 'd' to decrease
# Use 'r' to increase the gamma value and 'f' to decrease

import os, sys, cv2
sys.path.append(os.getcwd()[:os.getcwd().find(os.path.basename(os.getcwd())) - 1])
from Modified_Functions import Get_Image_Dir, Show_image

# Reading two images
scene_img = cv2.imread(os.path.join(Get_Image_Dir(), "Scenic.jpg"))
space_img = cv2.imread(os.path.join(Get_Image_Dir(), "Space.jpg"))

# To add, both the images shoud be of same shape
print(f"Image1.shape = {scene_img.shape}\nImage2.shape = {space_img.shape}")

# Basic adding
b_add = cv2.add(scene_img, space_img)
Show_image("Scene + Space", b_add)

# But, that is not always ideal, so we use the cv2.addWeighted() function
# The parameters are:
#   img1 : The first image
#   wt1 : The weight to be applied to the first image
#   img2 : The second image
#   wt2 : The weight to be applied to the second image
#   gammaValue : Measurement of light

wt1 = 0.5
wt2 = 0.4
g = 0.0
while True:
    cv2.imshow(f"Scene + Space", cv2.addWeighted(scene_img, wt1, space_img, wt2, g))
    print(f"wt1 = {wt1} and wt2 = {wt2} and gamme = {g}")
    ch = cv2.waitKey(0)
    if ch == ord('q'):
        break
    elif ch == ord('w'):
        wt1 += 0.01
    elif ch == ord('s'):
        wt1 -= 0.01
    elif ch == ord('e'):
        wt2 += 0.01
    elif ch == ord('d'):
        wt2 -= 0.01
    elif ch == ord('r'):
        g += 0.1
    elif ch == ord('f'):
        g -= 0.1
    else:
        print(f"Invalid ->{ch}<-")

cv2.destroyAllWindows()
