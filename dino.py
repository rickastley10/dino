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

import turtle as t

# Add these at the top with your other global variables
onground = 1
frame = 0
jumping_up = False
jumping_down = False

def jump1(x, y):
    global onground, jumping_up, frame
    if onground == 1:
        onground = 0
        jumping_up = True
        jumping_down = False
        frame = 0
        jump1anim()  # Start immediately

def jump1anim():
    global dinoy, frame, jumping_up, jumping_down
    if jumping_up and frame < 30:
        dinoy += 1
        frame += 1
        t.ontimer(jump1anim, 10)
    elif frame >= 30 and jumping_up:
        jumping_up = False
        t.ontimer(start_fall, 1000)  # Wait 1 second

def start_fall():
    global jumping_down, frame
    jumping_down = True
    frame = 0
    jump2anim()

def jump2anim():
    global dinoy, frame, jumping_down, onground
    if jumping_down and frame < 30:
        dinoy -= 1
        frame += 1
        t.ontimer(jump2anim, 10)
    elif frame >= 30 and jumping_down:
        jumping_down = False
        onground = 1
        dinoy = 0  # Ensure exact position

t.onscreenclick(jump1)

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
