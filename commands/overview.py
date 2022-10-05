"""
Examples:
overview AAPL
"""
class Overview:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.fa.overview(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for an overview, e.g. <!intern overview GSL>")