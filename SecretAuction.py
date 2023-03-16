from replit import clear
from art import logo

# print(logo)

bids = {}
bidding_end = False


def highest_bid():
    max_bid = max(bids.values())
    max_bidder = [k for k, v in bids.items() if v == max_bid]
    print(f"The winner is {max_bidder} with ${max_bid}.")


while not bidding_end:
    name = input("Tell me your name: ")
    bid = input("How much do you wanna bid in $? ")
    bids[name] = bid
    other = input("Is there anyone else wanna bid? 'yes' or 'no'? ")
    if other == "no":
        bidding_end = True
        highest_bid()
    elif other == "yes":
        clear()