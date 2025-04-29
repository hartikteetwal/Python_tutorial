from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry('433x366')
root.title('Notepad')

def myfunc():

    print('main ek bhot hi natkhat aur shaitaan function hu')

def help():
    print('I Will Help You')
    a =tmsg.showinfo(title='Help',message='Hartik can help you with this gui')

def rate():
    print('Rate us')
    a = tmsg.askquestion('Raiting','I hope your exprience is good')
    if a == 'yes':
        msg = 'Great. Rate us on playstore'
    else:
        msg = 'Go to help box and show your problem'
    tmsg.showinfo('exprience',msg)


Mainmenu = Menu(root)

m1 = Menu(Mainmenu,tearoff=0)
m1.add_command(label='New project',command=myfunc)
m1.add_command(label='Save',command=myfunc)
m1.add_separator()
m1.add_command(label='Save As',command=myfunc)
m1.add_command(label='Print',command=myfunc)
Mainmenu.add_cascade(label='File',menu=m1)
root.config(menu=Mainmenu)

m2 = Menu(Mainmenu,tearoff=0)
m2.add_command(label='Copy',command=myfunc)
m2.add_command(label='Paste',command=myfunc)
m2.add_separator()
m2.add_command(label='Cut',command=myfunc)
m2.add_command(label='Find',command=myfunc)
Mainmenu.add_cascade(label='File',menu=m2)
root.config(menu=Mainmenu)

m3 = Menu(Mainmenu,tearoff=0)
m3.add_command(label='Help',command=help)
m3.add_command(label='Rate us',command=rate)
Mainmenu.add_cascade(label='Help',menu=m3)
root.config(menu=Mainmenu)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text = Text(root,yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)



root.mainloop()