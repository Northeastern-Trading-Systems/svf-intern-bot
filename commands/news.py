"""
Examples:
news AAPL
"""

class News:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.news(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for news, e.g. <!intern pt AAPL>")