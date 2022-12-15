# Import necessary modules
import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt
import requests

# Create the main window
root = tk.Tk()
root.title("Stock Monitor")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create a function to update the stock data
def update_data():
    # Get the ticker symbol from the entry
    ticker = ticker_symbol_entry.get()

    # Get stock data for the specified ticker
    stock = yf.Ticker(ticker)

    # Update the price label with the current price of the stock
    price = stock.info["regularMarketPrice"]
    price_label["text"] = f"Current price: {price}"

    # Update the PE ratio label with the PE ratio of the stock
    pe = stock.info["trailingPE"]
    pe_label["text"] = f"PE ratio: {pe}"

    market_cap = stock.info["marketCap"]
    market_cap_label["text"] = f"Market Cap: {market_cap}"

    f_pe = stock.info["forwardPE"]
    forward_pe_label["text"] = f"Forward PE: {f_pe}"

    if '.ta' in ticker:
        dividend_rate = stock.info["dividendRate"]
        dividend = round((((dividend_rate * 100) / price)*100), 2)
        dividend_rate_label["text"] = f"Dividend: {dividend}%"
    else:
        dividend_rate = stock.info["dividendRate"]
        dividend = round(((dividend_rate * 100) / price), 2)
        dividend_rate_label["text"] = f"Dividend: {dividend}%"



    fifty_two_high = stock.info["fiftyTwoWeekHigh"]
    fiftyTwoWeekHigh_label["text"] = f"52 Week High: {fifty_two_high}"


def show_balance_sheet():
    # Get the ticker symbol from the entry
    ticker = ticker_symbol_entry.get()

    # Get stock data for the specified ticker
    stock = yf.Ticker(ticker)

    # show balance sheet
    balance_sheet = stock.balance_sheet
    print(balance_sheet)
    quarterly_balance_sheet = stock.quarterly_balance_sheet
    print(quarterly_balance_sheet)

# Create a function that will be called when the user inputs a stock symbol and clicks the "Get Price" button
def show_graph():
    update_data()
    # Get the stock symbol that the user entered
    ticker = ticker_symbol_entry.get()

    # Get the period
    period_user = period_user_entry.get()

    # Get the period
    interval_user = interval_user_entry.get()

    # Use the yfinance module to fetch the historical prices of the stock
    stock = yf.Ticker(ticker)
    if len(interval_user_entry.get()) == 0:
        prices = stock.history(period=period_user)
    else:
        prices = stock.history(period=period_user, interval=interval_user)

    # Use the matplotlib library to create a line chart of the stock's prices
    plt.cla()
    plt.plot(prices["Close"], label='Original data', color='black')
    plt.title("Price History for " + ticker)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

# Create a function that will be called when the user inputs a stock symbol and clicks the "Get Price" button
def show_graph_with_MA():
    update_data()
    # Get the stock symbol that the user entered
    ticker = ticker_symbol_entry.get()

    # Get the period
    period_user = period_user_entry.get()

    # Get the period
    interval_user = interval_user_entry.get()

    # Use the yfinance module to fetch the historical prices of the stock
    stock = yf.Ticker(ticker)
    if len(interval_user_entry.get()) == 0:
        prices = stock.history(period=period_user)
    else:
        prices = stock.history(period=period_user, interval=interval_user)

    # Use the matplotlib library to create a line chart of the stock's prices
    plt.cla()
    plt.plot(prices["Close"], label='Original data', color='black')
    plt.plot(prices["Close"].rolling(window=50).mean(), label='MA50', color='blue')
    plt.plot(prices["Close"].rolling(window=100).mean(), label='MA100', color='yellow')
    plt.plot(prices["Close"].rolling(window=200).mean(), label='MA200', color='red')
    plt.title("Price History for " + ticker)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

#-----------------------------------------------------------------------------------------

########################################### main frame
main_frame = tk.Frame(root, borderwidth=15)
main_frame.grid(row=0, column=0, pady=5, padx=5, sticky="n")

