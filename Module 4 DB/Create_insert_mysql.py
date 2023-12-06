import pymysql

try:
    db_con = pymysql.connect(host="localhost",user="root",password="",database="myinfo")

    cr = db_con.cursor()
    print("Database connected successfully")
except Exception as e:
    print(e)

#create table
crt_tbl = "create table student(id integer primary key auto_increment, name text, age integer, city text)"
try:
    cr.execute(crt_tbl)
    db_con.commit()
    print("Table Created Successfully")
except Exception as e:
    print(e)

# #insert values
# ist_val = "insert into student(name, age, city) values('Sanjay', 22, 'Surat'), ('Pankaj', 21, 'Jamnagar'), ('Vipul', 20, 'Baroda')"
# try:
#     cr.execute(ist_val)
#     db_con.commit()
#     print("Values insert Successfully")
# except Exception as e:
#     print(e)

# #update values
# up_val = "update student set city='Junagadh' where id=2"
# try:
#     cr.execute(up_val)
#     db_con.commit()
#     print("Values update Successfully")
# except Exception as e:
#     print(e)


# #delete data
# dlt_val = "delete from student where id=3"
# try:
#     cr.execute(dlt_val)
#     db_con.commit()
#     print("Data delete Successfully")
# except Exception as e:
#     print(e)


#Show data
slc_data = "select * from student"
try:
    cr.execute(slc_data)
    db_con.commit()
    data = cr.fetchall()
    print(data)
except Exception as e:
    print(e)