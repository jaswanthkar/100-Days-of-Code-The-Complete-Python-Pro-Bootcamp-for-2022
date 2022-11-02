import os
os.system('cls')
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
def highest_bidder(bid_record):
    bid_high=0
    winner=""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount>bid_high:
            bid_high = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${bid_high}")

bids={}
bidding_state=True
while bidding_state:
    name = input("What is your name: ")
    price = int(input("What is your bid? $"))
    bids[name]= price
    condition = input("Are there any other bidders? Tye 'yes' or 'no'. ")
    if condition=="no":
        bidding_state=False
        highest_bidder(bids)
    else:
        os.system('cls')

