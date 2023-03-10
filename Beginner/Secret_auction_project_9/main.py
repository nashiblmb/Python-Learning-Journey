import os
from art import logo

print(logo)

def replay():
    while True:
    # Asking user if they want to add another player
        status = input("Would you like to add another player? Press Y/N: ").lower()

        # Input validation
        if status == "n" or status == "no":
            os.system('cls')
            return False
        elif status == "y" or status == "yes":
            # Clearing the Screen
            os.system('cls')
            return True
        else:
            print("Invalid input, please enter 'y' or 'n'.\n")


def auction_bid(name, bid_value):
    # Create a dictionary for the new bid with the bidder's name and the bid value
    new_bid = {"name": name,
            "bid": bid_value,
            }
    
    return new_bid

def winning_bid(bids):

    # Find the highest bid and the corresponding bidder
    highest_bid = 0
    for count in range(len(bids)):
        if bids[count]["bid"] > highest_bid:
            highest_bid = bids[count]["bid"]
            winner = {"name": bids[count]["name"],
                      "bid": bids[count]["bid"]}
            
    # Print the name and the bid value of the winning bidder
    print(f"The winner is {winner['name']} with a bid of £{winner['bid']}.")



bids = []
print("Welcome to the secret auction program.")

# Start the auction
game_status = True
while game_status == True:

    # Input for name
    name = input("What is your name?: ")
    
    # Check input for bid
    while True:
        try:
            bid_value = int(input("What is your bid?: £"))
            if bid_value <= 0:
                print("Bid value must be a positive integer.")
            else:
                break
        except ValueError:
            print("Bid value must be a positive integer.")


    # Add the new bid to the list of bids
    bids.append(auction_bid(name, bid_value))

    # Ask the user if they want to add another player to the auction
    game_status = replay()

# Announce the winner
winning_bid(bids)

