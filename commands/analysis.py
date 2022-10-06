from openbb_terminal.api import openbb
"""
Examples:
analysis AAPL
"""
class Analysis:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.fa.analyst(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for analysis, e.g. <!intern analyst AAPL>")