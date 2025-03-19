import turtle
import math
import random
wn=turtle.Screen()
wn.bgcolor("yellow")

pen=turtle.Turtle()
pen.up()
pen.goto(-300,-300)
pen.down()
pen.pensize(4)
for i in range (4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()
sn=turtle.Turtle()
sn.color ("black")
sn.shape("square")
sn.penup()
sn.speed(0)


goal=turtle.Turtle()
goal.color("blue")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100,100)

speed=5

def turnrt():
    sn.rt(90)
def turnlt():
    sn.lt(90)
def speedup():
    global speed
    speed+=1

turtle.listen()
turtle.onkey(turnrt,"Left")
turtle.onkey(turnlt,"Right")
turtle.onkey(turnrt,"Up")

while True:
    sn.fd(speed)
    if sn.xcor()>300 or sn.xcor()<-300:
        sn.rt(180)
    if sn.ycor()>300 or sn.ycor()<-300:
        sn.lt(180)
    x1=sn.xcor()
    x2=goal.xcor()
    y1=sn.ycor()
    y2=goal.ycor()
    d=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if d<10:
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        



















        
