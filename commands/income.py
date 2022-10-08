from openbb_terminal.api import openbb
from tabulate import tabulate
import pandas as pd
import numpy as np
"""
Examples:
income AAPL
"""


class Income_Stmt:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = openbb.stocks.fa.fmp_income(self.ticker)
            result = result[0:34]
            result = result.drop(result.columns[[3, 4]], axis=1)
            result = f"```{tabulate(result, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for income statement, e.g. <!intern pt AAPL>")
            print(e)
