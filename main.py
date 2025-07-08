from exchanges import ExchangeConnector
from strategy import ArbitrageStrategy

pairs = ['BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'ADA/USDT', 'SOL/USDT', 'DOGE/USDT']

connector = ExchangeConnector()
strategy = ArbitrageStrategy(connector, pairs)

strategy.find_opportunities()