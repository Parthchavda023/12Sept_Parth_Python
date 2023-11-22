class myinfo:
    def __init__(self,id,nm):
        print('Id=',id)
        print('Name=',nm)

    def sum(self,a,b):
        print('Sum=',a+b)
    
sp=myinfo(101,'Parth')
print('-----------')
sp.sum(10,20)