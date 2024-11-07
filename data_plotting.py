import matplotlib.pyplot as plt
import pandas as pd
import logging


def create_and_save_plot(data, ticker, period, filename = None, style = input):
    """ Создаёт график, отображающий цены закрытия и скользящие средние. Отображает на графике дополнительные технические индикаторы  RSI и MACD.
         Предоставляет возможность сохранения графика в файл. """
    if style not in plt.style.available:
        logging.warning(f"Стиль '{style}' не найден. Выберите другой стиль, пожалуйста.")
        style = input()

    """ Применяем выбранный стиль """
    plt.style.use(style)
    plt.figure(figsize = (10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label = 'Close Price')
            plt.plot(dates, data['Moving_Average'].values, label = 'Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label = 'Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label = 'Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
    """ График RSI """
    if 'RSI' in data.columns:
        plt.plot(data.index, data['RSI'], label = 'RSI')
        plt.title('Relative Strength Index (RSI)')
        plt.xlabel("Дата")
        plt.ylabel("RSI")
        plt.legend()
    """ График MACD """
    if 'MACD' in data.columns and 'Signal' in data.columns:
        plt.plot(data.index, data['MACD'], label = 'MACD')
        plt.plot(data.index, data['Signal'], label = 'Signal')
        plt.title('Moving Average Convergence Divergence (MACD)')
        plt.xlabel("Дата")
        plt.ylabel("MACD")
        plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    logging.info(f"График сохранен как {filename}")
    print(f"График сохранен как {filename}")
