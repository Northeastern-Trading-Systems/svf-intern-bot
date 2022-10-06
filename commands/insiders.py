from openbb_terminal.api import openbb
"""
Examples:
insiders AAPL
"""
class Insiders:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.ins.stats(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for insider holdings, e.g. <!intern pt AAPL>")