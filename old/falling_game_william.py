from tphysics import *
from random import randint

game = Game("Falling Game", 600, 600, "light blue")

player = Rectangle(0, -200, 40, 20)
player.fill_colour = "green"

coin = Circle(randint(-250,250), randint(250,300), 5)
coin.fill_colour = "yellow"

game.add_shape(player)
game.add_shape(coin)

score = 0
stamina =1000
speed = stamina / 475  #Whatever you put

while True:
    if not(game.ispressed("Left") or(game.ispressed("Right"))):
        stamina +=1
    if stamina > 1000:
        stamina = 1000
    if stamina < 0:
        stamina = 0
    game.update()

    coin.y -= 1

    if game.ispressed("Left"):
        player.x -= speed
        stamina -= 1
    if game.ispressed("Right"):
        player.x += speed
        stamina -= 1

    
    if player.collide(coin):
        coin.x = randint(-250,250)
        coin.y = randint(250,300)
        score += 1
