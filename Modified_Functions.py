import cv2

def Get_Image():
    return cv2.imread("road.jpg")

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