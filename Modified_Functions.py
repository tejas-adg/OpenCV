import cv2
import numpy as np

def Get_Image():
    return cv2.imread("road.jpg")

def Read_Image(path):
    return cv2.imread(path)

def Show_image(name, img_array):
    cv2.imshow(name, img_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()