import os, sys, cv2
sys.path.append(os.getcwd()[:os.getcwd().find(os.path.basename(os.getcwd())) - 1])
from Modified_Functions import Show_image, Get_Image_Dir

# In here, we will erode an image away
