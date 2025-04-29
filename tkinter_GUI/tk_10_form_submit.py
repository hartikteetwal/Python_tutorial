from tkinter import *
root = Tk()

def getvels():

    print(f'{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}')

    if namevalue.get() == '':
        print('please enter your name: ')
    elif phonevalue.get() == '':
        print('please enter your phone number: ')
    elif gendervalue.get() == '':
        print('please enter your gender: ')
    elif emergencyvalue.get() == '':
        print('please enter emergency number: ')
    elif paymentmodevalue.get() == '':
        print('please enter payment method: ')
    elif foodservicevalue.get() ==  0:
        print('please check in the chechbox')
    else:
        print('your form has been submit')
        with open('record.txt','a') as f:
            f.write(f'{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get()}\n')
            f.close()



root.geometry('666x458')
root.minsize(300,300)
root.maxsize(600,500)

# heading with frame
f2 = Frame(root,bg='red',borderwidth=12,relief=GROOVE)
f2.grid(row=0,column=3)
L1 = Label(f2,text='Welcome to layout',font='elephant 23 bold',fg='blue',bg= 'red')
L1.grid()

# text for our form
name = Label(text='Name',border=4,relief='raised',bg='grey',fg='blue',padx=24)
phone = Label(text='phone',border=4,relief='raised',bg='grey',fg='blue',padx=23)
gender = Label(text='gender',border=4,relief='raised',bg='grey',fg='blue',padx=21.2)
emergency = Label(text='emergency',border=4,relief='raised',bg='grey',fg='blue',padx=10.2)
paymentmode = Label(text='paymentmode',border=4,relief='raised',bg='grey',fg='blue')

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
foodservice = Checkbutton(text='want to prebook your mals?',bg='grey',fg='blue',variable=foodservicevalue)
foodservice.grid(row=6,column=3)

# Button & packing it and assigning it a 
Button(text='submit my form',command = getvels,border=8,relief=RAISED,fg='red').grid(pady=15,row=7,column=3)


root.mainloop()
