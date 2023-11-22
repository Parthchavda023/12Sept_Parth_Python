class myinfo:
    def info(self,id,nm):
        print('Id=',id)
        print('Name=',nm)

class printinfo(myinfo):
    def info(self, id, nm):
        return super().info(id, nm)

sp=myinfo()
sp.info('100','Sanjay')

sp=printinfo()
sp.info(101,'Parth')