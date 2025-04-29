from tkinter import*
import tkinter.messagebox as tmsg
def order():
    tmsg.showinfo(title='flipkart_info',message=f'your order {var.get()} is booked now thanks for order',)
    with open('order.txt','a') as f:
        f.write(f"\nyour order {var.get()} is booked now")
        f.close()


root = Tk()
root.geometry("445x323")
root.title("radio button")

l1 = ['dosa','paratha','samosa','idly','roti','panipuri','😍']
a = len(l1)
var =StringVar()
var.set('dosa')
Label(root,text="what do you like to have sir",justify=LEFT,padx=14,font="lucida 19 bold").pack()
for i in range (a):
    radio = Radiobutton(root,text=l1[i],padx=14,variable=var,value=l1[i]).pack(anchor='w')

Button(text='order now',command=order).pack()

root.mainloop()