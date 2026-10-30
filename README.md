# Stock-Monitoring-GUI

A small Python desktop app for monitoring stocks. You enter a ticker (US tickers, or Tel Aviv tickers with the `.TA` suffix) to see its current price, P/E, forward P/E, market cap, dividend yield and 52-week high. You can also plot its price history with 50/100/200-day moving averages.

Built with Tkinter, [yfinance](https://github.com/ranaroussi/yfinance) and matplotlib.

## Run

```bash
python -m venv .venv
.venv/Scripts/activate      # Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python GUI_Stocks_graph_price_pe.py
```

## Using the chart

- **Period:** `1d`, `5d`, `1mo`, `6mo`, `1y`, `5y`, `ytd`, `max`, …
- **Interval** (optional): `1m`, `5m`, `15m`, `1h`, `1d`, `1wk`, `1mo`, …
  1-minute data only covers the last 7 days, and intervals under 1 day only cover the last 60 days.

## Files

`GUI_Stocks_graph_price_pe.py` is the main app. The other `GUI_*.py` scripts are earlier, simpler versions that were kept for reference.
