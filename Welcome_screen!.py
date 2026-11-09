import random
import sys
import Hanging_man
medium_words = ["cabinets", "earrings", "jamaican", "laboring", "church", "author", "budget", "doctor", "degree", "bishop"]
hard_words = ["political", "pyruvate", "earthworm", "countries", "chocolate", "education", "scratched", "committee", "abandoned"]
easy_words = ["bake", "exit", "cool", "race", "tide", "beam", "fry", "pit", "jug", "rap"]

""""
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
"""

menu=""""
Welcome to the Hangman Gallery!
Please Select Your Difficulty, and type in the designated number:

1. Easy
2. Medium
3. Hard
4. Quit

Enter your choice: """


difficulty=int(input(menu))
print(difficulty)

word_random = ""

if difficulty == 1:
    print("""
    ╔────────────────────────────────────────╗
    │                                        │
    │               Start Game!              │
    │                                        │
    ╚────────────────────────────────────────╝
    """)
    print("Difficulty Selected: easy")
    easy_word_random = random.sample(easy_words, 1)[0]
    print('_'* len(easy_word_random))

elif difficulty == 2:
    print("""
    ╔────────────────────────────────────────╗
    │                                        │
    │               Start Game!              │
    │                                        │
    ╚────────────────────────────────────────╝
    """)
    print("Difficulty Selected: medium")
    medium_word_random = random.sample(medium_words, 1)[0]
    print("_" * len(medium_word_random))


elif  difficulty == 3:
    print("""
    ╔────────────────────────────────────────╗
    │                                        │
    │               Start Game!              │
    │                                        │
    ╚────────────────────────────────────────╝
    """)
    print("Difficulty Selected: hard")
    hard_word_random = random.sample(hard_words, 1)[0]
    secret_word=( "_ " * len(hard_word_random))
    print("Secret Word: " + secret_word)
else:
    print("quit")
    sys.exit(0)
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
print(HANGMAN_PICS[0])
incorrect_guess = int("0 / 6")
print(incorrect_guess)
remaining_att = int("6")
print(remaining_att)
guesses = (input("Guess a letter:"))
