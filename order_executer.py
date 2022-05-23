import requests
import json

class Order_Executor:
    def __init__(self, host, port, name, password):
        self.host = host
        self.port = port
        self.name = name
        self.password = password

    def make_order(self, product_id, side, tpe, price, volume):
        order = {
            'prod_id': product_id,
            'side': side,
            'type': tpe,
            'price': price,
            'volume': volume,
        }
        self.send_order(order)

    def send_order(self, order):
        url = f"http://{self.host}:{self.port}/"
        data = {
            'message': order,
            'name': self.name,
            'password': self.password
        }
        res = requests.post(url, data=json.dumps(data))
        print(res.json())