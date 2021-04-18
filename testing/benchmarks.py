#!/usr/bin/python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import hvplot.pandas as hvplot
import preprocess
pd.set_option('display.width', None)


def percent_higher(ticker, period, interval='1d'):
    df = preprocess.preprocess(ticker, period, interval)
    df = df['Close']
    df = pd.DataFrame(df)
    # print(df)
    # Seeing how many times Close shift 1 was higher than Close

    df['Shifted'] = df.shift(-1)
    # print(df)

    df['Higher'] = np.where(df['Shifted'] > df['Close'], 1, 0)
    # print(df)

    sums = df.Higher.value_counts()

    higher = sums[1]
    lower = sums[0]
    years = df.index[-1] - df.index[0]
    print(
        f'In the last {years}, {ticker} has closed higher than the previous interval {higher} out of {higher + lower} times.')
    # print(sums)

    # How often is the next day close above the current day close?

    percent_higher = round(higher / (higher + lower) * 100, 2)
    print(
        f'That means, over the last {years} , {ticker} has had a higher next interval close {percent_higher}% of the time.')
    print(
        f'So if you 100% of the time said "in the next time interval the stock will close higher than the current one", you would be right {percent_higher}% of the time.')


percent_higher('AMZN', '60d', interval='15m')
