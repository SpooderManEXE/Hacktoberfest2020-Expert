import sys


# sys needed to import pacakges like cv2 from site-package in lib folder
from cv2 import cv2 #pip install opencv-python
import numpy as np

#Read a Video Stream and Display It

#Camera Object
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


# user_name = input("enter your name")


while True:
	ret,frame = cam.read()
	if ret==False:
		print("Something Went Wrong!")
		continue

	key_pressed = cv2.waitKey(1)&0xFF #Bitmasking to get last 8 bits
	if key_pressed==ord('q'): #ord-->ASCII Value(8 bit)
		break

	faces = face_cascade.detectMultiScale(frame,1.3,5)
	#print(faces)
	if(len(faces)==0):
		cv2.imshow("Video",frame)
		continue
	for face in faces:
		x,y,w,h = face
		face_section = frame[y-10:y+h+10,x-10:x+w+10]
		# face_section = cv2.resize(face_section,(100,100))
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
		
		 

	sketch = cv2.Canny(face_section,100,150)
	
	cv2.imshow("Video",frame)
	cv2.imshow("Video Face",face_section)
	cv2.imshow("Video Sketch",sketch)
	



# cv2.imwrite("./sketch.png",sketch)
cam.release()
cv2.destroyAllWindows()	
