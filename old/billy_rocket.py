import math
from tphysics import Circle, Game

game = Game("Rocket Game", "black")

rocket = Circle(0, 0, 20, "grey")
game.add_shape(rocket)

rocket_trail = Circle(30, 0, 5, "red")
game.add_shape(rocket_trail)

rocket_distance = 30
direction = 0
def calculate_rocket_trail_position():
    rocket_trail.x = rocket.x + (rocket_distance * math.sin(math.radians(direction)))
    rocket_trail.y = rocket.y + (rocket_distance * math.cos(math.radians(direction)))

while True:
    if game.ispressed("Left"):
        direction -= 1
        direction %= 360
    if game.ispressed("Right"):
        direction += 1
        direction %= 360

    if game.ispressed("space"):
        if rocket_distance < 50:
            rocket_distance += 1
    else:
        if rocket_distance > 30:
            rocket_distance -= 1

    frame_speed = rocket_distance - 30
    rocket.x -= (frame_speed * math.sin(math.radians(direction))) * 0.1
    rocket.y -= (frame_speed * math.cos(math.radians(direction))) * 0.1

    calculate_rocket_trail_position()

    game.update()
