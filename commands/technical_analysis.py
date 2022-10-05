"""
Examples:
ta AAPL
"""


class Technical_Analysis:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET TA FROM OPENBB
        return