#!/usr/bin/python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import hvplot.pandas as hvplot
sns.set_style('darkgrid')


def preprocess(ticker):
    ticker = ticker
    # Note: We could have period < 60d and an intraday return
    # Just change period to < 60 days and add interval = 1h
    df = yf.download(ticker,
                     period='5y',  # A period of 2 years from today
                     prepost=True,  # Pre and Post markets included
                     threads=True  # Multi-thread processing for faster output.
                     )
    df  # This data already looks like it is based of business days.
    # Rearranging the columns to help with the Heatmap
    df = df[['Close', 'Open', 'High', 'Low', 'Volume']]
    return df
