from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

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

@app.route('/', methods = ['POST'])
def post_order():
   order = request.get_json()
   
   # first check if we can match the order

   # if we match the order, move the matched order to logs (price, volume, side, {id: name, volume: })

   # if not match, leave in ladder (price, volumne, owner, age)

   
@app.route('/logs', methods = ['GET'])
def get_logs():
   return jsonify(orderbook)
   
@app.route('/ladder', methods = ['GET'])
def get_logs():
   return jsonify(orderbook)


if __name__ == '__main__':
   app.run(host="localhost", port=9001, debug = True)