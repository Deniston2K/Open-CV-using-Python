import cv2
import numpy as np
import matplotlib.pyplot as plt

data=cv2.imread(r"E:\KCT\Semester 5\RAC\RAC 2020\RAC Dec\Lectures\OpenCV Javid Hussain\Lecture 1\Open CV Images\kick.jpg")
# https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
font=cv2.FONT_HERSHEY_SIMPLEX
org=(100,50)
fontScale=1
color=(255,255,0)
thickness=3
image=cv2.putText(data,"Deniston_A",org,font,fontScale,color,thickness,cv2.LINE_AA)
cv2.imshow('image',data)
cv2.waitKey(0)
cv2.destroyAllWindows()