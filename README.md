# Project 2: Algo & Predictions

# Purpose

This projects sets out to create a strategy that can out perform the buy and hold strategy in the short run. We don't aim to beat the buy and hold strategy in the long run. In fact, we aim to use the buy and hold model along with the strategy when we deploy it. The idea that if the future outlook on an asset looks bleak, deploy this strategy as a means of hedging losses. However, to know when to deploy the model, we first had to create a model that could predict future stock prices with moderate accuracy.

# Strategy

The strategy is a simple moving average strategy with a short SMA of 40 units and a long sma of 80 units. In our case these units are in 15 minute intervals. When the short SMA crosses aboce the long sma, we take a long position on that particular asset. When the short SMA crosses below the long sma, we switch a long position for a short one. This means that no matter what the stock is doing, we always have a position open.

# Prediction Model

Our model is an LSTM Neural Network model. This is used to tell us the future expected price of a given asset. We believe the model doesn't have to be extremely accurate to be effective. The reason for this is because we are really just using it as a check for our own personal predictions of the asset's price. That is to say, we already have a prediction of what the stock price could be in the future, we are using the model as a means of reference.

# How it works

First, we get a prediction of the future asset price from our model. Based off of that and our own intuition, we either turn on the trading algorithm, or we don't.

# Results

Our model' performance is not guaranteed and is not consistent. That said, when it doesn't do well, it isn't usually much worse than the buy and hold strategy in the short run. Meaning, we didn't see very many cases where an investor would've lost their shirt running this strategy. However, when our model does do well, it really can do an amazing job. For example, if you gave our model $1,000 around the end of January 2021 and set it loose on GameStop (GME), you would have ended up with $57,052 in 60 days. Compare that to the buy and hold strategy which would've returned $1,952. Now it should be said that this case is an extreme outlier and should not be the expected result. Like said before, it's ideal use would be a risk limiter use in combination WITH the buy and hold strategy that could result in less money lost.

![GME Cumulative Returns](IMG/GME_Cumulative_returns.png)

The following picture represents the intended use for this strategy. That is, a loss mitigator. An investor would've lost more money in this 60 day period if they were to have only bought and held. Don't mistake this "bigger loss" with an overall bigger loss. The investor, depending on when they actually bought, could still have a higher return if the bought the stock 50 years ago. But in this short period, they could've reduced the loss incurred in the 60 day period if the employed this strategy.
![Expected Outcome](IMG/TSLA_expected_outcome.png)

# Conclusion

All in all, this strategy works well a lot of the time. And in all the tests we ran, it would never cause an investor to lose their shirt in a trade. However, the consistency of the algorithm is a little shakey. Because of this, it should only be used by those with a higher risk tolerance.
