import tkinter
from tkinter import *
root=Tk(className=" Interest Calculator")
root.config(width=400,height=350,bg="Cyan")
label1=Label(root,text="Interest Calculator",fg="Blue",bg="Cyan",font=('Comic Sans MS',10,'bold'))
label1.place(x=140,y=10)
label2=Label(root,text="Principal Amount:",fg="Blue",bg="Cyan")
label2.place(x=10,y=50)
entry1=Entry(root,width=20)
entry1.place(x=150,y=50)
label3=Label(root,text="Rate of Interest (%):",fg="Blue",bg="Cyan")
label3.place(x=10,y=80)
entry2=Entry(root,width=20)
entry2.place(x=150,y=80)
label4=Label(root,text="Time Period:",fg="Blue",bg="Cyan")
label4.place(x=10,y=110)
entry3=Entry(root,width=20)
entry3.place(x=150,y=110)
def optionSelected1(value):
    opt_value1=value
optionlist1=["Day(s)","Month(s)","Year(s)"]
opt_value1=StringVar()
opt_value1.set(optionlist1[0])
optionmenu1=OptionMenu(root,opt_value1,*optionlist1,command=optionSelected1)
optionmenu1.config(width=7)
optionmenu1.place(x=300,y=105)
label5=Label(root,width=15,height=1,text="Frequency:",fg="Blue",bg="Cyan")
label5.place(x=10,y=140)
def optionSelected2(value):
     opt_value2=value
optionlist2=["Simple Interest","Compunded Monthly","Compunded Quaterly","Compunded Half Yearly","Compunded Yearly"]
opt_value2=StringVar()
opt_value2.set(optionlist2[2])
optionmenu2=OptionMenu(root,opt_value2,*optionlist2,command=optionSelected2)
optionmenu2.config(width=20)
optionmenu2.place(x=130,y=135)
label6=Label(root,text="",fg="Black",bg="Cyan",font=('Andalus',10,'bold'))
label6.place(x=10,y=230)
label7=Label(root,text="",fg="Black",bg="Cyan",font=('Andalus',10,'bold'))
label7.place(x=10,y=260)
def buttonPressed1():
    os1=opt_value1.get()
    os2=opt_value2.get()
    p=float(entry1.get())
    r=float(entry2.get())
    r=float(r/100)
    t=float(entry3.get())
    if (os1=="Day(s)"):
        m=365
    elif (os1=="Month(s)"):
        m=12
    elif (os1=="Year(s)"):
        m=1
    if (os2=="Simple Interest"):
        n=0
    elif (os2=="Compunded Monthly"):
        n=12
    elif (os2=="Compunded Quaterly"):
        n=4
    elif (os2=="Compunded Half Yearly"):
        n=2
    elif (os2=="Compunded Yearly"):
        n=1   
    a=0
    if (t <= 90 and  m==365):
        n=0
    if (n==0):	#Simple interest
        a=float(p*(1+((r*t)/m)))
        a=a-p
    else:                   #Compound interest
        b=float(1+r/n)
        c=float((t*n/m))
        d=float(pow(b,c))
        a=p*d
        a=a-p
    a=round(a,2)
    k=str(a+p)
    label6["text"]="Maturity Value = ₹"+k
    a=str(a)
    label7["text"]="Intereset Earned = ₹"+a
button1=Button(root,width=10,text="CALCULATE",bg="blue",command=buttonPressed1)
button1.place(x=170,y=175)
label10=Label(root,width=15,height=1,text="Developed by JK",fg="Blue",bg="Cyan",font=('Comic Sans MS',15,'bold'))
label10.place(x=100,y=300)
root.mainloop()
