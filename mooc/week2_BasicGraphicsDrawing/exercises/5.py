'''使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。'''
# 参考代码
# import turtle as t
# t.pensize(2)
# for i in range(4):
#     t.seth(90*i)
#     t.fd(150)
#     t.right(90)
#     t.circle(-150, 45)
#     t.goto(0,0)

import turtle as t

angle = 0
for i in range(4):
    t.seth(angle)
    t.fd(150)
    t.left(90)
    t.circle(150, -45)
    t.left(90)
    t.fd(150)
    angle -= 90

t.done()
