import os
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import mysql.connector
from PIL import Image, ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        
        
        # ============== variable==============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        # self.var_photo=StringVar()
    
    
    
    
    
    
        img=Image.open(r"C:\Attendence Manaage System\college_images\student.jpg")
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
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        
        # left lebel frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("timee new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)
        
        img_left=Image.open(r"C:\Attendence Manaage System\college_images\student2.jpg")
        img_left=img_left.resize((720,300))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)
        
        
        # current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=750,height=115)
        
        
        # Deparment
        dep_label=Label(current_course_frame,text="Deparment",font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("timee new roman",12,"bold"),state="readonly",width=20)
        dep_combo['values']=("Select Dep","Computer science","Electrical","AI")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course
        
        Course_label=Label(current_course_frame,text="Course",font=("time new roman",12,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        
        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("timee new roman",12,"bold"),state="readonly",width=20)
        Course_combo['values']=("Select Course","FE","SE","AI","DS")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        # Year
        
        
        Year_label=Label(current_course_frame,text="Year",font=("time new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",12,"bold"),state="readonly",width=20)
        Year_combo['values']=("Select Year","2020-21","2021-22","2022-23","2023-24")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        # Semaster
        
        
        Semaster_label=Label(current_course_frame,text="Semaster",font=("time new roman",12,"bold"),bg="white")
        Semaster_label.grid(row=1,column=2,padx=10,sticky=W)
        
        
        Semaster_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("timee new roman",12,"bold"),state="readonly",width=20)
        Semaster_combo['values']=("Select Semaster","Semaster-1","Semaster-2")
        Semaster_combo.current(0)
        Semaster_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        # Class Student Information
        Class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=750,height=300)
        
        #Student ID
        StudentID_label=Label(Class_Student_frame,text="StudentID:",font=("time new roman",13,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,sticky=W)
        
        StudentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("time new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        
        #Student Name
        StudentName_label=Label(Class_Student_frame,text="StudentName:",font=("time new roman",13,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        StudentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("time new roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #Class Division
        Class_div_label=Label(Class_Student_frame,text="ClassDivision:",font=("time new roman",13,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=20,font=("time new roman",13,"bold"))
        Class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("timee new roman",12,"bold"),state="readonly",width=20)
        div_combo['values']=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Roll No
        roll_no_label=Label(Class_Student_frame,text="RollNo:",font=("time new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("time new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(Class_Student_frame,text="Gender:",font=("time new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=20,font=("time new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("time new roman",12,"bold"),state="readonly",width=20)
        gender_combo['values']=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(Class_Student_frame,text="DOB:",font=("time new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("time new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_label=Label(Class_Student_frame,text="Email:",font=("time new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("time new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #Phone
        phone_no_label=Label(Class_Student_frame,text="PhoneNo:",font=("time new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("time new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label=Label(Class_Student_frame,text="Address:",font=("time new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("time new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher Name
        TeacherName_label=Label(Class_Student_frame,text="TeacherName:",font=("time new roman",13,"bold"),bg="white")
        TeacherName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        TeacherName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("time new roman",13,"bold"))
        TeacherName_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        # self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #button Frame
        
        
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=735,height=70)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("timee new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("timee new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("timee new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset,width=15,font=("timee new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        
        take_photo_btn=Button(btn_frame1,text="Take a Photo Sample",command=self.generate_data,width=40,font=("time new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo",width=35,font=("time new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

            
        # right lebel frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("timee new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=700,height=580)
        
        img_right=Image.open(r"C:\Attendence Manaage System\college_images\student3.jpg")
        img_right=img_right.resize((720,300))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        
        # Searching System
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Searching System",font=("time new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=690,height=70)
        
        Search_label1=Label(Search_frame,text="Search By:",font=("time new roman",13,"bold"),bg="red")
        Search_label1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        
        
        Search_combo=ttk.Combobox(Search_frame,font=("time new roman",12,"bold"),state="readonly",width=15)
        Search_combo['values']=("Select","Roll_No","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(Search_frame,width=15,font=("time new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)
        
        
        
        ShowAll_btn=Button(Search_frame,text="ShowAll",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)
        
        
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=690,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","id","sem","name","roll","div","email","gender","dob","address","phone","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Dep")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semaster")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        
        
        
    # =============Function Declaration===========
    
    def add_data(self):
        if self.var_dep.get()=="Select dep" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                    
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Details Have Been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
        
        
        
        #========== Fetch Data ========
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if  len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    
    #====== Get Cursor ======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_sem.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_div.set(data[7]),
        self.var_email.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_address.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        
    #========= Update function =======
    
    
    def update_data(self):
        if self.var_dep.get()=="Select dep" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
            
        else:
            try:
                Update=messagebox.askyesno("update","Do You Want to Update the Record",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,year=%s,Semaster=%s,Name=%s,ROLL=%s,Division=%s,Email=%s,Gender=%s,DOB=%s,Address=%s,Phone=%s,Teacher=%s,PhotoSample=%s where StudentID=%s",(
                        
                        
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),   
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get()
                    
                        
                                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                
                messagebox.showinfo("Update","Student Details Successfully Update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
    # ============================= Delete ==============
    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from Student where StudentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Delete Completed",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
    #==================  Reset =========================
    
    def reset(self):
        self.var_dep.set("Select Deparment")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semaster")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
        
    #=========== Take A Photo Sample  =================
    def generate_data(self):
        if self.var_dep.get()=="Select dep" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
            
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from Student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
            
                conn=mysql.connector.connect(host="localhost",user="root",password='Admin@123',database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("update student set Dep=%s,Course=%s,year=%s,Semaster=%s,Name=%s,Division=%s,ROLL=%s,Gender=%s,Email=%s,DOB=%s,Address=%s,Phone=%s,Teacher=%s,PhotoSample=%s where StudentID=%s",(
                        
                        
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get()==id+1
                        
                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                
                #========= Frontal Face =========
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.5
                    #minimum neighbour = 5
                    
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set completed!!!!")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()