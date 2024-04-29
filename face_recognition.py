import os
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import mysql.connector
import numpy as np
from PIL import Image, ImageTk


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
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()