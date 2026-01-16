import turtle as t
import time
import random
t.setup(900,400)
t.penup()
t.hideturtle()
t.tracer(0, 0)
dinox, dinoy = -200, 0
cactusx = 200
score = 0
cactusspeed = 10
def dino():
    t.goto(dinox, dinoy)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()

def ground():
    t.goto(-500, 0)
    t.pendown()
    t.goto(500, 0)
    t.penup()

def cactus():
    t.goto(cactusx, 0)
    t.pendown()
    for _ in range(2):
        t.forward(25)
        t.left(90)
        t.forward(65)
        t.left(90)
    t.penup()

def jump1(x, y):
    global dinoy
    dinoy += 90
    t.ontimer(jump2, 1000)

def jump2():
    global dinoy
    dinoy -= 90
t.onscreenclick(jump1)
t.listen()


def mainloop():
    global cactusx
    global dinox, score, dinoy
    cactusx -= cactusspeed
    if cactusx < -300:
        cactusx = 200
        score += 1
    if dinox == cactusx and dinoy == 0:
        cactusx = 200
        dinoy = 0
        dinox = -200
        score = 0
    t.clear()
    t.goto(0, 10)
    t.write(f"{score}", align="center", font=("Aial", 16, "normal"))
    ground()
    dino()
    cactus()
    t.update()
    t.ontimer(mainloop, 30)
mainloop()
t.mainloop()