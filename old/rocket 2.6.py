#1.4 but 100x bigger and new control: atmosphere boost
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
p1 = Circle(0, 0, 12500)
p1.fill_colour="yellow"
others.append(p1)
p2 = Circle(35000, 30000, 5000)
p2.fill_colour="grey"
planets.append(p2)
p3 = Circle(-35000, 30000, 5000)
p3.fill_colour="grey"
planets.append(p3)
p4 = Circle(35000, -26000, 3900)
p4.fill_colour="grey"
planets.append(p4)
p5 = Circle(-35000, -26000, 5700)
p5.fill_colour="grey"
planets.append(p5)
p6 = Circle(0, 30000, 75000)
p6.fill_colour="grey"
planets.append(p6)
p7 = Circle(65000, 60000, 5000)
p7.fill_colour="grey"
planets.append(p7)
p8 = Circle(-35000, 60000, 5000)
p8.fill_colour="grey"
planets.append(p8)
p9 = Circle(65000, -56000, 3900)
p9.fill_colour="blue"
others.append(p9)
p10 = Circle(-65000, -56000, 5700)
p10.fill_colour="grey"
planets.append(p10)
p11 = Circle(0, 60000, 7500)
p11.fill_colour="grey"
planets.append(p11)
p12 = Circle(95000, 90000, 5000)
p12.fill_colour="grey"
planets.append(p12)
p13 = Circle(-65000, 90000, 5000)
p13.fill_colour="grey"
planets.append(p13)
p14 = Circle(95000, -86000, 3900)
p14.fill_colour="grey"
planets.append(p14)
p15 = Circle(-95000, -86000, 5700)
p15.fill_colour="grey"
planets.append(p15)
p16 = Circle(0, 90000, 7500)
p16.fill_colour="grey"
planets.append(p16)
p17 = Circle(125000, 120000, 5000)
p17.fill_colour="grey"
planets.append(p17)
p18 = Circle(-95000, 120000, 5000)
p18.fill_colour="grey"
planets.append(p18)
p19 = Circle(125000, -116000, 3900)
p19.fill_colour="grey"
planets.append(p19)
p20 = Circle(-125000, -116000, 5700)
p20.fill_colour="grey"
planets.append(p20)
p21 = Circle(0, 120000, 7500)
p21.fill_colour="grey"
planets.append(p21)
p22 = Circle(155000, 150000, 5000)
p22.fill_colour="grey"
planets.append(p22)
p23 = Circle(-125000, 150000, 5000)
p23.fill_colour="grey"
planets.append(p23)
p24 = Circle(155000, -146000, 3900)
p24.fill_colour="grey"
planets.append(p24)
p25 = Circle(-155000, -146000, 5700)
p25.fill_colour="grey"
planets.append(p25)
p26 = Circle(0, 150000, 7500)
p26.fill_colour="grey"
planets.append(p26)
p27 = Circle(185000, 180000, 5000)
p27.fill_colour="grey"
planets.append(p27)
p28 = Circle(-155000, 180000, 5000)
p28.fill_colour="grey"
planets.append(p28)
p29 = Circle(185000, -176000, 3900)
p29.fill_colour="blue"
others.append(p29)
p30 = Circle(-155000, -176000, 5700)
p30.fill_colour="grey"
planets.append(p30)
p31 = Circle(0, -30000, 7500)
p31.fill_colour="grey"
planets.append(p31)
p32 = Circle(0, -60000, 7500)
p32.fill_colour="grey"
planets.append(p32)
p33 = Circle(0, -90000, 7500)
p33.fill_colour="grey"
planets.append(p33)
p34 = Circle(0, -120000, 7500)
p34.fill_colour="grey"
planets.append(p34)
p35 = Circle(0, -180000, 7500)
p35.fill_colour="grey"
planets.append(p35)
a1 = Circle(0, -230000, 15000)
a1.fill_colour="blue"
others.append(a1)
a2 = Circle(0, -230000, 12500)
a2.fill_colour="cyan"
others.append(a2)
p36 = Circle(0, -230000, 7500)
p36.fill_colour="green"
planets.append(p36)
rocket = Rectangle(0, 0, 15, 45)
for other in others:
    game.add_shape(other)
for planet in planets:
    game.add_shape(planet)    
game.add_shape(rocket)
for other in others:
    other.y += 215000
for planet in planets:
    planet.y += 215000
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
    if game.ispressed("z") and(rocket.collide(a1)or(rocket.collide(a2))):
        yspeed *= 2
        xspeed *= 2    
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
