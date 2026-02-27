"""
Модуль для загрузки данных о котировках акций.
Источник: Alpha Vantage API (альтернативный источник)
"""

import pandas as pd

def load_stock_data(ticker, start_date, end_date):
    """
    Загрузка исторических данных по акции через Alpha Vantage
    
    Parameters:
    ticker (str): Тикер акции
    start_date (str): Начальная дата
    end_date (str): Конечная дата
    
    Returns:
    pd.DataFrame: DataFrame с котировками
    """
    print(f"Загрузка данных для {ticker} из Alpha Vantage...")
    
    # Заглушка для демонстрации
    print(f"Данные загружены: {ticker}")
    
    return pd.DataFrame()

if __name__ == "__main__":
    # Пример использования
    data = load_stock_data("AAPL", "2023-01-01", "2023-12-31")
    print("Тестовый запуск завершен")
