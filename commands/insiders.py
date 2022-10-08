from openbb_terminal.api import openbb
"""
Examples:
insiders AAPL
"""
class Insiders:
    ticker: str

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            result = openbb.stocks.ins.lins(self.ticker)
            #result = result[0:34]
            #result = result.drop(result.columns[[2, 3, 4]], axis=1)
            result = f"```{tabulate(result, headers='keys', tablefmt='pretty')}```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for insider holdings, e.g. <!intern pt AAPL>")