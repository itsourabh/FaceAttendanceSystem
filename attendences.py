import csv
import os
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import filedialog, messagebox, ttk

import cv2
import mysql.connector
import numpy as np
from PIL import Image, ImageTk

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")
        self.root.wm_iconbitmap("face.ico")
        
        #================ Text Variable =========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        img=Image.open(r"C:\Attendence Manaage System\college_images\student.jpg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        
        
        img1=Image.open(r"college_images\student2.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
    
        
        
        img3=Image.open(r"college_images\attendance.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=200,width=1530,height=710)
        
        title_lbl=Label(f_lbl,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=700)
        
        # left lebel frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("timee new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=500)
        
        
        img_left=Image.open(r"C:\Attendence Manaage System\college_images\student2.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=400)
        
        #LabelEntry
        #Attendance_id
        
        AttendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("time new roman",13,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,sticky=W)
        
        AttendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("time new roman",13,"bold"))
        AttendanceID_entry.grid(row=0,column=1,pady=10,sticky=W)
        
        # Name 
        
        rollLabel=Label(left_inside_frame,text="Roll:",font=("time new roman",13,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,pady=10,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("time new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,pady=10,sticky=W)
        
        # Date
        
        nameLabel=Label(left_inside_frame,text="Name:",font=("time new roman",13,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,pady=10,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("time new roman",13,"bold"))
        atten_name.grid(row=1,column=1,pady=10,sticky=W)
        
        
        #Deparment
        
        depLabel_label=Label(left_inside_frame,text="Deparment:",font=("time new roman",13,"bold"),bg="white")
        depLabel_label.grid(row=1,column=2,pady=10,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("time new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,pady=10,sticky=W)
        
        # Time
        
        timeLabel=Label(left_inside_frame,text="Time:",font=("time new roman",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,pady=10,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("time new roman",13,"bold"))
        atten_time.grid(row=2,column=1,pady=10,sticky=W)
        
        # Date
        
        dateLabel=Label(left_inside_frame,text="Date:",font=("time new roman",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,pady=10,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("time new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=10,sticky=W)
        
        # attendance
        
        attendancelabel=Label(left_inside_frame,text="Attendance Status",font=("time new roman",13,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0,pady=10,sticky=W)
        
        # atten_attendance=ttk.Entry(left_inside_frame,width=20,font=("time new roman",13,"bold"))
        # atten_attendance.grid(row=3,column=1,padx=10,sticky=W)
        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("timee new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)
        
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("timee new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("timee new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.resetdata,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
    #================ rIGHT frame=================
    
    
    
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=720,height=500)
        
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=455)
        
        
        #====== SCroll bar ======
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","deparment","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("deparment",text="Deparment")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("deparment",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.getCursor)
        
        
        
    #=== Fetch Data ==========
    
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.CSV"),("ALL File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
    #=========== Export CSV ========
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.CSV"),("ALL File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your Data Exported To"+os.path.basename(fin)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
                
                
                
    def getCursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    #=========== Update Data ===================================
    def update_data(self):
        if self.var_atten_dep.get()=="Select dep" or self.var_atten_name.get()=="" or self.var_atten_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
            
        else:
            try:
                Update=messagebox.askyesno("update","Do You Want to Update the Record",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password='',database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set roll=%s,name=%s,dep=%s where StudentID=%s",(
                        
                        
                                                                                                                                            self.var_atten_roll.get(),
                                                                                                                                            self.var_atten_name.get(),
                                                                                                                                            self.var_atten_dep.get(),
                                                                                                                                            self.var_atten_id.get()
                                                                                                                                                                                            
                        
                                                                                                                                        ))
                else:
                    if not update:
                        return
                
                messagebox.showinfo("Update","Student Details Successfully Update Completed",parent=self.root)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
#===================== update End  ========================
        
        
    def resetdata(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
                
    #============ Update Data ========================
            
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
