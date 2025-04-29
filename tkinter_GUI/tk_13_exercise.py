from tkinter import*
from PIL import ImageTk,Image

def every_100(text):
    final_text = ''
    for i in range (0,len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text+='\n'
    return final_text




root  = Tk()

root.title("hartik's news - Aapka apna akhabaar")
root.geometry('900x800')

texts =  []
photos = []
for i in range(0,3):
    with open(f'{i+1}.txt') as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f'{i+1}.png')
    #TODO resize these images
    image = image.resize((200,200),Image.ANTIALIAS)


    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width=800,height=70)
Label(f0,text="Hartik's News",font='lucida 33 bold').pack()
Label(f0,text='August, 23, 2023',font='lucida 13 bold').pack()
f0.pack()



f1 = Frame(root,width=900,height=100)
Label(f1,text=texts[0],padx=39,pady=5).pack(side='left')
Label(f1,image=photos[0],anchor='e',padx=450).pack()
f1.pack(anchor='w')


f2 = Frame(root,width=900,height=100,padx=39)
Label(f2,text=texts[1],padx=39,pady=22).pack(side='right')
Label(f2,image=photos[1],anchor='e',height=150).pack()
f2.pack(anchor='w')

f3 = Frame(root,width=900,height=100)
Label(f3,text=texts[2],padx=20,pady=22).pack(side='left')
Label(f3,image=photos[2],anchor='e',height=150,padx=300).pack()
f3.pack(anchor='w')

root.mainloop()
