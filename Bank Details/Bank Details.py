from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import *
from datetime import *
conn=pymysql.connect(host="localhost",user="root",passwd="ILoveYouRehanaKazi",database="my_statements")
cursor=conn.cursor()
def optionSelected(value):
    global typ
    typ=str(value)
def submit():
    particulars=str(entry3.get())
    cheque=str(entry4.get())
    debit=float(entry5.get())
    credit=float(entry6.get())
    balance=float(entry7.get())
    branch=str(entry8.get())
    s=list()
    x=str(entry1.get('0.0',END))
    x=x.partition("\n")
    x=str(x[0])
    s.append(x)
    s.append(typ)
    s.append(particulars)
    s.append(cheque)
    s.append(debit)
    s.append(credit)
    s.append(balance)
    s.append(branch)
    try:
        cursor.execute("INSERT INTO RECORDS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))
        cursor.execute("SELECT * FROM RECORDS WHERE DATES=%s",(s[0]))
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
    root=Tk(className=" Account Statements")
    root.config(width=650,height=420,bg="Cyan")
    label1=Label(root,text="Account Statements",fg="Blue",bg="Cyan",font=('Comic Sans MS',30,'bold'))
    label1.place(x=150,y=10)
    label2=Label(root,text="Date:",bg="Cyan",font=('monospace',10,'bold'))
    label2.place(x=20,y=80)
    label3=Label(root,text="Type:",bg="Cyan",font=('monospace',10,'bold'))
    label3.place(x=20,y=110)
    label4=Label(root,text="Particulars:",bg="Cyan",font=('monospace',10,'bold'))
    label4.place(x=20,y=140)
    label5=Label(root,text="Cheque No:",bg="Cyan",font=('monospace',10,'bold'))
    label5.place(x=20,y=170)
    label6=Label(root,text="Debit:",bg="Cyan",font=('monospace',10,'bold'))
    label6.place(x=20,y=200)
    label7=Label(root,text="Credit:",bg="Cyan",font=('monospace',10,'bold'))
    label7.place(x=20,y=230)
    label8=Label(root,text="Balance:",bg="Cyan",font=('monospace',10,'bold'))
    label8.place(x=20,y=260)
    label9=Label(root,text="Branch:",bg="Cyan",font=('monospace',10,'bold'))
    label9.place(x=20,y=290)
    label10=Label(root,text="Developed by JK",fg="Blue",font=('Comic Sans MS',20,'bold','italic'),bg="Cyan")
    label10.place(x=200,y=370)
    global entry1
    entry1=Text(root,width=60,height=1)
    x=date.today()
    x=x.strftime("%d %B %Y")
    entry1.insert(END,x)
    entry1.place(x=130,y=80)
    global entry2
    optionlist=["Select","Transfer","","POS","ATM","Cheque","NEFT"]
    opt_value=StringVar()
    opt_value.set(optionlist[0])
    entry2=OptionMenu(root,opt_value,*optionlist,command=optionSelected)
    entry2.place(x=130,y=105)
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
    button1=Button(root,text="Submit",width=10,command=submit)
    button1.place(x=130,y=350)
    button2=Button(root,text="Exit",width=10,command=close)
    button2.place(x=535,y=350)
    root.mainloop()
def closeA():
    conn.commit()
    conn.close()
    rootA.destroy()
def afterlogin():
    username=str(entry11.get())
    password=str(entry12.get())
    if(username=="60180594894" and password=="3786"):
        messagebox.showinfo("Success","Login Successful!!!")
        rootA.destroy()
        login()
    else:
        messagebox.showerror("Error","Invalid username or password!!")
        
rootA=Tk(className=" Account Statements")
rootA.config(width=500,height=250,bg="Cyan")
label11=Label(rootA,text="Account Statements",fg="Blue",bg="Cyan",font=('Comic Sans MS',30,'bold'))
label11.place(x=50,y=10)
label12=Label(rootA,text="Account Number:",bg="Cyan",font=('monospace',10,'bold'))
label12.place(x=20,y=80)
label13=Label(rootA,text="Pin:",bg="Cyan",font=('monospace',10,'bold'))
label13.place(x=20,y=110)
label14=Label(rootA,text="Developed by JK",fg="Blue",font=('Comic Sans MS',20,'bold','italic'),bg="Cyan")
label14.place(x=150,y=200)
entry11=Entry(rootA,width=50)
entry11.place(x=140,y=80)
entry12=Entry(rootA,width=50,show='*')
entry12.place(x=140,y=110)
button11=Button(rootA,text="Login",width=10,command=afterlogin)
button11.place(x=140,y=150)
button12=Button(rootA,text="Exit",width=10,command=closeA)
button12.place(x=365,y=150)
rootA.mainloop()
