from openbb_terminal.api import openbb
from openbb_terminal.stocks.fundamental_analysis import dcf_view


class DCF:

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            workbook = dcf_view.CreateExcelFA(self.ticker).create_workbook()
            return workbook
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for price target history, e.g. <!intern pt AAPL>")
