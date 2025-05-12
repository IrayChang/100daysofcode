import random

# Define card deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    """Calculates the score of a given hand, handling Aces (11 → 1 when needed)."""
    score = sum(hand)

    # Convert Ace (11) to (1) if the score exceeds 21
    while 11 in hand and score > 21:
        hand[hand.index(11)] = 1  # Change one Ace (11) to 1
        score = sum(hand)

    return score


def blackjack():
    """Main function to play one round of Blackjack."""
    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards)]

    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    print(f"\nYour cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")

    # Player's turn
    while user_score < 21:
        another = input("Do you want another card? Type 'y' or 'n': ").lower()
        if another == "y":
            user.append(random.choice(cards))
            user_score = calculate_score(user)  # Recalculate after drawing a card
            print(f"\nYour cards: {user}, current score: {user_score}")
        else:
            break

    # If user busts (score > 21), they lose immediately
    if user_score > 21:
        print("\nYou went over 21. You lose!")
        print(f"Your final hand: {user}, final score: {user_score}")
        return

    # Computer's turn: Draw cards until at least 17
    while computer_score < 17:
        computer.append(random.choice(cards))
        computer_score = calculate_score(computer)

    # Show final hands
    print("\n Final Results:")
    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")

    # Determine winner
    if computer_score > 21 or user_score > computer_score:
        print("You won!")
    elif user_score < computer_score:
        print("You lost!")
    else:
        print("It's a draw!")


while True:
    choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice == "y":
        blackjack()
    else:
        print("Thanks for playing! Goodbye!")
        break
