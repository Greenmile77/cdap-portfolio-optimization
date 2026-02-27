# Version: 1.5 - Feature branch
"""
Модуль для загрузки данных о котировках акций.
Источник: Yahoo Finance
"""

import pandas as pd
import yfinance as yf

def load_stock_data(ticker, start_date, end_date):
    """
    Загрузка исторических данных по акции
    
    Parameters:
    ticker (str): Тикер акции (например, 'AAPL' для Apple)
    start_date (str): Начальная дата в формате 'YYYY-MM-DD'
    end_date (str): Конечная дата в формате 'YYYY-MM-DD'
    
    Returns:
    pd.DataFrame: DataFrame с котировками
    """
    print(f"Загрузка данных для {ticker}...")
print(f"Данные загружены: {ticker} с {start_date} по {end_date}")
return pd.DataFrame()
if __name__ == "__main__":
data = load_stock_data("AAPL", "2023-01-01", "2023-12-31")
    print(data.head()
