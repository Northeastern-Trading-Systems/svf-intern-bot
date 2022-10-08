from openbb_terminal.api import openbb
from tabulate import tablulate

"""
Examples:
er AAPL
"""
class ER_Info:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = openbb.stocks.fa.earnings(self.ticker, True)
            result = result[:5]
            result = f"```{tabulate(result, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for earnings info, e.g. <!intern pt AAPL>")