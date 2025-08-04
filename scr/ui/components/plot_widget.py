# В файле src/ui/components/plot_widget.py
from core.api.moex import MoexClient

class PlotWidget(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.api = MoexClient()
        self.load_data("SBER")

    def load_data(self, ticker: str):
        df = self.api.get_candles(ticker)
        # Далее преобразование в Plotly...