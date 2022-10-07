from openbb_terminal.api import openbb
"""
Examples:
income AAPL
"""
class Income_Stmt:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = str(openbb.stocks.fa.av_income(self.ticker))
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for income statement, e.g. <!intern pt AAPL>")