#!/usr/bin/python3
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


def data_filter(df):
    correlation = df.pct_change()
    correlations = pd.DataFrame([correlation[x] for x in correlation][0])

    # Automatically keeping the high correlations
    keepers = correlations[correlations.Close > 0.6]
    keeper_columns = list(keepers.index)
    keeper_columns

    df = df.loc[:, keeper_columns]
    df = df[['Low', 'High', 'Close']]

    return df


def model_prep(df, feature_col, target_col, window_size):
    # I'm just going to assume the feature/target column is the last one.
    X = []
    y = []
    for i in range(len(df) - window_size - 1):
        features = df.iloc[i:(i + window_size), feature_col]
        target = df.iloc[(i + window_size), target_col]
        X.append(features)
        y.append(target)
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)

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
    return X_train, X_test, y_train, y_test, scaler


def model_creation(number_units, dropout_fraction, X_train, y_train):
    model = Sequential()
    number_units = number_units
    dropout_fraction = dropout_fraction

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

    return model.fit(X_train, y_train, epochs=5,
                     shuffle=False, batch_size=1, verbose=1)


def model_prediction(fit, X_test, y_test, scaler):
    predicted = fit.predict(X_test)
    predicted_prices = scaler.inverse_transform(predicted)
    real_prices = scaler.inverse_transform(y_test.reshape(-1, 1))
    return predicted_prices, real_prices


def model_prediction_plot(predicted_prices, real_prices, df):
    stocks = pd.DataFrame({
        "Actual": real_prices.ravel(),
        "Predicted": predicted_prices.ravel()
    }, index=df.index[-len(real_prices):])

    stocks.plot(title="Aint worth shit. But damn. Ain't it pretty",
                figsize=(30, 10))
