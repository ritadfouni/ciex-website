class ArbitrageStrategy:
    def __init__(self, connector, pairs):
        self.connector = connector
        self.pairs = pairs

    def find_opportunities(self):
        for pair in self.pairs:
            data = self.connector.fetch_prices(pair)
            if data:
                kraken_bid = data['kraken_bid']
                kraken_ask = data['kraken_ask']
                coinbase_bid = data['coinbase_bid']
                coinbase_ask = data['coinbase_ask']

                if kraken_bid > coinbase_ask:
                    profit = kraken_bid - coinbase_ask
                    print(f"✅ Buy on Coinbase at {coinbase_ask}, Sell on Kraken at {kraken_bid}, Profit: {profit:.2f} [{pair}]")
                elif coinbase_bid > kraken_ask:
                    profit = coinbase_bid - kraken_ask
                    print(f"✅ Buy on Kraken at {kraken_ask}, Sell on Coinbase at {coinbase_bid}, Profit: {profit:.2f} [{pair}]")
                else:
                    print(f"No opportunity for {pair}")