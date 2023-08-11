import turtle as turtle_module
import random
import colorgram
turtle_module.colormode(255)
colors = colorgram.extract('hirstpainting.jpeg',30)
rgbcolors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if not (255-r<50 and 255-g<50 and 255-b<50):
        new_color=(r,g,b)
        rgbcolors.append(new_color)
print(rgbcolors)
pen = turtle_module.Turtle()
initial_x = -300
initial_y = 300
pen.penup()
pen.setx(initial_x)
pen.sety(initial_y)
pen.pendown()
# pen.color(random.choice(rgbcolors))
pos = initial_y
for k in range(10):
    for i in range(10):
        pen.dot(20,random.choice(rgbcolors))
        pen.penup()
        pen.forward(50)
        pen.pendown()
    pen.penup()
    pen.setx(initial_x)
    pos-=50
    pen.sety(pos)
    pen.pendown()
pen.write('Damien Hirst Dot Painting',font=15)
sc = turtle_module.Screen()
sc.exitonclick()