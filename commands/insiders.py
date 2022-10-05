"""
Examples:
insiders AAPL
"""
class Insiders:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET TA FROM OPENBB
        return