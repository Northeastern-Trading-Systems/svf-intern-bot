from openbb_terminal.api import openbb
from tabulate import tabulate
import pandas as pd
"""
Examples:
news AAPL
"""

class News:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = "```\n"+tabulate(openbb.stocks.dd.news(self.ticker).head(8), headers='keys', tablefmt='psql', showindex=False)+"\n```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a single ticker for news, e.g. <!intern news AAPL>")