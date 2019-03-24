import pandas as pd
self.hist_prices = hist_prices
hist_prices = pd.read_csv('../../data/historical/prices.csv')


class Portfolio:

    def __init__(self, simulated, backtest, coins=None):

        self.simulated = simulated
        self.backtest = backtest

        self.exchange = Exchange(simulated, coins)

        if coins is None:
            if simulated:
                # Pick random coins
            else:
                coins = ???

        for coin in coins:
            self.coins[coin] = Coin()

        self.transactions = Transactions
        self.summary = Summary


    def update(self):
        update_summary()
        update_exchange()
        update_transactions()
        update_coins()


    def update_summary(Summary):
        pass


    def update_exchange(Exchange):
        pass


    def update_transactions(Transactions):
        pass


    def update_coins(Coins):
        pass
