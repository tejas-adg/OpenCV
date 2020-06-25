import os
import cv2

def Get_Image_Dir():
    return "E:\\Computer_Programs\\Python_Programs\\OpenCV\\Images"

def Get_Dir():
    return os.path.dirname(os.path.abspath(__file__))

def Get_Image():
    return cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Images", "road.jpg"))

def Get_Resized_Image():
    image = Get_Image()
    h, w, _ = image.shape
    return cv2.resize(image, (800, int(h * (800 / w))))

def Read_Image(path):
    return cv2.imread(path)

def Show_image(name, img_array):
    cv2.imshow(name, img_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rgb_to_cmyk(rgb_lis):
    RGB_SCALE = 255
    CMYK_SCALE = 100
    cmyk_lis = []

    for color in rgb_lis:
        cmyk_lis.append(1 - color / float(RGB_SCALE))

    min_cmy = min(cmyk_lis)
    for i in range(len(cmyk_lis)):
        cmyk_lis[i] = (cmyk_lis[i] - min_cmy)
    cmyk_lis.append(min_cmy)

    for i in range(len(cmyk_lis)):
        cmyk_lis[i] *= 100

    return cmyk_lis

def cmyk_to_rgb(cmyk_lis):
    rgb_lis = []
    for i in range(len(cmyk_lis) - 1):
         rgb_lis.append(255 * (1.0 - (cmyk_lis[i] + cmyk_lis[-1]) / 100.0))
    return rgb_lis


