import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
from uuid import uuid4


class Candle:

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            plt.rcParams.update({'font.size': 9})
            plt.rcParams["figure.dpi"] = 300
            fig, (ax1, ax2) = plt.subplots(2)
            openbb.stocks.candle(self.ticker, external_axes=[ax1, ax2])
            fig.suptitle('AAPL Price and Volume')
            path = f'/root/OpenBBUserData/exports/stocks/charts/{self.ticker}-{uuid4()}.png'
            fig.savefig(path, dpi=800)
            return ("IMG", path)
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol to quote, e.g. <!intern quote AAPL>")
