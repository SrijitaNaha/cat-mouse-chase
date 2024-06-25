import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

score = 0
game_over = False

cat = Actor("cat")
cat.pos = 100,100

rat = Actor("rat")
rat.pos = 200,200

def draw():
    screen.blit("background", (0,0))
    rat.draw()
    cat.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
            screen.fill("pink")
            screen.draw.text("Time's Up! Your Final Score: " + str(score), midtop=(WIDTH/2,10), 
            fontsize=40, color="red")


def place_rat():
    rat.x = randint(70, (WIDTH-70))
    rat.y = randint(70, (HEIGHT-70))


def time_up():
    global game_over 
    game_over = True

def update():
    global score

    if keyboard.left:
        cat.x = cat.x - 2
    if keyboard.right:
        cat.x = cat.x + 2
    if keyboard.up:
        cat.y = cat.y - 2
    if keyboard.down:
        cat.y = cat.y + 2

    rat_collected = cat.colliderect(rat)

    if rat_collected:
        score = score + 10
        place_rat()


clock.schedule(time_up, 60.0)



pgzrun.go()

