from openbb_terminal.api import openbb
from tabulate import tabulate

"""
Get a table summary of portfolio metrics.
"""
class PortSummary:

    def __init__(self):
        openbb.portfolio.load('OpenBBTerminal/portfolio/holdings/Public_Equity_Orderbook.xlsx')
        pass

    def execute(self):
        try:
            summary = f"```{tabulate(openbb.portfolio.summary, headers='keys', tablefmt='pretty')}```"
            return summary
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio summary information...")
