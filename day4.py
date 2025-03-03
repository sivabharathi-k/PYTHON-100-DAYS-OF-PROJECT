bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name: ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False

# Find the highest bidder
winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}")
