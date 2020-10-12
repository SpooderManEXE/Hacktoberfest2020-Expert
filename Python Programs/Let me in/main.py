import os
from tkinter import *
from tkinter import messagebox  
from PIL import ImageTk,Image
import numpy as np
import cv2
import time


# menubar
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.widgets()

    def widgets(self):
        menubar = Menu(root)
        file = Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='File', menu = file) 
        file.add_command(label ='Edit Api', command = edit_ap) 
        file.add_separator() 
        file.add_command(label ='Exit', command = root.destroy)

        help_ = Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='Help', command = info_help)
        help_.add_command(label ='About', command = info) 
        root.config(menu = menubar)

root = Tk()
root.title('Let Me In')
root.iconbitmap("file/home.ico")
root.resizable(False, False)

# edit api
def edit_ap():
    top = Toplevel()
    top.geometry("390x220")
    top.title("Edit API")
    top.iconbitmap("file/home.ico")
    top.resizable(False, False)
    label_1 = Label(top, text = "Enter API", font=('times', 15, ' bold '))
    entry_api = Entry(top, width=50)
    p = entry_api.get()


    button_1 = Button(top, text = "Done", font=('times', 15, ' bold '), command= None)
    

    label_1.place(x=145,y=25)
    entry_api.place(x=45,y=65)
    button_1.place(x=165,y=100)




# homepage
my_img = ImageTk.PhotoImage(Image.open("file/home.jpg"))
my_label = Label(image=my_img)
my_label.grid(row=0,column=0)


# define label
label_1 = Label(root, text="Let Me In", font=("Helvetica" ,56), bg="blue", fg="white")

def info():
   messagebox.showinfo("Info", "Made by Abhishek, Vishal, Vaibhav")

def info_help():
   messagebox.showinfo("Instruction", "If you are first time running this\n Click on 'Add Person' button\n Enter students Name\n Take their pic(it will take 5 minute)\n Train pics\n then exit this window\n Now you can use this app")

def add():
    top = Toplevel()
    top.geometry("400x300")
    top.title("Add Person")
    top.iconbitmap("file/home.ico")
    top.resizable(False, False)
    label_1 = Label(top, text = "Add Person", font=("Helvetica" ,56), bg="green", fg="white")
    label_2 = Label(top, text = "Enter Name", font=('times', 15, ' bold '))
    entry_name = Entry(top)
    
    def take():
        cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        cap = cv2.VideoCapture(0) #, cv2.CAP_DSHOW)
        dirName = "dataset/"+entry_name.get()
        imgname = dirName+"/"+ entry_name.get()
        try:
            os.makedirs(dirName)    
            i=1
            count=25
            start_time = time.time()
            while count>i:
                # Capture frame-by-frame
                ret, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                for (x, y, w, h) in faces:
                    #roi_grey = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    color = (0,255,0) #BGR
                    stroke = 2
                    end_x = x+w
                    end_y = y+h
                    cv2.rectangle(frame, (x, y), (end_x, end_y), color, stroke)
                    if time.time() - start_time >= 2: #<---- Check if 5 sec passed
                        img_item = imgname+str(i)+".png"
                        cv2.imwrite(img_item, frame)
                        start_time = time.time()
                        i += 1
                

                

                cv2.imshow('frame',frame)
                k = cv2.waitKey(20) & 0xff # Press 'ESC' for exiting video
                if k == 27:
                    messagebox.showinfo("Error", "Image taking process is interepted")
                    break
            
            messagebox.showinfo("complete", "Image taking is completed now click on train pic")

                    
            cap.release()
            cv2.destroyAllWindows()    
        except FileExistsError:
            messagebox.showwarning("Error","No Name / Name Already Exists")
        return


    def train():
        os.system("python trainner.py 1")
        
    button_1 = Button(top, text = "Take Pic", font=('times', 15, ' bold '), command=take)
    button_2 = Button(top, text = "Train Pic", font=('times', 15, ' bold '), command=train)
    button_3 = Button(top, text = "Exit", font=('times', 15, ' bold '), command=top.destroy)


    label_1.grid(row=0,column=0,columnspan=3)
    label_2.place(x=55,y=120)
    entry_name.place(x=175,y=125)
    button_1.place(x=25,y=175)
    button_2.place(x=165,y=175)
    button_3.place(x=300,y=175)


def letmein():
    os.system("python scanner.py 1")

# define button
button_1 = Button(root, text="Let Me In", fg="black", bg="green",width=15  ,height=2,font=('times', 15, ' bold '), padx=10, command=letmein)
button_add = Button(root, text="Add Person", padx=10, width=10 ,height=2, font=('times', 15, ' bold '), command=add)
button_exit = Button(root, text="Exit", padx=10, width=10 ,height=2, font=('times', 15, ' bold '), command=root.destroy)



# placing it on screen
label_1.place(x=389,y=50)
button_1.place(x=465,y=475)
button_add.place(x=100,y=475)
button_exit.place(x=850,y=475)



app = App(root)
root.mainloop()
