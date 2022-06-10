import "./App.css";
import React, { useState, useContext, useCallback, useEffect } from "react";
import {SocketContext} from "./context/socket";
import io from "socket.io-client";

function App(props) {
  const socket = useContext(SocketContext);

  // define needed variables for making an order
  const [orderVals, setOrderVals] = useState({
    id: "",
    side: "buy",
    type: "Limit Order",
    price: 0,
    volume: 0,
  });

  // collect all the needed info from the ladder
  const [ladderInfo, setLadderInfo] = useState({
    active_orders: [],
    all_bids: [],
    all_asks: [],
  });

  // collect all the needed info from the logs
  const [logInfo, setLogInfo] = useState({
    pnl: 0,
    positions: 0,
  });

  // working with sockets on the client side
  useEffect(() => {
    // socket = io.connect(
    //   "http://localhost:9001", 
    //   {
    //     reconnection: true,
    //     // transports: ["websocket"]
    //   },
    // );
    // console.log("socket open");

    socket.on("logs and ladders", data => {
      setLadderInfo({
        active_orders: data["active_orders"],
        all_bids: data["all_bids"],
        all_asks: data["all_asks"],
      });

      setLogInfo({
        pnl: data["pnl"],
        positions: data["positions"],
      });
    })

    // return () => {
    //   socket.close();
    //   console.log("socket closed");
    // }
  }, []);
  
  function handleChange(e) {
    const { name, value } = e.target;
    setOrderVals(prev => ({
      ...prev,
      [name]: value
    }));
  };

  function placeOrder(e) {
    e.preventDefault();
    const price = parseInt(orderVals.price);
    const volume = parseInt(orderVals.volume);
    if ((orderVals.id !== "") && (orderVals.price !== 0) && (orderVals.volume !== 0)) {
      const order = {
        "prod_id": orderVals.id,
        "side": orderVals.side,
        "type": orderVals.type,
        "price": price,
        "volume": volume,
      };

      const data = {
        "message": order,
        "name": "",
        "password": "",
      };

      socket.emit("send order", data);
      console.log("send order");

      // fetch("http://localhost:9001/make", {
      //   method: "POST",
      //   headers: {
      //     "Content-Type": "application/json"
      //   },
      //   body: JSON.stringify(data),
      // }).then(response => console.log(response.json()))
      //   .catch(error => console.log(error))

    }
  }

  return (
    <div className="App">
      <div className="body">
        <div id="placeOrder" className="column">
          <form onSubmit={placeOrder}>
            <label className="row font1">
              ID:
              <input type="text" name="id" className="box font1" value={orderVals.id} onChange={handleChange}/>
            </label>
            <label className="row font1">
              Side:
              <select name="side" id="side" className="box font1" value={orderVals.side} onChange={handleChange}>
                <option value="BUY">BUY</option>
                <option value="SELL">SELL</option>
              </select>
            </label>
            <label className="row font1">
              Order Type:
              <select name="type" id="type" className="box font1" value={orderVals.type} onChange={handleChange}>
                <option value="limit">Limit Order</option>
                <option value="market">Market Order</option>
              </select>
            </label>
            <label className="row font1">
              Price:
              <input type="text" name="price" className="box font1" value={orderVals.price} onChange={handleChange}/>
            </label>
            <label className="row font1">
              Volume:
              <input type="text" name="volume" className="box font1" value={orderVals.volume} onChange={handleChange}/>
            </label>
            <input type="submit" value="Submit" className="button font1"/>
          </form>
        </div>

        <div id="ownOrders" className="column">

          <div id="activeOrders" name="activeOrders" className="row box font1 margin" readOnly={true}>
            Active Orders:
            <br/>
            {/* need to fix formatting here in terms of both the css and what needs to be shown */}
            {ladderInfo["active_orders"].map(order => {
                return <span>{order["price"]}</span>;
            })}
          </div>

          <div id="positions" name="positions" className="row box font1 margin" readOnly={true}>
            Positions: {logInfo["positions"]}
            <br/>
            PNL: {logInfo["pnl"]}
          </div>

        </div>

        <div id="allOrders" className="column">
          <label className="row font1">
            Order Book:
            <div id="orderBook" name="orderBook" className="row box font1" readOnly={true}>
              Asks:
              {/* need to fix formatting here in terms of both the css and what needs to be shown */}
              {ladderInfo["all_asks"].map(ask => {
                  return <span>{ask["price"]}</span>;
              })}
              <br/>
              Bids:
              {/* need to fix formatting here in terms of both the css and what needs to be shown */}
              {ladderInfo["all_bids"].map(bid => {
                  return <span>{bid["price"]}</span>;
              })}
            </div>
          </label>
          <form>
            <input type="submit" value="Delete All Orders" className="button font1"/>
          </form>
          <form>
            <label className="row font1">
              Delete by Order ID:
              <input type="text" name="delete" className="box"/>
            </label>
            <input type="submit" value="Delete Order" className="button font1"/>
          </form>
        </div>
      </div>

    </div>
  );
}

export default App;