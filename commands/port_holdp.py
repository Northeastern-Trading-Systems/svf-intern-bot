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

    def __init__(self):
        self.portfolio = PORTFOLIO
        self.portfolio.load_portfolio_historical_prices()
        self.portfolio.populate_historical_trade_data()
        self.portfolio.calculate_value()

    def execute(self):

        try:
            holdp = pm.get_holdings_percentage(PORTFOLIO)
            plt.plot(holdp, labels=holdp.columns)
            plt.legend()
            plt.suptitle('Portfolio Holdings by Percentage')
            path = f'/home/charles/OpenBBUserData/exports/portfolio/charts/hold-p-{uuid4()}.png'
            plt.savefig(path, dpi=800)
            return ("IMG", path)
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio holdings percentages...")
