from openbb_terminal.api import openbb
from tabulate import tabulate
from constants import RISKFREERATE
from openbb_terminal.portfolio import portfolio_model as pm

"""
Get a table summary of portfolio performance metrics.
"""


class PortPerformance:

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def execute(self):
        try:
            perf = pm.get_performance_vs_benchmark(
                self.portfolio, interval='ytd')
            perf = f"```{tabulate(perf, headers='keys', tablefmt='pretty')}```"
            return perf
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio performance information...")
