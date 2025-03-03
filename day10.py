MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 124.5,  
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 207.5, 
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 249.0,  
    }
}


profit = 0
report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Checks if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > report[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total amount inserted in INR."""
    print("Please insert coins (₹10, ₹5, ₹2, ₹1).")
    total = 0
    total += int(input("How many ₹10 coins? ")) * 10
    total += int(input("How many ₹5 coins? ")) * 5
    total += int(input("How many ₹2 coins? ")) * 2
    total += int(input("How many ₹1 coins? ")) * 1
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment is successful, otherwise refunds money."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Your balance amount ₹{change}.")  # Display balance in INR
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts ingredients and serves coffee."""
    for item in order_ingredients:
        report[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {report['water']}ml")
        print(f"Milk: {report['milk']}ml")
        print(f"Coffee: {report['coffee']}g")
        print(f"Money: ₹{profit}")
    elif choice in MENU:
        drink = MENU[choice]
        print(f"The cost of {choice} is ₹{drink['cost']}.")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select a valid option.")
