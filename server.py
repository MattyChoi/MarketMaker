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

def match(name, password, order):
   ladder = orderbook[order['prod_id']['ladder']]

   return False

def add_to_logs(name, order):
   pass

@app.route('/', methods = ['POST'])
def place_order():
   req = request.get_json()
   order = req['message']
   name = req['name']
   password = req['password']

   match_status = match(name, password, order)

   if not match_status:
      add_to_logs(name, order)
   
   # first check if we can match the order (product_id, side, type, price, volume, name )
   # if we match the order, move the matched order to logs (price, volume, side, {id: name, volume: })
   # if not match, leave in ladder (price, volumne, owner, age)


   
@app.route('/logs', methods = ['GET'])
def get_logs():
   return jsonify(orderbook[product_id]['logs'])

   
@app.route('/ladder', methods = ['GET'])
def get_logs():
   return jsonify(orderbook[product_id]['ladder'])


if __name__ == '__main__':
   app.run(host="localhost", port=9001, debug = True)