import yfinance as yf
import logging
from fileinput import filename

def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_rsi(data, window=14):
    logging.info(f"Расчет RSI с размером окна {window}")
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    logging.info("RSI успешно рассчитан")
    return data

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    logging.info(f"Расчет MACD с коротким окном {short_window}, длинным окном {long_window} и сигнальным окном {signal_window}")
    data['EMA_short'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_long'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA_short'] - data['EMA_long']
    data['Signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    logging.info("MACD успешно рассчитан")
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

def export_data_to_csv(data, filename):
    logging.info(f'Экспорт данных в файл {filename}')
    data.to_csv(filename)
    logging.info(f'данные успешно сохранены в файл {filename}')

