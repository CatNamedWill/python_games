from tphysics import *
from random import randint
gravity = 0
ix=0
iy=0
xspeed=0
yspeed=0
score = 0
fly = False
show = False
game = Game("Cannon", "light blue", fullscreen=True)

shell = Circle(-300, -150, 5)
metery = Rectangle(-300, -150, 20, 20)
meterx = Rectangle(-300, -150, 20, 20)
ground = Rectangle(0, -300, 1500000, 89)
target = Circle(-300, -150, 15)
ground.fill_colour = "green"
game.add_shape(shell)
game.add_shape(meterx)
game.add_shape(ground)
game.add_shape(target)
target.y = ground.y + 37.5
target.x = randint(20, 278)
while True:
    game.write(200, 100, f"yspeed: {round(yspeed,1)}", "black", 20)
    game.write(200, 70, f"xspeed: {round(xspeed,1)}", "black", 20)
    if show:
        game.write(0, 0, f"hit", "black", 20)
    if shell.collide(target):
        target.x = randint(20, 278)
        show = True
    if game.ispressed("Right"):
       if not(fly):
            ix += 0.1
            meterx.x += 2.5 + xspeed / 2.5
    if game.ispressed("Left"):
       if not(fly):
            ix -= 0.1
            meterx.x -= 2.5 + xspeed / 2.5
            ix -= 0.1
    if game.ispressed("Up"):
        if not(fly):
            iy += 0.1
            meterx.x += 0.75
    if game.ispressed("Down"):
        if not(fly):
            iy -= 0.1
            meterx.x -= 0.75
    if game.ispressed("g"):
        yspeed = iy
        xspeed = ix
        show = False
        fly = True
    if game.ispressed("r"):
        fly = False
        shell.x = -300
        shell.y = -150
    if fly:
        
        gravity = -0.8000000000000000000000000000000099999999999999999
        if not(shell.collide(ground)):               
            shell.x = shell.x + xspeed
            shell.y = shell.y + yspeed
            yspeed += gravity
    if game.ispressed("r"):
        target.y = ground.y + 37.5
        shell.y = -150
        shell.x = -350
        gravity = 0
        fly = False
    game.update()
