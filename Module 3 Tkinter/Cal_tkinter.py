import tkinter
from tkinter import messagebox

scr=tkinter.Tk()
scr.geometry('500x500')
scr.config(bg="white")
scr.title('Calculator')


tkinter.Label(text="Enter First value=").grid(row=0,column=0,sticky="W")
tkinter.Label(text="Enter Second value=").grid(row=1,column=0,sticky="W")

fstval=tkinter.Entry()
fstval.grid(row=0,column=1,sticky="W")
lstval=tkinter.Entry()
lstval.grid(row=1,column=1,sticky="W")


def sum():
    messagebox.showinfo("Sum",f"First Value:{int(fstval.get())} and Second Value:{int(lstval.get())} = {int(fstval.get()) + int(lstval.get())}")

def sub():
    messagebox.showinfo("Sum",f"First Value:{int(fstval.get())} and Second Value:{int(lstval.get())} = {int(fstval.get()) - int(lstval.get())}")

def mul():
    messagebox.showinfo("Sum",f"First Value:{int(fstval.get())} and Second Value:{int(lstval.get())} = {int(fstval.get()) * int(lstval.get())}")

def div():
    messagebox.showinfo("Sum",f"First Value:{int(fstval.get())} and Second Value:{int(lstval.get())} = {int(fstval.get()) / int(lstval.get())}")

tkinter.Button(text="+",command=sum).place(x=50,y=50)
tkinter.Button(text="-",command=sub).place(x=100,y=50)
tkinter.Button(text="*",command=mul).place(x=150,y=50)
tkinter.Button(text="/",command=div).place(x=200,y=50)

tkinter.mainloop()

