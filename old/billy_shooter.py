import math
from tphysics import Game, Circle, Rectangle

game = Game("Shooter", "pink")

player = Rectangle(0, 0, 30, 30, "blue")
game.add_shape(player)

bullet = Circle(0, 0, 10, "red")

player_speed = 2
bullet_speed = 5

global bullet_x_speed
global bullet_y_speed

bullet_x_speed = 0
bullet_y_speed = 0

def click(x,y):
    global bullet_x_speed
    global bullet_y_speed
    
    dx = rocket.x - x
    dy = rocket.y - y

    v = math.sqrt(math.pow(dx,2) + math.pow(dy,2))
    ratio = bullet_speed / v

    bullet_x_speed = -(dx * ratio)
    bullet_y_speed = -(dy * ratio)

    game.add_shape(bullet)
    bullet.x = rocket.x
    bullet.y = rocket.y

game.addclick(click)

while True:

    if game.ispressed("w"):
        player.y += player_speed
    if game.ispressed("s"):
        player.y -= player_speed
    if game.ispressed("a"):
        player.x -= player_speed
    if game.ispressed("d"):
        player.x += player_speed

    bullet.x += bullet_x_speed + 5
    bullet.y += bullet_y_speed + 5

    game.update()
