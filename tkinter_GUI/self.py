from tkinter import*
def click(event):
    pass
root = Tk()
root.geometry("345x345")
S = StringVar()
E = Entry(textvariable=S,font='lucida 30 bold')
E.pack(padx=10,pady=10,fill=X,ipadx=34)

f = Frame(root)
b = Button(f,text='9',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='8',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='7',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='+',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
f.pack()
f = Frame(root)
b = Button(f,text='6',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='5',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='4',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='-',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
f.pack()
f = Frame(root)
b = Button(f,text='3',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='2',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='1',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='*',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
f.pack()
f = Frame(root)
b = Button(f,text='C',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='0',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='=',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='/',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
f.pack()

root.mainloop()


exit()
from tkinter import*
from PIL import Image,ImageTk
import os
root = Tk()
root.geometry("445x388")
Label(root,text='Login Page',font='elephant 24 bold').grid(row=0,column=0,padx=53)
Label(root,text='Username').grid(row=1,column=0)
Label(root,text='Password').grid(row=2,column=0)
Entry(root,textvariable=StringVar()).grid(row=1,column=1)
Entry(root,textvariable=StringVar()).grid(row=2,column=1)
root.mainloop()

exit()
from tkinter import*
def new_file():
    pass
def openfile():
    pass
def savefile():
    pass
def quitapp():
    exit()
def copy():
    pass
def cut():
    pass
def paste():
    pass
def helpmenu():
    pass
def rate_as():
    pass
def aboutmenu():
    pass

root = Tk()
root.wm_iconbitmap('1.ico')
root.geometry('345x222')
mymenu = Menu(root)
m1 = Menu(mymenu,tearoff=0)
m1.add_command(label='New File',command=new_file)
m1.add_command(label='Open',command=openfile)
m1.add_separator()
m1.add_command(label='Save',command=savefile)
m1.add_command(label='Exit',command=quitapp)
mymenu.add_cascade(menu=m1,label='File')

m2 = Menu(mymenu,tearoff=0)
m2.add_command(label='Copy',command=copy)
m2.add_command(label='Paste',command=paste)
m2.add_command(label='cut',command=cut)
mymenu.add_cascade(menu=m2,label='File')

m3 = Menu(mymenu,tearoff=0)
m3.add_command(label='Help',command=helpmenu)
m3.add_command(label='Rate as',command=rate_as)
m3.add_command(label='About',command=aboutmenu)
mymenu.add_cascade(menu=m3,label='Help')
root.config(menu=mymenu)
root.mainloop()

exit()
from tkinter import*
import tkinter.messagebox as tmsg

def help():
    tmsg.showinfo("Help-GUI","How can help you sir?")
def rate():
    tmsg.showinfo("Rate-GUI","Please goto playstore page give rate and share your exprience")
def about():
    with open('1.txt') as f:
        a = f.read()
        f.close
    tmsg.showinfo('about-GUI',a)

def rate():
    pass
root = Tk()
root.geometry('555x364')
root.title('menus')
mymenu = Menu(root)
m1 = Menu(mymenu,tearoff=0)
m1.add_command(label='New Project')
m1.add_command(label='Open')
m1.add_separator()
m1.add_command(label='Save')
m1.add_command(label='Save as')
mymenu.add_cascade(label='File',menu=m1)
root.config(menu=mymenu)

m2 = Menu(mymenu,tearoff=0)
m2.add_command(label='Copy')
m2.add_command(label='Paste')
m2.add_command(label='Cut')
m2.add_separator()
m2.add_command(label='Unod')
m2.add_command(label='Redo')
mymenu.add_cascade(label='Edit',menu=m2)

m3 = Menu(mymenu,tearoff=0)
m3.add_command(label='help',command=help)
m3.add_command(label='Rate us',command=rate)
m3.add_command(label='About',command=about)
mymenu.add_cascade(label='Help',menu=m3)
root.config(menu=mymenu)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text = Text(root,yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)


exit()
from tkinter import*
import tkinter.messagebox as tmsg
def yes(event):
    tmsg.showinfo('Login Sussecful','Yes! My name is hartik')
root = Tk()
root.geometry('555x367')
root.title('event')
Label(root,text='Hartik',bg='red',fg='blue',font=('script 33 bold')).pack()
b = Button(root,text='Verify')
b.pack()
b.bind('<Button-1>',yes)
b2 = Button(root,text='Exit',bg='red',fg='blue')
b2.pack()
b2.bind('<Double-1>',quit)


root.mainloop()

exit()
from tkinter import*
import tkinter.messagebox as tmsg
def submit():
    print(namevalue.get())
    if chack.get()==0:
        tmsg.showinfo('Note','Please check the check the chackbox')
    elif namevalue.get() == '':
        tmsg.showinfo('Note','Please enter your name')
    elif gendervalue.get() == '':
        tmsg.showinfo('Note','Please enter your gender')
    elif rollvalue.get() == '':
        tmsg.showinfo('Note','Please enter your roll no')
    elif phonevalue.get() == '':
        tmsg.showinfo('Note','Please enter your phone no.')
    else:
        tmsg.showinfo('Note','Your form has been submitted')
        with open('record.txt','a') as f:
            f.write(f'name = {namevalue.get()}, gender = {gendervalue.get()}, roll no = {rollvalue.get()}, phone no = {phonevalue.get()}')
            f.close()
        
root = Tk()
root.geometry('744x534')
root.title('form')
Label(text="My first form",bg='blue',font='arial 17 bold').grid(column=1,row=0)
Label(text='name',fg='red',font='elephant 12 bold').grid(column=0,row=1)
Label(text='roll  no',fg='red',font='elephant 12 bold').grid(column=0,row=2)
Label(text='gender',fg='red',font='elephant 12 bold').grid(column=0,row=3)
Label(text='phone no',fg='red',font='elephant 12 bold').grid(column=0,row=4)

namevalue = StringVar()
rollvalue = StringVar()
gendervalue = StringVar()
phonevalue = StringVar()
chack = IntVar()

Entry(root,bg='light grey',border=4,textvariable=namevalue).grid(column=1,row=1)
Entry(root,bg='light grey',border=4,textvariable=rollvalue).grid(column=1,row=2)
Entry(root,bg='light grey',border=4,textvariable=gendervalue).grid(column=1,row=3)
Entry(root,bg='light grey',border=4,textvariable=phonevalue).grid(column=1,row=4)
Checkbutton(root,text='are you 18 year old',bg='pink',fg='green',variable=chack).grid(column=1,row=5)

Button(root,text='Submit',command=submit,padx=41).grid(column=1,row=6,pady=3)
root.mainloop()

exit()
from tkinter import*
import tkinter.messagebox as tmsg
def submit():
    print(f'my name is {user_value.get()}')
    print(f'my password is {password_value.get()}')
    with open('record.txt','a') as f:
        f.write(f'my name is {user_value.get()} and'f'my password is {password_value.get()}')

root = Tk()
root.geometry('744x534')
root.title('button')
user = Label(text='user name')
password = Label(text="Password")
user.grid()
password.grid(row=1)

user_value = StringVar()
password_value = StringVar()

user_entry = Entry(root,textvariable=user_value)
password_entry = Entry(root,textvariable=password_value)
user_entry.grid(row=0,column=1)
password_entry.grid(row=1,column=1)
Button(root,text='Submit',border=6,command=submit).grid(row=2,column=1)
root.mainloop()

exit()
from tkinter import*
root = Tk()
root.geometry('345x333')
root.title('frames')
f = Frame(root,border=4,bg='grey',relief=SUNKEN,width=165)
Label(f,text='project 1 hartik image',bg='red').pack()
f.pack(side=LEFT,fill=Y)
f1 = Frame(root,borderwidth=34,relief='sunken')
Label(f1,text="welcome to hartik's code",font='elephent 15 bold').pack()
f1.pack(fill=X)
f2 = Frame(root,borderwidth=7,relief=SUNKEN,bg='pink')
img = PhotoImage(file ='hartik.png')
Label(f2,image=img).pack()
f2.pack(side='top',fill=X)
root.mainloop()

exit()
from tkinter import*
root = Tk()
root.geometry('345x567')
root.title('hello word')
Label(text='hello word',bg='red',fg='white',relief=SUNKEN,padx=45,font='elephent 23 bold').pack(fill=X,anchor=NW)
root.mainloop()


exit()
from tkinter import*
from PIL import Image,ImageTk
root = Tk()
root.title("image")
root.geometry('444x234')
idmage = ImageTk.PhotoImage(Image.open('hartik.jpg'))
Label(image=idmage).pack()
# Label(text = "My name is hartik",font='elephent 13 bold').pack()
root.mainloop()

