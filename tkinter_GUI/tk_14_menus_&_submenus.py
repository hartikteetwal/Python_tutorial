from tkinter import *
root = Tk()

root.geometry('733x566')
root.title('Pycharm')

def myfunc():
    print('main ek bhot hi natkhat aur shaitaan function hu')


## ---> use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label='file',command=myfunc)
# mymenu.add_command(label='Exit',command=quit)
# root.config(menu=mymenu)


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
Mainmenu.add_cascade(label='Edit',menu=m2)
root.config(menu=Mainmenu)



root.mainloop()