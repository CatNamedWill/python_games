from tphysics import *
from random import randint

game = Game("Falling Game", "light blue", fullscreen=True)

player = Rectangle(0, -200, 40, 20)
player.fill_colour = "cyan"

stop = Circle(0,1000, 750)
stop.fill_color = "blue"
boss = Circle(0, 15500, 100)
coin = Circle(randint(-250,250), randint(250,300), 5)
coin.fill_colour = "yellow"
bomb = Circle(randint(-250,250), randint(250,300), 5)
bomb.fill_colour = "black"
heart1 = Circle(-280, 268, 10)
heart1.fill_colour = "red"
heart2 = Circle(-260, 268, 10)
heart2.fill_colour = "red"
heart3 = Circle(-240, 268, 10)
heart3.fill_colour = "red"
game.add_shape(player)
game.add_shape(coin)
game.add_shape(bomb)
game.add_shape(heart1)
game.add_shape(heart2)
game.add_shape(heart3)
game.add_shape(boss)
game.add_shape(stop)
score = 0
scorey = score - 1000
lives = 3
stamina = 5000
boss_level = False

while True:

    if not(game.ispressed("Left") or(game.ispressed("Right"))):
        stamina += 0.1 
    if stamina < 0:
        stamina = 0
    if stamina > 1000 + score * 100:
        score = 1000 + score * 100
    coin.y -= 1
    bomb.y -= 1
    if game.ispressed("Left"):
        player.x -= stamina / 1425
        stamina -=1
    if game.ispressed("Right"):
        player.x += stamina / 1425
        stamina -= 1
    if player.collide(coin):
        coin.x = randint(-250,250)
        coin.y = randint(250,300)
        score +=1
    if coin.y < -200: 
        coin.x = randint(-250,250)
        coin.y = randint(250,300)
    if bomb.y < -200:
        bomb.x = randint(-250,250)
        bomb.y = randint(250,300)
    if player.collide(bomb):
        bomb.x = randint(-250,250)
        bomb.y = randint(250,300)
        lives -=1     
    if lives == 0:
        stop.y = 0
        break
    if score % 1 == 0:
        boss_level = True

    if lives < 3:
        heart3.y = 1000
    if lives < 2:
        heart2.y = 1000        
    if lives == 0:
        heart1.y = 1000
    if boss_level:
        boss.fill_colour = "red"
        game.fill_colour = "brown"
    if scorey == 14:
        player.fill_color = "black"

    game.write(-100, 100, f"Lives: {lives}", "black", 20)
    game.write(-100, 70, f"Score: {score - 1000 }", "black", 20)
    game.write(-100, 40, f"Boss level: {boss_level}", "black", 20)

    game.update()
