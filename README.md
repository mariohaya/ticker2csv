# ticker2csv
Don't go through the hassle of manually copy+pasting data from Yahoo Finance, or worse, paying for it.

A simple Python script that fetches Yahoo Finance data for one or more tickers and exports it to a CSV file. Enter one or multiple tickers and it will export the results directly to a `.csv` file. Requires `yfinance`

It returns:
- Date
- Price
- Open, Close, Adj Close
- High, Low
- Volume
- Daily, Log, Cumulative returns

## Usage
- Enter one or multiple tickers in this format: `VOO, AAPL, GLD`
- Enter a date range in the format `yyyy-mm-dd to yyyy-mm-dd`, or enter just `yyyy-mm-dd` to use that date as the start date and today as the end date

Clone the repository:
```bash
git clone https://github.com/mariohaya/ticker2csv.git
cd ticker2csv
