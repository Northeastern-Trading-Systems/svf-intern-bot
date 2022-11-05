import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
from uuid import uuid4
from constants import RISKFREERATE
from openbb_terminal.portfolio import portfolio_model as pm

"""
Get a chart of the rolling beta of the portfolio.
"""


class RollingBeta:

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def execute(self):
        try:
            rbeta = pm.get_rolling_beta(self.portfolio, window="6m")
            plt.plot(rbeta, label='Ticker')
            plt.suptitle('Rolling Portfolio Beta')
            plt.xlabel('Date')
            plt.ylabel('Beta')
            plt.rcParams.update({'font.size': 9})
            plt.rcParams["figure.dpi"] = 300
            path = f'/home/charles/OpenBBUserData/exports/portfolio/charts/rbeta-{uuid4()}.png'
            fig = plt
            fig.savefig(path, dpi=800)
            plt.clf()
            return ("IMG", path)
        except IndexError as e:
            raise ValueError(
                "Error retrieving rolling portfolio beta...")
