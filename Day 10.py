def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        print("Division cannot be zero")
        return
    else:
        return a / b

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def valid_num(user_input):
    while True:
        try:
            return float(input(user_input))
        except ValueError:
            print("Invalid input!")

def valid_operator():
    while True:
        print("+\n-\n*\n/")
        operator = input("Pick an operation: ")
        if operator in operations:
            return operator
        else:
            print("Invalid input!")

def valid_restart(result):
    while True:
        choice = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'e' to exit: ").lower()
        if choice in ['y', 'n', 'e']:
            return choice
        else:
            print("Invalid input!")

def calculator():
    accumulate = True
    num1 = valid_num("What's your first number: ")
    while accumulate:
        operation_symbol = valid_operator()
        num2 = valid_num("What's the next number: ")

        result = operations[operation_symbol](num1, num2)
        if result is not None:
            print(f"{num1} {operation_symbol} {num2} = {result}")
            num1 = result

        restart = valid_restart(result)

        if restart == "y":
            continue
        elif restart == "e":
            break
        else:
            accumulate = False
            print("\n" * 10)
            calculator()


calculator()