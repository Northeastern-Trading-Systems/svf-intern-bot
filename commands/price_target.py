from openbb_terminal.api import openbb
from tabulate import tablulate

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
            result = f"```{tabulate(openbb.stocks.dd.pt(self.ticker).head(16), headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for price target history, e.g. <!intern pt AAPL>")