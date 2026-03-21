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
import numpy as np

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

## daily ret
dret = df["Close"].pct_change()
dret = dret.rename(columns=lambda x: f"Daily Ret_{x}")
dftotal = pd.concat([df, dret], axis=1)

## log ret cum ret
logclose = df["Close"]
logret = np.log(logclose / logclose.shift(1))
logret = logret.rename(columns=lambda x: f"Log Ret_{x}")
cumret = (1 + dret).cumprod() - 1
cumret = cumret.rename(columns=lambda x: f"Cum Ret_{x}")
dftotal = pd.concat([dftotal, cumret], axis=1)
dftotal = pd.concat([dftotal, logret], axis=1)




#### output
timestamp = datetime.now().strftime("%b%d-%H%M").lower()
filename = "_".join(tickerlist) + "_" + "" + timestamp + ".csv" 
dftotal.to_csv(filename)

filepath = Path(filename).resolve()
print(f"Successfully exported to {filepath.resolve()}")
print(dftotal.head())

