import turtle

r=int(input("반지름:"))

t=turtle.Turtle()
screen=turtle.Screen()

t.color("green")
t.shape("turtle")
t.circle(r,90)
stamp1=t.stamp()
t.circle(r,90)
t.stamp()
t.circle(r,90)
stamp2=t.stamp()
t.circle(r,90)
t.stamp()



t.clearstamp(stamp1)
t.clearstamp(stamp2)
