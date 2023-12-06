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

# n = int(input("Enter Number of student:-"))

# for i in range(n):
#     name = str(input("Enter Student Name:"))
#     marks = int(input("Enter Student Marks:"))
#     age = int(input("Enter Student Age:"))
#     city = str(input("Enter Student City Name:"))

#     ist_tbl = "insert into schoolinfo(name,marks,age,city) values(?,?,?,?)"
#     try:
#         cr.execute(ist_tbl,(name,marks,age,city))
#         db_con.commit()
#         print("Value insert Successfully...!")
#     except Exception as e:
#         print(e)


'''---UPDATE VALUE---'''

# n = int(input('How many Id do you want to Update:'))
# for i in range(n):
#     id = int(input("Which ID you want to update:-"))
#     name = str(input("Enter Student Name:"))
#     marks = int(input("Enter Student Marks:"))
#     age = int(input("Enter Student Age:"))
#     city = str(input("Enter Student City Name:"))

#     upd_tbl = "update schoolinfo set name=?,marks=?,age=?,city=? where id=?"
#     try:
#         cr.execute(upd_tbl,(name,marks,age,city,id)) 
#         db_con.commit()
#     except Exception as e:
#         print(e)


'''---DELETE VALUES'''
id = int(input('Which id do you want to delete:'))

dlt_tbl="delete from schoolinfo where id=?"
try:
    cr.execute(dlt_tbl,(id,))
    db_con.commit()
except Exception as e:
    print(e)


'''---SHOW DATA(SELECT COMMAND)---'''
sh = int(input("How many id do you want to see:"))

shw_val = "select * from schoolinfo"
try:
    cr = db_con.cursor()
    cr.execute(shw_val)
    data = cr.fetchmany(sh)

    for i in data:
        print(i)

except Exception as e:
    print(e)