from tphysics import *
from random import randint
gravity = 0
ix=0
iy=0.7333333333333333333333333333333333333333333333333333
xspeed=0
yspeed=0
score = 0
fly = False
show = False
game = Game("Cannon", "light blue", fullscreen=True)

shell = Rectangle(-300, -150, 10, 25)
metery = Rectangle(-300, -150, 20, 20)
meterx = Rectangle(-300, -150, 20, 20)
ground = Rectangle(0, -300, 1500000, 150)
ground.fill_colour = "grey"
target = Circle(-300, -150, 15)
ground.fill_colour = "green"
game.add_shape(shell)
game.add_shape(ground)
target.y = ground.y + 37.5
target.x = randint(20, 278)
while True:
    game.write(200, 100, f"yspeed: {round(yspeed,1)}", "black", 20)
    game.write(200, 70, f"xspeed: {round(xspeed,1)}", "black", 20)
    if fly and(game.ispressed("a")):
               xspeed -= 0.3
    if fly and(game.ispressed("d")):
               xspeed += 0.3
    if fly and(game.ispressed("w")):
               yspeed += 0.8
    if fly and(game.ispressed("s")):
               yspeed -= 0.8
    if fly and(game.ispressed("e")):
               xspeed += 0.81
               yspeed += 0.81
    if fly and(game.ispressed("q")):
               xspeed -= 0.81
               yspeed -= 0.81           
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
        gravity = -0.1333333333333333333333333333333333333333333333333333333
        if shell.collide(ground):
            shell.y = ground.y + 77
            
        
            if (yspeed > -4) and ((xspeed < 4) and (xspeed > -4)):
                if fly:
                    game.write(0, 0, f"win", "black", 20)
            else:
                if fly:
                    game.write(0, 0, f"crash", "black", 20)
        if not(shell.collide(ground)):               
            shell.x = shell.x + xspeed
            shell.y = shell.y + yspeed
            yspeed -= gravity
            xspeed -= gravity
    if game.ispressed("r"):
        target.y = ground.y + 37.5
        shell.y = -150
        shell.x = -350
        gravity = 0
        fly = False
    game.update()
