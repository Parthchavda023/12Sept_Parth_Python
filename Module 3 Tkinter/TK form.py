import tkinter
from tkinter import ttk

# root = tk.Tk()
# root.title("District Selector")
# root.geometry("300x200")

# districts = ['Ahemdabad','Rajkot','Morbi','Baroda','Surat']
# combobox = ttk.Combobox(values=districts, state='readonly')
# combobox.grid(row=4, column=0)
# combobox.set('select Disctrict')  # Set the default selected district

# root.mainloop()

# Disple Screen
screen=tkinter.Tk()
screen.geometry('1370x730')
screen.config(bg='lightgrey')
screen.title('JOB INQUIRY FO/RM')

#form title
tkinter.Label(text='Employee Details',background="black",fg="white",font="Roman 20 bold").place(x='600',y='0')

#space
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=1,column=0,sticky='W')
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=2,column=0,sticky='W')

#personal details
tkinter.Label(text="Firstname:-",font="Consolas 11").grid(row=3,column=0,sticky='W')
tkinter.Entry().grid(row=3,column=1)
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=2,column=2,sticky='W')

tkinter.Label(text="Middlename:-",font="Consolas 11").grid(row=3,column=3,sticky='W')
tkinter.Entry().grid(row=3,column=4)
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=3,column=5,sticky='W')

tkinter.Label(text="Lastname:-",font="Consolas 11").grid(row=3,column=6,sticky='W')
tkinter.Entry().grid(row=3,column=7)
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=4,column=0,sticky='W')

# contact details
tkinter.Label(text="Mobil Number:-",font="Consolas 11").grid(row=5,column=0,sticky='W')
tkinter.Entry().grid(row=5,column=1)
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=5,column=2,sticky='W')

tkinter.Label(text="Email:-",font="Consolas 11").grid(row=5,column=3,sticky='W')
tkinter.Entry().grid(row=5,column=4)
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=6,column=0,sticky='W')

#Eduction details
tkinter.Label(text="Std / Course",font="Consolas 11").grid(row=7,column=0,sticky='W')
tkinter.Entry().grid(row=8,column=0)
tkinter.Entry().grid(row=9,column=0)
tkinter.Entry().grid(row=10,column=0)
tkinter.Entry().grid(row=11,column=0)

tkinter.Label(text="School/Collage name ",font="Consolas 11").grid(row=7,column=2,sticky='W')
tkinter.Entry().grid(row=8,column=2)
tkinter.Entry().grid(row=9,column=2)
tkinter.Entry().grid(row=10,column=2)
tkinter.Entry().grid(row=11,column=2)

tkinter.Label(text=" Board / Uni.",font="Consolas 11").grid(row=7,column=4,sticky='W')
tkinter.Entry().grid(row=8,column=4)
tkinter.Entry().grid(row=9,column=4)
tkinter.Entry().grid(row=10,column=4)
tkinter.Entry().grid(row=11,column=4)

tkinter.Label(text="Percentage(%)",font="Consolas 11").grid(row=7,column=6,sticky='W')
tkinter.Entry().grid(row=8,column=6)
tkinter.Entry().grid(row=9,column=6)
tkinter.Entry().grid(row=10,column=6)
tkinter.Entry().grid(row=11,column=6)

tkinter.Label(text="Passing year",font="Consolas 11").grid(row=7,column=8,sticky='W')
tkinter.Entry().grid(row=8,column=8)
tkinter.Entry().grid(row=9,column=8)
tkinter.Entry().grid(row=10,column=8)
tkinter.Entry().grid(row=11,column=8)
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=12,column=0,sticky='W')

#Language
tkinter.Label(text="Gujrati:-",font="Consolas 11").grid(row=13,column=0,sticky="W")
tkinter.Checkbutton(text="Read").grid(row=13,column=1,sticky="W")
tkinter.Checkbutton(text="Write").grid(row=13,column=2,sticky="W")
tkinter.Checkbutton(text="Speak").grid(row=13,column=3,sticky="W")

tkinter.Label(text="Hindi:-",font="Consolas 11").grid(row=14,column=0,sticky="W")
tkinter.Checkbutton(text="Read").grid(row=14,column=1,sticky="W")
tkinter.Checkbutton(text="Write").grid(row=14,column=2,sticky="W")
tkinter.Checkbutton(text="Speak").grid(row=14,column=3,sticky="W")

tkinter.Label(text="English:-",font="Consolas 11").grid(row=15,column=0,sticky="W")
tkinter.Checkbutton(text="Read").grid(row=15,column=1,sticky="W")
tkinter.Checkbutton(text="Write").grid(row=15,column=2,sticky="W")
tkinter.Checkbutton(text="Speak").grid(row=15,column=3,sticky="W")
tkinter.Label(text="  ",font="Consolas 11",background='lightgrey').grid(row=16,column=0,sticky='W')


#District
city=[
"AHMADABAD",
'AMRELI',
'ANAND',
'ARAVALLI',
'BANASKANTHA',
'BHARUCH',
'BHAVNAGAR',
'BOTAD',
'CHHOTA UDEPUR',
'DAHOD',
'DANGS',
'DEVBHUMI DWARKA',
'GANDHINAGAR',
'GIR SOMNATH',
'JAMNAGAR',
'JUNAGADH',
'KACHCHH',
'KHEDA',
'MAHESANA',
'MAHISAGAR',
'MORBI',
'NARMADA',
'NAVSARI',
'PANCHMAHALS',
'PATAN',
'PORBANDAR',
'RAJKOT',
'SABARKANTHA',
'SURAT',
'SURENDRANAGAR',
'TAPI',
'VADODARA',
'VALSAD']
combobox = ttk.Combobox(values=city, state='readonly')
combobox.grid(row=17, column=0)
combobox.set('select city')  # Set the default selected district


#call tkinter 
tkinter.mainloop()
