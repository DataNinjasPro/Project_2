from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import numpy as np
from numpy.random import seed
seed(1)
from tensorflow import random
random.set_seed(2)
import pandas as pd
import matplotlib.pyplot as plt

def window_data(df, window):
    X = []
    y = []
    feature_col_number = 0 
    target_col_number = 0
    for i in range(len(df) - window - 1):
        features = df.iloc[i:(i + window), feature_col_number]
        target = df.iloc[(i + window), target_col_number]
        X.append(features)
        y.append(target)
    return np.array(X), np.array(y).reshape(-1, 1)


def CreatingTheModel(X,y):

    split = int(0.80 * len(X))
    X_train = X[: split]
    X_test = X[split:]
    y_train = y[: split]
    y_test = y[split:]

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(X)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    y_scaler = scaler.fit(y)
    y_train = y_scaler.transform(y_train)
    y_test = y_scaler.transform(y_test)

    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    model = Sequential()
    number_units = 20
    dropout_fraction = 0.2

    # Layer 1
    model.add(LSTM(
        units=number_units,
        return_sequences=True,
        input_shape=(X_train.shape[1], 1))
    )
    model.add(Dropout(dropout_fraction))
    # Layer 2
    model.add(LSTM(units=number_units, return_sequences=True))
    model.add(Dropout(dropout_fraction))
    # Layer 3
    model.add(LSTM(units=number_units))
    model.add(Dropout(dropout_fraction))
    # Output layer
    model.add(Dense(1))

    model.compile(optimizer="adam", loss='mse', metrics=['mse'])
    model.summary()
    model.fit(X_train, y_train, epochs=3,shuffle=False, batch_size=1, verbose=0)

    model.evaluate(X_test, y_test)

    return model , X_test ,scaler ,y_test


def PredictWithModel(model, X_test,scaler,y_test):
    predicted = model.predict(X_test)
    predicted_prices = scaler.inverse_transform(predicted)
    real_prices = scaler.inverse_transform(y_test.reshape(-1, 1))
    return predicted_prices, real_prices


def PlotPrediction(predicted_prices, real_prices,df):
    stocks = pd.DataFrame({
        "Actual": real_prices.ravel(),
        "Predicted": predicted_prices.ravel()
    }, index=df.index[-len(real_prices):])

    return stocks.plot(title="Aint worth shit. But damn. Ain't it pretty", figsize=(30, 10),secondary_y = 'Predicted')
