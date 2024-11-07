import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    start = input("Введите дату начала анализа(yyyy-mm-dd):")
    end = input("Введите дату окончания для анализа данных(yyyy-mm-dd):")
    style = input("Введите стиль оформления графика (например, 'ggplot', 'default'): ")


    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Calculate RSI
    stock_data = dd.calculate_rsi(stock_data)

    # Calculate MACD
    stock_data = dd.calculate_macd(stock_data)

    # Calculate and display average price
    dd.calculate_and_display_average_price(stock_data)

    threshold = float(input("Уведомление о сильных колебаниях. Введите порог колебания цен в процентах: "))
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    dd.export_data_to_csv(stock_data, "dataframe.csv'")

    dplt.create_and_save_plot(stock_data, ticker, period, style = style)





if __name__ == "__main__":
    main()
