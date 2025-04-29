from tkinter import *
root = Tk()
root.title('hartik ka gui')
Canvas_width = 800
Canvas_height = 400

root.geometry(f'{Canvas_width}x{Canvas_height}')

Can_widget = Canvas(width=Canvas_width,height=Canvas_height)
Can_widget.pack()

# the line goes from x1,y1 to x2,y2
Can_widget.create_line(0,0,800,400,fill='red')
Can_widget.create_line(800,0,0,400,fill='red')

# to create a rectengule with specify perameters in this order - coor of top left and coors of bottom right
Can_widget.create_rectangle(100,50,700,350,fill='light blue')

# to creat_oval
Can_widget.create_oval(100,50,700,350,fill='red')

# to creat_text 
Can_widget.create_text(400,200,text='hartik',)


root.mainloop()