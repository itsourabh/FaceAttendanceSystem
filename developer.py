import os
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import mysql.connector
from PIL import Image, ImageTk


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        self.root.wm_iconbitmap("face.ico")
        
        
        
        title_lbl=Label(self.root,text="Developer", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=60)
        
        
        img=Image.open(r"C:\Attendence Manaage System\college_images\developer.webp")
        img=img.resize((1530,720))
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        main_frame=Frame(f_lbl,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        
        
        img1=Image.open(r"C:\Attendence Manaage System\college_images\developer.webp")
        img1=img1.resize((1530,720))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        
        # Developer
        title_lbl=Label(main_frame,text="Hello, My Name Is Sourabh Gupta", font=("time new roman",13,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=5)
        
        title_lbl=Label(main_frame,text="I am Full Stack Developer", font=("time new roman",13,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=40)
        
        
        img2=Image.open(r"C:\Attendence Manaage System\college_images\developer.webp")
        img2=img2.resize((500,390))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)
        















if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()