'''Write a Python class named Circle constructed by a radius and two methods 
which will compute the area and the perimeter of a circle.'''


# class Circle:
#     pi=3.14

#     def cir_area(self,radius):
#         # print('Area of Circle=',self.pi*radius*radius)
#         print('Area of Circle=',self.pi*radius**2)
        

#     def cir_parimeter(self,radius):
#         print('Parameter of Circle=',self.pi*radius*2)

# sp=Circle()
# sp.cir_area(5)
# sp.cir_parimeter(5)


#-----user input-----#
class Circle:
    radius=0
    pi=3.14

    def rad(self):
        self.radius=int(input('Enter Value of Radius:'))

    def cir_area(self):
        # print('Area of circle=',self.pi*self.radius*self.radius)
        print('Area of circle=',self.pi*self.radius**2)
    
    def cir_parimeter(self):
        print('Parimere of circle=',self.pi*self.radius*2)

sp=Circle()
sp.rad()
sp.cir_area()
sp.cir_parimeter()