'''使用turtle库，绘制一个正方形。'''

import turtle as t

t.pensize(2)
t.penup()
t.goto(-150, -150)
t.pendown()
for i in range(4):
    t.fd(300)
    t.left(90)

t.done()
