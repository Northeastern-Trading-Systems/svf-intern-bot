from openbb_terminal.api import openbb
from openbb_terminal.stocks.fundamental_analysis import dcf_view
from dbx_utils import DropboxUtils


class DCF:

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            workbook: str = dcf_view.CreateExcelFA(
                self.ticker).create_workbook()
            destination = workbook.replace(
                "/root/OpenBBUserData/exports", "/svf-intern-bot")
            return
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for price target history, e.g. <!intern pt AAPL>")
