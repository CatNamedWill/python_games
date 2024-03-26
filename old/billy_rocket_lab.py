import math
from tphysics import Circle, Game
from random import randint

score = 0

game = Game("Rocket Game", "black")

target = Circle(randint(-100, 100), randint(-100, 100), 5, "yellow")
game.add_shape(target)


rocket = Circle(0, 0, 20, "grey")
game.add_shape(rocket)

rocket_trail = Circle(30, 0, 5+score, "red")
game.add_shape(rocket_trail)

rocket_distance = 30
direction = 0
tricky = 0
def calculate_rocket_trail_position():
    rocket_trail.x = rocket.x + (rocket_distance * math.sin(math.radians(direction)))
    rocket_trail.y = rocket.y + (rocket_distance * math.cos(math.radians(direction)))

while True:
    #target.y += randint(-3 - tricky, 3 + tricky)
    #target.x += randint(-3 - tricky, 3 + tricky)
    game.write(200, 100, f"score: {score}", "white", 20)
    if rocket.collide(target):
        score += 1
        tricky +=1
        target.y = randint(-100, 100)
        target.x = randint(-100, 100)  
    if game.ispressed("Left"):
        direction -= 3 + score / 10
        direction %= 360
    if game.ispressed("Right"):
        direction += 3
        direction %= 360

    if game.ispressed("space"):
        if rocket_distance < 50:
            rocket_distance += 1
    else:
        if rocket_distance > 30:
            rocket_distance -= 1

    frame_speed = rocket_distance - 30
    rocket.x -= (frame_speed * math.sin(math.radians(direction))) * 0.3 + score / 30
    rocket.y -= (frame_speed * math.cos(math.radians(direction))) * 0.3 + score / 30

    calculate_rocket_trail_position()

    game.update()

  
