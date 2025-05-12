from scoreboard import Scoreboard
from snake import *

from turtle import Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()  # refresh
    time.sleep(0.1)  # update every point one second

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_on = False
        scoreboard.game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()