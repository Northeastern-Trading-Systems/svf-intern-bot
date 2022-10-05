from typing import List
from openbb_terminal.api import openbb

class Command:

    def __init__(self, words: List[str]):
        """
        Parse command strings and convert to command object.
        """
        self.result = ""
        if len(words) > 0 and words[0] == "quote":
            try:
                symbol = words[1]
                self.function = lambda x: str(openbb.stocks.quote(x[0]))
            except IndexError as e:
                raise ValueError("Please provide a symbol to quote, e.g. <!intern quote AAPL>")
    
    def apply(self, args: List):
        return self.function(args)



