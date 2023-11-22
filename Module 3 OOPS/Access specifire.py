# class info:
#     __id=111
#     __nm='Parth'

#     def printdata(self):    #public
#         print('Id=',self.__id)
#         print('Name=',self.__nm)

# sp=info()
# sp.printdata()
# =====================================

class info:
    __id=111
    __nm='Parth'

    def __printdata(self):    #public
        print('Id=',self.__id)
        print('Name=',self.__nm)

    def print(self):
        self.__printdata()

sp=info()
sp.print()