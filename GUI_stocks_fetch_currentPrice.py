# Import necessary modules
import tkinter as tk
# Import the yfinance module
import yfinance as yf

# Create the main window
root = tk.Tk()
root.title("Stock Monitor")


# Create a function that will be called when the user inputs a stock symbol and clicks the "Get Price" button
def get_price():
    # Get the stock symbol that the user entered
    symbol = stock_symbol_entry.get()

    # Use the yfinance module to fetch the current price of the stock
    stock = yf.Ticker(symbol)
    price = stock.info["regularMarketPrice"]

    # Update the label with the current price of the stock
    price_label.config(text="Price: " + str(price))


# Create a text entry for the user to input a stock symbol
stock_symbol_entry = tk.Entry(root)
stock_symbol_entry.pack()

# Create a button that will call the get_price function when clicked
get_price_button = tk.Button(root, text="Get Price", command=get_price)
get_price_button.pack()

# Create a label to display the current price of the stock
price_label = tk.Label(root, text="Price: ")
price_label.pack()

# Start the GUI event loop
root.mainloop()
