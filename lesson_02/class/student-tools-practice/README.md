# Student Tools · практика 2.7

Проект восстановлен из архива практики: файлы переименованы и разложены по ответственности. Код функций и импорты из заготовки сохранены. Программа считает среднюю оценку и выводит результат через Rich.

Нужен Python 3.10 или новее; проект проверен на Python 3.12.14. Все команды выполняются из этой папки, рядом с `app` и `requirements.txt`.

## Структура

```text
student-tools-practice/
├── app/                      # Пакет приложения
│   ├── __init__.py
│   ├── main.py               # Данные, расчёт и вывод результата
│   ├── services/             # Прикладной расчёт
│   │   ├── __init__.py
│   │   └── calculator.py     # Функция calculate_average
│   └── utils/                # Вспомогательное оформление
│       ├── __init__.py
│       └── formatter.py      # Функция format_average
├── tests/                    # Проверки функций из отдельной папки
│   └── test_calculator.py
├── .gitignore
├── README.md
└── requirements.txt          # Список библиотек из архива практики
```

В каждой папке пакета есть пустой `__init__.py`. Точка запуска импортирует расчёт и оформление; обратных импортов нет. `.venv` создаётся в корне проекта и не передаётся в Git.

## Windows · PowerShell

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
python -m pip install -r requirements.txt
python -m app.main
python -m pytest -v
```

Если `py` отсутствует, но доступен `python`, используется `python -m venv .venv`. Без активации команды выполняются так:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m app.main
.\.venv\Scripts\python.exe -m pytest -v
```

В VS Code выбирается интерпретатор `.venv/Scripts/python.exe` этой папки.

## macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m app.main
python -m pytest -v
```

## Ожидаемый результат

```text
Средний результат: 4.40
```

Три теста проверяют среднюю оценку, формат строки и ошибку для пустого списка. Итог: **3 passed**. Импорт `app.main` проходит без вывода. Поддержка цвета зависит от терминала.

Источник: [«Практика: верните файлам порядок», глава 2.7](https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/02-struktura-python-proekta/07-praktika.html).
