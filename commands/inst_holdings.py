"""
Examples:
inst-holdings AAPL
"""
class Inst_Holdings:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        # TODO: GET IH FROM OPENBB
        return