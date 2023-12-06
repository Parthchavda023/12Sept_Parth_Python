import pymysql

try:   
    db_con = pymysql.connect(host="localhost",user="root",password="",database="myinfo")

    cr = db_con.cursor()
    print("Connected...")
except Exception as e:
    print(e)


'''---CREATE TABLE---'''
ctr_tbl =  "create table studentmysql (id integer primary key auto_increment, name text, marks integer, city text, age integer)"
try:
    cr.execute(ctr_tbl)
    db_con()
    print("Created...")
except Exception as e:
    print(e)


'''---Insert---'''

# n = int(input("Enter Number of Student:"))
# for i in range(n):
#     name = str(input("Enter Student Name:"))
#     marks = int(input("Enter Student marks:"))
#     city = str(input("Enter Student Cityname:"))
#     age = int(input("Enter Student Age:"))

#     ist_val = "insert into studentmysql(name, marks, city, age) values(%s,%s,%s,%s)"
#     try:
#         cr.execute(ist_val,(name,marks,city,age))
#         db_con.commit()
#         print("Insert values...")
#     except Exception as e:
#         print(e)


'''---Update---'''
# print("What would you like to update?")
# print("Press 1 for Name\nPress 2 for Marks\nPress 3 for City\nPress 4 for Age")
# choice = int(input("Enter Your Choice:-")) 

# #Update NAME
# if choice == 1:
#     id = int(input("Enter Student Id Number:"))
#     name = str(input("Enter Student Name:"))

#     up_data = "update studentmysql set name=%s where id=%s"
#     try:
#         cr.execute(up_data,(name,id))
#         db_con.commit()
#         print("Name updates successfully...")
#     except Exception as e:
#         print(e)

# #Update MARKS
# elif choice == 2:
#     id = int(input("Enter Student Id Number:"))
#     marks = str(input("Enter Student Marks:"))

#     up_data = "update studentmysql set marks=%s where id=%s"
#     try:
#         cr.execute(up_data,(marks,id))
#         db_con.commit()
#         print("Marks updates successfully...")
#     except Exception as e:
#         print(e)

# #Update CITY
# elif choice == 3:
#     id = int(input("Enter Student Id Number:"))
#     city = str(input("Enter Student city:"))

#     up_data = "update studentmysql set city=%s where id=%s"
#     try:
#         cr.execute(up_data,(city,id))
#         db_con.commit()
#         print("city updates successfully...")
#     except Exception as e:
#         print(e)

# #Update AGE
# elif choice == 4:
#     id = int(input("Enter Student Id Number:"))
#     age = str(input("Enter Student age:"))

#     up_data = "update studentmysql set age=%s where id=%s"
#     try:
#         cr.execute(up_data,(age,id))
#         db_con.commit()
#         print("age updates successfully...")
#     except Exception as e:
#         print(e)
# else:
#     print("Please enter Valid choice & try again")


'''---delete---'''
# id = int(input("Enter Student id do you want to delete:"))
# dlt_val = "delete from studentmysql where id=%s"
# try:
#     cr.execute(dlt_val,(id,))
#     db_con.commit()
#     print("DAta deleted successfully")
# except Exception as e:
#     print(e)


'''---Show data---'''
id = int(input("How many id do you want to see:"))
shw_data = "Select * from studentmysql"
try:
    cr.execute(shw_data)
    data = cr.fetchmany(id)
    for i in data:
        print(i)
except Exception as e:
    print(e)