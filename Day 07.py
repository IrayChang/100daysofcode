# Generate a random word and underscores to represent each letter in the word

import random
from nltk.corpus import words
import nltk

# Download the 'words' dataset if not already available
nltk.download('words')
word_list = words.words()

random_word = random.choice(word_list)

print("Random word:", random_word)

num_of_letter = len(random_word)
underscore = " ".join("_" * num_of_letter)

print(underscore)

game_over = False
correct_letter = []
stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
          ]

lives = 6

while not game_over:

    display = ""
    guess = input("Guess a letter: ").lower()

    # Debugging: Check if input is a single letter
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input! Please enter a single letter.")
        continue

    if guess in correct_letter:
        print("You've already guessed it")

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
            num_of_letter -= 1
        elif letter in correct_letter:
            display += letter
        else:
            display += " _"

    print(display)

    if guess not in random_word:
        lives -= 1
        print(stages[lives])
        if lives == 1:
            print("You guessed " + guess + f" that's not in the word. Only one life remains. Be careful!")
        else:
            print("You guessed " + guess + f" that's not in the word. {lives} lives remains!")
        if lives == 0:
            game_over = True
            print("***********You lose!**********\nThe answar is: " + random_word)
    else:
        if "_" not in display:
            game_over = True
            print("**********You win!**********")
            print("Congraulation! You guessed the word: " + random_word)
        else:
            print("Excellent! Keep going!")


