from openbb_terminal.api import openbb
from tabulate import tabulate
from constants import RISKFREERATE

"""
Get a table summary of portfolio metrics.
"""
class PortSummary:

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def execute(self):
        try:
            summary = f"```{tabulate(openbb.portfolio.summary, headers='keys', tablefmt='pretty')}```"
            return summary
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio summary information...")
