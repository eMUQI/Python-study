'''使用turtle库，绘制一个叠边形，其中，叠边形内角为100度。'''
import turtle as t

t.pensize(3)
for i in range(9):
    t.fd(200)
    t.left(80)

t.done()