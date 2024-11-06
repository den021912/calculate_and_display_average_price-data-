## Описание
Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков. Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике. Проект также включает функции уведомления о сильных колебаниях цен, вычисления средней цены закрытия за период, а также добавления дополнительных технических индикаторов, таких как RSI (индекс относительной силы) и MACD (схождение-расхождение скользящих средних).
Структура и модули проекта
## Основные функции      
1 data_download.py:
- Отвечает за загрузку исторических данных о ценах на акции с использованием yfinance.
- Вычисление средней цены закрытия за период.
- Уведомление о сильных колебаниях цены (более чем на заданный процент).
- Расчет и добавление технических индикаторов: RSI и MACD.
- Сохранение данных в CSV файл.

2 main.py:
- Запрашивает у пользователя наименование акции и временной период, загружает данные, обрабатывает
 их и выводит результаты в виде графика.

3 data_plotting.py:
- Отвечает за визуализацию данных.
- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.