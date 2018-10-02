from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import *
from datetime import *
conn=pymysql.connect(host="localhost",user="root",passwd="ILoveYouRehanaKazi",database="expense")
cursor=conn.cursor()
def total():
    hotel=int(entry3.get())
    transport=int(entry4.get())
    education=int(entry5.get())
    petrol=int(entry6.get())
    phone=int(entry7.get())
    others=int(entry8.get())
    total=str(hotel+transport+education+petrol+phone+others)
    if (hotel==0):
        hotel=str('-')
    if (transport==0):
        transport=str('-')
    if (education==0):
        transport=str('-')
    if (petrol==0):
        petrol=str('-')
    if (phone==0):
        phone=str('-')
    if (others==0):
        others=str('-')
    entry9.insert(END,'')
    entry9.insert(END,total+'.0')
def submit():
    description=str(entry2.get())
    hotel=str(entry3.get())
    transport=str(entry4.get())
    education=str(entry5.get())
    petrol=str(entry6.get())
    phone=str(entry7.get())
    others=str(entry8.get())
    total=str(int(hotel)+int(transport)+int(education)+int(petrol)+int(phone)+int(others))
    total=str(total+".0")
    if (hotel=="0"):
        hotel=str('-')
    if (transport=="0"):
        transport=str('-')
    if (education=="0"):
        education=str('-')
    if (petrol=="0"):
        petrol=str('-')
    if (phone=="0"):
        phone=str('-')
    if (others=="0"):
        others=str('-')
    dateaaj=str(entry1.get("0.0",END))
    dateaaj=dateaaj.partition("\n")
    dateaaj=str(dateaaj[0])
    s=list()
    s.append(dateaaj)
    s.append(description)
    s.append(hotel)
    s.append(transport)
    s.append(education)
    s.append(petrol)
    s.append(phone)
    s.append(others)
    s.append(total)
    try:
        cursor.execute("INSERT INTO EXPENSE2018 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8]))
        cursor.execute("SELECT * FROM EXPENSE2018 WHERE DATE=%s",(s[0]))
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        print("Data added Successfully!!!")
    except:
        print(error)
def close():
    conn.commit()
    conn.close()
    root.destroy()
def login():
    global root
    root=Tk(className=" Expense 2018")
    root.config(width=650,height=420,bg="Cyan")
    label1=Label(root,text="Expense 2018",fg="Blue",bg="Cyan",font=('Comic Sans MS',30,'bold'))
    label1.place(x=200,y=10)
    label2=Label(root,text="Date:",bg="Cyan",font=('monospace',10,'bold'))
    label2.place(x=20,y=80)
    label3=Label(root,text="Description:",bg="Cyan",font=('monospace',10,'bold'))
    label3.place(x=20,y=110)
    label4=Label(root,text="Hotel:",bg="Cyan",font=('monospace',10,'bold'))
    label4.place(x=20,y=140)
    label5=Label(root,text="Transport:",bg="Cyan",font=('monospace',10,'bold'))
    label5.place(x=20,y=170)
    label6=Label(root,text="Education:",bg="Cyan",font=('monospace',10,'bold'))
    label6.place(x=20,y=200)
    label7=Label(root,text="Petrol:",bg="Cyan",font=('monospace',10,'bold'))
    label7.place(x=20,y=230)
    label8=Label(root,text="Phone:",bg="Cyan",font=('monospace',10,'bold'))
    label8.place(x=20,y=260)
    label9=Label(root,text="Others:",bg="Cyan",font=('monospace',10,'bold'))
    label9.place(x=20,y=290)
    label10=Label(root,text="Total:",bg="Cyan",font=('monospace',10,'bold'))
    label10.place(x=20,y=320)
    label11=Label(root,text="Developed by JK",fg="Blue",font=('Comic Sans MS',20,'bold','italic'),bg="Cyan")
    label11.place(x=200,y=370)
    global entry1
    entry1=Text(root,width=60,height=1)
    entry1.insert(END,date.today())
    entry1.place(x=130,y=80)
    global entry2
    entry2=Entry(root,width=80)
    entry2.place(x=130,y=110)
    global entry3
    entry3=Entry(root,width=80)
    entry3.place(x=130,y=140)
    global entry4
    entry4=Entry(root,width=80)
    entry4.place(x=130,y=170)
    global entry5
    entry5=Entry(root,width=80)
    entry5.place(x=130,y=200)
    global entry6
    entry6=Entry(root,width=80)
    entry6.place(x=130,y=230)
    global entry7
    entry7=Entry(root,width=80)
    entry7.place(x=130,y=260)
    global entry8
    entry8=Entry(root,width=80)
    entry8.place(x=130,y=290)
    global entry9
    entry9=Text(root,width=60,height=1)
    entry9.place(x=130,y=320)
    button1=Button(root,text="Total",width=10,command=total)
    button1.place(x=130,y=350)
    button2=Button(root,text="Submit",width=10,command=submit)
    button2.place(x=330,y=350)
    button3=Button(root,text="Exit",width=10,command=close)
    button3.place(x=535,y=350)
    root.mainloop()
def closeA():
    conn.commit()
    conn.close()
    rootA.destroy()
def afterlogin():
    username=str(entry11.get())
    password=str(entry12.get())
    if(username=="iamjrkoo6" and password=="6998"):
        messagebox.showinfo("Success","Login Successful!!!")
        rootA.destroy()
        login()
    else:
        messagebox.showerror("Error","Invalid username or password!!")
        
rootA=Tk(className=" Expense 2018")
rootA.config(width=500,height=250,bg="Cyan")
label11=Label(rootA,text="Expense 2018",fg="Blue",bg="Cyan",font=('Comic Sans MS',30,'bold'))
label11.place(x=125,y=10)
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
