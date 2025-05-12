gesture = ["Rock", "Paper", "Scissor"]

while True:
    try:
        user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
    except ValueError:
        print("Wrong Input!")
        continue

    computer = random.randint(0, 2)

    if user == 0:
        print(f"computer choose {computer} for " + gesture[computer])
        if computer == 0:
            print("It's a draw")
        elif computer == 2:
            print("You win!")
        else:
            print("You lose")
        break
    elif user == 1:
        print(f"computer choose {computer} for " + gesture[computer])
        if computer == 1:
            print("It's a draw")
        elif computer == 0:
            print("You win!")
        else:
            print("You lose")
        break
    elif user == 2:
        print(f"computer choose {computer} for " + gesture[computer])
        if computer == 2:
            print("It's a draw")
        elif computer == 1:
            print("You win!")
        else:
            print("You lose")
        break
    else:
        print("Wrong Input!")
        continue
