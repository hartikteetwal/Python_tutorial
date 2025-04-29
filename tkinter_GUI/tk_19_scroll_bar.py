from tkinter import*
root = Tk()
root.geometry("455x333")
root.title("scroll_bar")

# for connecting scrollbar to a Widget
# 1. Widget(yscrollcommand = Scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(root,yscrollcommand = scrollbar.set)
for i in range (334):
    listbox.insert(END,f'item {i}')
listbox.pack()
scrollbar.config(command=listbox.yview)

root.mainloop()