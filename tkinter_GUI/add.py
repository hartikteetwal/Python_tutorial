from tkinter import *

def greet():
    print(Uservalue.get() + Passwordvalue.get())

root = Tk()
root.geometry('633x291')
User = Label(root,text='Username')
Password = Label(root,text='Password')
User.grid()
Password.grid(row=1)

# ---> classes in tkinter
# 1. BooleanVar
# 2. DoubleVar
# 3. IntVar
# 4. StringVar

Uservalue = IntVar()
Passwordvalue = IntVar()

Userentry = Entry(root,textvariable=Uservalue)
Passwordentry = Entry(root,textvariable=Passwordvalue)

Userentry.grid(row=0,column=1)
Passwordentry.grid(row=1,column=1)

Button(text='Submit',fg='red',command=greet).grid()


root.mainloop()