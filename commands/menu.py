from tabulate import tabulate


class Menu:
    msg: str

    def __init__(self):
        self.msg = "```\n----------------- MENU -----------------\n\nexample: !intern quote AAPL\n\n--------------- General: ---------------\n\n1) quote <ticker>\n  - displays a quote for the ticker\n2) candle <ticker>\n - display a candle chart of price and volume\n3) news <ticker>\n  - displays recent news on a ticker\n4) ta <ticker>\n  - displays TA summary for a ticker\n5) heatmap\n  - displays a 15min delayed mkt heatmap\n6) overview <ticker>\n  - display company overview\n\n-------- Fundamental Analysis: ---------\n\n1) dcf <ticker>\n  - returns a .xlsx DCF for a ticker\n2) insiders <ticker>\n  - displays top insider transactions on\n    a ticker\n3) filings <ticker>\n  - lists most recent SEC filings\n4) analysis <ticker>\n  - analyze SEC filings using ML\n5) cf <ticker>\n  - get recent CF data\n6) income <ticker>\n  - get recent IS data\n7) fd <ticker>\n  - get fundamental data\n\n--------------- Earnings: ---------------\n\n1) er <ticker>\n  - displays most recent ER for a ticker\n\n---------------- Street: ----------------\n\n1) analyst <ticker>\n  - display analyst recs on a ticker\n2) pt <ticker>\n - display analyst pts on a ticker\n\n---------------- Insiders: ----------------\n\n1) insiders <ticker>\n  - get recent insider activity\n2) shrs <ticker>\n  - get significant shareholders\n\n----------------- SVF: ------------------\n\n1) port\n  - display portfolio holdings\n```"

    def execute(self):
        return self.msg
