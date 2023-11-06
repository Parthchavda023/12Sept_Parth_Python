class studinfo:
    id=0
    nm=''

    def getdata(self):
        self.id=int(input('Enter Id Number:'))
        self.nm=str(input('Enter Name:'))

    def printdata(self):
        print('-----------------')
        print('Id Number:',self.id)
        print('Student Name:',self.nm)

sp=studinfo()
sp.getdata()
sp.printdata()