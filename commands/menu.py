class Menu:
    msg: str

    def __init__(self):
        self.msg = "----------------- MENU -----------------\n\nexample: !intern quote AAPL\n\n--------------- General: ---------------\n\n1) quote <ticker>\n  - displays a quote for the ticker\n2) news <ticker>\n  - displays recent news on a ticker\n3) ta <ticker>\n  - displays TA summary for a ticker\n4) heatmap\n  - displays a 15min delayed mkt heatmap\n5) overview <ticker>\n  - display company overview\n\n-------- Fundamental Analysis: ---------\n\n1) dcf <ticker>\n  - returns a .xlsx DCF for a ticker\n2) inst-holdings <ticker>\n  - displays top institutional owners \n3) insiders <ticker>\n  - displays top insider transactions on\n    a ticker\n4) analysis <ticker>\n  - extract significant info from    SEC filings using ML\n\n\n--------------- Earnings: ---------------\n\n1) er <ticker>\n  - displays most recent ER for a ticker\n3) er-imp-move <ticker>\n  - displays implied move for a ticker\n    using options data\n\n---------------- Street: ----------------\n\n1) analyst <ticker>\n  - display analyst recs on a ticker\n2) pt <ticker>\n - display analyst pts on a ticker\n\n\n----------------- SVF: ------------------\n\n1) port\n  - display portfolio holdings"

    def execute(self):
        print(self.msg)