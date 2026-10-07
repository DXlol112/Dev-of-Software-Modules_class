# Student Tools

Мини-проект из глав 2.1–2.6: расчёт средней оценки и цветной вывод через Rich. Нужен Python 3.10 или новее; проект проверен на Python 3.12.14.

Все команды выполняются из этой папки, где находятся `app` и `requirements.txt`.

## Структура

```text
student-tools/
├── app/                      # Пакет приложения
│   ├── __init__.py
│   ├── main.py               # Данные, вызов функций и вывод через Rich
│   ├── services/             # Прикладные расчёты
│   │   ├── __init__.py
│   │   └── calculator.py     # Средняя оценка; пустой список вызывает ValueError
│   └── utils/                # Вспомогательные функции
│       ├── __init__.py
│       └── formatter.py      # Строка с двумя знаками после точки
├── tests/                    # Три проверки расчёта и оформления
│   └── test_calculator.py
├── .gitignore
├── README.md
└── requirements.txt          # Установленные пакеты с версиями
```

Локальная `.venv` создаётся рядом с `app` и исключена из Git. Точка запуска импортирует расчёт и оформление; эти модули от неё не зависят.

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

Если доступна команда `python`, а `py` отсутствует, окружение создаётся командой `python -m venv .venv`. Если активация запрещена, Python можно вызывать напрямую:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m app.main
.\.venv\Scripts\python.exe -m pytest -v
```

В VS Code команда **Python: Select Interpreter** выбирает `.venv/Scripts/python.exe` этого проекта.

## macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m app.main
python -m pytest -v
```

## Результат и проверки

Для оценок `[5, 4, 5, 3, 5]` программа выводит:

```text
Средний результат: 4.40
```

pytest выполняет три теста: средняя равна `4.4`, строка имеет два знака после точки, пустой список вызывает `ValueError`. Итог: **3 passed**. Импорт `app.main` не запускает расчёт и ничего не печатает.

`requirements.txt` получен через `python -m pip freeze` в окружении этого проекта, включая pytest. Для повторной установки создаётся новое окружение. Цвет вывода зависит от возможностей терминала.

Источник: [«Структура Python-проекта», главы 2.1–2.6](https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/02-struktura-python-proekta/01-venv.html).
