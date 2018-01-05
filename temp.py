from tkinter import *
import tkinter.messagebox as box
# import tkmessagebox.
from random import randint
die=['Draw without lifiting your chalk','Draw with your eyes closed','Draw with your non-dominent hand']
cate1=open('cat_1.txt','r+')
cate2=open('cat_2.txt','r+')
cate3=open('cat_3.txt','r+')
cate4=open('cat_4.txt','r+')
cat_1=[]
cat_2=[]
cat_3=[]
cat_4=[]
junk1=cate1.read().splitlines()
junk2=cate2.read().splitlines()
junk3=cate3.read().splitlines()
junk4=cate4.read().splitlines()
for temp1 in junk1:
    cat_1.append(temp1.split('.')[1])
for temp2 in junk2:
    cat_2.append(temp2.split('.')[1])
for temp3 in junk3:
    cat_3.append(temp3.split('.')[1])
for temp4 in junk4:
    cat_4.append(temp1.split('.')[1])
def draw1(cat_1):
    temp=randint(1,len(cat_1)-1)
    temp2=cat_1[temp]
    cat_1.remove(cat_1[temp])
    box.showinfo("Word is",temp2)
    return temp2
def draw1():
    temp=randint(1,len(cat_1)-1)
    temp2=cat_1[temp]
    cat_1.remove(cat_1[temp])
    box.showinfo("Word is",temp2)
    return temp2
def draw2():
    temp=randint(1,len(cat_2)-1)
    temp2=cat_2[temp]
    cat_2.remove(cat_2[temp])
    box.showinfo("Word is",temp2)
    return temp2
def draw3():
    temp=randint(1,len(cat_3)-1)
    temp2=cat_3[temp]
    cat_3.remove(cat_3[temp])
    box.showinfo("Word is",temp2)
    return temp2
def draw4():
    temp=randint(1,len(cat_4)-1)
    temp2=cat_4[temp]
    cat_4.remove(cat_4[temp])
    box.showinfo("Word is",temp2)
    return temp2
def throw_dice():
    box.showinfo("Challenge is ",die[randint(0,len(die)-1)])
    return die[randint(0,len(die)-1)]


top=Tk()
def helloCallBack():
    box.showinfo("Hellow World","Py")
B1=Button(top,text="Round 1",command=draw3)
B1.pack(padx=10,pady=10)
B2=Button(top,text="Round 2",command=draw4)
B2.pack(padx=10,pady=10)
B3=Button(top,text="Round 3",command=draw1)
B3.pack(padx=10,pady=10)
B5=Button(top,text="Roll_Dice",command=throw_dice)
B5.pack(padx=10,pady=10)
top.mainloop()
