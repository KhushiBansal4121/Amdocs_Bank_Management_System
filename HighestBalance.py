# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:46:54 2023

@author: khushiba
"""

from tkinter import*
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from datetime import date
import mysql.connector
import bank_main
from datetime import datetime


window=Tk()
window.geometry("1290x800")
window.title("Highest Balance")


image1 = Image.open("C:/Users/Administrator/Desktop/Amdocs Bank Management System/hey.jpg")
# Resize the image using resize() method
image1 = image1.resize((900, 900))

test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

 
# Custom font style and font size

#.create_text( 200, 250, text = "Welcome",font=("Times",35,"bold"))

# Position image
label1.place(x=0, y=0)

image1 = Image.open("C:/Users/Administrator/Desktop/Amdocs Bank Management System/hello.jpg")
# Resize the image using resize() method
image1 = image1.resize((1500, 900))

test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

 
# Custom font style and font size

#.create_text( 200, 250, text = "Welcome",font=("Times",35,"bold"))

# Position image
label1.place(x=450, y=0)

#melabel=Label(window,text="SERVICES",font=("Times",28,"bold"),height=2,width=20,bg="powder blue")
#melabel.place(x=55,y=100)

textin=StringVar()
textin2=StringVar() 
textin3=StringVar()
textin4=StringVar()

def TotalTransactionDate():
    window.destroy()
    import TotalTransactionDate

def HighestBalance():
    window.destroy()
    import HighestBalance

def CountTransactionDate():
    window.destroy()
    import CountTransactionDate

def CountTransactionMonth():
    window.destroy()
    import CountTransactionMonth
 

def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))

conn= mysql.connector.connect(
        host = "localhost" ,
        user = "USER1" ,
        password = "USER@1234" ,
        database = "amdocs_system"
        )

'''
def done():
    window.destroy()
    import home
'''   
thelabel_1=Label(window,width=90,height=30,bg="powder blue")
thelabel_1.place(x=550,y=120)

melabel=Label(window,text="Highest Balance In The \n Amdocs Bank . ",font=("Times",30,"bold"),bg="powder blue")
melabel.place(x=690,y=150)


thelabel_0=Label(window,text="Hello Amdocs Bank Admin . ",font="ariel 18 bold",bg="black",fg="white")
thelabel_0.place(x=50,y=100)

butequal1=Button(window,padx=125,pady=14,bd=2,bg="skyblue1",
                command=TotalTransactionDate,width=17,text="Total Transaction According To The Date . ",font=("Courier New",12,"bold")) 
butequal1.place(x=10,y=200)  

butequal2=Button(window,padx=125,pady=14,bd=2,bg="skyblue1",
                command=HighestBalance,width=17,text="Highest Balance In The Amdocs Bank . ",font=("Courier New",12,"bold")) 
butequal2.place(x=10,y=300)  

butequal3=Button(window,padx=125,pady=14,bd=2,bg="skyblue1",
                command=CountTransactionDate,width=17,text="Count Transaction According To The Date . ",font=("Courier New",12,"bold")) 
butequal3.place(x=10,y=400)  

butequal4=Button(window,padx=125,pady=14,bd=2,bg="skyblue1",
                command=CountTransactionMonth,width=17,text= "Count Transaction According To The Month . ",font=("Courier New",12,"bold")) 
butequal4.place(x=10,y=500)  



def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))
    
def home():
    window.destroy()
    import home
    
def mini_statement():
    mypointer=conn.cursor()
    acc_num=bank_main.acc_num
    q1= """select bk.Account_Number,cust.Name,bk.total_balance from customers as cust
        join balance as bk on
        bk.Account_Number=cust.Account_Number
        order by bk.total_balance DESC
        LIMIT 5;"""
    mypointer.execute(q1,[acc_num])
    result = mypointer.fetchall()
    print(result)
    thelabel_0=Label(window,text="ID",font="ariel 15 bold",bg="powder blue")
    thelabel_0.place(x=650,y=200)
    
    thelabel_0=Label(window,text="TYPE",font="ariel 15 bold",bg="powder blue")
    thelabel_0.place(x=825,y=200)
    
    thelabel_0=Label(window,text="AMOUNT",font="ariel 15 bold",bg="powder blue")
    thelabel_0.place(x=1000,y=200)
    
    y=250
    
    for i in range (len(result)):
        
        thelabel_1=Label(window,text=result[i][3],font="ariel 13 bold",bg="powder blue")
        thelabel_1.place(x=650,y=y)
        
        thelabel_1=Label(window,text=result[i][1],font="ariel 13 bold",bg="powder blue")
        thelabel_1.place(x=825,y=y)
        
        thelabel_1=Label(window,text=result[i][2],font="ariel 13 bold",bg="powder blue")
        thelabel_1.place(x=1000,y=y)
        
        y+=50

    butequal=Button(window,padx=32,height= -1,pady=14,bd=2,bg="powder blue",command=home,text="home",width=10,font=("Courier New",15,"bold")) 
    butequal.place(x=800,y=500)   
    changeOnHover(butequal, "yellow", "skyblue1")

butequal=Button(window,padx=32,pady=14,bd=2,bg="skyblue1",
                command=mini_statement,text="CHECK",
                font=("Courier New",15,"bold"))  
butequal.place(x=800,y=500)   
changeOnHover(butequal, "yellow", "skyblue1")

window.mainloop()



'''
butequal=Button(window,padx=32,pady=14,bd=2,bg="skyblue1",
                command=done,text="DONE",
                font=("Courier New",15,"bold")) 
butequal.place(x=780,y=500)  
changeOnHover(butequal, "yellow", "skyblue1")
'''
changeOnHover(butequal1, "yellow", "skyblue1")
changeOnHover(butequal2, "yellow", "skyblue1")
changeOnHover(butequal3, "yellow", "skyblue1")
changeOnHover(butequal4, "yellow", "skyblue1")
window.mainloop()










