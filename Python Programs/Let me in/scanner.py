import numpy as np
import cv2
import pickle
import time
from tkinter import *
from tkinter import messagebox  


cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}
    
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#name=input("Enter name")


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_grey = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_grey)
        if conf <100:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255,255) #BGR
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            #time.sleep(3)
            #messagebox.showinfo("Access granted", "Door is opening")
        else:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = "unknown"
            #name = labels[id_]
            color = (0,0,0) #BGR
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            messagebox.showinfo("Access Denied", "Access Denied")
        
        pic_name = "output//my-image"+ str(time.time()) +".png"
        img_item = pic_name
        cv2.imwrite(img_item, frame)

        color = (0,255,0) #BGR
        stroke = 2
        end_x = x + w
        end_y = y + h
        cv2.rectangle(frame, (x, y), (end_x, end_y), color, stroke)
        
    cv2.imshow('frame',frame)
    k = cv2.waitKey(20) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

    
            
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
