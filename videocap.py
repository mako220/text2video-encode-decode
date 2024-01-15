import cv2
import numpy as np


cap = cv2.VideoCapture('output.avi')
cv2.namedWindow("Frame")

while(cap.isOpened()):
    _, frame = cap.read()

    img = cv2.resize(frame , (1920//2,1080//2))
    cv2.imshow("Frame", img)
    key = cv2.waitKey(0)
#    if key == 27:
#         break

cap.release()
cv2.destroyAllWindows()
