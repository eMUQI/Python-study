'''使用turtle库，绘制一个六边形。'''

import turtle as t

t.pensize(3)
t.penup()
t.goto(0,-200)
t.circle(200,-30)
t.pendown()

t.seth(0)
for i in range(6):
    t.fd(200)
    t.left(60)

t.done()