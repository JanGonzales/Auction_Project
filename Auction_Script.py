import os
from ASCII_ART import logo

print(logo)

engine = True
winner = {}


def user_details(player_bids):
    current_bid = 0
    bidder_name = ""
    for bids in player_bids:
        if player_bids[bids] > current_bid:
            current_bid = player_bids[bids]
            bidder_name = bids
    print(f"The winner is {bidder_name} with a bid of ${current_bid}")


while engine is True:
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    restart = input("Are there any other bidders? Type 'yes or 'no'").lower()
    winner[name] = bid
    if restart == "y" or restart == "yes":  # put inside functions
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    elif restart == "no" or restart == "n":
        user_details(winner)
        engine = False

