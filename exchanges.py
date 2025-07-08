import ccxt

class ExchangeConnector:
    def __init__(self):
        self.kraken = ccxt.kraken()
        self.coinbase = ccxt.coinbase()

    def fetch_prices(self, pair):
        try:
            kraken_ticker = self.kraken.fetch_ticker(pair)
            coinbase_ticker = self.coinbase.fetch_ticker(pair)

            kraken_bid = kraken_ticker['bid']
            kraken_ask = kraken_ticker['ask']
            coinbase_bid = coinbase_ticker['bid']
            coinbase_ask = coinbase_ticker['ask']

            return {
                'kraken_bid': kraken_bid,
                'kraken_ask': kraken_ask,
                'coinbase_bid': coinbase_bid,
                'coinbase_ask': coinbase_ask
            }
        except Exception as e:
            print(f"Error fetching {pair}: {e}")
            return None