# Отчёт кафе — стартовый проект

Рабочий код без описаний в `app/`. Задача темы 04: задокументировать его
в формате Google и добиться, чтобы проверка проходила без замечаний.
Нужен Python 3.10 или новее; запуск и тесты проверены на Python 3.12.0.

## Windows · PowerShell

Команды выполняются из папки `lesson_04/class/cafe-report-starter`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
python type_examples.py
```

## macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
python type_examples.py
```

## Ожидаемый результат

Заголовок со сегодняшней датой, три строки с официантами:

```text
Петрова Анна                  2 480,50 ₽
Иванов Пётр                   1 685,00 ₽
Сидоров Илья                    772,00 ₽
```

Итог — **4 937,50 ₽**. Файл `data/shift.csv` находится относительно `main.py`,
поэтому запуск по пути из другой рабочей папки тоже поддерживается.

`type_examples.py` демонстрирует аннотации, границы оценок, сумму и подпись.
Вызов `reveal_type` выполняется только при статической проверке типов.

## Проверки

```powershell
python -m pytest -v
python -m mypy app main.py type_examples.py
python -m ruff check app
```

Проходят **12 тестов**, mypy не находит ошибок типов.
Ruff сообщает о **33 отсутствующих описаниях** в `app/`: это исходное состояние
учебной заготовки и предмет задания. Для проверки ошибок кода отдельно:

```powershell
python -m ruff check app main.py type_examples.py --select E,F
```

## Что в проекте

- `app/domain/` — заказ и смена: объекты предметной области.
- `app/services/` — чтение файла, расчёты и запись отчёта.
- `app/utils/` — имена, суммы и дата.
- `app/ui/` — печать в консоль.
- `data/shift.csv` — файл смены: официант и сумма заказа в копейках.
- `main.py` — сборка и печать отчёта.
- `type_examples.py` — запускаемые примеры аннотаций типов.
- `tests/` — проверки расчётов и форматирования.
- `requirements.txt`, `pyproject.toml` — зависимости и настройки проверок.
- `.gitignore`, `.vscode/settings.json` — правила Git и настройки редактора.
