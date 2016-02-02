#!/usr/bin/env python
# Mohammad Saad
# 2/2/2016
# get_video_feed.py
# A way to get the image feed 
# from the Parrot ARDrone
# using Venthur's libardrone
# originally by github.com/richardpenman

import numpy as np
import cv2

# connect to camera
cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
running = True

# display video feed
while running:
	running, frame = cam.read()
	if running:
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) && 0xFF == 27:
			running = False
	else:
		print 'error in getting video feed'

cam.release()
cv2.destoryAllWindows()