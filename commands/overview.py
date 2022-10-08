from openbb_terminal.api import openbb
from tabulate import tabulate

"""
Examples:
overview AAPL
"""


class Overview:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = "```\n" + \
                str(openbb.stocks.fa.av_overview(self.ticker))+"\n```"
            return result
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for an overview, e.g. <!intern overview GSL>")
