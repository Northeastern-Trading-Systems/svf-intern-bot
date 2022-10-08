from openbb_terminal.api import openbb
import numpy as np
import pandas as pd
from tabulate import tabulate
"""
Examples:
cf AAPL
"""
class Cash_Flow:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = openbb.stocks.fa.fmp_cash(self.ticker)
            result = result[0:34]
            result = result.drop(result.columns[[3, 4]], axis=1)
            result = f"```{tabulate(result, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for cash flows, e.g. <!intern cf AAPL>")