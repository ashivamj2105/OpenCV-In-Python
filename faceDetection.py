import cv2 
import sys

s = 0
if(len(sys.argv)>1):
    s = sys.argv[1]

src = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

net = cv2.dnn.readNetFromCaffe