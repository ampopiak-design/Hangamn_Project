import random

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
import sys

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
    print("easy")
    easy_word_random = random.sample(easy_words, 1)[0]
    print('_ '* len(easy_word_random))

elif difficulty == 2:
    print("medium")
    print("-" * len(word_random))
    print(len(random.sample(medium_words, 1)[0]))

elif  difficulty == 3:
    print("hard")
else:
    print("quit")
    sys.exit(0)
