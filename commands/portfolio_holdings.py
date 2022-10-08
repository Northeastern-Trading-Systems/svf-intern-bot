from tabulate import tablulate
import pandas as pd
import numpy as np


"""
Examples:
port
"""
class Portfolio_Holdings:
    

    def __init__(self):
        tickers = ['NTDOY', 'EVVTY', 'MODG', 'CVLT', 'NSIT', 'MAXR', 'MITK', 'TUP', 'WEB', 'OMI', 'GLXZ', 'USD']
        weights = ['8.50%', '6.24%', '8.40%', '7.08%', '6.10%', '4.38%', '5.56%', '5.04%', '3.72%', '4.12%', '6.71%', '34.14%']
        cost_basis = ['0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00']
        portfolio_dict = {'weight': weights, 'cost basis': cost_basis}
        self.portfolio_df = pd.DataFrame(portfolio_dict, index=tickers)
        

    def execute(self):
        result = f"```{tabulate(self.portfolio_df, headers='keys', tablefmt='pretty')}```"
        return result