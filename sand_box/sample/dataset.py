import cv2
import numpy as np

cam = cv2.VideoCapture(0);
faceDetect = cv2.CascadeClassifier(r'D:\Embedded\MicroController\Raspberry\Projects\SecurityCamera_telegram\haarcascade_frontalface_default.xml');

Id = input('enter user id');
sampleNum = 0;
while True:
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        #incrementing sample number
        sampleNum = sampleNum+1;
        #saving the captured face in the dataset folder
        cv2.imwrite('dataSet/User.'+str(Id)+'.'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w]);
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2);
        #cv2.waitKey(100)
        #break
        cv2.imshow('Face',img);
        cv2.waitKey(1);
        # break if the sample number is morethan 20
    if sampleNum > 200:
        break;
cam.release();
cv2.destroyAllWindows();
