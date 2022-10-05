class Heatmap:
    map: None

    def __init__(self):
        self.map = None

    def execute(self):
        try:
            result = str(openbb.stocks.disc.heatmap())  # Might not be a function
            return result
        except IndexError as e:
            raise ValueError("Please provide a symbol for price target history, e.g. <!intern pt AAPL>")