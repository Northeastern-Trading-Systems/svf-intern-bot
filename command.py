from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from multiprocessing.sharedctypes import Value
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
                self.result = str(openbb.stocks.quote(symbol))
            except IndexError as e:
                raise ValueError("Please provide a symbol to quote, e.g. <!intern quote AAPL>")
    
    def get_result(self):
        return self.result



