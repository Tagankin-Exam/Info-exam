from turtle import *
left(90)
speed(0)
kof = 40
for i in range(5):
    forward(kof * 9)
    right(90)
    forward(kof * 3)
    right(90)
pu()
for x in range(11):
    for y in range(11):
        goto(x * 40, y * 40)
        dot(5)
done()
    
    
