# supplements v2.4 refactored by Billy
from tphysics import Circle

planets = [
    p2 = Circle(3500, 3000, 500, "grey"), 
    p3 = Circle(-3500, 3000, 500, "grey"),
    p4 = Circle(3500, -2600, 390, "grey"),
    p5 = Circle(-3500, -2600, 570, "grey"),
    p6 = Circle(0, 3000, 750, "grey"),
    p7 = Circle(6500, 6000, 500, "grey"),
    p8 = Circle(-3500, 6000, 500, "grey"),
    p10 = Circle(-6500, -5600, 570, "grey"),
    p11 = Circle(0, 6000, 750, "grey"),
    p12 = Circle(9500, 9000, 500, "grey"),
    p13 = Circle(-6500, 9000, 500, "grey"),
    p14 = Circle(9500, -8600, 390, "grey"),
    p15 = Circle(-9500, -8600, 570, "grey"),
    p16 = Circle(0, 9000, 750, "grey"),
    p17 = Circle(12500, 12000, 500, "grey"),
    p18 = Circle(-9500, 12000, 500, "grey"),
    p20 = Circle(12500, -11600, 390, "grey"),
    p21 = Circle(-12500, -11600, 570, "grey"),
    p22 = Circle(0, 12000, 750, "grey"),
    p23 = Circle(15500, 15000, 500, "grey"),
    p24 = Circle(-12500, 15000, 500, "grey"),
    p25 = Circle(15500, -14600, 390, "grey"),
    p26 = Circle(-15500, -14600, 570, "grey"),
    p27 = Circle(0, 15000, 750, "grey"),
    p28 = Circle(18500, 18000, 500, "grey"),
    p29 = Circle(-15500, 18000, 500, "grey"),
    p30 = Circle(-15500, -17600, 570, "grey"),
    p31 = Circle(0, -3000, 750, "grey"),
    p32 = Circle(0, -6000, 750, "grey"),
    p33 = Circle(0, -9000, 750, "grey"),
    p34 = Circle(0, -1200, 750, "grey"),
    p35 = Circle(0, -1800, 750, "grey")            
]

sun = Circle(0, 0, 1250, "yellow")

portal_one = Circle(650, -560, 39, "blue")
portal_two = Circle(1850, -1760, 39, "blue")

a1 = Circle(0, -23000, 150, "blue")
a2 = Circle(0, -23000, 125, "cyan")
p36 = Circle(0, -23000, 750, "green")

planets.append(p36)
others = [
    sun,
    portal_one,
    portal_two,
    outer_atmosphere,
    inner_atmosphere
]
