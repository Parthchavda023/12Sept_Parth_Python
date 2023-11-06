class father:
    bal=0
    gold=0
    car=0

    def getdata(self):
        self.bal=input('Enter Balance:')
        self.car=input('Enter Car Details:')
        self.gold=input('Enter Gold Details:')

class son(father):

    def printdata(self):
        print('Balance=',self.bal)
        print('Car=',self.car)
        print(f'Gold={self.gold}kg')
    
sp=son()
sp.getdata()
print('-----------------')
sp.printdata()
