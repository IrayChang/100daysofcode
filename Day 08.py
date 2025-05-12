import string

def encrypt(original_text, shift_amount):
    alphabet = list(string.ascii_lowercase)
    text_encoded = ""

    for char in original_text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift_amount) % 26
            text_encoded += alphabet[new_index]

    print("Here is the encoded result: " + text_encoded)

def decrypt(original_text, shift_amount):
    alphabet = list(string.ascii_lowercase)
    text_decoded = ""

    for char in original_text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index - shift_amount) % 26
            text_decoded += alphabet[new_index]

    print("Here is the decoded result: " + text_decoded)


while True:
    option = str(input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to exit the game:\n"))
    if option != "encode" and option != "decode" and option != "exit":
        print("Invalid input! Please enter 'encode' or 'decode'.")
        continue

    if option == "encode":
        text = str(input("Type your message:\n"))
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif option == "decode":
        text = str(input("Type your message:\n"))
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("Goodbye~")
        break

