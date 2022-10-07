from openbb_terminal.api import openbb
"""
Examples:
insiders AAPL
"""
class Shareholders:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.fa.shrs(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for shareholder analysis, e.g. <!intern pt AAPL>")