import numpy as np
import cv2
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

ret1,frame1 = cap1.read()
ret2,frame2 = cap2.read()

##cv2.imshow('frame1',frame1)
##cv2.imshow('frame2',frame2)
##
##cv2.imwrite('imgR.png', frame1)
##cv2.imwrite('imgL.png', frame2)

while(True):
	ret1,frame1 = cap1.read()
	ret2,frame2 = cap2.read()
	
	cv2.imshow('frame1',frame1)
	cv2.imshow('frame2',frame2)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
                                                                                                                                                                                                                                                                                                                                                                                                                              
