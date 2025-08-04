# src/config.py
MOEX_API = {
    # Базовые URL
    "ISS_URL": "https://iss.moex.com/iss",
    "WS_URL": "wss://iss.moex.com/ws",
    
    # Параметры рынка
    "ENGINE": "stock",       # Рынок акций
    "MARKET": "shares",      # Биржевой рынок
    "BOARD": "TQBR",        # Основная сессия
    
    # Интервалы свечей (в минутах)
    "CANDLE_INTERVALS": {
        "1min": 1,
        "10min": 10,
        "1hour": 60, 
        "1day": 24
    },
    
    # Лимиты данных
    "DEFAULT_LIMIT": 100,    # Количество свечей по умолчанию
    "MAX_LIMIT": 500        # Максимальный лимит
}