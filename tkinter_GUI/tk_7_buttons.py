from tkinter import *
root = Tk()
root.geometry('444x233')

def hello():
    print('hello tkinter button')
def name ():
    print('my name is hartik')

f1 = Frame(root,borderwidth=4,bg='grey',relief=SUNKEN)
f1.pack(side=LEFT,anchor=NW)

b1 = Button(f1,fg='red',text='greet',padx=23,command=hello)
b1.pack(side=LEFT,padx=2)

b2 = Button(f1,fg='red',padx=23,text='name',command=name)
b2.pack(side=LEFT,padx=2)

b3 = Button(f1,fg='red',text='3',padx=23)
b3.pack(side=LEFT,padx=2)

b4 = Button(f1,fg='red',text='4',padx=23)
b4.pack(side=LEFT,padx=2)

b5 = Button(f1,fg='red',text='5',padx=23)
b5.pack(side=LEFT,padx=2)

root.mainloop()