import os
import tkinter
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from attendences import Attendance
from chat import ChatBot
from developer import Developer
from face_recognition import Face_Recognition
from help import Help
from student import Student
from train import Train


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        
        
        
        img=Image.open(r"C:\Attendence Manaage System\college_images\face.jpg")
        img=img.resize((500,300))
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open(r"C:\Attendence Manaage System\college_images\back.jpg")
        img1=img1.resize((500,300))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)
        
        img2=Image.open(r"C:\Attendence Manaage System\college_images\recog.jpg")
        img2=img2.resize((500,300))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        
        #bg image
        img3=Image.open(r"C:\Attendence Manaage System\college_images\bgimg.webp")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
    
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        #================= Time =============
        def time():
            string =strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font= ('time new roman ' , 13 ,'bold'),background = 'white' , foreground = 'blue')
        lbl.place(x=0, y=0,width=110,height=50)
        time()
        
        
        
        # Student Buttom 
        img4=Image.open(r"C:\Attendence Manaage System\college_images\student.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        
        b2=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=300,width=220,height=40)
        
        
        
        
        # Detect Image Buttom 
        img5=Image.open(r"C:\Attendence Manaage System\college_images\face_detect.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.Face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        
        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.Face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=300,width=220,height=40)
        
        
        # Attendence face Buttom 
        img6=Image.open(r"C:\Attendence Manaage System\college_images\attendance.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        
        b2=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=300,width=220,height=40)
        
        
        
        # Help Buttom 
        img7=Image.open(r"C:\Attendence Manaage System\college_images\chat1.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatB)
        b1.place(x=1100,y=100,width=220,height=220)
        
        
        b2=Button(bg_img,text="Chat Bot",cursor="hand2",command=self.chatB,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=300,width=220,height=40)
        
        
        
        # Train Face Buttom 
        img8=Image.open(r"C:\Attendence Manaage System\college_images\train.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        
        b2=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=580,width=220,height=40)
        
        
        
        # Photo face Buttom 
        img9=Image.open(r"C:\Attendence Manaage System\college_images\photos.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        
        b2=Button(bg_img,text="Photos",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=580,width=220,height=40)
        
        
        
        # Developer Image Buttom 
        img10=Image.open(r"C:\Attendence Manaage System\college_images\developer.webp")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.develop)
        b1.place(x=800,y=380,width=220,height=220)
        
        
        b2=Button(bg_img,text="Developer",cursor="hand2",command=self.develop, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=580,width=220,height=40)
        
        
        # Exit Image Buttom 
        img11=Image.open(r"C:\Attendence Manaage System\college_images\exit.png")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        
        b2=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=580,width=220,height=40)
        
        
        
        
    def open_img(self):
        os.startfile("data")
        
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
        
        # =================Function=============
        
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    
    def develop(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
        
    # def help(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Help(self.new_window)
        
    def chatB(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
        



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()