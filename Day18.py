from turtle import Turtle,Screen
import random
pen = Turtle()
pen.speed(50)
pen.penup()
pen.setx(-200)
pen.sety(200)
pen.pendown()
pen.pensize(2)
pen.write('Dashed Line ')
for i in range(10):
    pen.penup()
    pen.forward(10)
    pen.pendown()
    pen.forward(10)
pen.penup()
sides=4
colors=["green","blue","red","black","purple"]
# pen.width(3)
pen.setx(0)
pen.sety(0)

pen.write('Shapes ')
pen.pendown()
#shapes
for i in range(4,10):
    for i in range(sides):
        pen.forward(100)
        pen.right(360/sides)
    pen.color(random.choice(colors))
    sides+=1
pen.penup()
pen.setx(-500)
pen.pendown()
#Drawing a spirograph
pen.pensize(1)
for i in range(50):
    pen.color(random.choice(colors))
    pen.circle(100)
    pen.backward(1)
    pen.left(8)
pen.penup()
pen.sety(-300)
pen.write('Spirograph',font=20)
sc= Screen()
sc.exitonclick()