import urllib.request
import urllib.error
import requests
from tkinter import *
from tkinter import messagebox
from datetime import *

def send():
    sender='1234567890' #YOUR MOBILE NUMBER
    password='PASSWORD' #YOUR PASSWORD
    receiver=str(entry1.get())
    message=str(entry2.get('0.0',END))
    if len(receiver)==10:
        url=str('https://smsapi.engineeringtgr.com/send/?Mobile='+sender+'&Password='+password+'&Message='+message+'&To='+receiver+'&Key=jawadfg0MLDjbYV5hirZ')
        results=requests.get(url)
        if results.ok== True:
            messagebox.showinfo("Success","Message sent Successfully!!!")
        else:
            messagebox.showerror("Error","Message does not sent. Check the internet connection!!")
        print(url)
    else:
        messagebox.showerror("Error","Receiver number is invalid!!")
def charlength(event):
    label4["text"]=len(entry2.get('0.0',END))
    
def close():
    root.destroy()
def login():
    global root
    root=Tk(className=" Free SMS")
    root.config(width=650,height=320,bg="Cyan")
    label1=Label(root,text="Free SMS",fg="Blue",bg="Cyan",font=('Comic Sans MS',30,'bold'))
    label1.place(x=225,y=10)
    label2=Label(root,text="Receiver:",bg="Cyan",font=('monospace',10,'bold'))
    label2.place(x=20,y=80)
    label3=Label(root,text="Message:",bg="Cyan",font=('monospace',10,'bold'))
    label3.place(x=20,y=110)
    global label4
    label4=Label(root,text="",bg="Cyan",font=('monospace',10,'bold'))
    label4.place(x=100,y=110)
    label5=Label(root,text="Developed by JK",fg="Blue",font=('Comic Sans MS',20,'bold','italic'),bg="Cyan")
    label5.place(x=230,y=280)
    global entry1
    entry1=Entry(root,width=80)
    entry1.place(x=130,y=80)
    global entry2
    entry2=Text(root,width=60,height=5)
    entry2.place(x=130,y=110)
    entry2.bind("<Key>",charlength)
    button1=Button(root,text="Send",width=10,command=send)
    button1.place(x=130,y=250)
    button2=Button(root,text="Exit",width=10,command=close)
    button2.place(x=535,y=250)
    root.mainloop()
def closeA():
    conn.commit()
    conn.close()
    rootA.destroy()
def afterlogin():
    username=str(entry11.get())
    password=str(entry12.get())
    if(username=="1234567890" and password=="PASSWORD"):
        messagebox.showinfo("Success","Login Successful!!!")
        rootA.destroy()
        login()
    else:
        messagebox.showerror("Error","Invalid username or password!!")
        
rootA=Tk(className=" Free SMS")
rootA.config(width=500,height=250,bg="Cyan")
label11=Label(rootA,text="Free SMS",fg="Blue",bg="Cyan",font=('Comic Sans MS',30,'bold'))
label11.place(x=150,y=10)
label12=Label(rootA,text="Username:",bg="Cyan",font=('monospace',10,'bold'))
label12.place(x=20,y=80)
label13=Label(rootA,text="Password:",bg="Cyan",font=('monospace',10,'bold'))
label13.place(x=20,y=110)
label14=Label(rootA,text="Developed by JK",fg="Blue",font=('Comic Sans MS',20,'bold','italic'),bg="Cyan")
label14.place(x=150,y=200)
entry11=Entry(rootA,width=50)
entry11.place(x=130,y=80)
entry12=Entry(rootA,width=50,show='*')
entry12.place(x=130,y=110)
button11=Button(rootA,text="Login",width=10,command=afterlogin)
button11.place(x=130,y=150)
button12=Button(rootA,text="Exit",width=10,command=closeA)
button12.place(x=350,y=150)
rootA.mainloop()
