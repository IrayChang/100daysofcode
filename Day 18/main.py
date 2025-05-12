import colorgram

colors = colorgram.extract('/Users/iray/PycharmProjects/100daysofcode/Day 18/image.jpg', 19)
color_rgb = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_rgb.append(new_color)

from turtle import Turtle, Screen
import random

# Create turtle and screen
screen = Screen()
screen.title("Hirst Painting Project")
screen.setup(width=400, height=400)  # Larger canvas
screen.bgcolor("white")
screen.colormode(255)  # Enable RGB colors

painter = Turtle()
painter.penup()  # This prevents drawing lines when moving
painter.hideturtle()
painter.speed(0)

start_x = -100
start_y = -100
painter.goto(start_x, start_y)

def painting():
    y_position = start_y
    for _ in range(10):
        painter.goto(start_x, y_position)
        for _ in range(10):
            painter.dot(10, random.choice(color_rgb))
            painter.forward(20)

        y_position += 20

painting()

screen.exitonclick()
