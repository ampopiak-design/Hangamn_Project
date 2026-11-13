import random
import sys
import Hanging_man
while True:
    Hanging_man.welcome_message()

    # Give user chance to select difficulty
    word_random, level = Hanging_man.difficulty_check()

    secret_word = ("_ " * len(word_random))
    print("Difficulty Selected: " + level)
    Hanging_man.start_message()
    incorrect_guess = 0
    remaining_att = 6
    guessed_letters = []
    # While loop starts here
    while True:
        print(Hanging_man.display_hangman(incorrect_guess))
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
            break
        if remaining_att == 0:
            print("You hung the man. The word was: " + word_random)
            break
            # print(input("Would you like to play again?Y/n"))

        guesses = (input("Guess a letter: "))
        if guesses in guessed_letters:
            print("You already guessed '" + guesses + "'. Try something else.")
            continue
        guessed_letters.append(guesses)
        # Guess checker
        if guesses in word_random:
            print(guesses + "' is in the word!")
        else:
            print(guesses + " is not in the word.")
            remaining_att -= 1
            incorrect_guess += 1

    yes_no = input("Would you like to play again?Y/n")
    if yes_no == "Y":
        continue
    else:
        sys.exit(0)
