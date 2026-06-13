from tkinter import *
from random import *

screen=Tk()
screen.title("Jumbled words")
screen.geometry("500x500+500+150")
screen.config(bg="black")

title=Label(screen,text="JUMBLED WORDS GAME!",font=("roboto",28,"bold"),bg="black",fg="white")
title.pack(pady=5)

word=Label(screen,text="xyz",font=("roboto",20,"bold"),bg="black",fg="white")
word.pack(pady=30,ipady=10,ipadx=10)

ans=StringVar()
ent=Entry(screen,font=("roboto",20,"bold"),textvariable=ans)
ent.pack(ipady=10)

screen.mainloop()