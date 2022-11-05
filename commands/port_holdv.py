import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
from uuid import uuid4
from constants import RISKFREERATE
from openbb_terminal.portfolio import portfolio_model as pm

"""
Get a chart of the values of all holdings in the portfolio.
"""
class HoldV:

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def execute(self):
        try:
            holdv = pm.get_holdings_value(self.portfolio)
            plt.plot(holdv, label='Ticker')
            plt.legend(holdv)
            plt.suptitle('Portfolio Holdings by Value')
            plt.xlabel('Date')
            plt.ylabel('Value of Holding')
            plt.rcParams.update({'font.size': 9})
            plt.rcParams["figure.dpi"] = 300
            path = f'/home/charles/OpenBBUserData/exports/portfolio/charts/holdv-{uuid4()}.png'
            fig = plt
            fig.savefig(path, dpi=800)
            return ("IMG", path)
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio holdings values...")
