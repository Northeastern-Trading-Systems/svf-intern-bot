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

class PortfolioHoldings:
    """
    Multipurpose portfolio class. Provides:
    - top-level portfolio construction on initialization
    - portfolio overview command
    - subclasses to provide other commands on the top-level portfolio object
    """

    def __init__(self):
        portfolio2 = pmdf.load_portfolio('Public_Equity_Orderbook.xlsx')
        portfolio2 = portfolio2.drop(columns=['Type', 'Side', 'Currency', 'Industry', 'Country', 'Region', 'Fees', 'Premium'], axis=1)
        portfolio2.round(2)
        self.portfolio = portfolio2

    def execute(self):
        try:
            result = f"```{tabulate(self.portfolio, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError(
                "Error retrieving portfolio holdings...")