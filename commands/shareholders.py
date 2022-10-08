from openbb_terminal.api import openbb
from tabulate import tablulate

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
            result = openbb.stocks.fa.shrs(self.ticker)
            result = f"```{tabulate(result, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for shareholder analysis, e.g. <!intern shrs AAPL>")