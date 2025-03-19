from turtle import*
bgcolor("black")
color= ['yellow','orange','green','cyan','blue']
pensize(4)
penup()
setpos(-90,30)
pendown()
for i in range(5):
      pencolor(color[i])
      forward(200)
      right(144)
penup()
setpos(80,-140)
pendown()
pencolor("Black")
done()