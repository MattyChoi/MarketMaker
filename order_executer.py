import requests
import json

class Order_Executor:
    def __init__(self, host, port):
        pass

    def make_order():
        pass

    def send_order(host, port):
        url = f"http://{host}:{port}/products"
        res = requests.get(url)
        print(res.json())

    send_order("localhost", 9001)