class myclass:
    id=101
    nm='Parth'

    def info(self):
        print('\nHello..')
        print("I'm Parth Chavda")
        print('Thank you !!!\n')

    def getinfo(self):
        id=input('Enter Id:')
        nm=input('Enter Name:')

sp=myclass()
print('Id:',sp.id)
print('Name:',sp.nm)
sp.info()
sp.getinfo()
