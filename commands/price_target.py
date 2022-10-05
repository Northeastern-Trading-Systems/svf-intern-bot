"""
Examples:
pt AAPL
"""
class Price_Target:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET CHART FROM OPENBB
        return