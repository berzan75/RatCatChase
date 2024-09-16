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
        screen.fiil("RED")
        screen.draw.text("Time's up,you're final score is..."+str(score),
                         center=(200,250),
                         color="yellow")


pgzrun.go()