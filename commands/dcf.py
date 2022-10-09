from openbb_terminal.api import openbb
from openbb_terminal.stocks.fundamental_analysis import dcf_view
from . import dbx_utils as du
from tabulate import tabulate


class DCF:

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            workbook: str = dcf_view.CreateExcelFA(
                self.ticker).create_workbook()
            return ("XLSX", workbook)
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for price target history, e.g. <!intern pt AAPL>")
