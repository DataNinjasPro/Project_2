# Project Title

Automated Trading Strategy

# Team Members.

Tyler Ryan, Jimmy Hackett, Jeffrey Scott

# Project Description

Our project will consist of two trading strategies that work regardless of a bull or bear market, a predictive algorithm such as, but not necessarily, a regression model and/or neural network model. We intend to be able to predict the price of a particular asset using our regression/nn model. Then based of that price, our code will be able to decide which of the two of our trading strategies it will deploy. Finally, if we have time to code this part, trade based off of those predicted asset prices.

# Research questions to answer

1. Can we create a strategy that can do well in bear markets?
2. Can we create a strategy that can do well in bull markets?
3. Can we create code that can switch between these strategies and outperform a buy and hold strategy over a period of time where both bull and bear markets have occured?
4. Can we apply these strategies to predicted values?

- Will this perform better than not using predicted values?

# Datasets to be used

We plan on using some sort of stock/crypto asset as our data.

# Rough Breakdown of tasks

## Trading Strategies

### Poor outlook

I want to get data where prices are going down.
Using this data, I want to create a strategy that would at least make some money.
The only goal of this strategy is to not lose money.

### Good outlook

I want to create a strategy that buys the dips in a bull market.

### Overall

I want a strategy that at least outperforms a buy and hold strategy over the same period.

# Market Prediction

I want to at least get a general idea of what the stock price will be a few weeks to a month out with reasonable accuracy.

# Tying it all together.

A few weeks out, if the stock is expected to be a lot lower than the current value, then we would need to changestrategies from bull to bear. The question is then when would we switch strategies? If we do it too early, then we would lose money in the beginning.

## Solution.

Our model should predict when the price turns. We would then use that index/date and the corresponding peak as the point and dollar value we would switch strategies.

## Set up (Step by step as of 4/11/21)

# Todo

- [ ] Data = API of some sort.
  - [ ] Preprocess the data
- [ ] Strategy Creation.
  - [ ] Create a strategy that does well in bull markets.
  - [ ] Create a strategy that does well in bear markets.
- [ ] Backtest and forwardtest these strategies.
  - [ ] Did they make money on seen data?
  - [ ] Did they make money on unseen data?
- [ ] Combine these strategies.
  - [ ] Figure out an indicator that can be used to switch between strategies.
  - [ ] Backtest and forward test the combined strategy and compare it to a buy and hold strategy.
    - This should absolutely make more money than buy and hold!
  - [ ] Forward test the strategy vs buy and hold on unseen data - Again, this should absolutely make more money than buy and hold.
        Note: We could implement trading costs. But for stocks, I don't think there are any with some brokers.
- [ ] Create a model that can accurately predict future asset values.
  - Doesn't need to be precise, just close enough.
  - [ ] Check to see the fit of the model. Over, under, or just right?
- [ ] Apply the indicator we came up with to switch strategies to the model's predictions.
