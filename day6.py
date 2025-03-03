import random


EASY_LEVEL = 10
HARD_LEVEL = 5

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)
    turns = choose_difficulty()
    
    while turns > 0:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        
        if guess > answer:
            print("Too high.")
        elif guess < answer:
            print("Too low.")
        else:
            print(f"You win!! The correct number was {answer}.")
            return  # Exit the function if the user wins
        
        turns -= 1  # Reduce attempts
        
        if turns == 0:
            print(f"You've run out of attempts! The correct number was {answer}.")
        else:
            print("Guess again.")

def choose_difficulty():
    """Asks user to choose difficulty and returns the number of attempts."""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return EASY_LEVEL
        elif difficulty == "hard":
            return HARD_LEVEL
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

# Start the game
game()
