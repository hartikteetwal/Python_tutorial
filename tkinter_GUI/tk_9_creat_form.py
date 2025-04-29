from tkinter import *
root = Tk()

def getvels():
    print('your form has been submit')

root.geometry('666x458')
root.minsize(300,300)
root.maxsize(600,500)

# heading with frame
f2 = Frame(root,bg='red',borderwidth=12,relief=GROOVE)
f2.grid(row=0,column=3)
L1 = Label(f2,text='Welcome to layout',font='elephant 23 bold',fg='blue',bg= 'red')
L1.grid()

# text for our form
name = Label(text='Name',border=4,relief='raised',bg='red',fg='blue')
phone = Label(text='phone',border=4,relief='raised',bg='red',fg='blue')
gender = Label(text='gender',border=4,relief='raised',bg='red',fg='blue')
emergency = Label(text='emergency',border=4,relief='raised',bg='red',fg='blue')
paymentmode = Label(text='paymentmode',border=4,relief='raised',bg='red',fg='blue')

# pack our form with the help of grid
name.grid(row=1,column=0)
phone.grid(row=2,column=0)
gender.grid(row=3,column=0)
emergency.grid(row=4,column=0)
paymentmode.grid(row=5,column=0)

# tkinter Variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# entries for our forms
nameentry = Entry(root,textvariable=namevalue,border=4,relief='raised')
phoneentry = Entry(root,textvariable=phonevalue,border=4,relief='raised')
genderentry = Entry(root,textvariable=gendervalue,border=4,relief='raised')
emergencyentry = Entry(root,textvariable=emergencyvalue,border=4,relief='raised')
paymentmodeentry = Entry(root,textvariable=paymentmodevalue,border=4,relief='raised')

# packing the entries with the help of grid
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# checkbox & packing
foodservice = Checkbutton(text='want to prebook your mals?',bg='red',fg='blue',variable=foodservicevalue)
foodservice.grid(row=6,column=3)

# Button & packing it and assigning it a 
Button(text='submit my form',command = getvels,border=8,relief=RAISED,fg='red').grid(pady=15,row=7,column=3)


root.mainloop()
