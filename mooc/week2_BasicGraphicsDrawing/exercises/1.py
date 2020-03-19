# PythonDraw.py
import turtle

# initialize pen settings
turtle.setup(650, 350, 200, 200)
turtle.ht()
turtle.penup()
turtle.fd(-250)
turtle.pendown()


# draw the snake's body
turtle.pensize(25)
turtle.pencolor("green")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)

# draw the snake's eye
turtle.dot(8,"white")

turtle.done()
