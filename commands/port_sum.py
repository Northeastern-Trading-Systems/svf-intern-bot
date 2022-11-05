from openbb_terminal.api import openbb
from tabulate import tabulate
from constants import RISKFREERATE
from openbb_terminal.portfolio import portfolio_model as pm

"""
Get a table summary of portfolio metrics.
"""
class PortSummary:

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def execute(self):
        try:
            summary = f"```{tabulate(pm.get_summary(self.portfolio, window='6m'), headers='keys', tablefmt='pretty')}```"
            return summary
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio summary information...")
