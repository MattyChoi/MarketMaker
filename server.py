from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# test id
product_id = '12345'

orderbook = {
   product_id: {
      'logs': [],
      'ladder': {
         'bids': [],
         'asks': []
      },
   }
}

def fill_order(name, order):
   pass


def add_to_ladder(name, order, side):
   info = {
      'price': order['price'],
      'volume': order['volume'],
      'name': name,
      # in the future, need a parameter for time
   }
   orderbook[order['prod_id']]['ladder'][side].append(order)

   # can optimize here
   orderbook[order['prod_id']]['ladder'][side].sort(reverse=(side=='bids'), key=lambda x: x['price'])


def match(name, order):
   ladder = orderbook[order['prod_id']]['ladder']
   side = order['side']
   price = order['price']
   if side == 'BUY':
      if ladder['asks'][0]['price'] <= price:
         fill_order(name, order)
      else:
         add_to_ladder(name, order, 'bids')
   elif side == 'SELL':
      if ladder['bids'][0]['price'] >= price:
         fill_order(name, order)
      else:
         add_to_ladder(name, order, 'asks')


@app.route('/', methods = ['POST'])
def place_order():
   req = request.get_json(force=True)
   order = req['message']
   name = req['name']
   password = req['password']

   # first check if we can match the order (product_id, side, type, price, volume, name )
   # if we match the order, move the matched order to logs (price, volume, side, {id: name, volume: })
   # if not match, leave in ladder (price, volumne, owner, age)
   match(name, order)

   
@app.route('/logs', methods = ['GET'])
def get_logs():
   return jsonify(orderbook[product_id]['logs'])

   
@app.route('/ladder', methods = ['GET'])
def get_ladder():
   return jsonify(orderbook[product_id]['ladder'])


if __name__ == '__main__':
   app.run(host="localhost", port=9001, debug = True)