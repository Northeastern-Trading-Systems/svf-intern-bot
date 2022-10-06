from openbb_terminal.api import openbb
from tabulate import tabulate
import pandas as pd
"""
Examples:
news AAPL
"""

class News:

    def __init__(self, *param):
        self.param = " ".join(param)

    def execute(self):
        try:
            result = "```\n"+tabulate(openbb.common.news(self.param).head(n=10), headers='keys', tablefmt='psql', showindex=False)+"\n```"
            return result
        except IndexError as e:
            raise ValueError("Please provide a single search term for news, e.g. <!intern news twitter>")