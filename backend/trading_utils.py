import numpy as np


def get_bids_and_asks(ladder):
    bids = ladder["bids"]
    asks = ladder["asks"]
    return bids, asks

def get_active_orders(ladder, name):
    orders = []
    for order in ladder["asks"]:
        if order["name"] == name:
            orders.append(order)

    for order in ladder["bids"]:
        if order["name"] == name:
            orders.append(order)

    return orders

def compute_pnl_and_positions(logs, name):
    pnl = 0
    positions = 0
    for order in logs:
        if order["name"] == name:
            sgn = (order["side"] == "SELL") * 2 - 1
            pnl += sgn * order["price"] * order["volume"]
            positions += -sgn * order["volume"]
            
    return pnl, positions

# def 

#     ts, age, name, bids, asks