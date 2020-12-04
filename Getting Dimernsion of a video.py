# the dimension of the video is calculated by considering 1 frame(Image) of a video and cheching its dimensions
import cv2

vid = cv2.VideoCapture('test.mp4')  # 0=camera

if vid.isOpened():
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH) #or width = vid.get(3)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)#or height = vid.get(4)
    fps = vid.get(cv2.CAP_PROP_FPS)#or fps = vid.get(5)
    print(width,height,fps)



