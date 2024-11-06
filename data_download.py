import yfinance as yf
import logging
from fileinput import filename

def fetch_stock_data(ticker, period, start_date = None, end_date = None):
    """ Получает исторические данные об акциях для указанного тикера и временного периода.
     Возвращает DataFrame с данными. """
    stock = yf.Ticker(ticker)
    logging.info(f'Объект "Ticker" {stock}')
    if period:
        data = stock.history(period = period)
        logging.info(f'Временной период с определенным интервалом {type(data)}')
        return data
    elif start_date and end_date:
        data = stock.history(start = start_date, end = end_date)
        logging.info(f'Временной период с заданным интервалом {type(data)}')
        return data



def add_moving_average(data, window_size=5):
     """ Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия."""
    data['Moving_Average'] = data['Close'].rolling(window = window_size).mean()
    return data

def calculate_rsi(data, window=14):
     """Добавляет и рассчитывает дополнительный технический индикатор RSI."""
    logging.info(f"Расчет RSI с размером окна {window}")
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    logging.info("RSI успешно рассчитан")
    return data

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
     """Добавляет и рассчитывает дополнительный технический индикатор MACD"""
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
    max_price = data['Close'].max()
    min_price = data['Close'].min()
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
    """ Сохранение данных в csv файл """
    logging.info(f'Экспорт данных в файл {filename}')
    data.to_csv(filename)
    logging.info(f'данные успешно сохранены в файл {filename}')

