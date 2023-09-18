# pip install vpython
from vpython import *

canvas(background = color.orange)
circle_1 = ring(radius = 0.55, thickness = 0.25, color = vector(400, 300, 200))
circle_2 = ring(radius = 0.6, thickness = 0.25, color = vector(0.4, 0.2, 0.9))
radii = 0

while True:
    rate(12)
    circle_1.pos = vector(3 * cos(radii), sin(radii), 0.3)
    circle_2.pos = vector(3 * cos(radii), sin(radii), 0.3)
    radii += 0.03
