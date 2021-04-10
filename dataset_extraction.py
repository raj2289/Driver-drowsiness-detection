
import numpy as np
import os
import cv2
dirFace = 'cropped_eye'
face_cascade = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haar cascade files\haarcascade_eye.xml')
##eye_cascade = cv2.CascadeClassifier(' haar cascade files/haarcascade_righteye_2splits.xml')
# Create if there is no cropped face directory
if not os.path.exists(dirFace):
    os.mkdir(dirFace)
    print("Directory " , dirFace ,  " Created ")
else:    
    print("Directory " , dirFace ,  " has found.")
cap = cv2.VideoCapture('video from image cropped')
while True:
     ret, img = cap.read()
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     count=1
     for (x,y,w,h) in faces:
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = img[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for (ex,ey,ew,eh) in eyes:
             crop_img = roi_color[ey: ey + eh, ex: ex + ew]
             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
             s="{0}.jpg"
             s1='C:/Users/LENOVO/Desktop/MachineLearning/Drowsiness detection/Webcam/'+s.format(count)   ##cropped images is saved here
             count=count+1
             FaceFileName = "cropped_eye/eye_" + str(y+x) + ".jpg"
             cv2.imwrite( FaceFileName,crop_img)
     cv2.imshow('img',img)
     k = cv2.waitKey(30) & 0xff
     if k==27:
         break

cap.release()
cv2.destroyAllWindows()