
import os
import tkinter
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

# from attendences import Attendance
# from developer import Developer
# from face_recognition import Face_Recognition
# from help import Help
# from student import Student
# from train import Train


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("730x620+0+0")
        self.root.title("ChatMe")
        self.root.bind('<Return>',self.enter_funct)
        self.root.wm_iconbitmap("face.ico")
        
        
        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()
        
        img4=Image.open(r"college_images\chatbot1.webp")
        img4=img4.resize((200,70))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        
        f_lbl=Label(main_frame,bd=3,relief=RIDGE,image=self.photoimg4,text="Chat Me",font=("times new roman",30,"bold"),fg="green",bg="white")
        f_lbl.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=2,relief=RAISED,font=("ariel",14,"bold"),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()
        
        f_lbl=Label(btn_frame,text="Try Something?",fg="green",bg="white",font=("time new roman",12,"bold"))
        f_lbl.grid(row=0,column=0,padx=5,sticky=W)
        
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("time new roman",15,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send=Button(btn_frame,text="Send>>",command=self.sent,font=("ariel",14,"bold"),width=8,bg="green")
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=("ariel",14,"bold"),width=8,bg="red",fg="white")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label=Label(btn_frame,text=self.msg,fg="red",bg="white",font=("time new roman",14,"bold"))
        self.label.grid(row=1,column=1,padx=5,sticky=W)
    
    
    #============ Function Declaration ==============
    
    def enter_funct(self,event):
        self.send.invoke()
        self.entry.set('')
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
        
    
    def sent(self):
        sent='\t\t\t'+'You:  '+self.entry.get()
        self.text.insert(END,'\n'+sent)
        self.text.yview(END)
        
        
        
        if (self.entry.get()==''):
            self.msg='Please Enter Some Input'
            self.label.config(text=self.msg,fg="red")
        else:
            self.msg=''
            self.label.config(text=self.msg,fg="red")
        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        elif (self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')
        elif (self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+'Bot: Fine and You?')
        elif (self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice To Hear')
        elif (self.entry.get()=='Who Create  you?'):
            self.text.insert(END,'\n\n'+'Bot: Sourabh Gupta Using Python')
        elif (self.entry.get()=='what is your name?'):
            self.text.insert(END,'\n\n'+'Bot: My Name Is Cosmobot')
        elif (self.entry.get()=='can you speak hindi'):
            self.text.insert(END,"\n\n"+"Bot: I'm still learning it...")
        elif (self.entry.get()=='how to contact admin or developer'):
            self.text.insert(END,"\n\n"+"Bot: send email on given email address \n sg900@gmail.com")
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get that")
            
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()