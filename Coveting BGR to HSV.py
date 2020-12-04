#HSV=Hue,Saturation and Lightness
import cv2
import numpy as np
import matplotlib.pyplot as plt
vid=cv2.VideoCapture("test.mp4")

while(True):
    # Reading the video
    ret,frame=vid.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',hsv)
    if(cv2.waitKey(30) & 0xFF==ord('q')):
        break
vid.release()
cv2.destroyAllWindows()