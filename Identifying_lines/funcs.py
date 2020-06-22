import numpy as np
import cv2

def imageNegative(img):
    for i in img:
        for j in i:
            j[0] = abs(255 - j[0])
            j[1] = abs(255 - j[1])
            j[2] = abs(255 - j[2])

def bgrSplitNSave(img, path, name):
    cv2.imwrite(path + name + "_b.jpg", img[:, :, 0])
    cv2.imwrite(path + name + "_g.jpg", img[:, :, 1])
    cv2.imwrite(path + name + "_r.jpg", img[:, :, 2])

def img_bgrDifferences(img):
    height, width, depth = img.shape
    print(f"Height = {height}\nWidth = {width}\nDepth = {depth}")
    img_diff = np.empty([int(height / 2), int(width / 2), depth], 'uint8')
    for i in range(0, int(height / 2)):
        for j in range(0, int(width / 2)):
            img_diff[i, j, 0] = abs(img[i*2, j*2, 0] - img[i*2+1, j*2+1, 0])
            img_diff[i, j, 1] = abs(img[i*2, j*2, 1] - img[i*2+1, j*2+1, 1])
            img_diff[i, j, 2] = abs(img[i*2, j*2, 2] - img[i*2+1, j*2+1, 2])
    return img_diff

image = cv2.imread("E:\\My_Pictures\\Saved Pictures\\Captures\\Chicago\\Chicago_Pic.jpg")
image_diff = img_bgrDifferences(image)
cv2.imwrite("C:\\Users\\hp\\Desktop\\Chicago_Differences.jpg", image_diff)

#bgrSplitNSave(img_bgrDifferences(image), "C:\\Users\\hp\\Desktop\\", "Chicago_Highlights")
