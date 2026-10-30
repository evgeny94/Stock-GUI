# Agent guide

Instructions for every coding agent in this repository (Claude Code reads them through `CLAUDE.md`).

A Tkinter desktop app for looking up stock data with `yfinance` and plotting price history with `matplotlib`. Written in PyCharm in Dec 2022 (the `.idea/` project files are committed). There are no tests, no lint config and no packaging.

## Setup and run

```bash
python -m venv .venv
.venv/Scripts/activate          # Windows; use .venv/bin/activate elsewhere
pip install -r requirements.txt
python GUI_Stocks_graph_price_pe.py
```
`tkinter` ships with Python. Every script opens its own window and blocks in `root.mainloop()`, so running one requires a display.

## Structure

Each `GUI_*.py` file is a **standalone script**, not a module. They were successive experiments, and none of them imports another. `main.py` is the untouched PyCharm template and `GUI.py` is a 6-line `yfinance` smoke test. The most complete version is **`GUI_Stocks_graph_price_pe.py`**: unless told otherwise, build new work on it.

| Script | What it adds |
|---|---|
| `GUI_stocks_fetch_currentPrice.py` | Enter a ticker, then fetch its price |
| `GUI_updating_price_60sec.py` | Re-polls a hard-coded ticker (`DORL.TA`) with `root.after` (the interval is actually 1 s, despite the name) |
| `GUI_with_pe.py` | Price + P/E |
| `GUI_Stocks_graph.py` | Price history chart with MA50/100/200; `getTicker()` does a company-name → ticker lookup |
| `GUI_Stocks_graph_price_pe.py` | Two frames: fundamentals (price, P/E, forward P/E, market cap, dividend %, 52-week high), plus a chart frame that takes period/interval inputs; balance-sheet dump to stdout |
| `GUI_with_dropdown_menu.py` | Unrelated experiment: loads an `.xlsx` with pandas and lists its columns in a dropdown |

## Pitfalls in the existing code

- Widgets are module-level globals, and the callbacks read them directly. Layout uses `grid` with `row`/`column` numbers chosen by hand.
- All data comes from `stock.info[...]` with direct key access and no error handling. A missing key raises `KeyError`, and `dividendRate` is `None` for stocks that pay no dividend, which makes the dividend math raise. `yfinance` changes its `info` keys over time, so check the current key names when something breaks.
- The dividend % calculation is special-cased for Tel Aviv tickers (`'.ta' in ticker`, lowercase only), because TASE prices are quoted in agorot.
- `getTicker()` calls the old Yahoo autocomplete endpoint `s.yimg.com/aq/autoc`, which is probably no longer available.
- All network calls run on the Tk main thread, so the UI freezes while they run.


## How to report back

End every reply, short ones too, with a plain-language summary and no jargon:
- **Before:** what the state was.
- **Now:** what changed.
- **WHAT TO DO:** what Evgeny has to do, numbered with the cheapest step first, or "nothing". It must be self-contained: file paths, commands, and a ready-to-paste prompt if a new session is needed. Never write "see my previous message"; repeat a step for as long as it is still the next one.

Also:
- Do everything you can yourself. Don't put work on Evgeny's list that you could do.
- When something is blocked (a permission, a login, a step that needs Evgeny's hands), say what was blocked and give the exact steps or a ready-to-paste snippet to unblock it.
- Ask questions as multiple choice with the recommended option first (in Claude Code, use the AskUserQuestion tool), not as plain-text questions.
- Reply in the language Evgeny writes in (Hebrew or English). Code, file names and docs stay in English.
- Keep delivery lean: one report at the end, and no extra plan or record files.
