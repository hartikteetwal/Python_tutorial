from tkinter import*
import tkinter.messagebox as tmsg
scvalue =''
def click(event):
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                value = 'error'
                screen.update()
        scvalue.set(value)
        if value == 'error':
            tmsg.showerror('warrning',"don't write wrong calculation")
        screen.update()

    elif text =='DEL':
        if scvalue.get()=='error':
            scvalue.set('')
            screen.update()
        else:
            new_list = [i for i in scvalue.get() if scvalue.get() != '']
            new_list.pop(-1)
            s = ''.join([str(i) for i in new_list])
            scvalue.set(s)
            screen.update()

    elif text=='C':
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root = Tk()
root.geometry("345x350")
root.title('my calculator')
root.wm_iconbitmap("2.ico")

scvalue  = StringVar()
scvalue.set('')
screen = Entry(root,textvariable=scvalue,font='lucida 30 bold')
screen.pack(fill=X,pady=10,padx=10,ipadx=8)

f1 = Frame(root)
b = Button(f1,text='9',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='8',height=2,width=9)
b.pack(side='left',padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='7',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='+',height=2,width=9,fg='blue')
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

f1.pack(pady=8) 

f1 = Frame(root)
b = Button(f1,text='6',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='5',height=2,width=9)
b.pack(side='left',padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='4',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='-',height=2,width=9,fg='blue')
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)


f1.pack(pady=8)

f1 = Frame(root)
b = Button(f1,text='3',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='2',height=2,width=9)
b.pack(side='left',padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='1',height=2,width=9)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='*',height=2,width=9,fg='blue')
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

f1.pack(pady=8)

f1 = Frame(root)
b = Button(f1,text='C',height=2,width=9,fg='white',bg='yellow')
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='0',height=2,width=9)
b.pack(side='left',padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text="DEL",height=2,width=9,fg='red')
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

b = Button(f1,text='/',height=2,width=9,fg='blue')
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

f1.pack(pady=8)

f1 = Frame(root)
b = Button(f1,text='=',height=2)
b.pack(fill=X,padx=7)
b.bind('<Button-1>',click)
f1.pack(fill=X)

root.mainloop()