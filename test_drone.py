#!/usr/bin/env python

# Mohammad Saad
# test_drone.py

import libardrone
import time

drone = libardrone.ARDrone()
drone.reset_to_true()

try:
	for i in range(0,100):
		print drone.image
		time.sleep(1)
	# drone.takeoff()
	# print "takeoff"
	# time.sleep(1)

	# drone.hover()
	# print "hovering"
	# time.sleep(5)
	
	# print "setting speed: 0.1"

	# print "moving left"
	# drone.move_left()
	# time.sleep(1)
	
	# print "moving right"
	# drone.move_right()
	# time.sleep(1)

	# print "move forward"
	# drone.move_forward()
	# time.sleep(1)

	# print "move backward"
	# drone.move_backward()
	# time.sleep(1)

	
	# drone.land()
	# print "land"
except KeyboardInterrupt:
	drone.land()
	print "CTRL+C, halting"
	drone.halt()


drone.halt()
