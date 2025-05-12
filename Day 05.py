import string
import random

lowercases = []
uppercases = []
numbers = []
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
password = []
final_password = ""

for lowercase in range(26):
    lowercases.append(string.ascii_lowercase[lowercase])

for uppercase in range(26):
    uppercases.append(string.ascii_uppercase[uppercase])

for number in range(10):
    numbers.append(str(number))

print("Welcome to the PyPassword Generator!")
total_lowercases = int(input("How many lowercase letters would you like in your password?\n"))
total_uppercases = int(input("How many uppercase letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))
total_passwords = total_lowercases + total_uppercases + total_symbols + total_numbers

for total_lowercase in range(total_lowercases):
    password.append(random.choice(lowercases))

for total_uppercase in range(total_uppercases):
    password.append(random.choice(uppercases))

for total_symbol in range(total_symbols):
    password.append(random.choice(symbols))

for total_number in range(total_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)  # 隨機打亂順序
final_password = "".join(password)  # 轉換成字串

print("Your password is: " + final_password)
