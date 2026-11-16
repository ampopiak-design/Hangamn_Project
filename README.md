
# The Popiak Yohannes Game Console – Hangman

Welcome to the Popiak Yohannes Game Console! This project is a Python-based Hangman game created by Anastasia and Isabella. Players select a difficulty level, guess letters, and try to figure out a randomly selected word before running out of attempts.

We hope you enjoy HANGMAN!

## How to Play

1. Run the Python program to open the Hangman Gallery.
2. Select your difficulty:
   - **Easy:** Shorter, simpler words.
   - **Medium:** More challenging words.
   - **Hard:** Longer and more difficult words.
   - **Quit:** Exit the game.
3. Once the game begins, a random word will be selected based on your difficulty.
4. Guess one letter at a time.
5. Correct guesses reveal the letter's position in the secret word.
6. Incorrect guesses add another part to the Hangman drawing and reduce your remaining attempts.
7. Try to guess the entire word before using all six attempts!
8. After the round, you can choose whether to play again or exit.

**Goal:** Guess the secret word before the Hangman drawing is completed!

## Features

- Three difficulty levels: Easy, Medium, and Hard
- Random word selection
- A different word bank for each difficulty
- Visual Hangman drawings that update with incorrect guesses
- Letter tracking to keep track of previous guesses
- Duplicate-guess detection
- A maximum of six incorrect attempts
- Win and loss messages
- Option to play another round
- Custom welcome and start-game messages

## How It Works

The application uses Python functions, conditional statements, loops, lists, and user input to run the game.

1. The program welcomes the player to the Popiak Yohannes Game Console.
2. The player selects a difficulty level.
3. The program randomly selects a word from the word bank.
4. The player enters letter guesses through the console.
5. The program checks whether each guessed letter appears in the secret word.
6. Correct guesses reveal the matching letters, while incorrect guesses update the Hangman drawing and remaining attempts.
7. The game checks whether the player has guessed the entire word or used all available attempts.
8. The player can choose to play another round or exit.

## How to Run

1. Make sure Python is installed on your computer.
2. Downloadthe project repository.
3. Make sure the `Hanging_man.py` is included in the same project directory.
4. Run the main Python file.
5. Follow the instructions displayed in the console.

**Requirements:**
- Python 3
- The `random` and `sys` standard-library modules
- The accompanying `Hanging_man.py` file

## Code Structure

The project uses multiple sections of code to organize the game's functionality.

### Main Python File

- Displays the welcome message and game menu.
- Stores the Easy, Medium, and Hard word banks.
- Handles difficulty selection and random word selection.
- Tracks guessed letters and incorrect guesses.
- Determines whether the player wins or loses.
- Manages the option to play again or exit.

### Hanging_man Module

- Contains supporting functions imported into the main program.
- Handles the welcome message and game-start message.
- Provides the difficulty-selection functionality.
- Displays the Hangman drawing based on the number of incorrect guesses.

### Word Banks

The game uses three separate lists to organize words by difficulty:

- `easy_words`
- `medium_words`
- `hard_words`

The `random` module selects a word from the appropriate list.

## Challenges & Bugs

Throughout development, we encountered several challenges that required debugging, research, and collaboration.

### 1. Importing Functions and Modules

- One of our challenges was figuring out how to import functions from another Python file.
- We initially had trouble with commeted out lines passing information between our main file and the imported module.
- We had to understand how imports work and how functions can communicate across separate files.

### 2. Debugging

- Debugging was one of the more challenging parts of development.
- We encountered errors that made it difficult to determine whether the problem was in our main program or the imported module.
- We had to carefully review our code, test different sections, and troubleshoot problems to get the game working as intended.

### 3. User Input

- Getting user inputs to work correctly was another challenge.
- We had to figure out how to accept the player's difficulty selection and letter guesses.
- We also had to account for repeated guesses and make sure the program took all into account.

### 4. Creating Custom Functions

- Learning how to create our own functions and determine what responsibilities each function should have was challenging.
- We had to understand how to pass information into functions and return information back to the main program.
- Organizing the game into separate functions helped us better understand how to structure a larger Python program.
-Learned to think in Ideas not Code!

## Credits & Acknowledgments

- **Anastasia & Isabella** – Game development and programming.
- Thank you to Coach George, Izzy and Cliff & Caleb  who helped us debug, troubleshoot, and develop our understanding of Python throughout this project!
