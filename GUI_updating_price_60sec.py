# Import necessary modules
import time
import tkinter as tk
import yfinance as yf

# Define the stock ticker
ticker = "DORL.TA"

# Get stock data
stock = yf.Ticker(ticker)

# Create the main window
root = tk.Tk()
root.title("Stock Monitor")

# Create a label to display the current price
price_label = tk.Label(root, text="Current price:")
price_label.pack()

# Create a function to update the price label
def update_price():
    # Get the current price
    current_price = stock.info["regularMarketPrice"]

    # Update the label text
    price_label.config(text=f"Current price: {current_price}")

    # Schedule the next update in 1 second
    root.after(1000, update_price)

# Schedule the first update
root.after(1000, update_price)

# Run the main loop
root.mainloop()
