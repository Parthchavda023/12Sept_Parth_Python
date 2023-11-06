class static:

    @staticmethod   #staticmethod no use kro tyre func ma default value (Self) no use nahi thay
    def getdata(id,nm):
        print('Id number:',id)
        print('Name:',nm)
    
    @staticmethod
    def getsum(a,b):
        print('Sum=',a+b)

sp=static()
sp.getdata(100,'Parth')
print('-----------')
sp.getsum(10,25)