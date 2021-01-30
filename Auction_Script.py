import os

player_list = []
engine = True
winner = {}

def user_details(user_name, user_bid):
    player_details = {
        "Name": user_name,
        "Bid": user_bid
    }
    player_list.append(player_details)


while engine is True:
    name = input("What is your name?: ").lower()
    bid = int(input("What is your name?: $"))
    restart = input ("Are there any other bidders? Type 'yes or 'no'").lower()
    user_details(name, bid)
    if restart == "y" or restart == "yes":
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    elif restart == "no" or restart == "n":
        for key in range(player_list):
            if player_list[key]["Bid"] > winner:
                chosen = {
                    player_list[key]
                }
                print(winner["Name"], winner["bid"])

