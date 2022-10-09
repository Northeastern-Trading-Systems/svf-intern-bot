from openbb_terminal.api import openbb
from tabulate import tabulate
import pandas as pd
from uuid import uuid4
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
            df: pd.DataFrame = openbb.stocks.fa.analysis(self.ticker)
            destination = f"/root/OpenBBUserData/exports/stocks/sheets/{self.ticker}-{uuid4()}.csv"
            df.to_csv(destination)
            return ("CSV", destination)
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for analysis, e.g. <!intern analysis AAPL>")
