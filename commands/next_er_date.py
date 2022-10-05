"""
Examples:
next-er AAPL
"""


class Next_ER_Date:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET ER FROM OPENBB
        return