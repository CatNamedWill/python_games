#2.4, refactored by Billy
from tphysics import *
from random import randint
from entities import *

yspeed=0
xspeed=0
cyspeed=0
cxspeed=0
cometi=0

game = Game("Rocket Game", "black", fullscreen=True)

rocket = Rectangle(0, 154, 15, 45)

for other in others:
    game.add_shape(other)
for planet in planets:
    game.add_shape(planet)

game.add_shape(rocket)
while True:

    # Player movement checks
    if game.ispressed("w"):
        yspeed -= 0.15
    if game.ispressed("d"):
        xspeed -= 0.15
    if game.ispressed("a"):
        xspeed += 0.15
    if game.ispressed("s"):
        yspeed += 0.15
    if game.ispressed("b"):
        yspeed /= 2
        xspeed /= 2

    # Sun collision
    if rocket.collide(sun):
        xspeed *= 1.5
        yspeed *= 1.5

    # Planet collision
    for planet in planets:
        if rocket.collide(planet):
            xspeed *= -1
            yspeed *= -1

    # Teleport portal one
    if rocket.collide(portal_one):
        for planet in planets:
            planet.x -= 1200 - xspeed * 30
            planet.y += 1200 + yspeed * 30
        for other in others:
            other.x -= 1200 - xspeed * 30
            other.y += 1200 + yspeed * 30

    # Teleport portal two
    if rocket.collide(portal_two):
        for planet in planets:
            planet. x += 1200 + xspeed * 30
            planet.y -= 1200 - yspeed * 30
        for other in others:
            other.x += 1200 + xspeed * 30
            other.y -= 1200 - yspeed * 30

    # Atmosphere
    if rocket.collide(outer_atmosphere):
        xspeed = xspeed *0.99
        yspeed = yspeed *0.99
    if rocket.collide(inner_atmosphere):
        xspeed = xspeed *0.95
        yspeed = yspeed *0.95

    # Move planets in inverse direction to player speed
    for planet in planets:
        planet.y += yspeed
        planet.x += xspeed
    for other in others:
        other.y += yspeed
        other.x += xspeed

    # Render next frame
    game.update()
