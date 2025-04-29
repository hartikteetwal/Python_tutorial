from tkinter import *
root = Tk()
root.title('project pycharm')

root.geometry('544x234')
f1 = Frame(root,bg='grey',borderwidth=8,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

f2 = Frame(root,bg='red',borderwidth=12,relief=GROOVE)
f2.pack(side=TOP,fill = X)
L1 = Label(f2,text='Welcome to subline text',font='elephant 23 bold',fg='blue',bg= 'red')
L1.pack()

f3 = Frame(root,bg='white',borderwidth=12,relief=GROOVE)
f3.pack(side=TOP,fill = X)

photo = PhotoImage(file='hartik.png')
L1 = Label(f3,image=photo)
L1.pack()



L1 = Label(f1,text='project tkinter - pycharm')
L1.pack(pady=142)
root.mainloop()