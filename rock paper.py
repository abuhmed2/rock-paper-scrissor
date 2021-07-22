from tkinter import *
import tkinter.font
import random
window =Tk()



window.geometry('1275x760')
window.title('ROCK PAPER SCISSORS')

window = Label(text='ROCK PAPER SCISSORS',font =100,fg = 'brown',width=50)

rock = Label(text='ROCK',fg='light blue')
paper = Label(text='PAPER',fg='red')
scissors = Label(text='SCISSORS',fg='light green')

important = Label(text='YOU PLAYING WITH COMPUTER PLEASE CHOISE')
your = Label(text='Your Score :')
computer = Label(text='Computer Score :')
co = Label(text='Computer Choise :')
myss = 0

mys =Label(fg='red')
mys.config(text=myss)
coms = Label(text='0',fg='red')
importantf = tkinter.font.Font(size=10)
important.configure(font=importantf)

yourf = tkinter.font.Font(family='Bell MT',size=15)
your.configure(font=yourf)

computerf = tkinter.font.Font(family='Bell MT',size=15)
computer.configure(font=computerf)

cof = tkinter.font.Font(family='Bell MT',size=15)
co.configure(font=cof)

baslik = tkinter.font.Font(family='Lucida Fax',size=50,weight='bold')
window.configure(font=baslik)

yazi1 = tkinter.font.Font(family= 'Comic Sans MS',size=20,weight='bold')
rock.configure(font=yazi1)

yazi2 = tkinter.font.Font(family= 'Comic Sans MS',size=20,weight='bold')
paper.configure(font=yazi2)

yazi3 = tkinter.font.Font(family= 'Comic Sans MS',size=20,weight='bold')
scissors.configure(font=yazi3)

cizgi1 = Frame(bg='light blue',height=70)
cizgi1.pack(fill='x',side = BOTTOM)

photo1 = PhotoImage(file='Rock.jpeg')
photo2 = PhotoImage(file='Paper.jpeg')
photo3 = PhotoImage(file='scissors2.png')









def ortak ():
    foo = ['Rock', 'Paper', 'Scissors']
    r = random.choice(foo)
    secilmis.config(text=r)

secilmis= Label(fg='green')






btn1 = Button(image=photo1,width=200,height=190,bd=30,activebackground='white',command=ortak,cursor='hand2')
btn2 = Button(image=photo2,width=200,height=190,bd=30,activebackground='white',command=ortak,cursor='hand2')
btn3 = Button(image=photo3,width=200,height=190,bd=30,activebackground='white',command=ortak,cursor='hand2')
cks = Button(text="Quit Game",fg='red',width = 8,height=3,command=lambda :quit(),cursor='hand2')

window.pack()

your.place(x=310,y=600)
mys.place(x=340,y=620)
computer.place(x=890,y=600)
coms.place(x=945,y=620)
co.place(x=590,y=450)
rock.place(x=310,y=300)
paper.place(x=610,y=300)
scissors.place(x=890,y=300)
important.place(x=515,y=350)
cks.place(x=200,y=650)
btn1.place(x=230,y=100)
btn2.place(x=530,y=100)
btn3.place(x=830,y=100)
secilmis.place(x=625,y=475)

window.mainloop()
