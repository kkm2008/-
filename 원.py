
import turtle
import random


t=turtle.Turtle()
wn=turtle.Screen()




speed=int(input("속도입력:"))
radius=random.randint(50,80)
t.circle(-radius,speed)
