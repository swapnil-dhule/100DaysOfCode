import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

loop = "yes"
bidders = {}

while loop == "yes":
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    loop = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bidders[name] = bid

    os.system('cls')

highest_bidder = max(bidders, key=bidders.get)
highest_bid = max(bidders.values())

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")