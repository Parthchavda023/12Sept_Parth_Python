'''Write a Python class named Rectangle constructed by a length and width 
and a method which will compute the area of a rectangle'''


# class Rectangle:
#     def rec_area(self,length,width):
#         print('Value of Length:',length)
#         print('Value of Width:',width)
#         print('Are of Rectangle=',length*width)

# sp=Rectangle()
# sp.rec_area(4,5)


#-----user input-----#
class Rectangle:
    length=0
    width=0

    def getvalue(self):
        self.length=int(input('Enter Value of Length:'))
        self.width=int(input('Enter Value of Width:'))

    def rec_area(self):
        print('Area of Rectangle=',self.length*self.width)

sp=Rectangle()
sp.getvalue()
sp.rec_area()