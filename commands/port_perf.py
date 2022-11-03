from openbb_terminal.api import openbb
from tabulate import tabulate
from constants import RISKFREERATE

"""
Get a table summary of portfolio performance metrics.
"""
class PortPerformance:

    def __init__(self):
        pass

    def execute(self):
        try:
            perf = f"```{tabulate(openbb.portfolio.perf, headers='keys', tablefmt='pretty')}```"
            return perf
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio performance information...")
