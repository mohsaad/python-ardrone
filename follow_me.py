#!/usr/bin/env python
# TAG-DSP
# 3/1/2016

import numpy as np
import cv2
import libardrone
import time

drone = libardrone.ARDrone()
drone.trim()

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
print "Successfully connected to camera!"
running = True
count = 0

time.sleep(5)
try:
	drone.takeoff()
	time.sleep(6)

	drone.hover()

	while running:
		running, frame = cam.read()
		if running:
			print "Got frame!"
			count += 1
		else:
			print "error"
			drone.land()
			break
		if count == 10000:
			break



except KeyboardInterrupt:
	drone.land()

drone.halt()

