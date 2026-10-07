# Student Tools

Мини-проект Student Tools: расчёт средней, минимальной и максимальной оценки и цветной вывод отчёта через Rich. Проект и зафиксированные зависимости проверены на Python 3.12.0.

Все команды выполняются из этой папки, где находятся `app` и `requirements.txt`.

## Структура

```text
student-tools/
├── app/                      # Пакет приложения
│   ├── __init__.py
│   ├── main.py               # Данные, вызов функций и вывод через Rich
│   ├── services/             # Прикладные расчёты
│   │   ├── __init__.py
│   │   └── calculator.py     # Средняя, минимум и максимум; ValueError для пустого списка
│   └── utils/                # Вспомогательные функции
│       ├── __init__.py
│       └── formatter.py      # Три строки отчёта; средняя с двумя знаками после точки
├── tests/                    # Пять тестов расчётов, оформления и пустого списка
│   └── test_calculator.py
├── .gitignore
├── README.md
└── requirements.txt          # Установленные пакеты с версиями
```

Локальная `.venv` создаётся рядом с `app` и исключена из Git. Точка запуска импортирует расчёт и оформление; эти модули от неё не зависят.

Окружение не передаётся через Git: в нём находятся установленные библиотеки и пути к Python на конкретном компьютере. На другом компьютере его нужно создать заново и установить версии пакетов из `requirements.txt`. Это позволяет восстановить зависимости без копирования чужого окружения.

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
Минимальная оценка: 3
Максимальная оценка: 5
```

pytest выполняет пять тестов: средняя равна `4.4`, минимум равен `3`, максимум равен `5`, отчёт содержит три строки, а все три расчётные функции вызывают `ValueError` для пустого списка. Итог: **5 passed**. Проверки пустых списков объединены в одну тестовую функцию; по условию домашнего задания требуется не менее семи отдельных тестов.

Импорт `app.main` не запускает расчёт и ничего не печатает.

`requirements.txt` фиксирует версии библиотек, включая pytest. Для повторной установки создаётся новое окружение. Цвет вывода зависит от возможностей терминала.

## Проверка чистой копии

07.10.2026 исходники скопированы в отдельную временную папку без старой `.venv` и кеша. Создано новое окружение, зависимости установлены из `requirements.txt`. Переменная `PYTHONPATH` удалена перед запуском: приложение использует только файлы чистой копии и её окружение.

Для повторения проверки выполните из корня репозитория в PowerShell:

```powershell
$source = (Resolve-Path .\lesson_02\hw\student-tools).Path
$check = Join-Path $env:TEMP ('student-tools-check-' + [guid]::NewGuid().ToString('N'))
robocopy $source $check /E /XD .venv __pycache__ .pytest_cache .git /XF .gitkeep *.pyc
# Для robocopy коды 0–7 означают успешное копирование, 8 и выше — ошибку.
& .\.venv\Scripts\python.exe -m venv (Join-Path $check '.venv')
Set-Location -LiteralPath $check
Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
$env:PYTHONIOENCODING = 'utf-8'
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m pip check
& .\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.version); print(sys.prefix != sys.base_prefix)"
& .\.venv\Scripts\python.exe -m app.main
& .\.venv\Scripts\python.exe -m pytest -v
& .\.venv\Scripts\python.exe -c "import app.main; print('Import OK')"
```

В команде создания окружения использован Python существующей `.venv` репозитория. При проверке на другом компьютере её можно заменить на `py -3.12 -m venv`.

Фактический вывод сведений о новом окружении:

```text
C:\Users\vovay\AppData\Local\Packages\sandbox.{d79d52da-584a-404b-8d15-f79fbee092a8}\AC\Temp\lesson02-clean-d373c4a157a94665b63df64a07cad278\.venv\Scripts\python.exe
3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)]
True
```

`True` подтверждает запуск внутри виртуального окружения. Зависимости установились успешно; `pip check` вывел `No broken requirements found.`. Программа напечатала отчёт `4.40`, `3`, `5`, совпадающий с разделом выше. Результат тестов: **5 passed in 0.03s**. При отдельном импорте напечаталось только `Import OK`.

Источник: [«Структура Python-проекта», главы 2.1–2.6](https://algorthimization-course-vvodnoe.vercel.app/mdk0101-razrabotka-modulei/lessons/02-struktura-python-proekta/01-venv.html).
