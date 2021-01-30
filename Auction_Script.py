import os
from ASCII_ART import logo

print(logo)

player_list = []
engine = True
winner = {
    "Name": "",
    "Bid": 0
}


def user_details(user_name, user_bid):
    player_details = {
        "Name": user_name,
        "Bid": user_bid
    }
    player_list.append(player_details)


while engine is True:
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    restart = input("Are there any other bidders? Type 'yes or 'no'").lower()
    user_details(name, bid)
    if restart == "y" or restart == "yes":
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    elif restart == "no" or restart == "n":
        for key in range(len(player_list)):
            if player_list[key]["Bid"] > winner["Bid"]:
                winner = {
                    "Name": player_list[key]["Name"],
                    "Bid": player_list[key]["Bid"]
                }
        engine = False
User_name = winner["Name"]
User_Bid = winner["Bid"]
print(f"The winner is {User_name} with a bid of ${User_Bid}")
