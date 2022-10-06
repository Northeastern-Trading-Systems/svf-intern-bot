from openbb_terminal.api import openbb
"""
Examples:
news AAPL
"""

class News:

    def __init__(self, param):
        self.param = param

    def execute(self):
        try:
            result = str(openbb.common.news(self.param))
            return result
        except IndexError as e:
            raise ValueError("Please provide a single search term for news, e.g. <!intern news twitter>")