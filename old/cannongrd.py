from tphysics import *
gravity = 0
xspeed=0
yspeed=0
fly = False
game = Game("Cannon", "light blue", fullscreen=True)

shell = Circle(-300, -150, 5)
metery = Rectangle(-300, -150, 20, 20)
meterx = Rectangle(-300, -150, 20, 20)
ground = Rectangle(0, -300, 1500000, 89)
ground.fill_colour = "green"
game.add_shape(shell)
game.add_shape(meterx)
game.add_shape(ground)
while True:
    game.write(200, 100, f"yspeed: {round(yspeed,1)}", "black", 20)
    game.write(200, 70, f"xspeed: {round(xspeed,1)}", "black", 20)
    if game.ispressed("Right"):
       xspeed += 0.1
       meterx.x += 2.5 + xspeed / 2.5
    if game.ispressed("Left"):
       xspeed -= 0.1
       meterx.x -= 2.5 + xspeed / 2.5
    if game.ispressed("Up"):
        yspeed += 0.1
        meterx.x += 0.75
    if game.ispressed("Down"):
        yspeed -= 0.1
        meterx.x -= 0.75    
    if game.ispressed("g"):
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
        shell.y = -150
        shell.x = -350
        xspeed = 0
        yspeed = 0
        gravity = 0
        fly = False
        meterx.x = -300
    game.update()
