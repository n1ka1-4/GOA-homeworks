
# i=0
# while i<20:
#  i=i+1
#  print('programming is fun!')

# menu='food'
# box='toy'
# computer='game'
# house='home'
# book='page'

# print(menu ,box ,computer ,house ,book)
from turtle import *

# Setup turtle
speed(20)
penup()

# Set the background color
bgcolor("lightblue")

# Color for the towers
color("darkorange")
begin_fill()

# Left tower (make it longer)
goto(-300, -200)
pendown()
forward(100)
left(90)
forward(300)  # Taller tower
left(90)
forward(100)
left(90)
forward(300)
left(90)
end_fill()

# Right tower (make it longer)
penup()
goto(150, -200)
pendown()
begin_fill()
forward(100)
left(90)
forward(300)  # Taller tower
left(90)
forward(100)
left(90)
forward(300)
left(90)
end_fill()

# Color for the wall
color("darkred")
begin_fill()

# Wall between the towers
penup()
goto(-200, -200)
pendown()
forward(350)
left(90)
forward(150)
left(90)
forward(350)
left(90)
forward(150)
left(90)
end_fill()

# Battlements with same color as wall (darkgray)
color("darkorange")
begin_fill()

# Battlement 1 on the wall
penup()
goto(-150, -50)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

# Battlement 2 on the wall
penup()
goto(-75, -50)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

# Battlement 3 on the wall
penup()
goto(0, -50)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

# Battlement 4 on the wall
penup()
goto(75, -50)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
end_fill()

# Color for the wall
color("darkred")
begin_fill()

# Wall between the towers
penup()
goto(-200, -200)
pendown()
forward(350)
left(90)
forward(150)
left(90)
forward(350)
left(90)
forward(150)
left(90)
end_fill()

color('darkorange')
begin_fill()
battlement_size = 45  # Smaller size for the battlements
penup()
goto(-330, 100)  # First battlement on the left tower
pendown()
begin_fill()
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
end_fill()

penup()
goto(-275, 100)  # Second battlement on the left tower
pendown()
begin_fill()
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
end_fill()

penup()
goto(-215, 100)  # Third battlement on the left tower
pendown()
begin_fill()
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
end_fill()

# Smaller battlements on top of the right tower (4 side by side)
penup()
goto(120, 100)  # First battlement on the right tower
pendown()
begin_fill()
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
end_fill()

penup()
goto(175, 100)  # Second battlement on the right tower
pendown()
begin_fill()
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
end_fill()

penup()
goto(235, 100)  # Third battlement on the right tower
pendown()
begin_fill()
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
forward(battlement_size)
left(90)
end_fill()



# Door color changed to skin tone (light beige)
color("lightyellow")
begin_fill()

# Door in the middle of the wall
penup()
goto(-50, -200)
pendown()
forward(100)
left(90)
forward(120)
left(90)
forward(100)
left(90)
forward(120)
left(90)
end_fill()

# Hide the turtle


# Hide the turtle
exitonclick()