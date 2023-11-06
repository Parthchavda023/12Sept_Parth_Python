class parth:        #1
    pid=0
    pbnc=''

    def pgetdata(self):
        self.pid=input('Enter Parth ID:')
        self.pbnc=input('Enter Parth Branch:')

class vipul:        #2
    vid=0
    vbnc=''

    def vgetdata(self):
        self.vid=input('Enter Parth ID:')
        self.vbnc=input('Enter Vipul Branch:')

class sanjay:       #3
    sid=0
    sbnc=''

    def sgetdata(self):
        self.sid=input('Enter Sanjay ID:')
        self.sbnc=input('Enter Sanjay Branch:')

class mehul:        #4
    mid=0
    mbnc=''

    def mgetdata(self):
        self.mid=input('Enter Mehul ID:')
        self.mbnc=input('Enter Mehul Branch:')

class collage(parth,vipul,sanjay,mehul):
    def printdata(self):
        print('-----Parth Details-----')
        print('Parth Id Number=',self.pid)
        print('Parth Branch=',self.pbnc)

        print('-----Vipul Details-----')
        print('Vipul Id Number=',self.vid)
        print('Vipul Branch=',self.vbnc)
        print('-----Sanjay Details-----')
        print('Sanjay Id Number=',self.sid)
        print('Sanjay Branch=',self.sbnc)

        print('-----Mehul Details-----')
        print('Mehul Id Number=',self.mid)
        print('Mehul Branch=',self.mbnc)
    
sp=collage()
sp.pgetdata()
sp.vgetdata()
sp.sgetdata()
sp.mgetdata()
sp.printdata()