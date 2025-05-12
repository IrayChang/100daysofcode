print("Welcome to the tip calculator!")

# Validate total bill input
while True:
    try:
        total_bill = float(input("What was the total bill? $"))
        if total_bill > 0:
            break  # Exit loop if input is valid
        else:
            print("Pleas enter a postive number!")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Validate tip percentage input
while True:
    try:
        tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
        if tip in [10, 12, 15]:  # Only accept valid tip values
            break
        else:
            print("Please enter 10, 12, or 15.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Validate number of people input
while True:
    try:
        num_of_people = int(input("How many people to split the bill? "))
        if num_of_people > 0:
            break
        else:
            print("Number of people must be greater than zero.")
    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Calculate bill per person
bill_per_person = total_bill * (1 + tip / 100) / num_of_people

# Print the result with currency formatting
print(f"Each person should pay: ${bill_per_person:.2f}")
