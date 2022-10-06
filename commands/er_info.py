from openbb_terminal.api import openbb
"""
Examples:
er AAPL
"""
class ER_Info:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = "Command not yet supported..."
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for price target history, e.g. <!intern pt AAPL>")