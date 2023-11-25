import tkinter
from tkinter import ttk # For district
scr=tkinter.Tk()
scr.geometry("1000x1000")
scr.config(bg='lightyellow')
scr.title("Myform")

# .pack()
'''tkinter.Label(text="First Name:-").pack()
tkinter.Label(text="Last Name:-").pack()'''

# .place(x=_ , y=_ )
'''tkinter.Label(text="First Name=").place(x='0',y='0')
tkinter.Label(text="Last Name=").place(x='0',y='25')'''

# .grid(row=_ , column=_ )
tkinter.Label(text="Firstname=",bg='lightyellow',font='Gabriola 25 bold').grid(row=0,column=0,sticky="W")
tkinter.Label(text="Lastname=",bg='lightyellow',font='Gabriola 25 bold').grid(row=1,column=0,sticky="W")

# .entry (input details)
tkinter.Entry().grid(row=0,column=1,sticky="W")
tkinter.Entry().grid(row=1,column=1,sticky="W")
 
# .Radiobutton(select one button)
tkinter.Radiobutton(value="m",text='Male',bg='lightyellow',font='Gabriola 25 bold').grid(row=2,column=0,sticky="W")
tkinter.Radiobutton(value="f",text="Female",bg='lightyellow',font='Gabriola 25 bold').grid(row=2,column=1,sticky="W")

# .Checkbutton(select two/more button)
tkinter.Checkbutton(text="Gujrati",bg='lightyellow',font='Gabriola 25 bold').grid(row=3,column=0,sticky="W")
tkinter.Checkbutton(text="Hindi",bg='lightyellow',font='Gabriola 25 bold').grid(row=3,column=1,sticky="W")
tkinter.Checkbutton(text="English",bg='lightyellow',font='Gabriola 25 bold').grid(row=3,column=2,sticky="W")

# from tkinter import ttk    - use
disctrict=['Ahemdabad','Rajkot','Morbi','Baroda','Surat']
ttk.Combobox(values=disctrict,state='readonly').grid(row=4,column=0)

# submit button
def click():
    print("Your information has been submit successfully.")

tkinter.Button(text='Submit',command=click).place(x='450',y='350')


# call your info
tkinter.mainloop()