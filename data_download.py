import yfinance as yf
import logging


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    """Вычисляет и выводит среднюю цену закрытия акций за заданный период."""
    average_price = data['Close'].mean(axis=0)
    logging.info(f'Выводится среднее значение колонки "Close": {average_price}')
    print(f'Среднее значение колонки "Close": {average_price}\n')
    return data