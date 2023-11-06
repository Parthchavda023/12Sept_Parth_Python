class studinfo:
    def getdata(self,id,nm):
        print('Id Number:',id)
        print('Studen Number:',nm)
    
sp=studinfo()
sp.getdata(101,'Parth')     #static
print('---------------------------')
stid=input('Enter Id number:')
stnm=input('Enter Name:')
sp.getdata(stid,stnm)       #daynamic