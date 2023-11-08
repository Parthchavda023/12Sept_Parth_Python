class opnen_acc:
    acnum=0
    actyp=''
    acnm=''

    def acc_getadata(self):
        import random
        self.acnum=random.randint(100000000000,999999999999)
        print('Acoount Number:',self.acnum)

        print('Press S to Saving Account\nPress C  for Currect Account')
        self.actyp=input('Enter Account Type(C/S):')

        self.acnm=input('Enter Bank Holder Name:')

class deposite:
    dp=0
    def d_getdata(self):
        while True:
            self.dp=int(input('Enter Deposite amount:'))

            if self.dp<=1000:
                print('Enter Minimun amount 1000/-')
            else:
                print(f'{self.dp}/- is successfully Deposited...')
                break

class withdraw(deposite):
    wd=0
    tb=0
    def w_getdata(self):
        while True:
            self.wd=int(input('Enter withdraw amount:'))
            self.tb=self.dp-self.wd
        
            if self.tb<1000:
                print('You have to keep at least 1000/- amount in the account')       
                    
            else:
                print(f'{self.wd}/- is successfully withdraw...')
                break 
                

class statment(opnen_acc,withdraw):
    def printdata(self):
        print('----Bank Details----')
        print('Account Number=',self.acnum)
        
        if self.actyp.upper()=='S':
            type=('Saving Account')
        elif self.actyp.upper()=='C':
            type=('Current Account')
        print('Account Type=',type)
        
        print('Account Holder Name=',self.acnm)
        print('Clear Bank Balance=',self.tb)
    
sp=statment()
sp.acc_getadata()
sp.d_getdata()
sp.w_getdata()
sp.printdata()