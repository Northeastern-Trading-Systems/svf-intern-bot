"""
Examples:
analyst AAPL
"""
class Analyst_Recommendations:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET RECS FROM OPENBB
        return