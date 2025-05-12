import random

num_list = []

for i in range(1, 101):
    num_list.append(i)


def game():
    return random.choice(num_list)


# Alternative:
# from random import randint
# randint(1, 100)

def compare(a, b):
    if a > b:
        return ("Too high")
    elif a < b:
        return ("Too low")
    else:
        return ("Bingo!")


def valid_response(promt, valid_responses):
    while True:
        respond = input(promt).lower()
        if respond in valid_responses:
            return respond
        else:
            print("Invalid input! Please enter:", ', '.join(valid_responses))


def valid_guess():
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")


def rule(attempt):
    answer = game()
    guess = 0
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to gusee")
        guess = valid_guess()
        result = compare(guess, answer)
        print(result)

        if result == "Bingo!":
            print(f"Congratulations! You guessed the number: {answer}")
            return  #
        else:
            attempt -= 1

    print(f"Game Over! The correct number was {answer}.")


def start_game():
    while True:
        print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100.")

        difficulty = valid_response("Choose a difficulty. Type 'easy' or 'hard'", ["easy", "hard"])
        attempts = 10 if difficulty == "easy" else 5

        rule(attempts)

        choice = input("Do you want to play again? Type 'y' to continue and 'n' to exit")

        if choice == "n":
            print("Thank you")
            break
        else:
            continue


start_game()

