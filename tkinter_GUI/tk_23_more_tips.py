from tkinter import*
root = Tk()
root.geometry("555x344")
root.title('title of my gui')
root.wm_iconbitmap('1.ico')
root.configure(background='light grey')

Width = root.winfo_screenwidth()
height = root.winfo_screenwidth()

print(f"{Width}x{height}")
Button(text='close',command=root.destroy).pack()

root.mainloop()