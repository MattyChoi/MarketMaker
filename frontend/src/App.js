import './App.css';
import React, { useState, useEffect } from 'react';

function App(props) {

  const [orderVals, setOrderVals] = useState({
    id: "",
    side: "buy",
    type: "Limit Order",
    price: 0,
    volume: 0,
  });

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
        'prod_id': orderVals.id,
        'side': orderVals.side,
        'type': orderVals.type,
        'price': price,
        'volume': volume,
      };

      const data = {
        'message': order,
        'name': "",
        'password': "",
      };

      const res = fetch('http://localhost:9001/make', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
      }).then(response => console.log(response.json()))
        .catch(error => console.log(error))

      console.log(res);

    }
  }

  return (
    <div className="App">
      <div className="body">
        <div id="placeOrder" className="column">
          <form onSubmit={placeOrder}>
            <label className="row">
              ID:
              <input type="text" name="id" value={orderVals.id} onChange={handleChange}/>
            </label>
            <label className="row">
              Side:
              <select name="side" id="side" value={orderVals.side} onChange={handleChange}>
                <option value="BUY">BUY</option>
                <option value="SELL">SELL</option>
              </select>
            </label>
            <label className="row">
              Order Type:
              <select name="type" id="type" value={orderVals.type} onChange={handleChange}>
                <option value="limit">Limit Order</option>
                <option value="market">Market Order</option>
              </select>
            </label>
            <label className="row">
              Price:
              <input type="text" name="price" value={orderVals.price} onChange={handleChange}/>
            </label>
            <label className="row">
              Volume:
              <input type="text" name="volume" value={orderVals.volume} onChange={handleChange}/>
            </label>
            <input type="submit" value="Submit" className="row" />
          </form>
        </div>

        <div id="ownOrders" className="column">

          <div id="activeOrders" name="activeOrders" className="row">
            Active Orders
          </div>

          <div id="positions" name="positions" className="row">
            Positions: 0
          </div>

        </div>

        <div id="allOrders" className="column">
          <label className="row">
            Order Book
            <div id="orderBook" name="orderBook">
              Asks:<br></br>
              Bids:<br></br>
            </div>
          </label>
          <form>
            <input type="submit" value="Delete All Orders"/>
          </form>
          <form>
            <label className="row">
              Delete by Order ID:
              <input type="text" name="delete" />
            </label>
            <input type="submit" value="Delete Order"/>
          </form>
        </div>
      </div>

    </div>
  );
}

export default App;