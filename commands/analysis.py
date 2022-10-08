from openbb_terminal.api import openbb
from tabulate import tabulate
"""
Examples:
analysis AAPL
"""


class Analysis:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = f"```{tabulate(openbb.stocks.fa.analysis(self.ticker), headers='keys', tablefmt='pretty')}```"
            
            return result
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for analysis, e.g. <!intern analysis AAPL>")
