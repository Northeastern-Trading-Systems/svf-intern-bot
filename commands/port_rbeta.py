import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
from uuid import uuid4
from constants import RISKFREERATE

"""
Get a chart of the rolling beta of the portfolio.
"""
class RollingBeta:

    def __init__(self):
        pass

    def execute(self):
        try:
            plt.rcParams.update({'font.size': 9})
            plt.rcParams["figure.dpi"] = 300
            fig, (ax1, ax2) = plt.subplots(2)
            openbb.portfolio.rbeta(external_axes=[ax1, ax2])
            fig.suptitle('Rolling Portfolio Beta')
            path = f'/home/charles/OpenBBUserData/exports/portfolio/charts/{rbeta}-{uuid4()}.png'
            fig.savefig(path, dpi=800)
            return ("IMG", path)
        except IndexError as e:
            raise ValueError(
                "Error retrieving rolling portfolio beta...")