# Create a label for the user to input a stock symbol
ticker_symbol_label = tk.Label(main_frame, text="Enter ticker symbol:")
ticker_symbol_label.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")

# Create a text entry for the user to input a stock symbol
ticker_symbol_entry = tk.Entry(main_frame, width=10)
ticker_symbol_entry.grid(row=0, column=1, sticky="nsew", pady=5, padx=5)

# Create a label to display the current price of the stock
price_label = tk.Label(main_frame, text="Current price:")
price_label.grid(row=1, column=1, pady=5, padx=5, sticky="w")

# Create a label to display the PE ratio of the stock
pe_label = tk.Label(main_frame, text="PE ratio:")
pe_label.grid(row=2, column=1, pady=5, padx=5, sticky="w")

#--------------------------------------------------------
market_cap_label = tk.Label(main_frame, text="Market Cap:")
market_cap_label.grid(row=3, column=1, pady=5, padx=5, sticky="w")

forward_pe_label = tk.Label(main_frame, text="Forward PE:")
forward_pe_label.grid(row=4, column=1, pady=5, padx=5, sticky="w")

dividend_rate_label = tk.Label(main_frame, text="Dividend:")
dividend_rate_label.grid(row=5, column=1, pady=5, padx=5, sticky="w")

fiftyTwoWeekHigh_label = tk.Label(main_frame, text="52 Week High:")
fiftyTwoWeekHigh_label.grid(row=6, column=1, pady=5, padx=5, sticky="w")

# Create a button to trigger the update function
update_button = tk.Button(main_frame, text="Update", command=update_data)
update_button.grid(row=0, column=2, pady=5, padx=5, sticky="e")

# Create a button to show balance sheet
balance_sheet_button = tk.Button(main_frame, text="Balance sheet", command=show_balance_sheet)
balance_sheet_button.grid(row=10, column=0, pady=5, padx=5, sticky="nsew")

########################################### graphs frame
graphs_frame = tk.Frame(root, borderwidth=15)
graphs_frame.grid(row=0, column=1, pady=5, padx=5, sticky="n")

# Create a label for the user to input a period
period_user_label = tk.Label(graphs_frame, text="Enter period:")
period_user_label.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")

# Create a text entry for the user to input a period
period_user_entry = tk.Entry(graphs_frame, width=10)
period_user_entry.grid(row=0, column=1, columnspan=2, pady=5, padx=5, sticky="nsew")

# Create a label for the user to input an interval
interval_user_label = tk.Label(graphs_frame, text="Enter interval:")
interval_user_label.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

# Create a text entry for the user to input an interval
interval_user_entry = tk.Entry(graphs_frame, width=10)
interval_user_entry.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="nsew")


# Create a button that will call the get_price function when clicked
show_graph_button = tk.Button(graphs_frame, text="Show Graph", command=show_graph)
show_graph_button.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")

# Create a button that will call the get_price function when clicked
show_graph_ma_button = tk.Button(graphs_frame, text="Show Graph with MA", command=show_graph_with_MA)
show_graph_ma_button.grid(row=2, column=1, pady=5, padx=5, sticky="nsew")

# Legend periods
legend_label = tk.Label(graphs_frame, text="Valid Periods:\nday(d)\nmonth(mo)\nyears(y)\nmaximum(max)\nyear to date(ytd)\n")
legend_label.grid(row=3, column=0, pady=5, padx=5, sticky="ne")

# Legend intervals
legend_label = tk.Label(graphs_frame, text="Valid Intervals:\n1, 2, 5, 15, 30, 60, 90\nminutes(m)\nhour(h)\nday(d)\nweek(wk)\nmonth(mo)"
                                           "\nnote #1: 1m data is only for available for last 7 days"
                                           "\nnote #2: data interval <1d for the last 60 days")
legend_label.grid(row=3, column=1, pady=5, padx=5, sticky="ne")
########################################### analysis frame



# Start the GUI event loop
root.mainloop()
