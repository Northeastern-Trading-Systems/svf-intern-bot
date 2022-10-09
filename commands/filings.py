from openbb_terminal.api import openbb
from tabulate import tabulate

"""
Examples:
filings AAPL
"""


class Filings:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = openbb.stocks.dd.sec(self.ticker)
            result = result.drop(
                ['Document Date', 'Category', 'Amended'], axis=1)
            result = result[:8]
            result = f"```{tabulate(result, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for filings, e.g. <!intern filings AAPL>")
