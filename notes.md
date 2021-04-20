Note on "prepost". If True, then strategy does better.
Strategy performs much better than buy and hold when using shorter time frames.
I believe this is because no matter when you buy using the strategy, you cannot get a lower price than buy or hold in the long term. However, in the short term, you can.



# Import Inital Libaries
# Set the random seed for reproducibility
# Read in data from API
# Create a DataFrame with yFinance prices
# Show the DataFrame head
# Looking for missing values
# Filling missing values with the previous ones
#### Create the Features `X` and Target `y` Data

Use the `window_data()` function bellow, to create the features set `X` and the target vector `y`. Define a window size of `30` days and use the column of the closing gold price (`USD (PM)`) for as feature and target column; this will allow your model to predict gold prices in USD.
# Define the window size
# Set the index of the feature and target columns
# Create the features (X) and target (y) data using the window_data() function.
# Print a few sample values from X and y
# Manually splitting the data
# Importing the MinMaxScaler from sklearn
# Create a MinMaxScaler object
# Fit the MinMaxScaler object with the features data X
# Scale the features training and testing sets
# Fit the MinMaxScaler object with the target data Y
# Scale the target training and testing sets
The LSTM API from Keras needs to receive the features data as a _vertical vector_, so that reshape the `X` data in the form `reshape((X_train.shape[0], X_train.shape[1], 1))`. Both sets, training, and testing should be reshaped.
# Reshape the features data
# Print some sample data after reshaping the datasets
---

### Build and Train the LSTM RNN

In this section, you will design a custom LSTM RNN in Keras and fit (train) it using the training data we defined.

You will need to:

1. Define the model architecture in Keras.

2. Compile the model.

3. Fit the model with the training data.
# Importing required Keras modules
#### Create the LSTM RNN Model Structure

Design the structure of your RNN LSTM as follows:

* Number of units per layer: `30` (same as the window size)

* Dropout fraction: `0.2` (20% of neurons will be randomly dropped on each epoch)

* Add three `LSTM` layers to your model, remember to add a `Dropout` layer after each `LSTM` layer, and to set `return_sequences=True` in the first two layers only.

* Add a `Dense` output layer with one unit.
# Define the LSTM RNN model.
# Initial model setup
# Layer 1
# Layer 2
# Layer 3
# Output layer
#### Compile the LSTM RNN Model

Compile the model using the `adam` optimizer, and `mean_square_error` as loss function since the value you want to predict is continuous.
# Compile the model
# Show the model summary
#### Train the Model

Train (fit) the model with the training data using `10` epochs and a `batch_size=90`. Since you are working with time-series data, remember to set `shuffle=False` since it's necessary to keep the sequential order of the data.
# Train the model
# Evaluate the model
# Make predictions using the testing data X_test
# Recover the original prices instead of the scaled version
# Create a DataFrame of Real and Predicted values
# Plot the real vs predicted prices as a line chart