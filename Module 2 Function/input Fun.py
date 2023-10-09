def getdata(id,nm,add,age):
    print("Id:",id)
    print('Name:',nm)
    print('Adddress:',add)
    print('Age:',age)


p=int(input("Enter Number of Members:"))

for i in range(p):
    stid=int(input("Enter ID Number:"))
    stnm=input('Enter Your Name:')
    stadd=input('Enter Your Address:')
    stage=int(input('Enter your Age:'))
    
    getdata(stid,stnm,stadd,stage)