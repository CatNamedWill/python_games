#1.0 just bigger 
from tphysics import *
from random import randint
yspeed=0
xspeed=0
cyspeed=0
cxspeed=0
lxspeed=0
lyspeed=0
cometi=0
dock = False
con = False
game = Game("Rocket Game", "black", fullscreen=True)
p1 = Circle(0, 0, 125)
p1.fill_colour="yellow"
p2 = Circle(350, 300, 50)
p2.fill_colour="grey"
p3 = Circle(-350, 300, 50)
p3.fill_colour="grey"
p4 = Circle(350, -260, 39)
p4.fill_colour="grey"
p5 = Circle(-350, -260, 57)
p5.fill_colour="grey"
p6 = Circle(0, 300, 75)
p6.fill_colour="grey"
p7 = Circle(650, 600, 50)
p7.fill_colour="grey"
p8 = Circle(-350, 600, 50)
p8.fill_colour="grey"
p9 = Circle(650, -560, 39)
p9.fill_colour="grey"
p10 = Circle(-650, -560, 57)
p10.fill_colour="grey"
p11 = Circle(0, 600, 75)
p11.fill_colour="grey"
p12 = Circle(950, 900, 50)
p12.fill_colour="grey"
p13 = Circle(-650, 900, 50)
p13.fill_colour="grey"
p14 = Circle(950, -860, 39)
p14.fill_colour="grey"
p15 = Circle(-950, -860, 57)
p15.fill_colour="grey"
p16 = Circle(0, 900, 75)
p16.fill_colour="grey"
p17 = Circle(1250, 1200, 50)
p17.fill_colour="grey"
p18 = Circle(-950, 1200, 50)
p18.fill_colour="grey"
p19 = Circle(1250, -1160, 39)
p19.fill_colour="grey"
p20 = Circle(-1250, -1160, 57)
p20.fill_colour="grey"
p21 = Circle(0, 1200, 75)
p21.fill_colour="grey"
p22 = Circle(1550, 1500, 50)
p22.fill_colour="grey"
p23 = Circle(-1250, 1500, 50)
p23.fill_colour="grey"
p24 = Circle(1550, -1460, 39)
p24.fill_colour="grey"
p25 = Circle(-1550, -1460, 57)
p25.fill_colour="grey"
p26 = Circle(0, 1500, 75)
p26.fill_colour="grey"
p27 = Circle(1850, 1800, 50)
p27.fill_colour="grey"
p28 = Circle(-1550, 1800, 50)
p28.fill_colour="grey"
p29 = Circle(1850, -1760, 39)
p29.fill_colour="grey"
p30 = Circle(-1550, -1760, 57)
p30.fill_colour="grey"
p31 = Circle(0, -300, 75)
p31.fill_colour="grey"
p32 = Circle(0, -600, 75)
p32.fill_colour="grey"
p33 = Circle(0, -900, 75)
p33.fill_colour="grey"
p34 = Circle(0, -1200, 75)
p34.fill_colour="grey"
p34 = Circle(0, -1500, 75)
p34.fill_colour="grey"
p35 = Circle(0, -1800, 75)
p35.fill_colour="grey"
rocket = Rectangle(0, 154, 15, 45)
game.add_shape(p1)
game.add_shape(p2)
game.add_shape(p3)
game.add_shape(p4)
game.add_shape(p5)
game.add_shape(p6)
game.add_shape(p7)
game.add_shape(p8)
game.add_shape(p9)
game.add_shape(p10)
game.add_shape(p11)
game.add_shape(p12)
game.add_shape(p13)
game.add_shape(p14)
game.add_shape(p15)
game.add_shape(p16)
game.add_shape(p17)
game.add_shape(p18)
game.add_shape(p19)
game.add_shape(p20)
game.add_shape(p21)
game.add_shape(p22)
game.add_shape(p23)
game.add_shape(p24)
game.add_shape(p25)
game.add_shape(p26)
game.add_shape(p27)
game.add_shape(p28)
game.add_shape(p29)
game.add_shape(p30)
game.add_shape(p31)
game.add_shape(p32)
game.add_shape(p33)
game.add_shape(p34)
game.add_shape(p35)
game.add_shape(rocket)
while True:
    cometi = randint(5, 518)
    if game.ispressed("w"):
        yspeed -= 0.1
    if game.ispressed("d"):
        xspeed -= 0.1
    if game.ispressed("a"):
        xspeed += 0.1
    if game.ispressed("s"):
        yspeed += 0.1
    if rocket.collide(p1):
        xspeed *= 1.3
        yspeed *= 1.3
    if rocket.collide(p2):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p3):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p4):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p5):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p6):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p7):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p8):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p9):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p10):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p11):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p12):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p13):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p14):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p15):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p16):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p17):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p18):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p19):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p20):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p21):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p22):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p23):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p24):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p25):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p26):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p27):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p28):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p29):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p30):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p31):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p32):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p33):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p34):
        xspeed *= -1
        yspeed *= -1
    if rocket.collide(p35):
        xspeed *= -1
        yspeed *= -1     
    p1.y += yspeed
    p2.y += yspeed
    p3.y += yspeed
    p4.y += yspeed
    p5.y += yspeed
    p1.x += xspeed
    p2.x += xspeed
    p3.x += xspeed
    p4.x += xspeed
    p5.x += xspeed
    p6.x += xspeed
    p7.x += xspeed
    p8.x += xspeed
    p9.x += xspeed
    p11.x += xspeed
    p12.x += xspeed
    p13.x += xspeed
    p14.x += xspeed
    p10.x += xspeed
    p15.x += xspeed
    p16.x += xspeed
    p17.x += xspeed
    p18.x += xspeed
    p19.x += xspeed
    p20.x += xspeed
    p21.x += xspeed
    p22.x += xspeed
    p23.x += xspeed
    p24.x += xspeed
    p25.x += xspeed
    p26.x += xspeed
    p27.x += xspeed
    p28.x += xspeed
    p29.x += xspeed
    p30.x += xspeed
    p31.x += xspeed
    p32.x += xspeed
    p33.x += xspeed
    p34.x += xspeed
    p35.x += xspeed
    p6.y += yspeed
    p7.y += yspeed
    p8.y += yspeed
    p9.y += yspeed
    p10.y += yspeed
    p11.y += yspeed
    p12.y += yspeed
    p13.y += yspeed
    p14.y += yspeed
    p15.y += yspeed
    p16.y += yspeed
    p17.y += yspeed
    p18.y += yspeed
    p19.y += yspeed
    p20.y += yspeed
    p21.y += yspeed
    p22.y += yspeed
    p23.y += yspeed
    p24.y += yspeed
    p25.y += yspeed
    p26.y += yspeed
    p27.y += yspeed
    p28.y += yspeed
    p29.y += yspeed
    p30.y += yspeed
    p31.y += yspeed
    p32.y += yspeed
    p33.y += yspeed
    p34.y += yspeed
    p35.y += yspeed
    game.update()
