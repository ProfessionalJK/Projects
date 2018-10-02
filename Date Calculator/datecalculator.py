from datetime import *
from dateutil import *
from tkinter import *
root=Tk(className=" Date Calculator")
label1=Label(root,text="Date Calculator",bg="Cyan",font=('Times New Roman',10,'bold','italic'),fg="Blue")
label1.place(x=120,y=5)
label2=Label(root,text="Start date (yyyy mm dd hh mm ss)",bg="Cyan")
label2.place(x=10,y=30)
entry1=Entry(root)
entry1.place(x=200,y=30)
label3=Label(root,text="End date (yyyy mm dd hh mm ss)",bg="Cyan")
label3.place(x=10,y=55)
entry2=Entry(root)
entry2.place(x=200,y=55)
def buttonPressed1():
    d1=str(entry1.get()).split()
    d1=datetime(int(d1[0]),int(d1[1]),int(d1[2]),int(d1[3]),int(d1[4]),int(d1[5]))
    d2=str(entry2.get()).split()
    d2=datetime(int(d2[0]),int(d2[1]),int(d2[2]),int(d2[3]),int(d2[4]),int(d2[5]))
    difference = relativedelta.relativedelta(d2, d1)
    years = difference.years
    months = difference.months
    days = difference.days
    hours = difference.hours
    minutes = difference.minutes
    seconds = difference.seconds
    differ_days=(d2-d1).days
    label4["text"]="Years= "+str(years)
    label5["text"]="Months= "+str(months)
    label6["text"]="Days= "+str(days)
    label7["text"]="Hours= "+str(hours)
    label8["text"]="Minutes= "+str(minutes)
    label9["text"]="Seconds= "+str(seconds)
    label10["text"]="Total Days= "+str(differ_days)
button1=Button(root,text="Calculate",command=buttonPressed1,bg="White")
button1.place(x=130,y=80)
label4=Label(root,text="",fg="Blue",bg="Cyan",font=('Times New Roman',10,'bold','italic'))
label4.place(x=10,y=110)
label5=Label(root,text="",fg="Blue",bg="Cyan",font=('Times New Roman',10,'bold','italic'))
label5.place(x=10,y=130)
label6=Label(root,text="",fg="Blue",bg="Cyan",font=('Times New Roman',10,'bold','italic'))
label6.place(x=10,y=150)
label7=Label(root,text="",fg="Blue",bg="Cyan",font=('Times New Roman',10,'bold','italic'))
label7.place(x=10,y=170)
label8=Label(root,text="",fg="Blue",bg="Cyan",font=('Times New Roman',10,'bold','italic'))
label8.place(x=10,y=190)
label9=Label(root,text="",fg="Blue",bg="Cyan",font=('Times New Roman',10,'bold','italic'))
label9.place(x=10,y=210)
label10=Label(root,text="",fg="Blue",bg="Cyan",font=('Times New Roman',10,'bold','italic'))
label10.place(x=10,y=230)
label11=Label(root,text="Developed by JK",fg="Blue",font=('Comic Sans MS',20,'bold','italic'),bg="Cyan")
label11.place(x=50,y=270)
root.config(bg="Cyan",height=333,width=333)
root.mainloop()
