from openbb_terminal.api import openbb
from tabulate import tabulate
"""
Examples:
quote AAPL
"""

class Quote:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = tabulate(openbb.stocks.quote(self.ticker), headers='keys', tablefmt='pretty')
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol to quote, e.g. <!intern quote AAPL>")