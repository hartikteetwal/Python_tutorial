from tkinter import *

# ---> for png images
img_root = Tk()
img_root.title('png')
img_root.geometry("315x394")
photo = PhotoImage(file = "hartik.png")
image_label = Label(image = photo)
image_label.pack() 
img_root.mainloop()




#---> for jpg images
from PIL import Image,ImageTk
img_root = Tk()
img_root.title('jpg')
img_root.geometry("400x533")
image = Image.open("hartik.jpg")
photo = ImageTk.PhotoImage(image)
image_label = Label(image = photo)
image_label.pack() 
img_root.mainloop()