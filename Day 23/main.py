import time
from turtle import Screen
from player import *
from car_manager import  CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    if turtle.ycor() > 280:
        cars.level_up()
        score.level_up()
        turtle.goto(STARTING_POSITION)

    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()