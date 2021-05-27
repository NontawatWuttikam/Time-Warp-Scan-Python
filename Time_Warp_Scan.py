import cv2
import numpy as np
import sys
import argparse
parser = argparse.ArgumentParser('parser')
parser.add_argument('-cam',default=0)
parser.add_argument('-speed',default=1)

args = parser.parse_args()
cap = cv2.VideoCapture(int(args.cam))
speed = int(args.speed)
counter = 0
_, f = cap.read()
hist_frame = f[:, 0:counter+1]

while True:
    _, frame = cap.read()
    frame = frame[:,::-1,:]
    line = np.full((frame.shape[0], 3, 3), 1) * np.array([255,0,255])
    hist_frame = np.hstack((hist_frame, frame[:,counter:counter+speed]))
    counter = counter + speed
    frame_show = np.hstack((hist_frame, frame[:, counter:]))
    frame_show[:, counter:counter + 3] = line
    cv2.imshow('frame',frame_show)
    cv2.waitKey(1)
    if counter > frame.shape[1] - 3:
        counter = 0
        hist_frame = f[:, 0:counter+1]
        cv2.waitKey(0)