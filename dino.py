import turtle as t


t.setup(500,350)
t.penup()
t.hideturtle()
t.tracer(0, 0)
t.title("dino")
dinox, dinoy = -200, 0
cactusx = 200
cactusy = 0
score = 0
cactusspeed = 10
onground = 1

t.register_shape("dino.gif") 




dino_turtle = t.Turtle()
dino_turtle.penup()
dino_turtle.shape("dino.gif")  
dino_turtle.hideturtle()  

t.register_shape("cactus.gif")

cactus_turtle = t.Turtle()
cactus_turtle.penup()
cactus_turtle.shape("cactus.gif")
cactus_turtle.hideturtle()


def dino():
    
    
    
    
    dino_turtle.goto(dinox, dinoy + 15)
    dino_turtle.showturtle()
    

def ground():
    t.goto(-500, 0)
    t.pendown()
    t.goto(500, 0)
    t.penup()



def cactus():
    cactus_turtle.goto(cactusx, cactusy + 15)
    cactus_turtle.showturtle()

def jump1(x, y):
    global onground
    if onground == 1:
        onground = 0
        global dinoy
        dinoy += 40
        t.ontimer(jump2, 1000)
    

def jump2():
    global onground
    global dinoy
    dinoy -= 40
    onground = 1

t.onscreenclick(jump1)
t.listen()

def mainloop():
    global cactusx
    global dinox, score, dinoy
    cactusx -= cactusspeed
    if cactusx < -300:
        cactusx = 200
        score += 1
    if  cactusx <= dinox <= cactusx + 25 and dinoy < 20:
        cactusx = 200
        dinoy = 0
        dinox = -200
        score = 0
    
    
    dino_turtle.hideturtle()
    cactus_turtle.hideturtle()
    
    t.clear()
    t.goto(0, 10)
    t.write(f"{score}", align="center", font=("Arial", 16, "normal"))
    ground()
    cactus()
    dino()  
    
    t.update()
    t.ontimer(mainloop, 30)

mainloop()
t.mainloop()
