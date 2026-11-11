import random
import sys
import Hanging_man

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
│              Game Consule              │
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
print(difficulty)

# If statement to choose difficulty
if difficulty == 1:
    print("""
    ╔────────────────────────────────────────╗
    │                                        │
    │               Start Game!              │
    │                                        │
    ╚────────────────────────────────────────╝
    """)
    print("Difficulty Selected: easy")
    word_random = random.sample(easy_words, 1)[0]
elif difficulty == 2:
    print("""
    ╔────────────────────────────────────────╗
    │                                        │
    │               Start Game!              │
    │                                        │
    ╚────────────────────────────────────────╝
    """)
    print("Difficulty Selected: medium")
    word_random = random.sample(medium_words, 1)[0]
elif difficulty == 3:
    print("""
    ╔────────────────────────────────────────╗
    │                                        │
    │               Start Game!              │
    │                                        │
    ╚────────────────────────────────────────╝
    """)
    print("Difficulty Selected: hard")
    word_random = random.sample(hard_words, 1)[0]
else:
    print("quit")
    sys.exit(0)

secret_word = ["_"] * len(word_random)
print(secret_word)

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


def displayBoard(incorrect_guess, correctLetters, secretWord):
    print(HANGMAN_PICS[len(incorrect_guess)])
    print()


incorrect_guess = 0
print(f"Incorrect Guess: {incorrect_guess}")
remaining_att = 6
print(f"Remaining Attempts: {remaining_att}")

# While loop starts here
while True:
    guesses = (input("Guess a letter: "))

    # Guess checker
    if guesses in word_random:
        for i in range(len(word_random)):
             if word_random[i]==guesses:
                 secret_word[i] = guesses
    else:
        print(False)
        remaining_att -= 1
        print(remaining_att)
        incorrect_guess += 1
        print(incorrect_guess)
        print(HANGMAN_PICS[incorrect_guess])

    print(secret_word)

