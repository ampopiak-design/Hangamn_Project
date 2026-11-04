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
Select Your Difficulty:

1. Easy
2. Medium
3. Hard
4. Quit

Enter your choice: """


difficulty=int(input(menu))
print(difficulty)

if difficulty == 1:
    print("easy")
elif difficulty == 2:
    print("medium")
elif  difficulty == 3:
    print("hard")
else:
    print("quit")
    sys.exit(0)