import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read(r'D:\Embedded\MicroController\Raspberry\Projects\SecurityCamera_telegram\recognizer\trainningData.yml')
Id=0
#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,3,1,0,2)

while True:
	ret,img=cam.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		Id, conf=rec.predict(gray[y:y+h,x:x+w])
		if(conf<50):
			if(Id==1):
				Id='Mathi'
				a=0
				b=255
				c=0
		else:
			Id='unknown'
			a=0
			b=0
			c=255
			
		font = cv2.FONT_HERSHEY_COMPLEX_SMALL
		
		cv2.putText(img, str(Id), (x,y+h), font, 2, (a, b, c), 2, cv2.LINE_AA)
	cv2.imshow('Face',img)
	if cv2.waitKey(10)==ord('q'):
		break
cam.release()
cv2.destroyAllWindows()
