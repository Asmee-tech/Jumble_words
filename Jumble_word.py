from tkinter import *
import random
from tkinter import messagebox

screen=Tk()
screen.title("Jumbled words")
screen.geometry("500x500+500+150")
screen.config(bg="black")

words = ["cat", "dog", "sun", "tree", "book", "ball", "fish", "house", "chair", "apple",
    "water", "milk", "bird", "shoe", "phone", "car", "table", "door", "cake", "school",
    "flower", "river", "bed", "pencil", "paper", "clock", "window", "hat", "garden", "train",
    "baby", "hand", "foot", "smile", "beach", "rain", "snow", "bread", "cheese", "monkey",
    "rabbit", "mountain", "lamp", "basket", "orange", "family", "friend", "music", "happy", "dream"]

jumbled_words = ["tca", "gdo", "nus", "reet", "kobo", "llab", "hsfi", "sehou", "ircha", "lepap",
    "terwa", "klim", "drib", "ehos", "onphe", "rac", "lebat", "oord", "ekac", "olsoch",
    "werflo", "vreir", "dbe", "cilpen", "repap", "koclc", "owdwin", "tha", "edngra", "nrait",
    "abby", "ndha", "toof", "misel", "heacb", "nari", "owns", "adber", "eeehsc", "yekmon",
    "bbitra", "tainmoun", "pmal", "ketbas", "georan", "lyfami", "endifr", "sicmu", "ppyha", "meard"]

num=random.randrange(0,len(jumbled_words),1)
correct_ans=0
score_text=0
total_at=0

def reset():
    global num
    num=random.randrange(0,len(jumbled_words),1)
    word.config(text=jumbled_words[num])
    ent.delete(0,END)

def randword():
    word.config(text=jumbled_words[num])

def check():
    global ans, total_at, words, correct_ans, score_text, s1
    ans=ent.get()
    total_at+=1
    if ans==words[num]:
        messagebox.showinfo("Good job!", "It's correct!")
        correct_ans+=1
    else: 
        messagebox.showerror("Sorry", "It's wrong, try again")
    s1= "Score:"+str(correct_ans)+"/"+str(total_at)
    s.config(text=s1)
    reset()


title=Label(screen,text="JUMBLED WORDS GAME!",font=("roboto",28,"bold"),bg="black",fg="white")
title.pack(pady=5)

word=Label(screen,text="xyz",font=("roboto",20,"bold"),bg="black",fg="white")
word.pack(pady=30,ipady=10,ipadx=10)

s=Label(screen,text="",font=("roboto",20,"bold"),bg="black",fg="white")
s.pack(pady=10)

ans=StringVar()
ent=Entry(screen,font=("roboto",20,"bold"),textvariable=ans)
ent.pack(ipady=10)

che=Button(screen,text="Check",font=("roboto",20,"bold"),bg="grey",fg="green",width=10,relief=GROOVE, command=check)
che.pack(pady=40)

res=Button(screen,text="Reset",font=("roboto",20,"bold"),bg="grey",fg="yellow",width=10,relief=GROOVE, command=reset)
res.pack()


screen.mainloop()
