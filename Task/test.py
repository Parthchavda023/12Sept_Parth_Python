# import turtle
# turtle.bgcolor('black')

# sp=turtle.Turtle()
# sp.speed(25)
# sp.pencolor('pink')
# for i in range(400):
#     sp.forward(i)
#     sp.left(91)


# #====================================#

import turtle
p=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
p.width(1)
p.speed(50)
color=('magenta','yellow','green','red')
for i in range(500):
    p.pencolor(color[i%4])
    p.forward(i*2)
    p.right(121)
