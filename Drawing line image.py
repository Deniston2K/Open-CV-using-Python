import cv2
import numpy as np
import matplotlib.pyplot as plt

data=cv2.imread(r"E:\KCT\Semester 5\RAC\RAC 2020\RAC Dec\Lectures\OpenCV Javid Hussain\Lecture 1\Open CV Images\kick.jpg")

start_point=(0,0)
end_point=(250,250)
color=(255,255,0)
thickness=3
image=cv2.line(data,start_point,end_point,color,thickness)
cv2.imshow('image',data)
cv2.waitKey(0)
cv2.destroyAllWindows()