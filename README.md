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
- Рассчитывает стандартное отклонение цены закрытия.
- Вычисляет среднее значение колонки 'Close', результат выводиться в консоль.

2 main.py:
- Запрашивает у пользователя наименование акции и временной период, загружает данные, обрабатывает
 их и выводит результаты в виде графика.

3 data_plotting.py:
- Отвечает за визуализацию данных.
- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.
## Пример 
```python
Добро пожаловать в инструмент получения и построения графиков биржевых данных.
Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).
Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
Введите тикер акции (например, «AAPL» для Apple Inc):»GOOGL
Введите период для данных (например, '1mo' для одного месяца): 1mo
Введите дату начала анализа(yyyy-mm-dd):2023-12-09
Введите дату окончания для анализа данных(yyyy-mm-dd):2024-01-09
Введите стиль оформления графика (например, 'ggplot', 'default'): ggplot
```
