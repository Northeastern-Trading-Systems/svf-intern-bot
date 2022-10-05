"""
Examples:
er AAPL
"""
class ER_Info:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET ER FROM OPENBB
        return