from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

cors = CORS()

app = Flask(__name__)
cors.init_app(app)

# test id
product_id = "1"
order_id = 0

orderbook = {
   product_id: {
      "logs": [],
      "ladder": {
         "bids": [],
         "asks": []
      },
   }
}


def add_to_logs(price, volume, name, side, prod_id):
   if side == "bids":
      side = "BUY"
   elif side == "asks":
      side = "SELL"

   info = {
      "price": price,
      "volume": volume,
      "name": name,
      "side": side,
      # in the future, need a parameter for time
   }
   orderbook[prod_id]["logs"].append(info)


def add_to_ladder(name, order, side):
   info = {
      "price": order["price"],
      "volume": order["volume"],
      "name": name,
      "order_id": order["order_id"],
      # in the future, need a parameter for time
   }
   orderbook[order["prod_id"]]["ladder"][side].append(info)

   # can optimize here
   orderbook[order["prod_id"]]["ladder"][side].sort(reverse=(side=="bids"), key=lambda x: x["price"])


def match(name, order):
   global order_id
   order["order_id"] = order_id
   order_id += 1

   ladder = orderbook[order["prod_id"]]["ladder"]
   side = order["side"]
   price = order["price"]

   mult = 1
   aggress, passive = "bids", "asks"
   print(side)
   if side == "SELL":
      aggress, passive = passive, aggress
      mult = -1

   # check if the price is low enough
   while ladder[passive] and (mult * ladder[passive][0]["price"] <= mult * price):
      passive_price = ladder[passive][0]["price"]
      passive_name = ladder[passive][0]["name"]

      if ladder[passive][0]["volume"] > order["volume"]:
         vol = order["volume"]
         ladder[passive][0]["volume"] -= order["volume"]
         order["volume"] = 0
      else:
         vol = ladder[passive][0]["volume"]
         order["volume"] -= ladder[passive][0]["volume"]
         ladder[passive].pop(0)

      add_to_logs(passive_price, vol, passive_name, passive, order["prod_id"])
      add_to_logs(passive_price, vol, name, aggress, order["prod_id"])
      print(orderbook[order["prod_id"]]["logs"])

      if not order["volume"]:
         return orderbook[order["prod_id"]]["ladder"]
   
   add_to_ladder(name, order, aggress)
   print(orderbook[order["prod_id"]]["ladder"])
   return orderbook[order["prod_id"]]["ladder"]


@app.route("/make", methods = ["POST"])
def place_order():
   req = request.get_json(force=True)
   order = req["message"]
   name = req["name"]
   password = req["password"]

   # first check if we can match the order (product_id, side, type, price, volume, name )
   # if we match the order, move the matched order to logs (price, volume, side, {id: name, volume: })
   # if not match, leave in ladder (price, volumne, owner, age)
   return match(name, order)
   
   
@app.route("/logs", methods = ["GET"])
def get_logs():
   return jsonify(orderbook[product_id]["logs"])

   
@app.route("/ladder", methods = ["GET"])
def get_ladder():
   return jsonify(orderbook[product_id]["ladder"])


if __name__ == "__main__":
   app.run(host="localhost", port=9001, debug = True)