#1.4 but 10x bigger
from tphysics import *
from random import randint
yspeed=0
xspeed=0
score=1
fuel=50
stfuel=0
fuel_storage=50
p1p = False
p2p = False
p3p = False
p4p = False
p5p = False
p6p = False
p7p = False
p8p = False
p9p = False
p10p = False
p11p = False
p12p = False
p13p = False
p14p = False
p15p = False
p16p = False
p17p = False
p18p = False
p19p = False
p20p = False
p21p = False
p22p = False
p23p = False
p24p = False
p25p = False
p26p = False
p27p = False
p28p = False
p29p = False
p30p = False
p31p = False
p32p = False
p33p = False
p34p = False
p35p = False
p36p = False
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
station = Rectangle(0, 0, 20, 105)
rocket = Rectangle(0, 0, 15, 45)
for other in others:
    game.add_shape(other)
for planet in planets:
    game.add_shape(planet)    
game.add_shape(rocket)
game.add_shape(station)
for other in others:
    other.y += 1275
for planet in planets:
    planet.y += 1275
while True:
    game.write(200, 100, f"fuel: {fuel}", "white", 20)
    game.write(200, 80, f"fuel_storage: {fuel_storage}", "white", 20)
    if station.collide(rocket)and(not(fuel == fuel_storage)):
        fuel += 1
    if game.ispressed("w") and(not(fuel == 0 or (fuel < 0))):
        yspeed -= 0.3 * score
        fuel -= 1
    if game.ispressed("d") and(not(fuel == 0 or (fuel < 0))):
        xspeed -= 0.3 * score
        fuel -= 1
    if game.ispressed("a") and(not(fuel == 0 or (fuel < 0))):
        xspeed += 0.3 * score
        fuel -= 1
    if game.ispressed("s") and(not(fuel == 0 or (fuel < 0))):
        yspeed += 0.3 * score
        fuel -= 1
    if game.ispressed("b") and(not(fuel == 0 or (fuel < 0))):
        yspeed /= 2
        xspeed /= 2
        fuel -= 2
    if rocket.collide(p1):
        xspeed *= 1.5
        yspeed *= 1.5    
    for planet in planets:
        if rocket.collide(planet):
            xspeed *= -1
            yspeed *= -1
            if rocket.collide(p1) and(p1p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p2) and(p2p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p3) and(p3p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p4) and(p4p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p5) and(p5p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p6) and(p6p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p7) and(p7p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p8) and(p8p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p9) and(p9p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p10) and(p10p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p11) and(p11p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p12) and(p12p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p13) and(p13p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p14) and(p14p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p15) and(p15p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p16) and(p16p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p17) and(p17p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p18) and(p18p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p19) and(p19p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p20) and(p20p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p21) and(p21p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p22) and(p22p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p23) and(p23p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p24) and(p24p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p25) and(p25p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p26) and(p26p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p27) and(p27p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p28) and(p28p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p29) and(p29p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p30) and(p30p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p31) and(p31p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p32) and(p32p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p33) and(p33p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p34) and(p34p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p35) and(p35p == False):
                score += 1
                fuel_storage += 50
            if rocket.collide(p36) and(p36p == False):
                score += 1
                fuel_storage += 50
    if rocket.collide(a1):
        xspeed = xspeed *0.99
        yspeed = yspeed *0.99
    if rocket.collide(a2):
        xspeed = xspeed *0.95
        yspeed = yspeed *0.95    
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
    for planet in planets:
        planet.y += yspeed
        planet.x += xspeed
    for other in others:
        other.y += yspeed
        other.x += xspeed
    station.y += yspeed
    station.x += xspeed
    game.update()
