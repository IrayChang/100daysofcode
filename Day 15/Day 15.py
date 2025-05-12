from data import MENU, profit, resources

def resources_report(a):
    Water = a["water"]
    Milk = a["milk"]
    Coffee = a["coffee"]
    Money = a["money"]
    print(f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}g\nMoney: ${Money:.2f}")


def valid_choice():
    while True:
        choice = input("What would you like or 'off' to leave? (espresso/latte/cappuccino)").lower()
        if choice in ["espresso", "latte", "cappuccino", "report", "off"]:
            return choice
        else:
            print("Invalid input")


def input_coin():
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            return quarters, dimes, nickles, pennies
        except ValueError:
            print("Invalid_input")


def resources_used(coffee_choice):
    resources["money"] += coffee_choice["cost"]
    resources["water"] -= coffee_choice["ingredients"]["water"]
    resources["milk"] -= coffee_choice["ingredients"]["milk"]
    resources["coffee"] -= coffee_choice["ingredients"]["coffee"]


def check(coffee_choice, available_resources, user_choice):
    for ingredient in coffee_choice["ingredients"]:
        if coffee_choice["ingredients"][ingredient] > available_resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    print("Please insert coins.")
    QUARTERS, DIMES, NICKLES, PENNIES = input_coin()
    total_input = 0.25 * QUARTERS + 0.1 * DIMES + 0.05 * NICKLES + 0.01 * PENNIES

    if total_input >= coffee_choice["cost"]:
        change = round(total_input - coffee_choice["cost"], 2)
        print(f"Here is ${change:.2f} dollars in change.")
        print(f"Here is your {user_choice}. Enjoy!")
        resources_used(coffee_choice)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

turn_on = True

while turn_on:
    choice = valid_choice()

    if choice == "report":
        resources_report(resources)
    elif choice in MENU:
        check(MENU[choice], resources, choice)
    elif choice == "off":
        turn_on = False