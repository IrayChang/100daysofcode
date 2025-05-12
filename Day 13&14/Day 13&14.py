from data import data
import random

def comparison(a, b, score):
    if a["follower_count"] > b["follower_count"]:
        score += 1
        print(f"***You're right! Current score: {score}***")
        print("\n")
        return score, True
    else:
        print(f"***Sorry, that's wrong. Final score: {score}***")
        return score, False


def get_random_account():
    return random.choice(data)


def valid_guess():
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess in ["a", "b"]:
            return guess
        else:
            print("Invalid input!")


def play_game():
    score = 0
    game_continue = True

    account_b = get_random_account()

    while game_continue:

        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print("Compare A:")
        print(f"{account_a['name']}, a {account_a['description']} from {account_a['country']}")

        print("VS")

        print("Compare B:")
        print(f"{account_b['name']}, a {account_b['description']} from {account_b['country']}")

        GUESS = valid_guess()

        if GUESS == "a":
            score, correct = comparison(account_a, account_b, score)
        else:
            score, correct = comparison(account_b, account_a, score)

        if not correct:
            print("Game over")
            game_continue = False


play_game()