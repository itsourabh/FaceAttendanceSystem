import datetime
import os
import random
import time
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import mysql.connector
from PIL import Image, ImageTk


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x900+0+0")
        self.root.wm_iconbitmap("face.ico")
        
        #====== Variable =========
        self.var_FirstName=StringVar()
        self.var_LastName=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_conf_password=StringVar()
        
        self.bg=ImageTk.PhotoImage(file=r"college_images\register.jpg")
        
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        self.bg1=ImageTk.PhotoImage(file=r"college_images\new.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        
        #============ main frame ======
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        
        reg_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",20,"bold"),fg="darkgreen",bg="white")
        reg_lbl.place(x=20,y=20)
        
        
        
        #============== label and entry ===============
        
        FirstName_label=Label(frame,text="First Name",font=("time new roman",15,"bold"),bg="white")
        FirstName_label.place(x=50,y=100)
        
        FirstName=ttk.Entry(frame,textvariable=self.var_FirstName,width=20,font=("time new roman",15,"bold"))
        FirstName.place(x=50,y=130,width=250)
        
        
        LastName_label=Label(frame,text="Last Name",font=("time new roman",15,"bold"),bg="white")
        LastName_label.place(x=370,y=100)
        
        LastName=ttk.Entry(frame,textvariable=self.var_LastName,width=15,font=("time new roman",15,"bold"))
        LastName.place(x=370,y=130,width=250)
        
        Contact_label=Label(frame,text="Contact",font=("time new roman",15,"bold"),bg="white")
        Contact_label.place(x=50,y=170)
        
        Contact=ttk.Entry(frame,textvariable=self.var_contact,width=15,font=("time new roman",15,"bold"))
        Contact.place(x=50,y=200,width=250)
        
        email_label=Label(frame,text="Email",font=("time new roman",15,"bold"),bg="white")
        email_label.place(x=370,y=170)
        
        email=ttk.Entry(frame,textvariable=self.var_email,width=15,font=("time new roman",15,"bold"))
        email.place(x=370,y=200,width=250)
        
        
        #====== Row ==============
        securityQ_label=Label(frame,text="Select Security Question",font=("time new roman",15,"bold"),bg="white",fg="black")
        securityQ_label.place(x=50,y=240)
        
        self.securityQ_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",12,"bold"),state="readonly",width=20)
        self.securityQ_combo['values']=("Select","Your Birthday Date","your Birth Place","Your Pet Name")
        self.securityQ_combo.current(0)
        self.securityQ_combo.place(x=50,y=270,width=250)
        
        
        
        securityA_label=Label(frame,text="Security Answer",font=("time new roman",15,"bold"),bg="white",fg="black")
        securityA_label.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        password_label=Label(frame,text="Password",font=("time new roman",15,"bold"),bg="white")
        password_label.place(x=50,y=310)
        
        self.password=ttk.Entry(frame,textvariable=self.var_password,font=("time new roman",15,"bold"))
        self.password.place(x=50,y=340,width=250)
        
        
        conf_password_label=Label(frame,text="Confirm Password",font=("time new roman",15,"bold"),bg="white")
        conf_password_label.place(x=370,y=310)
        
        self.conf_password=ttk.Entry(frame,textvariable=self.var_conf_password,font=("time new roman",15,"bold"))
        self.conf_password.place(x=370,y=340,width=250)
        
        self.var_radio1=StringVar()
        radiobtn1=Checkbutton(frame,textvariable=self.var_radio1,text="I Agree The terms  & Condition",font=("time new roman",12,"bold"),onvalue=1,offvalue=0)
        radiobtn1.place(x=50,y=380)
        
        #=========== Buttom ==============
        img=Image.open(r"C:\Attendence Manaage System\college_images\r5.jpg")
        img=img.resize((100,55))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_record,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)
        
        
        
        img1=Image.open(r"C:\Attendence Manaage System\college_images\l.png")
        img1=img1.resize((200,50))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
        
        
        
        
    #================ Function ===========
    
    def register_record(self):
        if self.var_FirstName.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Field Are Required")
        elif self.var_password.get()!=self.var_conf_password.get():
            messagebox.showerror("Error","Password Are Not Matching")
        elif self.var_radio1.get()==0:
            messagebox.showerror("Error","Please Check Terms & Condition")
            
        else:
            # messagebox.showinfo("Success","Register Successfully")
            conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User Already Exist")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_FirstName.get(),
                                                                                                self.var_LastName.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_password.get(),
                    
                    
                    
                    
                                                                                            ))
                
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")
                
            



        
        
       
        
        
        

        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()