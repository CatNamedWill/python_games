from tphysics import *
from time import sleep

game = Game("Cloning game", "black")

x = -200
y = 200
direction = 1

while True:
    game.add_shape(Circle(x,y,5,"white"))
    x += 10 * direction
    if x == 200 or x == -200:
        direction = direction * -1
        y -= 10
    game.update()

    if y == -200:
        break
