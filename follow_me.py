#!/usr/bin/env python
# TAG-DSP
# 3/1/2016

import numpy as np
import cv2
import libardrone
import time

drone = libardrone.ARDrone()
drone.trim()

detector = cv2.CascadeClassifier("./haar_cascades/haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
print "Successfully connected to camera!"


running = True
count = 0

action_array = [0 for i in range(0,10)]
try:
	drone.takeoff()
	time.sleep(6)

	# drone.hover()
	print "Ready..."
	


	while running:
		drone.move_left()

		running, frame = cam.read()
		if running:

			# print frame.shape
			
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# detect faces

			rects = detector.detectMultiScale(gray,1.3, 5)

			# for (x,y,w,h) in rects:
			# 	# draws rectangles
			# 	cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

			# cv2.imshow('frame', frame)
			# cv2.waitKey(1)
					

					
			if(len(rects) == 0):
				continue

			print rects	
			(x,y,w,h) = rects[0]

			if(x < 240):
				action_array[count] = 1
			elif(x > 400): 
				action_array[count] = 2
			else:
				action_array[count] = 0


			


		
			count += 1

			if(count == 9):
				count = 0
				total_left = 0
				total_right = 0
				total_hover = 0
				for i in range(0, len(action_array)):
					if action_array[i] == 0:
						total_hover += 1
					elif action_array[i] == 1:
						total_left += 1
					elif action_array[i] == 2:
						total_right +=1

				action = [total_hover, total_left, total_right]
				action = action.index(max(action))
				if action == 0:
					print "hover"
					drone.hover()
				elif action == 1:
					print "left"
					drone.move_left()
				elif action == 2:
					print "right"
					drone.move_right()


			
		else:
			print "error"
			drone.land()
			break
		if count == 100000:
			break


		drone.move_right()




except KeyboardInterrupt:
	drone.land()

drone.halt()

