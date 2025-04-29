from tkinter import*
import tkinter.messagebox as tmsg


def rating():
    if myslider2.get()==0:
        feed = "very bad"
        print(feed)    
    elif myslider2.get()==1:
        feed = "bad"
        print(feed)
    elif myslider2.get()==2:
        feed = "not bad"
        print(feed)
    elif myslider2.get()==3:
        feed = "good"
        print(feed)
    elif myslider2.get()==4:
        feed = "very good"
        print(feed)
    else:
        feed = "excellent"
        tmsg.showinfo(title = 'thank you',message = "go to playstore and give rating")
        print(feed)
    
    with open("rating.txt","a") as f:
        f.write(f"\nmy rating for this game is {feed}")
        f.close()

    return 0

root = Tk()

root.geometry('555x333')
root.title('slider tutorial')



# myslider = Scale(root,from_=0,to=555)
# myslider.pack()
f1 = Frame(root,border=4,bg='grey',relief=SUNKEN)
f1.pack()
Label(f1,text='my game is bgmi, is you want to give rating ?').pack()
myslider2 = Scale(root,from_=0,to=5,orient=HORIZONTAL,tickinterval=1)
Button(root,text = "cancle",border=7,command=exit).pack()
myslider2.set(34)
myslider2.pack()
Button(root,text="submit",border=8,relief="raised",command=rating,bg='red').pack()

root.mainloop()