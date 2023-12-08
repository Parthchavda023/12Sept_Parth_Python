import sqlite3


db_con = sqlite3.connect("task_table.db")

cr = db_con.cursor()

'''---CREATE TABLE---'''

tbl_crt = "create table schoolinfo(id integer primary key autoincrement, name text, marks integer, age integer, city text)"
try:
    db_con.execute(tbl_crt)
    print("Table create successfully... !")
except Exception as e:
    print(e)


'''---INSERT VALUE---'''

n = int(input("Enter Number of student:-"))

for i in range(n):
    name = str(input("Enter Student Name:"))
    marks = int(input("Enter Student Marks:"))
    age = int(input("Enter Student Age:"))
    city = str(input("Enter Student City Name:"))

    ist_tbl = "insert into schoolinfo(name,marks,age,city) values("'{name}','{marks}','{age}','{city}'")"
    try:
        cr.execute(ist_tbl,(name,marks,age,city))
        db_con.commit()
        print("Value insert Successfully...!")
    except Exception as e:
        print(e)