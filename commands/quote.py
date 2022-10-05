"""
Examples:
quote AAPL
"""
class Quote:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.quote(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol to quote, e.g. <!intern quote AAPL>")