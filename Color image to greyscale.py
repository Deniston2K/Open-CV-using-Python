import cv2
import numpy as np
import matplotlib.pyplot as plt

data=cv2.imread(r"E:\KCT\Semester 5\RAC\RAC 2020\RAC Dec\Lectures\OpenCV Javid Hussain\Lecture 1\Open CV Images\kick.jpg")
grey=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
cv2.imshow('image',grey)
cv2.waitKey(0)
cv2.destroyAllWindows()