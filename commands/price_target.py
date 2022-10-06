from openbb_terminal.api import openbb
"""
Examples:
pt AAPL
"""
class Price_Target:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.dd.pt(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for price target history, e.g. <!intern pt AAPL>")