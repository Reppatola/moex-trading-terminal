import requests
import pandas as pd
from datetime import datetime
from config import MOEX_API

class MoexClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "MOEX-Terminal/1.0"})

    def _build_url(self, endpoint: str) -> str:
        return f"{MOEX_API['ISS_URL']}{endpoint}"

    def get_candles(self, ticker: str, interval: int = 1, limit: int = 100) -> pd.DataFrame:
        """Получение свечей по спецификации ISS"""
        url = self._build_url(
            f"/engines/{MOEX_API['ENGINE']}/markets/{MOEX_API['MARKET']}/securities/{ticker}/candles.json"
        )
        params = {
            "interval": interval,
            "limit": limit,
            "from": datetime.now().strftime("%Y-%m-%d")
        }
        
        response = self.session.get(url, params=params)
        data = response.json()
        
        return pd.DataFrame(
            data["candles"]["data"],
            columns=data["candles"]["columns"]
        ).assign(
            begin=lambda x: pd.to_datetime(x['begin']),
            end=lambda x: pd.to_datetime(x['end'])
        )

    def get_orderbook(self, ticker: str, depth: int = 10) -> dict:
        """Получение стакана цен"""
        url = self._build_url(
            f"/engines/{MOEX_API['ENGINE']}/markets/{MOEX_API['MARKET']}/securities/{ticker}/orderbook.json"
        )
        return self.session.get(url, params={"depth": depth}).json()

    def get_securities(self) -> pd.DataFrame:
        """Список всех инструментов"""
        url = self._build_url(
            f"/engines/{MOEX_API['ENGINE']}/markets/{MOEX_API['MARKET']}/boards/{MOEX_API['BOARD']}/securities.json"
        )
        data = self.session.get(url).json()
        return pd.DataFrame(
            data["securities"]["data"],
            columns=data["securities"]["columns"]
        )