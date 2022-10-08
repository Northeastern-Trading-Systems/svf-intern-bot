from openbb_terminal.api import openbb
from tabulate import tablulate
"""
Examples:
analyst AAPL
"""
class Analyst_Recommendations:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = f"```{tabulate(openbb.stocks.dd.analyst(self.ticker), headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for analyst recommendations, e.g. <!intern analyst AAPL>")