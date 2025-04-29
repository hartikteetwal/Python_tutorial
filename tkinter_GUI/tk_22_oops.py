from tkinter import*
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("455x244")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.status = Label(self,textvariable=self.var,relief=SUNKEN,anchor='w').pack(side=BOTTOM,fill=X)

    def click(self):
        print("clicked button")

    def creatbutton(self,inptext):
        Button(text=inptext,command=self.click).pack()

if __name__=='__main__':
    window = GUI()
    window.status()
    window.creatbutton('press')
    window.mainloop()