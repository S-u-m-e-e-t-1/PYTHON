from turtle import *
import time

bgcolor("black")
speed(5)
time.sleep(20)
pencolor("white")
up()
goto(0,-280)
down()
fillcolor("red")
begin_fill()
circle(280)
end_fill()

up()
goto(0,-240)
down()
fillcolor("white")
begin_fill()
circle(240)
end_fill()

up()
goto(0,-200)
down()
fillcolor("red")
begin_fill()
circle(200)
end_fill()

up()
goto(0,-160)
down()
fillcolor("blue")
begin_fill()
circle(160)
end_fill()

lt(72)
fd(300)
fillcolor("white")
begin_fill()
for i in range(5):
    lt(144)
    fd(300)
end_fill()
            
