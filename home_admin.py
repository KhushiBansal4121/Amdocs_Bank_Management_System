# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:28:23 2023

@author: Administrator
"""

from tkinter import*
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import ttk

window=Tk()
window.geometry("1290x800")
window.title("Amdocs Bank Admin . ")


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

'''
def done():
    window.destroy()
    import home
'''   
thelabel_1=Label(window,width=90,height=30,bg="powder blue")
thelabel_1.place(x=550,y=120)

melabel=Label(window,text="Amdocs Bank \n Admin Statements",font=("Times",30,"bold"),bg="powder blue")
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