import cv2
import numpy as np

vid=cv2.VideoCapture(r"E:\KCT\Semester 5\RAC\RAC 2020\RAC Dec\Lectures\OpenCV Javid Hussain\Lecture 1\Open CV Videos\test.mp4")
# print(data)
while(True):
    boolean,frame=vid.read()
    if boolean== True:
        cv2.imshow('video',frame)
    if(cv2.waitKey(30) & 0xFF==ord('q')):
        break
vid.release()
cv2.destroyAllWindows()