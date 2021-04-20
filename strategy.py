#!/usr/bin/python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def download(ticker, period, interval, prepost):
    # Note: We could have period < 60d and an intraday return
    # Just change period to < 60 days and add interval = 1h
    df = yf.download(ticker,
                     period=period,  # A period of 2 years from today
                     prepost=prepost,  # Pre and Post markets included
                     # Multi-thread processing for faster output.
                     threads=True,
                     interval=interval)
    return df


def returns(df):

    df1 = df.copy()
    # Set the short window and long windows
    # 40,80 works best so far.
    short_sma = 40
    long_sma = 80

    df1[f"{short_sma} SMA"] = df1.Close.rolling(short_sma).mean()
    df1[f"{long_sma} SMA"] = df1.Close.rolling(long_sma).mean()

    df1['Position'] = np.where(
        df1[f'{short_sma} SMA'] > df1[f'{long_sma} SMA'], 1, -1)

    df1['log_returns'] = np.log(df1['Close'] / df1['Close'].shift(1))

    df1['strategy_returns'] = df1.Position.shift(1) * df1['log_returns']
    df1 = df1[['log_returns', 'strategy_returns']]

    returns = df1[['log_returns', 'strategy_returns']
                  ].sum().apply(np.exp) * 1000
    return df1, returns


def plot_returns(df):
    df['BH CR'] = df['log_returns'].cumsum().apply(np.exp) * 1000
    df['S CR'] = df['strategy_returns'].cumsum().apply(np.exp) * 1000

    return df[['BH CR', 'S CR']].plot()
