import turtle

turtle.bgcolor("lightblue")
turtle.pensize(1.8)
turtle.speed(0)
color = ["red","blue","green","orange"]

for a in range(11):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(13)

turtle.mainloop()