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
        """
        Construct an openBB portfolio object from the save location. 
        """

        portfolio = pm.PortfolioModel(pmdf.load_portfolio(
            'Public_Equity_Orderbook.xlsx'))
        rf_rate = yf.Ticker("^TNX").info["regularMarketPrice"]
        portfolio.set_risk_free_rate(float(rf_rate))
        portfolio.load_portfolio_historical_prices()
        portfolio.populate_historical_trade_data()
        portfolio.calculate_value()
        PORTFOLIO = portfolio

    def execute(self):
        raise NotImplementedError()