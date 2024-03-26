#1.4 but 10x bigger
from tphysics import *
from random import randint
yspeed=0
xspeed=0
cyspeed=0
cxspeed=0
cometi=0
game = Game("Rocket Game", "black", fullscreen=True)
planets = []
others = []
p1 = Circle(0, 0, 1250)
p1.fill_colour="yellow"
others.append(p1)
p2 = Circle(3500, 3000, 500)
p2.fill_colour="grey"
planets.append(p2)
p3 = Circle(-3500, 3000, 500)
p3.fill_colour="grey"
planets.append(p3)
p4 = Circle(3500, -2600, 390)
p4.fill_colour="grey"
planets.append(p4)
p5 = Circle(-3500, -2600, 570)
p5.fill_colour="grey"
planets.append(p5)
p6 = Circle(0, 3000, 750)
p6.fill_colour="grey"
planets.append(p6)
p7 = Circle(6500, 6000, 500)
p7.fill_colour="grey"
planets.append(p7)
p8 = Circle(-3500, 6000, 500)
p8.fill_colour="grey"
planets.append(p8)
p9 = Circle(6500, -5600, 390)
p9.fill_colour="blue"
others.append(p9)
p10 = Circle(-6500, -5600, 570)
p10.fill_colour="grey"
planets.append(p10)
p11 = Circle(0, 6000, 750)
p11.fill_colour="grey"
planets.append(p11)
p12 = Circle(9500, 9000, 500)
p12.fill_colour="grey"
planets.append(p12)
p13 = Circle(-6500, 9000, 500)
p13.fill_colour="grey"
planets.append(p13)
p14 = Circle(9500, -8600, 390)
p14.fill_colour="grey"
planets.append(p14)
p15 = Circle(-9500, -8600, 570)
p15.fill_colour="grey"
planets.append(p15)
p16 = Circle(0, 9000, 750)
p16.fill_colour="grey"
planets.append(p16)
p17 = Circle(12500, 12000, 500)
p17.fill_colour="grey"
planets.append(p17)
p18 = Circle(-9500, 12000, 500)
p18.fill_colour="grey"
planets.append(p18)
p19 = Circle(12500, -11600, 390)
p19.fill_colour="grey"
planets.append(p19)
p20 = Circle(-12500, -11600, 570)
p20.fill_colour="grey"
planets.append(p20)
p21 = Circle(0, 12000, 750)
p21.fill_colour="grey"
planets.append(p21)
p22 = Circle(15500, 15000, 500)
p22.fill_colour="grey"
planets.append(p22)
p23 = Circle(-12500, 15000, 500)
p23.fill_colour="grey"
planets.append(p23)
p24 = Circle(15500, -14600, 390)
p24.fill_colour="grey"
planets.append(p24)
p25 = Circle(-15500, -14600, 570)
p25.fill_colour="grey"
planets.append(p25)
p26 = Circle(0, 15000, 750)
p26.fill_colour="grey"
planets.append(p26)
p27 = Circle(18500, 18000, 500)
p27.fill_colour="grey"
planets.append(p27)
p28 = Circle(-15500, 18000, 500)
p28.fill_colour="grey"
planets.append(p28)
p29 = Circle(18500, -17600, 390)
p29.fill_colour="blue"
others.append(p29)
p30 = Circle(-15500, -17600, 570)
p30.fill_colour="grey"
planets.append(p30)
p31 = Circle(00, -3000, 750)
p31.fill_colour="grey"
planets.append(p31)
p32 = Circle(0, -6000, 750)
p32.fill_colour="grey"
planets.append(p32)
p33 = Circle(0, -9000, 750)
p33.fill_colour="grey"
planets.append(p33)
p34 = Circle(0, -12000, 750)
p34.fill_colour="grey"
planets.append(p34)
p35 = Circle(0, -18000, 750)
p35.fill_colour="grey"
planets.append(p35)
a1 = Circle(0, -23000, 1500)
a1.fill_colour="blue"
others.append(a1)
a2 = Circle(0, -23000, 1250)
a2.fill_colour="cyan"
others.append(a2)
p36 = Circle(0, -23000, 750)
p36.fill_colour="green"
planets.append(p36)
rocket = Rectangle(0, 0, 15, 45)
for other in others:
    game.add_shape(other)
for planet in planets:
    game.add_shape(planet)    
game.add_shape(rocket)
for other in others:
    other.y += 1275
for planet in planets:
    planet.y += 1275
while True:
    if game.ispressed("w"):
        yspeed -= 0.3
    if game.ispressed("d"):
        xspeed -= 0.3
    if game.ispressed("a"):
        xspeed += 0.3
    if game.ispressed("s"):
        yspeed += 0.3
    if game.ispressed("b"):
        yspeed /= 2
        xspeed /= 2
    if rocket.collide(p1):
        xspeed *= 1.5
        yspeed *= 1.5
    for planet in planets:
        if rocket.collide(planet):
            xspeed *= -1
            yspeed *= -1
    if rocket.collide(p9):
        for planet in planets:
            planet.x -= 1200 - xspeed * 30
            planet.y += 1200 + yspeed * 30
        for other in others:
            other.x -= 1200 - xspeed * 30
            other.y += 1200 + yspeed * 30    
    if rocket.collide(p29):
        for planet in planets:
            planet. x += 1200 + xspeed * 30
            planet.y -= 1200 - yspeed * 30
        for other in others:
            other.x += 1200 + xspeed * 30
            other.y -= 1200 - yspeed * 30    
    if rocket.collide(a1):
        xspeed = xspeed *0.99
        yspeed = yspeed *0.99
    if rocket.collide(a2):
        xspeed = xspeed *0.95
        yspeed = yspeed *0.95    
    for planet in planets:
        planet.y += yspeed
        planet.x += xspeed
    for other in others:
        other.y += yspeed
        other.x += xspeed    
    game.update()
