#play around ,bouce around and fly into hyperspace
from tphysics import *
from random import randint
yspeed=0
xspeed=0
cyspeed=0
cxspeed=0
cometi=0
dock = False
con = False
game = Game("Rocket Game", "black", fullscreen=True)

s1 = Circle(randint(-300, 300), randint(-300,300) ,3)
s1.fill_colour ="white"
s2 = Circle(randint(-300, 300), randint(-300,300) ,3)
s2.fill_colour ="white"
s3 = Circle(randint(-300, 300), randint(-300,300) , 3)
s3.fill_colour ="white"
s4 = Circle(randint(-300, 300), randint(-300,300) , 3)
s4.fill_colour ="white"            
s5 = Circle(randint(-300, 300), randint(-300,300) , 3)
s5.fill_colour ="white"
s6 = Circle(randint(-300, 300), randint(-300,300) , 3)
s6.fill_colour ="white"
s7 = Circle(randint(-300, 300), randint(-300,300) ,3)
s7.fill_colour ="white"
s8 = Circle(randint(-300, 300), randint(-300,300) ,3)
s8.fill_colour ="white"
s9 = Circle(randint(-300, 300), randint(-300,300) , 3)
s9.fill_colour ="white"
s10 = Circle(randint(-300, 300), randint(-300,300) , 3)
s10.fill_colour ="white"            
s11 = Circle(randint(-300, 300), randint(-300,300) , 3)
s11.fill_colour ="white"
s12 = Circle(randint(-300, 300), randint(-300,300) , 3)
s12.fill_colour ="white"
p1 = Circle(0, 0, 75)
p1.fill_colour="grey"
p2 = Circle(350, 300, 50)
p2.fill_colour="grey"
p3 = Circle(-350, 300, 50)
p3.fill_colour="grey"
p4 = Circle(350, -260, 39)
p4.fill_colour="grey"
p5 = Circle(-350, -260, 57)
p5.fill_colour="grey"
rocket = Rectangle(0, 99, 15, 45)
comet = Circle(1000, 1000, 40)
land = Rectangle(0, 100, 30, 10)

comet.fill_colour="grey"
game.add_shape(s1)
game.add_shape(s2)
game.add_shape(s3)
game.add_shape(s4)
game.add_shape(s5)
game.add_shape(s6)
game.add_shape(s7)
game.add_shape(s8)
game.add_shape(s9)
game.add_shape(s10)
game.add_shape(s11)
game.add_shape(s12)
game.add_shape(p1)
game.add_shape(p2)
game.add_shape(p3)
game.add_shape(p4)
game.add_shape(p5)
game.add_shape(rocket)
game.add_shape(comet)
game.add_shape(land)
while True:
    cometi = randint(5, 518)
    if game.ispressed("w"):
        yspeed += 0.1
    if game.ispressed("d"):
        xspeed += 0.1
    if game.ispressed("a"):
        xspeed -= 0.1
    if game.ispressed("s"):
        yspeed -= 0.1
    if game.ispressed("c") and(rocket.collide(land)):
        dock = True
    if dock:
        rocket.y = land.y
        rocket.x = land.x
    if game.ispressed("g"):
        dock = False
    if rocket.collide(p1):
        xspeed *= -1
        yspeed *= -1
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
        xspeed *= -3.9
        yspeed *= -3.9
    if rocket.collide(comet):
        xspeed *= -3.9
        yspeed *= -3.9    
    if p1.collide(comet):
        cxspeed *= -1
        cyspeed *= -1
    if comet.collide(p2):
        cxspeed *= -1
        cyspeed *= randint(-1, 0)
    if comet.collide(p3):
        cxspeed *= -1
        cyspeed *= -0.7
    if comet.collide(p4):
        cxspeed *= -1
        cyspeed *= -0.7
    if comet.collide(p5):
        cxspeed *= -3.9
        cyspeed *= -3.9 
    if cometi == 517:
        comet.x = -1000
        comet.y = 5
        cxspeed = -35
        cyspeed = 0
        con = True
    if con:
        cxspeed = 5
        cyspeed = randint(-2, 2)
        con = False
    rocket.x += xspeed
    rocket.y += yspeed
    comet.x += cxspeed
    comet.y += cyspeed
    game.update()
