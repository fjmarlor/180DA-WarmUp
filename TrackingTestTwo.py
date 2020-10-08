# This text uses a mixture of the Save Video Tutorial at https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html and the tutorial for object tracking at https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces 
# Expansions include saving multiple streams of different data in the form of multiple different files that can be watched separately, the merging of the two files, and finding the HSV values for red instead of using Blue like the example.

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

# Define the code and create VideoWriter object
size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('TrackingTestFrame.avi',fourcc, 20.0, size)
out2 = cv2.VideoWriter('TrackingTestMask.avi',fourcc, 20.0, size)
out3 = cv2.VideoWriter('TrackingTestRes.avi',fourcc, 20.0, size)

while(cap.isOpened()):
	ret, frame = cap.read()
	
	if ret==True:
		
		# Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		# define range of red color in HSV
		low_red = np.array([161, 155, 84])
		high_red = np.array([179, 255, 255])
		
		# Threshold the HSV image to get only red colors
		mask = cv2.inRange(hsv, low_red, high_red)
		
		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(frame, frame, mask = mask)
		
		# write the flipped frame
		out1.write(frame)
		out2.write(mask)
		out3.write(res)
		
		cv2.imshow('frame',frame)
		cv2.imshow('mask', mask)
		cv2.imshow('res', res)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

# Release everything if job is finished
cap.release()
out1.release()
out2.release()
out3.release()
cv2.destroyAllWindows()
