from openbb_terminal.api import openbb
from openbb_terminal.stocks.fundamental_analysis import dcf_view
from . import dbx_utils as du


class DCF:

    def __init__(self, ticker):
        self.ticker = ticker

    def execute(self):
        try:
            workbook: str = dcf_view.CreateExcelFA(
                self.ticker).create_workbook()
            destination = workbook.replace(
                "/root/OpenBBUserData/exports", "/svf-intern-bot")
            return du.DropboxUtils().upload_and_link(workbook, destination)
        except IndexError as e:
            raise ValueError(
                "Please provide a symbol for price target history, e.g. <!intern pt AAPL>")
