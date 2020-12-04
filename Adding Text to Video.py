import cv2
import numpy as np
import matplotlib.pyplot as plt
#locating the Video
vid=cv2.VideoCapture("test.mp4")

while(True):
    # Reading the video
    ret,frame=vid.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (100, 50)
    fontScale = 1
    color = (255, 255, 0)#color= (blue,green, red)
    thickness = 3
    video = cv2.putText(frame, "Deniston_A", org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(30) & 0xFF==ord('q')):
        break
vid.release()
cv2.destroyAllWindows()