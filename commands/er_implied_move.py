"""
Examples:
er-impl-move AAPL
"""
class ER_Implied_Move:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET ER FROM OPENBB
        return