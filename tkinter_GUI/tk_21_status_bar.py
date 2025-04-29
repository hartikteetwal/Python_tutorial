from tkinter import*

def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(3)
    statusvar.set('Ready now')

root = Tk()
root.geometry("555x345")
root.title("status_bar")

statusvar = StringVar()
statusvar.set('Ready')
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor='w')
sbar.pack(side=BOTTOM,fill=X)
Button(root,text='Upload',command=upload).pack()
root.mainloop()