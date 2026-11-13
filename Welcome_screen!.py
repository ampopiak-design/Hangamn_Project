import random
import sys

from Hangman_backup import word_random

medium_words = ["cabinets", "earrings", "jamaican", "laboring", "church", "author", "budget", "doctor", "degree",
                "bishop"]
hard_words = ["political", "pyruvate", "earthworm", "countries", "chocolate", "education", "scratched", "committee",
              "abandoned"]
easy_words = ["bake", "exit", "cool", "race", "tide", "beam", "fry", "pit", "jug", "rap"]

# Welcome Message
print("""
╔────────────────────────────────────────╗
│                                        │
│                                        │
│                                        │
│      Thank you for stopping by         │
│         The Popiak Yohannes            │
│              Game Console              │
│                                        │
│      We Hope you enjoy HANGMAN!        │
│     CODE BY: Anastasia & Isabella      │
│                                        │
│                                        │
╚────────────────────────────────────────╝
""")

# Difficulty selection message #
menu = """
Welcome to the Hangman Gallery!
Please Select Your Difficulty, and type in the designated number:

1. Easy
2. Medium
3. Hard
4. Quit

Enter your choice: """

# Give user chance to select difficulty
difficulty = int(input(menu))

def select_random_word(difficulty):
    # If statement to choose difficulty
    if difficulty == 1:
        level = ("easy")
        word_random = random.choice(easy_words)
    elif difficulty == 2:
        level = ("medium")
        word_random = random.choice(medium_words)

    elif difficulty == 3:
        level = ("hard")
        word_random = random.choice(hard_words)
    else:
        print("quit")
        sys.exit(0)
    return word_random
win = 0
losses = 0
print("""
   ╔────────────────────────────────────────╗
   │                                        │
   │               Start Game!              │
   │                                        │
   ╚────────────────────────────────────────╝
   """)

word_random = select_random_word(difficulty)
secret_word = ("_ " * len(word_random))
#print("Difficulty Selected: " + level)
HANGMAN_PICS = [r'''
   +---+
       |
       |
       |
      ===''', r'''
   +---+
   O   |
       |
       |
      ===''', r'''
   +---+
   O   |
   |   |
       |
      ===''', r'''
   +---+
   O   |
  /|   |
       |
      ===''', r'''
   +---+
   O   |
  /|\  |
       |
      ===''', r'''
   +---+
   O   |
  /|\  |
  /    |
      ===''', r'''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
#print(HANGMAN_PICS[0])


incorrect_guess = 0
remaining_att = 6
guessed_letters = []
# While loop starts here
while True:
    print(HANGMAN_PICS[incorrect_guess])
    secret_word = ""
    for letter in word_random:
        if letter in guessed_letters:
            secret_word += letter + " "
        else:
            secret_word += "_ "
    print("Secret word: " + secret_word)
    print(f"Incorrect Guess: {incorrect_guess}")
    print(f"Remaining attempts: {remaining_att}")
    print(guessed_letters)
    if "_" not in secret_word:
        print("You win and figured out the word was: " + word_random)
        question = input("Would you like tp play again?Y/n")
        #if question == "Y":

        break
    if remaining_att == 0:
        print("You hung the man. The word was: " + word_random)
        break
        print(input("Would you like to play again?Y/n"))

# def check_guess(guesses, remaining_att=None, incorrect_guess=None):
#     guesses = (input("Guess a letter: "))
#     if guesses in guessed_letters:
#         print("You already guessed '" + guesses + "'. Try something else.")
#     guessed_letters.append(guesses)
#     # Guess checker
#     if guesses in word_random:
#         print(guesses + "' is in the word!")
#     else:
#         print(guesses + " is not in the word.")
#         remaining_att -= 1
#         incorrect_guess += 1
