'''Write a Python program to calculate surface volume and area of a cylinder.
->volume = pi*radius*radius*height
         =3.14*6*6*4
         =452.1599999999
->area=((2*pi*radius)*height)+((pi*radius**2)*2)
      =((2*3.14*6)*4)+((3.14*6**2)*2)
      =376.8   '''


r=6
h=4
pi=3.14
print('Volume of cylinder:',pi*r*r*h)
print('Area of cylinder:',((2*pi*r)*h)+((pi*r**2)*2))


#-------User input-----#
r=float(input('Enter Value of Radius:'))
h=float(input('Enter Value of Height:'))
pi=3.14
print('Volume of cylinder:',pi*r*r*h)
print('Area of cylinder:',((2*pi*r)*h)+((pi*r**2)*2))