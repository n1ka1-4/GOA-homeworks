from turtle import *
from turtle import color

speed(30)

width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)

color("yellow")
begin_fill()

left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("brown")

penup()
goto(15, 130)
pendown()

color("blue")
begin_fill()

right(150)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

penup()
goto(125, 130)
pendown()

right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

end_fill()


exitonclick()