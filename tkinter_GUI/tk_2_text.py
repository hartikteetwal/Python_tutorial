from tkinter import *

teetwal_root = Tk()

# "Width x height"                   ---> order of geometry
teetwal_root.geometry("733x445")

# width,height                     ---> order of minsize , Use to lock window in limited minimum frame
teetwal_root.minsize(500,300)

# width,height                     ---> order of maxsize , Use to lock window in limited maximum frame
teetwal_root.maxsize(800,400)

# label --->    This  is widget implements a display box where you can place text or images.
hartik = Label(text = "welcome to pycharm")
hartik.pack()

teetwal_root.mainloop()










