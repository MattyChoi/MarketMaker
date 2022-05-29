import './App.css';
import React, { useState } from 'react';

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
    console.log(orderVals);
  }

  return (
    <div className="App">
      {/* column where you put */}
      <div id="placeOrder">
        <form onSubmit={placeOrder}>
          <label>
            ID:
            <input type="text" name="id" value={orderVals.id} onChange={handleChange}/>
          </label>
          <label>
            Side:
            <select name="side" id="side" value={orderVals.side} onChange={handleChange}>
              <option value="buy">BUY</option>
              <option value="sell">SELL</option>
            </select>
          </label>
          <label>
            Order Type:
            <select name="type" id="type" value={orderVals.type} onChange={handleChange}>
              <option value="limit">Limit Order</option>
              <option value="market">Market Order</option>
            </select>
          </label>
          <label>
            Price:
            <input type="text" name="price" value={orderVals.price} onChange={handleChange}/>
          </label>
          <label>
            Volume:
            <input type="text" name="volume" value={orderVals.volume} onChange={handleChange}/>
          </label>
          <input type="submit" value="Submit"/>
        </form>

      </div>

      {/* column where the information is  */}
      <div id="ownOrders">
        
        <div id="activeOrders" name="activeOrders">
          Active Orders
        </div>

        <div id="positions" name="positions">
          Positions: 0
        </div>

      </div>

      {/* column where you put  */}
      <div id="allOrders">
        
        
        <label>
          Order Book
          <div id="orderBook" name="orderBook">
            Asks:<br></br>
            Bids:<br></br>
          </div>
        </label>
        <input type="submit" value="Delete All Orders"/>
        <form>
          <label>
              Delete by Order ID:
              <input type="text" name="delete"/>
          </label>
          <input type="submit" value="Delete Order"/>
        </form>
      </div>
    
    </div>
  );
}

export default App;