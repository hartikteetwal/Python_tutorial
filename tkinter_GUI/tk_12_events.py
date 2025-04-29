from tkinter import*
root = Tk()

def hartik(event):
    print(f'thank you {event.x},{event.y}')

root.title('events in tkinter')
root.geometry('667x200')

Widget = Button(text='x',fg = 'red')
Widget.pack(side=RIGHT,anchor=N)
Widget.bind('<Double-1>',quit)

Widget = Button(text='click here on button at',fg = 'red')
Widget.pack()
Widget.bind('<Button-1>',hartik)


root.mainloop()