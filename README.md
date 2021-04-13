# Project 2

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
