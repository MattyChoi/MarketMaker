import requests

def get_bids_and_asks(book):
    pass

def get_active_orders(ladder, name):
    orders = []
    for order in ladder['asks']:
        if order['name'] == name:
            orders.append(order)

    for order in ladder['bids']:
        if order['name'] == name:
            orders.append(order)

    return orders

# def 

#     ts, age, name, bids, asks