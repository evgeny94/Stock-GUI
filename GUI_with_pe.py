# Import necessary libraries
import yfinance as yf
import tkinter as tk

# Create the GUI window
root = tk.Tk()
root.title("Stock Monitor")

# Create an entry for the user to enter the ticker symbol
ticker_entry = tk.Entry(root)
ticker_entry.pack()

# Create a label to display the current price of the stock
price_label = tk.Label(root, text="Current price:")
price_label.pack()

# Create a label to display the PE ratio of the stock
pe_label = tk.Label(root, text="PE ratio:")
pe_label.pack()

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

# Create a button to trigger the update function
update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack()

# Start the GUI event loop
root.mainloop()
