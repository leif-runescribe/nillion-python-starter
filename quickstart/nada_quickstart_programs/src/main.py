from nada_dsl import *


def initialize_bidders(nr_bidders):
    
    bidders = []
    for i in range(nr_bidders):
        bidders.append(Party(name="Bidder" + str(i + 1)))
    return bidders


def initialize_bids(nr_bidders, bidders):
   
    bids = []
    for i in range(nr_bidders):
        bids.append(SecretUnsignedInteger(Input(name=f"bidder{i+1}_bid", party=bidders[i])))
    return bids


def determine_highest_bid(bids):
    
    highest_bid = bids[0]
    for i in range(1, len(bids)):
        condition = bids[i] > highest_bid
        highest_bid = condition.if_else(bids[i], highest_bid)
    return highest_bid


def nada_main():
    # 0. Compiled-time constants
    nr_bidders = 3

    # 1. Parties initialization
    bidders = initialize_bidders(nr_bidders)
    auctioneer = Party(name="Auctioneer")

    # 2. Inputs initialization
    bids = initialize_bids(nr_bidders, bidders)

    # 3. Computation: Determine the highest bid
    highest_bid = determine_highest_bid(bids)

    # 4. Output: Revealing the highest bid to the auctioneer
    output = Output(highest_bid, "highest_bid", auctioneer)

    return [output]
