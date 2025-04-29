from tkinter import*
root = Tk()
def resize():
    print("updateing the gui")
    root.geometry(f"{width.get()}x{height.get()}")
    
    # ----> self
    data=StringVar(value=f"{width.get()}x{height.get()}")
    Label(text='now your gui is').grid(row=4,column=0)
    Label(root,textvariable=data).grid(row =4,column=1)
    # Entry(root,textvariable=data).grid(row=4,column=1)

root.geometry("220x120")
root.title('resize gui')

Label(text='RESIZE GUI',font='elephant',fg='red').grid(column=1,row=0)
width = StringVar()
height = StringVar()
Label(text='width').grid(row=1,column=0,padx=15)
Entry(root,textvariable=width).grid(row=1,column=1)
Label(text='height').grid(row=2,column=0)
Entry(root,textvariable=height).grid(row=2,column=1)
Button(text='apply',command=resize,bg='grey').grid(row=3,column=1)

root.mainloop()