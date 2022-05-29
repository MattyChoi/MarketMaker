import './App.css';

function App() {
  return (
    <div className="App">
      {/* column where you put */}
      <div id="placeOrder">
        <form>
          <label>
            ID:
            <input type="text" name="id"/>
          </label>
          <label>
            Side:
            <select name="side" id="side">
              <option value="buy side">BUY</option>
              <option value="sell side">SELL</option>
            </select>
          </label>
          <label>
            Order Type:
            <select name="side" id="side">
              <option value="limit">Limit Order</option>
              <option value="market">Market Order</option>
            </select>
          </label>
          <label>
            Price:
            <input type="text" name="price"/>
          </label>
          <label>
            Volume:
            <input type="text" name="volume"/>
          </label>
          <input type="submit" value="Submit"/>
        </form>

      </div>

    </div>
  );
}

export default App;