import os
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import mysql.connector
from PIL import Image, ImageTk


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        self.root.wm_iconbitmap("face.ico")
        
        
        
        title_lbl=Label(self.root,text="Developer", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=60)
        
        
        img=Image.open(r"C:\Attendence Manaage System\college_images\help_deck.jpg")
        img=img.resize((1530,720))
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        title_lbl=Label(f_lbl,text="Email:SG9003229@gmail.com", font=("time new roman",25,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=550,y=260)
        
    
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()