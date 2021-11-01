import turtle as trtl

import time
import random
import threading

t = trtl.Turtle()
rect = trtl.Turtle()
explosion = trtl.Turtle()

from playsound import playsound


g = trtl.Turtle()
f = trtl.Turtle()
ufo = trtl.Turtle()
wn = trtl.Screen()
wn.setup(600,600)
wn.addshape('ghost-flash1.gif')
f.shape('ghost-flash1.gif')
f.hideturtle()
wn.addshape("explosion.gif")
explosion.hideturtle()
explosion.penup()
explosion.shapesize(2)
explosion.shape("explosion.gif")
explosion.goto(0,200)
powerupcounter = 0
wn.addshape("background.gif")
wn.bgpic("background.gif")
wn.addshape('ghost-flash.gif')
g.shape('ghost-flash.gif')
wn.addshape('ufo.gif')
ufo.shape('ufo.gif')
#wn.addshape('IMG_0933.gif')

wn.addshape('pumpkin.gif')
powerupcounter1 = trtl.Turtle()
powerupcounter1.hideturtle()
powerupcounter1.shape('pumpkin.gif')
powerupcounter1.shapesize(3)

rectCors = ((-5,20),(5,20),(5,-20),(-5,-20))

wn.register_shape('rectangle',rectCors)

rect.penup()
rect.turtlesize(2)
rect.goto(0,-275)
rect.color("orange")
rect.shape("square")
rect.stamp()


t.penup()
t.setheading(90)
t.goto(0,-250)
t.shape('rectangle')
t.color("orange")
ufo.speed(0)
ufo.penup()
ufo.goto(0, 200)
ufo.color("white")
g.hideturtle()
g.penup()
g.goto(t.xcor(), t.ycor())
g.speed(0)
timerinput = int(wn.textinput('Menu', 'How much time for your game in seconds?'))
timer = timerinput
v = False
counter = trtl.Turtle()
counter.hideturtle()

s = trtl.Turtle()
s.hideturtle()

s.speed(0)
s.penup()
s.color("white")
s.goto(-250, 200)
s.pendown()
s.clear()
s.write("Score: 0", font=("Cosmic Sans",10, "normal"))


global scores 
scores = 0
def countdown():
  counter.speed(0)
  counter.penup()
  counter.color("white")
  counter.goto(-250, 250)
  counter.pendown()
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=("Cosmic Sans",10, "normal"))
    timer_up = True
    wn.bye()
    time.sleep(1)
    trtl.bye()
  else:
    counter.write("Timer: " + str(timer), font=("Cosmic Sans",10, "normal"))
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
counter_interval = 1000
timer_up = False

countdown()





powerupchecker = False
def left():
    if t.heading() <= 112.5:
        t.left(5.62500)

    else:
        print ("left")
def right():
    if t.heading() >= 67.5:
        t.right(5.62500)
    else:
        print ("right")
def powerupcheck(x,y):
    global powerupchecker
    powerupchecker = True
def attack():
    global powerupcounter
    if powerupcounter >= 2:
        powerupcounter1.penup()
        powerupcounter1.goto(200,0)
        powerupcounter1.showturtle()
        powerupcounter1.color('white')
        powerupcounter1.onclick(powerupcheck)

    psotiontogo = random.randint(-200,200)
    global v
    if v == False:
        v = True
        global powerupchecker
        if powerupchecker == True:
            powerupchecker = False
            #wn.bgpic('bkg.png')
            powerupcounter = 0
            g.shape('ghost-flash1.gif')
            powerupcounter1.hideturtle()
            playsound('smb_1-up.wav')


        g.penup()
        g.goto(t.xcor(), t.ycor())
        g.setheading(t.heading())
        g_a = g.clone()
        g_a.speed(0.51)
        g_a.showturtle()




        g_a.forward(475)
        time.sleep(0.00000001)
        print(str(g_a.xcor()) + ',' + str(g_a.ycor()))
        if int(ufo.xcor()-50)<g_a.xcor()<int(ufo.xcor()+50) and  100<g_a.ycor()<300:
            global scores
            scores = scores + 1
            s.speed(0)
            s.penup()
            s.color("white")
            s.goto(-250, 200)
            s.pendown()
            s.clear()
            s.write("Score: " + str(scores), font=("Cosmic Sans",10, "normal"))
            powerupcounter = powerupcounter + 1
            print(str(powerupcounter))
            print('hit')
            g_a.hideturtle()
            explosion1 = explosion.clone()
            explosion1.goto(ufo.xcor(),ufo.ycor())
            explosion1.showturtle()
            time.sleep(0.1)
            explosion1.hideturtle()
            ufo.goto(psotiontogo,200)
            print('hiaaa')
            wn.bgpic('background.gif')
        v = False


        g_a.hideturtle()








wn.onkey(left, "Left")
wn.onkey(right, "Right") 
wn.onkey(attack, "Up")


wn.listen()
wn.ontimer(countdown, counter_interval)

wn.mainloop()



'''
while True:
  ufomove()
  time.sleep(1)
'''
# Snytax for keypress