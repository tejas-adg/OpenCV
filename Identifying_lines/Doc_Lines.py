import numpy as np
import cv2

counter1 = 1
counter2 = 1
while True:
    img = cv2.imread("E:\\My_Pictures\\Saved Pictures\\Captures\\Capture.jpg", 0)
    print(f"Counter 1 = {counter1}")
    print(f"Counter 2 = {counter2}")
    cv2.imshow("CannyDoc", cv2.Canny(img, counter1, counter2))
    ch = cv2.waitKey(0)
    if ch == ord('q'):
        break
    elif ch == ord('f'):
        counter1 += 1
    elif ch == ord('g'):
        counter2 += 1
    elif ch == ord('r'):
        counter1 -= 1
    elif ch == ord('t'):
        counter2 -= 1
    
cv2.destroyAllWindows()
