import matplotlib.pyplot as plt
from openbb_terminal.api import openbb


class Candle:

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            plt.rcParams.update({'font.size': 10})
            plt.rcParams["figure.dpi"] = 300
            fig, (ax1, ax2) = plt.subplots(2)
            plot = openbb.stocks.candle('AAPL', external_axes=[ax1, ax2])
            fig.suptitle('AAPL Price and Volume')
            ###
            return
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol to quote, e.g. <!intern quote AAPL>")
