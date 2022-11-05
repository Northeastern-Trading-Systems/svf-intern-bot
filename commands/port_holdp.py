from distutils.util import rfc822_escape
from tabulate import tabulate
import pandas as pd
import numpy as np
import openbb_terminal.api as openbb
from openbb_terminal.portfolio.portfolio_analysis import portfolio_model as pmdf
from openbb_terminal.portfolio import portfolio_model as pm
import yfinance as yf
import matplotlib.pyplot as plt
from uuid import uuid4
from constants import PORTFOLIO

class HoldP:
    """
    Holdings percentage command.
    """

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def execute(self):

        try:
            holdp = pm.get_holdings_percentage(self.portfolio)
            plt.plot(holdp, label='Ticker')
            plt.legend(holdp)
            plt.suptitle('Portfolio Holdings by Percentage')
            plt.xlabel('Date')
            plt.ylabel('Percentage of Portfolio')
            plt.rcParams.update({'font.size': 9})
            plt.rcParams["figure.dpi"] = 300
            path = f'/home/charles/OpenBBUserData/exports/portfolio/charts/holdp-{uuid4()}.png'
            fig = plt
            fig.savefig(path, dpi=800)
            return ("IMG", path)

        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio holdings percentages...")
