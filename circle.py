#!/usr/bin/python3

import turtle
import sys
import math
import colorsys

radius = float(sys.argv[1])
x = 0
y = 0

turtle.width(8)

# go to starting point
turtle.up()
start_x = x + radius * math.cos(0)
start_y = y - radius * math.sin(0)
turtle.setpos(start_x, start_y)
turtle.down()

# draw circle
for i in range(0, 1000):
    alpha = 2*math.pi*i/1000
    new_x = x + radius * math.cos(alpha)
    new_y = y - radius * math.sin(alpha)
    turtle.goto(new_x, new_y)
    turtle.pencolor(colorsys.hsv_to_rgb(i / 1000, 0.75, 0.75))

turtle.Screen().exitonclick()
