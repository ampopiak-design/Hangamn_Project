import random
import sys
medium_words = ["cabinets", "earrings", "jamaican", "laboring", "church", "author", "budget", "doctor", "degree",
                "bishop"]
hard_words = ["political", "pyruvate", "earthworm", "countries", "chocolate", "education", "scratched", "committee",
              "abandoned"]
easy_words = ["bake", "exit", "cool", "race", "tide", "beam", "fry", "pit", "jug", "rap"]

def welcome_message():
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
def start_message():
    #Start message for Hangman pictures later
    print("""
╔────────────────────────────────────────╗
│                                        │
│               Start Game!              │
│                                        │
╚────────────────────────────────────────╝
    """)

HANGMAN_PICS = [r'''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''',r'''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''',r'''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''',r'''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''',r'''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''',r'''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''',r'''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']

def display_hangman(incorrect_guess):
    print(HANGMAN_PICS[incorrect_guess])

def difficulty_check():
    # Difficulty selection message #
    menu = """
    Welcome to the Hangman Gallery!
    Please Select Your Difficulty, and type in the designated number:

    1. Easy
    2. Medium
    3. Hard
    4. Quit

    Enter your choice: """
    difficulty = int(input(menu))
    # If statement to choose difficulty
    if difficulty == 1:
        level = "easy"
        word_random = random.choice(easy_words)
    elif difficulty == 2:
        level = "medium"
        word_random = random.choice(medium_words)
    elif difficulty == 3:
        level = "hard"
        word_random = random.choice(hard_words)
    else:
        print("quit")
        sys.exit(0)
    return word_random, level
