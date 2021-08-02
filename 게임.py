import turtle
import random
import  time
from functools import partial

playing=False
t=turtle.Turtle()
t1=turtle.Turtle()


time_turtle=turtle.Turtle()
time_turtle.hideturtle()

bluefollowturtle=turtle.Turtle()
redfollowturtle=turtle.Turtle()

s=turtle.Screen()
s.setup(1200,800)

circle1=turtle.Turtle()
circle2=turtle.Turtle()

blue_enemy_list=[bluefollowturtle,circle1,circle2]
red_enemy_list=[redfollowturtle,circle1,circle2]

def Circle():
    circle1.circle(350,10)
    circle2.circle(150,20)

def check_time():
    global time
    time+=1
    time_turtle.clear()
    time_turtle.write('score:'+str(time),False,"center",("",20))

def setting():
    t.home()
    t1.home()
    redfollowturtle.penup()
    redfollowturtle.goto(-100,-100)
    redfollowturtle.shape("square")
    redfollowturtle.speed(12)
    redfollowturtle.color("red")
    bluefollowturtle.penup()
    bluefollowturtle.goto(-100,-100)
    bluefollowturtle.shape("square")
    bluefollowturtle.speed(12)
    bluefollowturtle.color("blue")

    time_turtle.pu()
    time_turtle.goto(-500,250)

    circle1.shape("square")
    circle1.speed(0)
    circle1.penup()
    circle1.home()
    circle1.sety(-350)
    circle2.shape("square")
    circle2.speed(0)
    circle2.penup()
    circle2.home()
    circle2.sety(-150)

def follow():
    ang=redfollowturtle.towards(t1.pos())
    redfollowturtle.setheading(ang)
    redfollowturtle.fd(10)
    ang1=bluefollowturtle.towards(t.pos())
    bluefollowturtle.setheading(ang1)
    bluefollowturtle.fd(10)


def turn_right(a):
    a.setheading(0)
def turn_up(a):
    a.setheading(90)
def turn_left(a):
    a.setheading(180)
def turn_down(a):
    a.setheading(270)
def message(m1,m2):
    turtle.clear()
    turtle.goto(0,100)
    turtle.write(m1,False,"center",("",20))
    turtle.goto(0,-100)
    turtle.write(m2,False,"center",("",20))
    turtle.home()
def start():
    global playing, time
    if playing==False:
        playing=True
        turtle.clear()
        setting()
        time=0
        play()

def enemyplay():
    follow()
    Circle()
def play():
    global score
    global playing
    global time
    enemyplay()

    t.forward(30)
    t1.forward(30)
    check_time()
    for i in blue_enemy_list:
        if t.distance(i)<30 or -600>t.xcor()>600 or -600>t.xcor() or t.ycor()<-400 or t.ycor()>400:
            playing=False
            text="score:"+str(time)
            message("game over red win",text)
    for i in red_enemy_list:
        if t1.distance(i)<30 or -600>t1.xcor()>600 or -600>t1.xcor() or t1.ycor()<-400 or t1.ycor()>400:        
            playing=False
            text="score:"+str(time)
            message("game over blue win",text)
    if playing:
        turtle.ontimer(play,100)
        
if __name__=="__main__":
    turtle.title("Turtle Run")
    turtle.hideturtle()
    turtle.bgcolor("orange")
    turtle.up()
    turtle.speed(0)

    t.shape("turtle")
    t1.shape("turtle")
    
    t.speed(0)
    t1.speed(0)
    t.up()
    t1.up()
    t.color("sky blue")
    t1.color("red")

    turtle.onkeypress(partial(turn_right,a=t),"Right")
    turtle.onkeypress(partial(turn_up,a=t),"Up")
    turtle.onkeypress(partial(turn_left,a=t),"Left")
    turtle.onkeypress(partial(turn_down,a=t),"Down")
    
    turtle.onkeypress(partial(turn_right,a=t1),"d")
    turtle.onkeypress(partial(turn_up,a=t1),"w")
    turtle.onkeypress(partial(turn_left,a=t1),"a")
    turtle.onkeypress(partial(turn_down,a=t1),"s")
    
    turtle.onkeypress(start,"space")
    turtle.listen()
    message("turtle avoid","[start:press space]")
    #time.sleep(9999)

    
    
