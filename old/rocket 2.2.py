#best version for speedometers and atmosphere planet update
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
planets = []

p1 = Circle(0, 0, 125)
p1.fill_colour="yellow"
planets.append(p1)
p2 = Circle(350, 300, 50)
p2.fill_colour="grey"
planets.append(p2)
p3 = Circle(-350, 300, 50)
p3.fill_colour="grey"
planets.append(p3)
p4 = Circle(350, -260, 39)
p4.fill_colour="grey"
planets.append(p4)
p5 = Circle(-350, -260, 57)
p5.fill_colour="grey"
planets.append(p5)
p6 = Circle(0, 300, 75)
p6.fill_colour="grey"
planets.append(p6)
p7 = Circle(650, 600, 50)
p7.fill_colour="grey"
planets.append(p7)
p8 = Circle(-350, 600, 50)
p8.fill_colour="grey"
planets.append(p8)
p9 = Circle(650, -560, 39)
p9.fill_colour="blue"
planets.append(p9)
p10 = Circle(-650, -560, 57)
p10.fill_colour="grey"
planets.append(p10)
p11 = Circle(0, 600, 75)
p11.fill_colour="grey"
planets.append(p11)
p12 = Circle(950, 900, 50)
p12.fill_colour="grey"
planets.append(p12)
p13 = Circle(-650, 900, 50)
p13.fill_colour="grey"
planets.append(p13)
p14 = Circle(950, -860, 39)
p14.fill_colour="grey"
planets.append(p14)
p15 = Circle(-950, -860, 57)
p15.fill_colour="grey"
planets.append(p15)
p16 = Circle(0, 900, 75)
p16.fill_colour="grey"
planets.append(p16)
p17 = Circle(1250, 1200, 50)
p17.fill_colour="grey"
planets.append(p17)
p18 = Circle(-950, 1200, 50)
p18.fill_colour="grey"
planets.append(p18)
p19 = Circle(1250, -1160, 39)
p19.fill_colour="grey"
planets.append(p19)
p20 = Circle(-1250, -1160, 57)
p20.fill_colour="grey"
planets.append(p20)
p21 = Circle(0, 1200, 75)
p21.fill_colour="grey"
planets.append(p21)
p22 = Circle(1550, 1500, 50)
p22.fill_colour="grey"
planets.append(p22)
p23 = Circle(-1250, 1500, 50)
p23.fill_colour="grey"
planets.append(p23)
p24 = Circle(1550, -1460, 39)
p24.fill_colour="grey"
planets.append(p24)
p25 = Circle(-1550, -1460, 57)
p25.fill_colour="grey"
planets.append(p25)
p26 = Circle(0, 1500, 75)
p26.fill_colour="grey"
planets.append(p26)
p27 = Circle(1850, 1800, 50)
p27.fill_colour="grey"
planets.append(p27)
p28 = Circle(-1550, 1800, 50)
p28.fill_colour="grey"
planets.append(p28)
p29 = Circle(1850, -1760, 39)
p29.fill_colour="blue"
planets.append(p29)
p30 = Circle(-1550, -1760, 57)
p30.fill_colour="grey"
planets.append(p30)
p31 = Circle(0, -300, 75)
p31.fill_colour="grey"
planets.append(p31)
p32 = Circle(0, -600, 75)
p32.fill_colour="grey"
planets.append(p32)
p33 = Circle(0, -900, 75)
p33.fill_colour="grey"
planets.append(p33)
p34 = Circle(0, -1200, 75)
p34.fill_colour="grey"
planets.append(p34)
p35 = Circle(0, -1800, 75)
p35.fill_colour="grey"
planets.append(p35)
a1 = Circle(0, -2300, 150)
a1.fill_colour="blue"
planets.append(a1)
a2 = Circle(0, -2300, 125)
a2.fill_colour="cyan"
planets.append(a2)
p36 = Circle(0, -2300, 75)
p36.fill_colour="green"
planets.append(p36)

rocket = Rectangle(0, 154, 15, 45)

for planet in planets:
    game.add_shape(planet)

game.add_shape(rocket)

while True:
    cometi = randint(5, 518)
    if game.ispressed("w"):
        yspeed -= 0.15
    if game.ispressed("d"):
        xspeed -= 0.15
    if game.ispressed("a"):
        xspeed += 0.15
    if game.ispressed("s"):
        yspeed += 0.15
    if rocket.collide(p1):
        xspeed *= 50
        yspeed *= 50
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
        for planet in planets:
            planet.x -= 1200 - xspeed * 30
            planet.y += 1200 + yspeed * 30
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
        for planet in planets:
            planet. x += 1200 + xspeed * 30
            planet.y -= 1200 - yspeed * 30
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
    if rocket.collide(p36):
        xspeed *= -1
        yspeed *= -1    
    if rocket.collide(a1):
        xspeed = xspeed *0.99
        yspeed = yspeed *0.99
    if rocket.collide(a2):
        xspeed = xspeed *0.95
        yspeed = yspeed *0.95    
    for planet in planets:
        planet.y += yspeed
        planet.x += xspeed

    game.update()
