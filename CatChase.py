import pgzrun
from random import randint

HEIGHT= 500
WIDTH= 500
TITLE="CAT"

score=0
game_over=False

cat=Actor("cat")
rat=Actor("rat")

cat.pos=200,200

def draw():
    screen.blit("screen",(0,0))
    cat.draw()
    rat.draw()
    screen.draw.text("score:"+str(score),
                     topleft=(10, 10),
                     color="yellow")
    if game_over :
        screen.fill("RED")
        screen.draw.text("Time's up,you're final score is..."+str(score),
                         center=(200,250),
                         color="yellow")
def rat_place():
    rat.x=randint(45, 455)
    rat.y=randint(45, 455)

def update():
    global score  
    if keyboard.left:
        cat.x=cat.x-2
    if keyboard.right:
        cat.x=cat.x+2
    if keyboard.up:
        cat.y=cat.y-2
    if keyboard.down:
        cat.y=cat.y+2

    if cat.colliderect(rat):
        rat_place()
        score=score+10

def time_up():
    global game_over
    game_over= True

clock.schedule(time_up, 10.0)



pgzrun.go()
