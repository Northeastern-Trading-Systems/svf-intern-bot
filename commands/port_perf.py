from openbb_terminal.api import openbb
from tabulate import tabulate

"""
Get a table summary of portfolio performance metrics.
"""
class PortPerformance:

    def __init__(self):
        openbb.portfolio.load('OpenBBTerminal/portfolio/holdings/Public_Equity_Orderbook.xlsx')
        pass

    def execute(self):
        try:
            perf = f"```{tabulate(openbb.portfolio.perf, headers='keys', tablefmt='pretty')}```"
            return perf
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio performance information...")
