import matplotlib.pyplot as plt
import pandas as pd
import logging


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if 'RSI' in data.columns:
        plt.plot(data.index, data['RSI'], label='RSI')
        plt.title('Relative Strength Index (RSI)')
        plt.xlabel("Дата")
        plt.ylabel("RSI")
        plt.legend()

    if 'MACD' in data.columns and 'Signal' in data.columns:
        plt.plot(data.index, data['MACD'], label='MACD')
        plt.plot(data.index, data['Signal'], label='Signal')
        plt.title('Moving Average Convergence Divergence (MACD)')
        plt.xlabel("Дата")
        plt.ylabel("MACD")
        plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    logging.info(f"График сохранен как {filename}")
    print(f"График сохранен как {filename}")
