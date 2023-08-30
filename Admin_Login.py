# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:18:12 2023

@author: Administrator
"""

import tkinter as tk 
from tkinter import ttk
from tkinter import *
from PIL import Image
from PIL import ImageTk

window = Tk()
window.geometry("1250x900")
window.title("Amdocs Bank Admin . ")
image = Image.open("C:/Users/Administrator/Desktop/Amdocs Bank Management System/bank_admin_login_python.png")
image = image.resize((1290 , 800))
bg = ImageTk.PhotoImage(image)

label1 = tk.Label(image = bg)
label1.image = bg
label1.place(x = 0 , y = 0)


label2 = Label(window , text = "Welcome Amdoce Bank Admin . ")
label2.pack(pady = 100)

frame1 = Frame(window)
frame1.pack(pady = 20)

melabel=Label(window,text="AMDOCS BANK",
              bg="powder blue",width=15,font=("Algerian",50,"bold"))
melabel.place(x=350,y=40)


textin=StringVar()
textin2=StringVar()

metext11=Entry(window,font=("Courier New",12,"bold"),
               textvar=textin,width=25,bd=5,bg="powder blue")
metext11.place(x=650,y=230)

thelabel=Label(window,text="Username",bg="powder blue", width=15,font="arial 15 bold")
thelabel.place(x=400,y=230)

metext13=Entry(window,font=("Courier New",12,"bold"),
               textvar=textin2,width=25,bd=5,bg="powder blue")
metext13.place(x=650,y=330)

thelabel1=Label(window,text="Password",bg="powder blue",width=15,font="arial 15 bold")
thelabel1.place(x=400,y=330)

def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))

def Login():
    
    import mysql.connector
    
    mydbconn_1 = mysql.connector.connect(
            host = "localhost" ,
            user = "USER1" ,
            password = "USER@1234" ,
            database = "Amdocs_System"
            )
        
        #for fetching all 
    mypointer = mydbconn_1.cursor()
    mypointer.execute("SELECT * FROM ADMIN ")
    myrecords = mypointer.fetchall()
        
    login_id = metext11.get()
    password = metext13.get()
        
    list_1 = []
    list_1.append(login_id)
    list_1.append(password)
    

     
    if(list_1[0] == myrecords[0][0]) :
        if(list_1[1] == myrecords[0][1]) :
            window.destroy()
            import home_admin
            
    else :
        print("Incorrect Password Or User ID")
        window.destroy()
        
    mydbconn_1.commit()
    
         


#Buttons
butequal=Button(window,padx=15,pady=10,bd=3,bg="skyblue1",
                command=Login,text="Login",
                font=("Algerian",16,"bold"))
butequal.place(x=600,y=430)



changeOnHover(butequal, "yellow", "skyblue1")


window.mainloop()