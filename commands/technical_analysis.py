"""
Examples:
ta AAPL
"""
class Technical_Analysis:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.ta.summary(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for TA summary, e.g. <!intern ta AAPL>")