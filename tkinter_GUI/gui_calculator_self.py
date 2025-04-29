from tkinter import*
# 
expression = ''
def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)
    # 
def clear():
    global expression
    expression = ''
    equation.set('')
# 
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression =''
    except:
        equation.set('error')
        expression=''
# 
if __name__ == '__main__':
    root = Tk()
    root.title('simple calculator')
    root.wm_iconbitmap('1.ico')
    root.geometry('270x150')
    equation = StringVar()
    expression_field = Entry(root,textvariable=equation)
    expression_field.grid(columnspan=4,ipadx=70)
# 
Button(root,text="1",command=lambda: press(1),height=1,width=7).grid(row =2,column=0)
Button(root,text="2",command=lambda: press(2),height=1,width=7).grid(row =2,column=1)
Button(root,text="3",command=lambda: press(3),height=1,width=7).grid(row =2,column=2)
Button(root,text="+",command=lambda: press('+'),height=1,width=7).grid(row =2,column=3)
Button(root,text="4",command=lambda: press(4),height=1,width=7).grid(row =3,column=0)
Button(root,text="5",command=lambda: press(5),height=1,width=7).grid(row =3,column=1)
Button(root,text="6",command=lambda: press(6),height=1,width=7).grid(row =3,column=2)
Button(root,text="-",command=lambda: press('-'),height=1,width=7).grid(row =3,column=3)
Button(root,text="7",command=lambda: press(7),height=1,width=7).grid(row =4,column=0)
Button(root,text="8",command=lambda: press(8),height=1,width=7).grid(row =4,column=1)
Button(root,text="9",command=lambda: press(9),height=1,width=7).grid(row =4,column=2)
Button(root,text="*",command=lambda: press('*'),height=1,width=7).grid(row =4,column=3)
Button(root,text="0",command=lambda: press(0),height=1,width=7).grid(row =5,column=0)
Button(root,text="clear",command=clear,height=1,width=7).grid(row =5,column=1)
Button(root,text="=",command=equalpress,height=1,width=7).grid(row =5,column=2)
Button(root,text="/",command=lambda: press("/"),height=1,width=7).grid(row =5,column=3)
Button(root,text=".",command=lambda: press("."),height=1,width=7).grid(row =6,column=0)
# 
root.mainloop()

exit()
from tkinter import*
import tkinter.messagebox as tmsg
scvalue =''
def click(event):
    text = event.widget.cget('text')
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                v = e
                value = 'error'
                screen.update()
        scvalue.set(value)
        if value == 'error':
            tmsg.showerror('warning',v)
        screen.update()
    elif text =='C':
        scvalue.set('')
        screen.update()

    elif text =='❌':
        new_list = [i for i in scvalue.get() if scvalue.get() != '']
        new_list.pop(-1)
        s = ''.join([str(i) for i in new_list])
        scvalue.set(s)
        screen.update()
    
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root = Tk()
# root.geometry('300x150')
scvalue = StringVar()
scvalue.set('')
screen = Entry(root,textvariable=scvalue,font = 'lucida 25 bold')
screen.pack(fill=X)

f = Frame(root)
b = Button(f,text='9',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='8',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='7',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='+',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

f.pack(pady=8)
f = Frame(root)
b = Button(f,text='6',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='5',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='4',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='-',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

f.pack(pady=8)
f = Frame(root)
b = Button(f,text='3',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='2',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='1',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='*',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)

f.pack(pady=8)
f = Frame(root)
b = Button(f,text='C',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='0',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='❌',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)
b = Button(f,text='/',height=2,width=8)
b.pack(side=LEFT,padx=8)
b.bind('<Button-1>',click)


f.pack(pady=8)

f = Frame(root)
b = Button(f,text='=',height=2)
b.pack(fill=X,padx=25)
b.bind('<Button-1>',click)
f.pack(fill=X)



root.mainloop()
