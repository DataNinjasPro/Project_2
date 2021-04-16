#!/usr/bin/python3

# Preprocess
import yfinance as yf

# Model Prediction
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Personal Functions
import create_model
import preprocess

df = pd.DataFrame(preprocess.preprocess('AAPL').Close)
print(df)


X_train, X_test, y_train, y_test, scaler = create_model.model_prep(
    df, 0, 0, 10)

fit = create_model.model_creation(20, 0.2, X_train, y_train

prediction=create_model.model_prediction(fit, X_test, y_test, scaler)
