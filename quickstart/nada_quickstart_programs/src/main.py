from nada_dsl import *

def nada_main():
    # 0. Compiled-time constants
    nr_bidders = 3

    # 1. Parties initialization
    bidders = [Party(name=f"Bidder{i+1}") for i in range(nr_bidders)]
    auctioneer = Party(name="Auctioneer")

    # 2. Inputs initialization
    bids = []
    for i in range(nr_bidders):
        bids.append(SecretUnsignedInteger(Input(name=f"bidder{i+1}_bid", party=bidders[i])))

    # 3. Computation: Determine the highest bid
    highest_bid = bids[0]
    for i in range(1, nr_bidders):
        condition = bids[i] > highest_bid
        highest_bid = condition.if_else(bids[i], highest_bid)

    # 4. Output: Revealing the highest bid to the auctioneer
    output = Output(highest_bid, "highest_bid", auctioneer)

    return [output]
