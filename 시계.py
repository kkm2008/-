import turtle

t=turtle.Turtle(shape='turtle')
t.penup()
t.goto(0,-200)
t.pencolor('blue')
t.turtlecolor('blue')
for num in range(60):
    if num%5==0:
        t.stamp()
    else:
        t.dot()
    t.circle(200,6)
   
turtle.done()
