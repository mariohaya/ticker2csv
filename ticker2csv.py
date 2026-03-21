#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:21:02 2026

@author: mario
"""

# ticker2csv

##### libs
import yfinance as yf
import pandas as pd
from pathlib import Path

from datetime import datetime

##### Initial input
# ticker
print("Enter ticker(s), separate with commas (e.g. AAPL, VOO, GLD).")
tickerinputs = input("Ticker(s): ")
tickerlist = [t.strip().upper() for t in tickerinputs.split(",") if t.strip()]
# date
print("Enter date range (yyyy-mm-dd to yyyy-mm-dd):")
date_input = input("Date range: ").strip()

if " to " in date_input:
    start_date, end_date = [d.strip() for d in date_input.split(" to ")]
else:
    start_date = date_input
    end_date = pd.Timestamp.today().strftime("%Y-%m-%d")

##### lookback
df = yf.download(
    tickerlist,
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=True)

#### output
timestamp = datetime.now().strftime("%b%d-%H%M").lower()
filename = "_".join(tickerlist) + "_" + "" + timestamp + ".csv" 
df.to_csv(filename)

filepath = Path(filename).resolve()
print(f"Successfully exported to {filepath.resolve()}")
print(df.head())



