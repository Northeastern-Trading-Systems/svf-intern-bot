from tabulate import tabulate
import pandas as pd
import numpy as np


"""
Examples:
port
"""


class Portfolio_Holdings:

    def __init__(self):
        tickers = ['NTDOY', 'EVVTY', 'MODG', 'NSIT',
                   'MAXR', 'USD']
        weights = ['8.54%', '6.27%', '7.63%', '6.13%', '4.77%', '66.66%']
        cost_basis = ['9.47', '215.24', '20.24', '108.16', '29.75', '1.00']
        portfolio_dict = {'weight': weights, 'cost basis': cost_basis}
        self.portfolio_df = pd.DataFrame(portfolio_dict, index=tickers)

    def execute(self):
        result = f"```{tabulate(self.portfolio_df, headers='keys', tablefmt='pretty')}```"
        return result
