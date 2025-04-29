from tkinter import *
root = Tk()
root.geometry('744x233')
root.title('My GUI with Hartik')

# ---> Important label option 
# text --> adds the text
# bg --> background
# fg --> foreground
# font ---> sets the font     1. font=('Bell MT',12,'bold'),   2. font='Broadway 12 bold'
# padx --> x padding
# pady --> y padding
# relief --> border styling(SUNKEN,RAISED,GROOVE,RIDGE)

title_label = Label(text = '''Salman Salim Abdul Rashid Khan is an Indian actor, \nfilm producer, writer and television personality who works predominantly in Hindi films.\n In a film career spanning over thirty five years, Khan has received numerous awards,\n including two National Film Awards as a film producer, and two Filmfare Awards as an actor.[3] \nHe is cited in the media as one of the most ''',bg='red',fg='white',padx=23,pady=44,font='elephant 8 bold',borderwidth=8,relief=RIDGE)

# ---> Important pack options
# anchor = 'nw'(northwast), 'ne'(northeast)
# side = BOTTOM,TOP,LEFT,RIGHT
# fill 
# padx
# pady


title_label.pack(side='bottom',anchor='nw',fill=X ,padx=34,pady=56)
root.mainloop()
