
#Added Instagram Followers Comparison Game 🎯🔥

import random

instagram_followers = {
    "Instagram": {
        "name": "Instagram",
        "country": "United States",
        "followers": 686
    },
    "Cristiano Ronaldo": {
        "name": "Cristiano Ronaldo",
        "country": "Portugal",
        "followers": 650
    },
    "Lionel Messi": {
        "name": "Lionel Messi",
        "country": "Argentina",
        "followers": 505
    },
    "Selena Gomez": {
        "name": "Selena Gomez",
        "country": "United States",
        "followers": 421
    },
    "Dwayne Johnson": {
        "name": "Dwayne 'The Rock' Johnson",
        "country": "United States",
        "followers": 395
    },
    "Kylie Jenner": {
        "name": "Kylie Jenner",
        "country": "United States",
        "followers": 394
    },
    "Ariana Grande": {
        "name": "Ariana Grande",
        "country": "United States",
        "followers": 376
    },
    "Kim Kardashian": {
        "name": "Kim Kardashian",
        "country": "United States",
        "followers": 357
    }
}

print("\n--- Top Instagram Accounts ---")
for key, value in instagram_followers.items():
    print(f"{value['name']} ({value['country']}) - {value['followers']}M followers")

def play_game():
    points = 0

    while True:
        account1, account2 = random.sample(list(instagram_followers.keys()), 2)

        followers1 = instagram_followers[account1]["followers"]
        followers2 = instagram_followers[account2]["followers"]

        print(f"\nWho has more Instagram followers? (Type 1 or 2)")
        print(f"1. {instagram_followers[account1]['name']} ({account1}) - {followers1}M followers")
        print(f"2. {instagram_followers[account2]['name']} ({account2}) - {followers2}M followers")

        try:
            choice = int(input("Your choice (1/2): "))
            if choice == 1:
                user_guess = account1
            elif choice == 2:
                user_guess = account2
            else:
                print("❌ Invalid input! Please enter 1 or 2.")
                continue

        except ValueError:
            print("❌ Invalid input! Please enter a number (1 or 2).")
            continue

        correct_answer = account1 if followers1 > followers2 else account2

        if user_guess == correct_answer:
            points += 1
            print("✅ Correct! You earned 1 point.")
            print(f"🎯 Current Points: {points}")
        else:
            print(f"❌ Wrong answer! {instagram_followers[correct_answer]['name']} has more followers.")
            print(f"🎯 Your Final Score: {points}")
            break

play_game()
