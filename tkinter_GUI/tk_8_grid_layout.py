from tkinter import *

def greet():
    print(f'The use name is {Uservalue.get()}')
    print(f'The user password is {Passwordvalue.get()}')
    with open('record.txt','a') as f:
        f.write(f'{Uservalue.get()},{Passwordvalue.get()}\n')                                            
        f.close()

root = Tk()
root.geometry('633x291')
User = Label(text='Username')
Password = Label(text='Password')
User.grid()
Password.grid(row=1)

# ---> classes in tkintery
# 1. BooleanVar
# 2. DoubleVar
# 3. IntVar
# 4. StringVar

Uservalue = StringVar()
Passwordvalue = StringVar()

Userentry = Entry(root,textvariable=Uservalue)
Passwordentry = Entry(root,textvariable=Passwordvalue)

Userentry.grid(row=0,column=1)
Passwordentry.grid(row=1,column=1)

Button(text='Submit',fg='red',command=greet).grid()


root.mainloop()