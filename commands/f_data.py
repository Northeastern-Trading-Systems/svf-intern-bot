from openbb_terminal.api import openbb
from tabulate import tablulate

"""
Examples:
insiders AAPL
"""
class Fundamental_Data:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.fa.data(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for fundamental data, e.g. <!intern fd AAPL>")