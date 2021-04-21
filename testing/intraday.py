import yfinance as yf
import pandas as pd
import numpy as np

def grab(ticker,freq):
    data = yf.download(ticker,
        start= '2021-02-22',
        stop= '2021-04-05',
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        interval = freq,
        auto_adjust = True,
        prepost = False,)
    return data


def grab_prepost(ticker,freq):
    data = yf.download(ticker,
        start= '2021-02-22',
        stop= '2021-04-05',
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        interval = freq,
        auto_adjust = True,
        prepost = True,)
    return data

def grab_daily(ticker):
    data = yf.download(ticker,
        start= '2018-01-05',
        stop= '2021-04-05',
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        interval = '1d',
        auto_adjust = True,
        prepost = True,)
    return data


def window_data(df, window, feature_col_number, target_col_number):
    X = []
    y = []
    for i in range(len(df) - window):
        features = df.iloc[i:(i + window), feature_col_number]
        target = df.iloc[(i + window), target_col_number]
        X.append(features)
        y.append(target)
    return np.array(X), np.array(y).reshape(-1, 1)