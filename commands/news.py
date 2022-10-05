"""
Examples:
news AAPL
"""

class News:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET NEWS FROM OPENBB
        return