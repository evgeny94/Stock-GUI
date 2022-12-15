# Import necessary modules
import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt
import requests

# Create the main window
root = tk.Tk()
root.title("Stock Monitor")

def getTicker(company_name):
    url = "https://s.yimg.com/aq/autoc"
    parameters = {'query': company_name, 'lang': 'en-US'}
    response = requests.get(url = url, params = parameters)
    data = response.json()
    company_code = data['ResultSet']['Result'][0]['symbol']
    return company_code

# Create a function to update the stock data
def update_data():
  # Get the ticker symbol from the entry
  ticker = ticker_entry.get()

  # Get stock data for the specified ticker
  stock = yf.Ticker(ticker)

  # Update the price label with the current price of the stock
  price = stock.info["regularMarketPrice"]
  price_label["text"] = f"Current price: {price}"

  # Update the PE ratio label with the PE ratio of the stock
  pe = stock.info["trailingPE"]
  pe_label["text"] = f"PE ratio: {pe}"

# Create a function that will be called when the user inputs a stock symbol and clicks the "Get Price" button
def show_graph():
    # Get the stock symbol that the user entered
    ticker = ticker_entry.get()

    # Use the yfinance module to fetch the historical prices of the stock
    stock = yf.Ticker(ticker)
    prices = stock.history(period="30y")

    # Use the matplotlib library to create a line chart of the stock's prices
    plt.cla()
    plt.plot(prices["Close"], label='Original data', color='black')
    plt.title("Price History for " + ticker)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

# Create a function that will be called when the user inputs a stock symbol and clicks the "Get Price" button
def show_graph_with_MA():
    # Get the stock symbol that the user entered
    ticker = ticker_entry.get()

    # Use the yfinance module to fetch the historical prices of the stock
    stock = yf.Ticker(ticker)
    prices = stock.history(period="30y")

    # Use the matplotlib library to create a line chart of the stock's prices
    plt.cla()
    plt.plot(prices["Close"], label='Original data', color='black')
    plt.plot(prices["Close"].rolling(window=50).mean(), label='MA50', color='blue')
    plt.plot(prices["Close"].rolling(window=100).mean(), label='MA50', color='yellow')
    plt.plot(prices["Close"].rolling(window=200).mean(), label='MA50', color='red')
    plt.title("Price History for " + ticker)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()


# Create a text entry for the user to input a stock symbol
ticker_entry = tk.Entry(root)
ticker_entry.pack()

# Create a button that will call the get_price function when clicked
get_price_button = tk.Button(root, text="Show Graph", command=show_graph)
get_price_button.pack()

# Create a button that will call the get_price function when clicked
get_price_button = tk.Button(root, text="Show Graph with MA", command=show_graph_with_MA)
get_price_button.pack()

# Create a label to display the current price of the stock
price_label = tk.Label(root, text="Current price:")
price_label.pack()

# Create a label to display the PE ratio of the stock
pe_label = tk.Label(root, text="PE ratio:")
pe_label.pack()

# Create a button to trigger the update function
update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack()

# Start the GUI event loop
root.mainloop()
