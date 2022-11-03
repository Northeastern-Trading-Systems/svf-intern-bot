import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
from uuid import uuid4
from constants import RISKFREERATE

"""
Get a chart of the rolling vol of the portfolio.
"""
class RollingVolatility:

    def __init__(self):
        openbb.portfolio.load('OpenBBTerminal/portfolio/holdings/Public_Equity_Orderbook.xlsx', RISKFREERATE)
        pass

    def execute(self):
        try:
            plt.rcParams.update({'font.size': 9})
            plt.rcParams["figure.dpi"] = 300
            fig, (ax1, ax2) = plt.subplots(2)
            openbb.portfolio.rvol(external_axes=[ax1, ax2])
            fig.suptitle('Rolling Portfolio Volatility')
            path = f'/home/charles/OpenBBUserData/exports/portfolio/charts/{rvol}-{uuid4()}.png'
            fig.savefig(path, dpi=800)
            return ("IMG", path)
        except IndexError as e:
            raise ValueError(
                "Error retrieving rolling portfolio vol...")
