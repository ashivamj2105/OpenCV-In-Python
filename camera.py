import cv2
import sys

s = 0
if (len(sys.argv) > 1):
    s = sys.argv[1]
    
src = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:
    ret, frame = src.read()
    if not ret:
        break
    cv2.imshow(win_name, frame)
    
src.release()
cv2.destroyWindow(win_name)