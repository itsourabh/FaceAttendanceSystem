import datetime
import os
import random
import time
import tkinter
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import cx_Freeze
import mysql.connector
from PIL import Image, ImageTk

from attendences import Attendance
from chat import ChatBot
from developer import Developer
from face_recognition import Face_Recognition
# from help import Help
from main import Face_Recognition_System
from register import Register
from student import Student
from train import Train


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Login")
        self.root.bind('<Return>',self.enter_funct)
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.root.wm_iconbitmap("face.ico")
        
        
        
        
        self.photoimg=ImageTk.PhotoImage(file="C:\Attendence Manaage System\college_images\wall.jpeg")
        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Attendence Manaage System\college_images\log1.jpg")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        
        
        get_str=Label(frame,text="Get Started",font=("time new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        
        #======Label ==================
        UserName_label=Label(frame,text="UserName",font=("time new roman",13,"bold"),fg="white",bg="black")
        UserName_label.place(x=70,y=155)
        
        self.UserName=ttk.Entry(frame,width=20,font=("time new roman",15,"bold"))
        self.UserName.place(x=40,y=180,width=270)
        
        
        UserPass_label=Label(frame,text="Password",font=("time new roman",13,"bold"),fg="white",bg="black")
        UserPass_label.place(x=70,y=225)
        
        
        self.UserPass=ttk.Entry(frame,width=20,font=("time new roman",15,"bold"))
        self.UserPass.place(x=40,y=250,width=270)
        
        
        #==== icon image =======
        
        img2=Image.open(r"C:\Attendence Manaage System\college_images\icon.jpg")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        
        img3=Image.open(r"C:\Attendence Manaage System\college_images\pass.jpg")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        
        
        #========= Login Buttom =========
        self.b2=Button(frame,text="LogIn",command=self.login,cursor="hand2",font=("times new roman",15,"bold"),bd=3,bg="red",relief=RIDGE,fg="white",activeforeground="white",activebackground="red")
        self.b2.place(x=110,y=300,width=120,height=35)
        
        
        # RegisterButtom
        b1=Button(frame,text="New User Register",command=self.register_window,cursor="hand2",font=("times new roman",10,"bold"),borderwidth=0,bg="black",relief=RIDGE,fg="white",activebackground="black")
        b1.place(x=13,y=350,width=160)
        
        b3=Button(frame,text="Forget Password?",command=self.forget_password,cursor="hand2",font=("times new roman",10,"bold"),borderwidth=0,bg="black",relief=RIDGE,fg="white",activebackground="black")
        b3.place(x=10,y=370,width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def face_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)
        
    def enter_funct(self,event):
        self.b2.invoke()
        self.entry.set('')
        
        
        
        
    def login(self):
        if self.UserName.get()=="" or self.UserPass.get()=="":
            messagebox.showerror("Error","All Field Required",parent=self.root)
        elif self.UserName.get()=="UserName" and self.UserPass.get()=="UserPass":
                messagebox.showinfo("Success","Welcome To DashBoard")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.UserName.get(),
                                                                                    self.UserPass.get()
                
                
                                                                            ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Email Or Password")
            else:
                open_main=messagebox.askyesno("Yes","Access Only User")
                if open_main >0:
                    self.face_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.face_window)
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()
            
            
    
#======================= forget Password ==========================
    def reset_pass(self):
        if self.securityQ_combo.get()=="Select":
            messagebox.showerror("Error","Select The Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error" "Please Enter The Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error" "Please Enter New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.UserName.get(),self.securityQ_combo.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Data",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.UserName.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("info","Your Password has been reset ,please login with new password ",parent=self.root)
                self.root2.destroy()
    
    
    #========== Forget Password
    
    def forget_password(self):
        if self.UserName.get()=="":
            messagebox.showerror("Error","Please Written The Email Address To Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.UserName.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("My Error","Please Enter Valid User Name",parent=self.root2)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                securityQ_label=Label(self.root2,text="Select Security Question",font=("time new roman",15,"bold"),bg="white",fg="black")
                securityQ_label.place(x=50,y=80)
                
                self.securityQ_combo=ttk.Combobox(self.root2,font=("time new roman",12,"bold"),state="readonly",width=20)
                self.securityQ_combo['values']=("Select","Your Birthday Date","your Birth Place","Your Pet Name")
                self.securityQ_combo.current(0)
                self.securityQ_combo.place(x=50,y=110,width=250)
                
                
                
                securityA_label=Label(self.root2,text="Security Answer",font=("time new roman",15,"bold"),bg="white",fg="black")
                securityA_label.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("time new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_pass_label=Label(self.root2,text="New Reset",font=("time new roman",15,"bold"),bg="white",fg="black")
                new_pass_label.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("time new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                b4=Button(self.root2,text="Reset",command=self.reset_pass,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
                b4.place(x=100,y=330)
                
            
            
            
            
            
            # messagebox.showerror("Error", "Invalid UserName Or Password")
            
#======================== Register ===================================

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x900+0+0")
        
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
        b1=Button(frame,image=self.photoimage1,command=self.retur_login,borderwidth=0,cursor="hand2")
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
            conn=mysql.connector.connect(host="localhost",user="root",password='',database="mydata")
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
    def retur_login(self):
        self.root.destroy()
            
            
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        
        
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
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
    
    def open_img(self):
        os.startfile("data")
        
    
    
        
        
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
        
        
    def chatB(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
            
            
            
            
            
#=============Def Login ==================
    # def login_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Face_Recognition_System(self.new_window)
    
    # def register_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Register(self.new_window)

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        
        
        title_lbl=Label(self.root,text="Face Recognition", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        
        
        
        
        img_top=Image.open(r"college_images\face_detect.jpg")
        img_top=img_top.resize((650,750))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=750)
        
        
        
        img_side=Image.open(r"college_images\recog.jpg")
        img_side=img_side.resize((950,750))
        self.photoimg_side=ImageTk.PhotoImage(img_side)
        
        
        f_lbl=Label(self.root,image=self.photoimg_side)
        f_lbl.place(x=650,y=55,width=950,height=750)
        
        
        b2=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2", font=("times new roman",18,"bold"),bg="Blue",fg="white")
        b2.place(x=365,y=620,width=200,height=40)
        # cv2.destroyAllWindows()
        
        
        #+======= Attendence ================
    def mark_attendence(self,s,i,r,d):
        with open("atten.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((s not in name_list) and (i not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{i},{r},{d},{dtString},{d1},Present")
        
        
        
        
        # ======= face recognition ===========
        
        
    def face_recog(self):
        def draw_boundary(img,classifier,ScaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,ScaleFactor,minNeighbors)
            
            
            coord=[]
                
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="face_recognition")
                my_cursor=conn.cursor()
                    
                my_cursor.execute("select Name from student where StudentID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                    
                my_cursor.execute("select ROLL from student where StudentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                    
                my_cursor.execute("select Dep from student where StudentID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                    
                    
                my_cursor.execute("select StudentID from student where StudentID="+str(id))
                s=my_cursor.fetchone()
                s="+".join(s)
                
                
                
                if confidence>77:
                    cv2.putText(img,f"StudentID:{s}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(s,i,r,d)
                        
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        
                coord=[x,y,w,h]
                    
                    
            return coord
            # cv2.destroyAllWindows()
    
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
                
                
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
                
                
        video_cap=cv2.VideoCapture(0)
                
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
                    
                
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyWindow(recognize)
        cv2.destroyAllWindows(self.root)

        
        
        
        
        
        
        
        
        

if __name__ == "__main__":
    main()
    # root=Tk()
    # obj=Login_Window(root)
    # root.mainloop()
    # cv2.destroyAllWindows()
