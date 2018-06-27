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
