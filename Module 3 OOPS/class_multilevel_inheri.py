class a:
    aid=0
    anm=''
    def a_getdata(self):
        self.aid=input('Enter A id:')
        self.anm=input('Enter A Name:')

class b(a):
    bid=0
    bnm=''
    def b_getdata(self):
        self.bid=input('Enter b id:')
        self.bnm=input('Enter B Name:')

class c(b):
    cid=0
    cnm=''
    def c_getdata(self):
        self.cid=input('Enter C id:')
        self.cnm=input('Enter B Name:')

class d(c):
    def printdata(self):
        print('--- A-Student Data---')
        print('A Student Id number=',self.aid)
        print('A student Name=',self.anm)
        
        print('--- B-Student Data---')
        print('B Student Id number=',self.bid)
        print('B student Name=',self.bnm)
        
        print('--- C-Student Data---')
        print('C Student Id number=',self.cid)
        print('C student Name=',self.cnm)

sp=d()
sp.a_getdata()
sp.b_getdata()
sp.c_getdata()
sp.printdata()