print("Welcome to the secret auction program.")
users = {}
bid = 0
winner = ""

while True:
    user = input("What is your name:\n")
    bid = int(input("What is your bid:\n"))
    users[user] = bid
    while True:
        others = str(input("Are there any other bidders? Type 'Yes' or 'No'\n")).lower()
        if others in ["yes", "no"]:
            break
        else:
            print("wrong input")

    if others == "no":
        break

winner = max(users, key=users.get)
highest_bid = users[winner]

print(f"The winner is user {winner} with a bid of ${highest_bid}")

import os


def get_valid_bid():
    while True:
        try:
            bid = int(input("What is your bid: $"))
            if bid < 0:
                print("Bids cannot be negative. Please enter a valid amount.")
                continue
            return bid
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_valid_response(prompt, valid_responses):
    while True:
        response = input(prompt).strip().lower()
        if response in valid_responses:
            return response
        print("Invalid input! Please enter:", ', '.join(valid_responses))


print("Welcome to the Secret Auction Program!")
users = {}

while True:
    user = input("What is your name (or type 'exit' to stop bidding):\n")

    if user.lower() == "exit":
        break

    bid = get_valid_bid()
    users[user] = bid

    others = get_valid_response("Are there any other bidders? Type 'Yes' or 'No':\n", ["yes", "no"])

    os.system('cls' if os.name == 'nt' else 'clear')

    if others == "no":
        break

if users:
    winner = max(users, key=users.get)
    highest_bid = users[winner]
    print(f"The winner is **{winner}** with a bid of **${highest_bid}**!")
else:
    print("No valid bids were placed. Auction canceled.")
