from tabulate import tabulate


class Menu:
    msg: str

    def __init__(self):
        self.msg = "```\n----------------- MENU -----------------\n\nexample: !intern quote AAPL\n\n--------------- General: ---------------\n\n```"

    def execute(self):
        return self.msg
