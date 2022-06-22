import cv2
import sys
import numpy

PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict(maxCorners=300, qualityLevel=0.3, minDistance=7, blockSize=7)

s = 0
if(len(sys.argv)>1):
    s = sys.argv[1]
    
image_filter = PREVIEW
alive = True

win_name = 'Camera Filters'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)  
result = None

src = cv2.VideoCapture(s)

while alive: 
    has_frame, frame = src.read()
    if not has_frame:
        break
    
    frame = cv2.flip(frame, 1)
    
    if(image_filter == PREVIEW):
        result = frame
    elif(image_filter == BLUR):
        result = cv2.blur(frame, (13,13))
    elif(image_filter == CANNY):
        result = cv2.Canny(frame, 145, 150)
    elif(image_filter == FEATURES):
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, mask=None, **feature_params)
        if(corners is not None):
            for x, y in numpy.float32(corners).reshape(-1, 2):
                cv2.circle(result, (x,y), 10, (0,255,0), 1)
        
    cv2.imshow(win_name, result)
    
    key = cv2.waitKey(1)
    if(key == ord('q') or key == ord('Q') or key == 27):
        alive = False
    elif(key == ord('b') or key == ord('B')):
        image_filter = BLUR
    elif(key == ord('c') or key == ord('C')):
        image_filter = CANNY
    elif(key == ord('f') or key == ord('F')):
        image_filter = FEATURES
    elif(key == ord('p') or key == ord('P')):
        image_filter = PREVIEW

src.release()
cv2.destroyWindow(win_name)