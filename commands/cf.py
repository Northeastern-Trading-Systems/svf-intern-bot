from openbb_terminal.api import openbb
"""
Examples:
cf AAPL
"""
class Cash_Flow:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.fa.av_cash(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for cash flows, e.g. <!intern pt AAPL>")