from openbb_terminal.api import openbb
"""
Examples:
analyst AAPL
"""
class Analyst_Recommendations:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.dd.analyst(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for analyst recommendations, e.g. <!intern analyst AAPL>")