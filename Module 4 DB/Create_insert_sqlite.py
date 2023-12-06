import sqlite3

dbcon = sqlite3.connect("mytable.db")


#Create table
tbl_crt="create table studinfo(id integer primary key autoincrement, name text, age integer, city tect)"
try:

    dbcon.execute(tbl_crt)

except Exception as e:
    print(e)


# #insert value in table
# ins_data="insert into studinfo(name,age,city)values('Parth',21,'Halvad'),('Hitesh',28,'Morbi')"
# try:
#     dbcon.execute(ins_data)
#     dbcon.commit()
# except Exception as e:
#     print(e)


# #update value on table
# upd_tbl="update studinfo set city='Rajpar' where id=2"
# try:
#     dbcon.execute(upd_tbl)
#     dbcon.commit()
# except Exception as e:
#     print(e)


# #Delete table value
# dlt_tbl="delete from studinfo where id=2"
# try:
#     dbcon.execute(dlt_tbl)
#     dbcon.commit()
# except Exception as e:
#     print(e)


#select table(shoe data)
cr=dbcon.cursor()

shw_val = "select * from studinfo"
try:

    cr.execute(shw_val)
    data=cr.fetchall()

    # data=cr.fetchmany(2)
    # data=cr.fetchone()
    # print(data)

    for i in data:
        print(i)
        # print(i[0])
        # print(i[1])
        # print(i[2])
        # print(i[3])
        
        
except Exception as e:
    print(e)