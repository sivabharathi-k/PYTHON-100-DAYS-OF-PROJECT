import random

# Hangman ASCII stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """  # Final stage (Game Over)
]

# Word selection
namelist = ["siva", "raj", "mani", "veera"]
randomlist = random.choice(namelist)

# Placeholder setup
placeholder = "_ " * len(randomlist)
print(placeholder)

# Game variables
gameover = False
emptylist = []  # Stores correct guesses
lives = 6  # Define lives

while not gameover:
    guess = input("Guess a letter: ").lower()

    if guess in emptylist:
        print("You already guessed that letter!")
        continue

    display = ""
    for i in randomlist:
        if i == guess:
            display += i + " "
            emptylist.append(guess)  # Store correct guesses
        elif i in emptylist:
            display += i + " "
        else:
            display += "_ "

    print(display.strip())  # Print the updated word with guessed letters

    if guess not in randomlist:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            gameover = True
            print("You lose! The word was:", randomlist)

    if "_ " not in display:
        gameover = True
        print("You win!")

    print(hangman_stages[6 - lives])  # Show the Hangman progress
