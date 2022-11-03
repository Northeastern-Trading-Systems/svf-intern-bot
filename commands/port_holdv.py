import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
from uuid import uuid4
from constants import RISKFREERATE

"""
Get a chart of the values of all holdings in the portfolio.
"""
class HoldV:

    def __init__(self):
        openbb.portfolio.load('OpenBBTerminal/portfolio/holdings/Public_Equity_Orderbook.xlsx', RISKFREERATE)
        pass

    def execute(self):
        try:
            plt.rcParams.update({'font.size': 9})
            plt.rcParams["figure.dpi"] = 300
            fig, (ax1, ax2) = plt.subplots(2)

            # change to get a picture of holdv
            openbb.portfolio.holdv(external_axes=[ax1, ax2])

            fig.suptitle('Portfolio Holdings by Value')
            path = f'/home/charles/OpenBBUserData/exports/portfolio/charts/{hold-v}-{uuid4()}.png'
            fig.savefig(path, dpi=800)
            return ("IMG", path)
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio holdings values...")
