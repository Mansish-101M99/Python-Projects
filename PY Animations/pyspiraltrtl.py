import turtle

# The greater the number for speed(), the slower the drawer
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
colors = ["red","orange","yellow","green","blue"]

for i in range(500):
    for c in colors:
        turtle.color(c)
        turtle.forward(i)
        turtle.left(91)
        turtle.tracer(10)

turtle.mainloop()