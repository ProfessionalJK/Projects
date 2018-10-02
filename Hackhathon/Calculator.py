from tkinter import *
root=Tk(className=" Calculator")
root.config(bg="Cyan",width=300,height=200)
def b1Pressed():
    s1=e1.get()
    s2=e2.get()
    try:
        t1=(float)(e1.get())
        t2=(float)(e2.get())
        t3=t1+t2
        l3["text"]=t3
    except ValueError as ve: 
        l3["text"]="Digits Only"
def b2Pressed():
    s1=e1.get()
    s2=e2.get()
    try:
        t1=(float)(e1.get())
        t2=(float)(e2.get())
        t3=t1-t2
        l3["text"]=t3
    except ValueError as ve: 
        l3["text"]="Digits Only"
def b3Pressed():
    s1=e1.get()
    s2=e2.get()
    try:
        t1=(float)(e1.get())
        t2=(float)(e2.get())
        t3=t1*t2
        l3["text"]=t3
    except ValueError as ve: 
        l3["text"]="Digits Only"
def b4Pressed():
    s1=e1.get()
    s2=e2.get()
    try:
        t1=(float)(e1.get())
        t2=(float)(e2.get())
        t3=t1/t2
        l3["text"]=t3
    except ValueError as ve: 
        l3["text"]="Digits Only"
def b5Pressed():
    s1=e1.get()
    s2=e2.get()
    try:
        t1=(float)(e1.get())
        t2=(float)(e2.get())
        t3=t1%t2
        l3["text"]=t3
    except ValueError as ve: 
        l3["text"]="Digits Only"
l1=Label(root,text="Enter First Number",bg="Cyan")
l1.place(x=10,y=10)
e1=Entry(root,width=20)
e1.place(x=150,y=10)
l2=Label(root,text="Enter Second Number",bg="Cyan")
l2.place(x=10,y=30)
e2=Entry(root,width=20)
e2.place(x=150,y=30)
b1=Button(root,width=5,text="+",command=b1Pressed)
b1.place(x=10,y=60)
b2=Button(root,width=5,text="-",command=b2Pressed)
b2.place(x=70,y=60)
b3=Button(root,width=5,text="*",command=b3Pressed)
b3.place(x=130,y=60)
b4=Button(root,width=5,text="/",command=b4Pressed)
b4.place(x=190,y=60)
b5=Button(root,width=5,text="%",command=b5Pressed)
b5.place(x=250,y=60)
l3=Label(root,text="",fg="blue",bg="Cyan")
l3.place(x=100,y=100)
l4=Label(root,text="Developed by JK",bg="Cyan",fg="Blue",font=('Comic Sans MS',15,"bold"))
l4.place(x=70,y=150)
root.mainloop()
