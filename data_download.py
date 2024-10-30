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

def notify_if_strong_fluctuations(data, threshold):
    """ Уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период. """
    list_prices_close = data['Close'].tolist()
    max_price = max(list_prices_close)
    min_price = min(list_prices_close)
    difference = max_price - min_price
    """Средняя цена и порог колебания цен в процентах:"""
    average_price = (max_price + min_price) / 2
    threshold = difference / (average_price / 100)
    """Разница между максимальной и минимальной ценой в процентах."""
    percentage_difference = difference / min_price * 100

    if percentage_difference > threshold:
        logging.info(f'Значение колебаний: {percentage_difference}')
        print(f'Превышен порог цен -{percentage_difference}, допустимое значение -{threshold}')
