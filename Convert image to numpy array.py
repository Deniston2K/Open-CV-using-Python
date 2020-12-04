import cv2
import numpy as np
import matplotlib.pyplot as plt

data=cv2.imread(r"E:\KCT\Semester 5\RAC\RAC 2020\RAC Dec\Lectures\OpenCV Javid Hussain\Lecture 1\Open CV Images\kick.jpg")
data=data/255
hello=np.array(data)

print(hello)
