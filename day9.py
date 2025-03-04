import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS'''

choices = [rock, paper, scissors]
choices_text = ["Rock", "Paper", "Scissors"]

points = 0  

while True:
    try:
        user = int(input("\nEnter a number (0: Rock, 1: Paper, 2: Scissors): "))
        
        if user not in [0, 1, 2]:
            print("❌ Invalid input! Please enter 0, 1, or 2.")
            continue

        print(f"\nYou chose {choices_text[user]}:\n{choices[user]}")

        computer = random.randint(0, 2)
        print(f"\nComputer chose {choices_text[computer]}:\n{choices[computer]}")

        results = {
            (0, 1): "❌ You lose! Paper covers Rock.",
            (1, 2): "❌ You lose! Scissors cut Paper.",
            (2, 0): "❌ You lose! Rock smashes Scissors.",
            (1, 0): "✅ You win! Paper covers Rock.",
            (2, 1): "✅ You win! Scissors cut Paper.",
            (0, 2): "✅ You win! Rock smashes Scissors."
        }

        if user == computer:
            print("🤝 It's a tie!")
        elif (user, computer) in results:
            print(results[(user, computer)])
            if "✅ You win!" in results[(user, computer)]:
                points += 1
        else:
            print(results[(computer, user)])  
            print(f"\n❌ You lost! Final Score: {points} points.")
            break  

        print(f"🎯 Current Points: {points}")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print(f"Thanks for playing! 🎮 Final Score: {points} points.")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a number (0, 1, or 2).")
