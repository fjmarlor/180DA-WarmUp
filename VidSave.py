# Using https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html as a tutorial

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

# Define the code and create VideoWriter object
size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ATest.avi',fourcc, 20.0, size)

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:
		# write the frame
		out.write(frame)

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	else:
		break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
