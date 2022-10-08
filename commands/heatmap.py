from openbb_terminal.api import openbb
from tabulate import tabulate


class Heatmap:
    map: None

    def __init__(self):
        self.map = None

    def execute(self):
        try:
            # Might not be a function
            result = str(openbb.stocks.disc.heatmap())
            return result
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for price target history, e.g. <!intern pt AAPL>")
