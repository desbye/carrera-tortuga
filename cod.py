from turtle import *
from random import randint

speed(20)
penup()
goto(-140, 140)

for paso in range(15):
    write(paso, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ana = Turtle()
ana.color('red')
ana.shape('turtle')

ana.penup()
ana.goto(-160, 105)
ana.pendown()

juan = Turtle()
juan.color('blue')
juan.shape('turtle')

juan.penup()
juan.goto(-160, 70)
juan.pendown()

alber = Turtle()
alber.color('green')
alber.shape('turtle')

alber.penup()
alber.goto(-160, 50)
alber.pendown()

alesia = Turtle()
alesia.color('pink')
alesia.shape('turtle')

alesia.penup()
alesia.goto(-160, 40)
alesia.pendown()

casia = Turtle()
casia.color('orange')
casia.shape('turtle')

casia.penup()
casia.goto(-160, 80)
casia.pendown()

for turn in range(100):
    ana.forward(randint(1,5))
    juan.forward(randint(1,5))
    alber.forward(randint(1,5))
    alesia.forward(randint(1,5))
    casia.forward(randint(1,5))

for giro in range(8):
    ana.right(360)
    juan.right(360)
    alber.right(360)
    alesia.right(360)
    casia.right(360)
