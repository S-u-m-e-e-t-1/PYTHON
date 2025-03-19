from turtle import *
from random import *
import turtle
import time
setup(800,600)
bgcolor("black")
speed(0)
color("red")
up()
goto(-500,350)
down()
begin_fill()
for i in range (2):
    fd(1000)
    rt(90)
    fd(700)
    rt(90)
end_fill()
s=20
shape("square")
up()
color("white")
for i in range (18):
    goto(400,340-(i*s*2))
    stamp()
up()
for i in range (17):
    goto(400+s,320-(i*s*2))
    stamp()
up()
color("black")
for i in range (18):
    goto(400,320-(i*s*2))
    stamp()
up()
for i in range (18):
    goto(400+s,340-(i*s*2))
    stamp()
aturtle=Turtle()
aturtle.color("green")
aturtle.shape("turtle")
aturtle.shapesize(2)
aturtle.up()
aturtle.goto(-480,320)
aturtle.down()


bturtle=Turtle()
bturtle.color("yellow")
bturtle.shape("turtle")
bturtle.shapesize(2)
bturtle.up()
bturtle.goto(-480,120)
bturtle.down()

cturtle=Turtle()
cturtle.color("white")
cturtle.shape("turtle")
cturtle.shapesize(2)
cturtle.up()
cturtle.goto(-480,-120)
cturtle.down()


dturtle=Turtle()
dturtle.color("blue")
dturtle.shape("turtle")
dturtle.shapesize(2)
dturtle.up()
dturtle.goto(-480,-320)
dturtle.down()

time.sleep(10)

while aturtle.xcor()<=400 and bturtle.xcor()<=400 and cturtle.xcor()<=400 and dturtle.xcor()<=400 :
    aturtle.fd(randint(1,10))
    bturtle.fd(randint(1,10))
    cturtle.fd(randint(1,10))
    dturtle.fd(randint(1,10))
if aturtle.xcor()>bturtle.xcor() and aturtle.xcor()>cturtle.xcor() and aturtle.xcor()>dturtle.xcor() :
    print("blue turtle wins!!!")
    for i in range(4):
        aturtle.rt(90)
        aturtle.shapesize(3)
        
elif bturtle.xcor()>aturtle.xcor() and bturtle.xcor()>cturtle.xcor() and bturtle.xcor()>dturtle.xcor() :
    print("blue turtle wins!!!")
    for i in range(4):
        bturtle.rt(90)
        bturtle.shapesize(3)
  
elif cturtle.xcor()>bturtle.xcor() and cturtle.xcor()>aturtle.xcor() and cturtle.xcor()>dturtle.xcor() :
    print("blue turtle wins!!!")
    for i in range(4):
        cturtle.rt(90)
        cturtle.shapesize(3)                      
else:
    print("blue turtle wins!!!")
    for i in range(4):
        dturtle.rt(90)
        dturtle.shapesize(3)
        
done()

    
    
