from openbb_terminal.api import openbb
from tabulate import tablulate

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
            result = openbb.stocks.ins.lins(self.ticker)
            result = result.drop(columns=['#Shares Total', 'Insider Trading', 'SEC Form 4'], axis=1)
            result = result[:10]
            result = f"```{tabulate(result, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for insider activity, e.g. <!intern insiders AAPL>")