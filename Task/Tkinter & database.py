
import tkinter
import sqlite3

scr = tkinter.Tk()
scr.geometry("500x500")

tkinter.Label(text="Id=").grid(row=0, column=0, sticky="W")
tkinter.Label(text="Name=").grid(row=1, column=0, sticky="W")
tkinter.Label(text="Sub=").grid(row=2, column=0, sticky="W")
tkinter.Label(text="Age=").grid(row=3, column=0, sticky="W")
tkinter.Label(text="City=").grid(row=4, column=0, sticky="W")

id = tkinter.Entry()
id.grid(row=0, column=1, sticky="W")

nm = tkinter.Entry()
nm.grid(row=1, column=1, sticky="W")

Sub = tkinter.Entry()
Sub.grid(row=2, column=1, sticky="W")

Age = tkinter.Entry()
Age.grid(row=3, column=1, sticky="W")

City = tkinter.Entry()
City.grid(row=4, column=1, sticky="W")


try:
    db_con = sqlite3.connect("Tkinter1.db")
    print("Connect...")
    cr = db_con.cursor()
except Exception as e:
    print(e)


crt_tbl = "create table student00(id integer ,name text,sub text,age integer,city text)"
try:
    cr.execute(crt_tbl)
    db_con.commit()
    print("Create...")
except Exception as e:
    print(e)


def insert_val():
    Id = id.get()
    name = nm.get()
    sub = Sub.get()
    age = Age.get()
    city = City.get()
    ist_val = "insert into student00 values ('"+Id+"','"+name+"','"+sub+"','"+age+"','"+city+"')"
 
    try:
        cr.execute(ist_val)
        db_con.commit()
        print("Inserted...")
    except Exception as e:
        print(e)



def update_data():
    Id = id.get()
    name = nm.get()
    sub = Sub.get()
    age = Age.get()
    city = City.get()
    upd_dt = "update student00 set name='"+name+"',sub='"+sub+"',age='"+age+"',city='"+city+"' where id=("+Id+")"
 
    try:
        cr.execute(upd_dt)
        db_con.commit()
        print("Update...")
    except Exception as e:
        print(e)


def delete_id():
    Id = id.get()
    del_id = "delete from student00 where id='"+Id+"'"
    try:
        cr.execute(del_id)
        db_con.commit()
        print("Delete...")
    except Exception as e:
        print(e)


tkinter.Button(text="INSERT",command=insert_val).grid(row=6,column=0,sticky="W")
tkinter.Button(text="UPDATE",command=update_data).grid(row=6,column=1,sticky="W")
tkinter.Button(text="DELETE",command=delete_id).grid(row=6,column=2,sticky="W")


tkinter.mainloop()