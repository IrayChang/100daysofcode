from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race: ")


def create_turtles():
    start_y = -120
    for color_name in range(0, 6):
        t = Turtle(shape="turtle")
        t.color(colors[color_name])
        t.penup()
        t.goto(x=-230, y=start_y)
        start_y += 50

        all_turtles.append(t)


def movement(t):
    race_on = True
    while race_on:
        for each in all_turtles:
            if each.xcor() > 210:
                race_on = False
                winner = each.pencolor()
                if user_bet == each:
                    print("You've win!")
                else:
                    print("You've lose!")
                print(f"The winner is {winner}.")

            each.forward(random.randint(1, 10))


create_turtles()
movement(all_turtles)

s.exitonclick()