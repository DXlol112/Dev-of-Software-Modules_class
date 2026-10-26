# Cafe Report

Программа читает заказы кофейни из файла `data/orders.csv` и печатает отчёт:
количество заказов, выручку, средний чек и суммы по официантам.

Внешних библиотек нет, нужен только Python 3.10 или новее.

## Запуск

Команды выполняются из папки `lesson_03/hw/cafe-report`, рядом с `app/` и `data/`.

```
python -m app.main
python -m unittest discover -s tests -v
```

На Windows вместо `python` можно использовать `py`, если он доступен.
Установка пакетов не требуется.

## Ожидаемый результат

```
ОТЧЁТ ПО ЗАКАЗАМ
----------------------------------
Заказов: 6
Выручка: 3 702,00 ₽
Средний чек: 617,00 ₽
----------------------------------
Анна Петрова      770,00 ₽
Игорь Смирнов     1 793,00 ₽
Мария Ким         1 139,00 ₽
```

Тесты дают строку `Ran 9 tests` и `OK`.

## Структура

```text
cafe-report/
├── app/
│   ├── services/
│   │   ├── __init__.py
│   │   ├── orders.py
│   │   └── report.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── money.py
│   │   └── text.py
│   ├── __init__.py
│   └── main.py
├── data/
│   └── orders.csv
├── docs/
│   └── about.md
├── tests/
│   ├── __init__.py
│   ├── test_orders.py
│   └── test_report.py
├── .gitignore
├── README.md
└── requirements.txt
```

