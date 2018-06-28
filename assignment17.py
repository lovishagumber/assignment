#Q1
from tkinter import*
master=Tk()
frame=Frame(master,bg='pink')
frame.pack()
pinkbutton=Button(frame,text='hello world',fg='pink')
pinkbutton.pack(side=LEFT)
bluebutton=Button(frame,text='exit',fg='blue',command='exit')
bluebutton.pack(side=LEFT)
master.mainloop()
#Q2
from tkinter import *
master=Tk()
frame=Frame(master,bg='pink')
frame.pack()
def cmdl():
    lbl.config(text='hello world')
pinkbutton=Button(frame,text='click',fg='pink',command=cmdl)
pinkbutton.pack(side=LEFT)
bluebutton=Button(frame,text='exit',fg='blue',command=exit)
bluebutton.pack(side=LEFT)
lbl=Label(master,text='')
lbl.pack()
master.mainloop()

#Q3
from tkinter import *
master=Tk()
frame=Frame(master,bg='red')
frame.pack()
def cmdl():
    lbl.config(text='hello world')
redbutton=Button(frame,text='click',fg='red',command=cmdl)
redbutton.pack(side=LEFT)
purplebutton=Button(frame,text='exit',fg='purple',command=exit)
purplebutton.pack(side=LEFT)
lbl=Label(master,text='hello mr.X')
lbl.pack()
master.mainloop()

#Q4
from tkinter import *
master=Tk()
frame=Frame(master,bg='sky blue')
frame.pack()
Label(frame,text="First Name").grid(row=0)
Label(frame,text="Last Name").grid(row=1)
e1=Entry(frame)
e2=Entry(frame)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
def input():
    a=e1.get()
    b=e2.get()
    c=a+b
    lbl=Label(frame,text=c)
    lbl.grid(row=2,column=1)
    lbl.config(text=a+b)
bluebutton=Button(frame,text='click',fg='blue',command=input)
bluebutton.grid(row=3,column=1)
mainloop()
