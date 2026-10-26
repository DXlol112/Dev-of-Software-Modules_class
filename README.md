# Разработка программных модулей

## О чём этот репозиторий

Он служит заменой тетради: здесь публикуются записи лекций, домашние работы и другие материалы по предмету **«Разработка программных модулей»**.

## Оглавление

| Номер | Занятие                                                                        | Домашняя работа                                                         |
| :---: | :----------------------------------------------------------------------------- | :---------------------------------------------------------------------- |
|   1   | [Введение](lesson_01/class/introduction.md)                                    | [Задание № 1](lesson_01/hw/hw-01.md)                                    |
|   2   | [Структура Python-проекта](lesson_02/class/python-project-structure.md)        | [Задание № 2](lesson_02/hw/hw-02.md)                                    |
|   3   | —                                                                              | [Практикум «Структура проекта»](lesson_03/hw/hw-03.md)                  |
|   4   | [Отчёт кафе — стартовый проект](lesson_04/class/cafe-report-starter/README.md) | [Практикум «Младший разработчик: первая неделя»](lesson_04/hw/hw-04.md) |

## Структура

```text
├── .github/
│   └── assets/
│       ├── lesson_01/
│       │   ├── grading.png
│       │   ├── internet-addresses.png
│       │   └── sprints.png
│       ├── lesson_02/
│       │   ├── 02-rich.png
│       │   ├── 05-venv-inside.png
│       │   ├── 11-freeze.png
│       │   ├── 14-vscode-interpreter.png
│       │   ├── 16-name-demo.png
│       │   ├── 25-tree.png
│       │   ├── 26-two-runs.png
│       │   ├── 29-activate-toggle.png
│       │   └── 32-pytest-ok.png
│       ├── lesson_03/
│       │   └── .gitkeep
│       └── lesson_04/
│           └── .gitkeep
├── lesson_01/
│   ├── class/
│   │   └── introduction.md
│   └── hw/
│       └── hw-01.md
├── lesson_02/
│   ├── class/
│   │   ├── student-tools-practice/
│   │   │   ├── app/
│   │   │   │   ├── services/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── calculator.py
│   │   │   │   ├── utils/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── formatter.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── main.py
│   │   │   ├── tests/
│   │   │   │   └── test_calculator.py
│   │   │   ├── .gitignore
│   │   │   ├── README.md
│   │   │   └── requirements.txt
│   │   ├── .gitkeep
│   │   └── python-project-structure.md
│   └── hw/
│       ├── trip/
│       │   ├── calculator.py
│       │   ├── README.md
│       │   ├── requirements.txt
│       │   └── trip.py
│       └── hw-02.md
├── lesson_03/
│   ├── class/
│   │   └── .gitkeep
│   └── hw/
│       ├── cafe-report/
│       │   ├── app/
│       │   │   ├── services/
│       │   │   │   ├── __init__.py
│       │   │   │   ├── orders.py
│       │   │   │   └── report.py
│       │   │   ├── utils/
│       │   │   │   ├── __init__.py
│       │   │   │   ├── money.py
│       │   │   │   └── text.py
│       │   │   ├── __init__.py
│       │   │   └── main.py
│       │   ├── data/
│       │   │   └── orders.csv
│       │   ├── docs/
│       │   │   └── about.md
│       │   ├── tests/
│       │   │   ├── __init__.py
│       │   │   ├── test_orders.py
│       │   │   └── test_report.py
│       │   ├── .gitignore
│       │   ├── README.md
│       │   └── requirements.txt
│       ├── text-kit/
│       │   ├── app/
│       │   │   ├── services/
│       │   │   │   ├── __init__.py
│       │   │   │   ├── statistics.py
│       │   │   │   └── validation.py
│       │   │   ├── utils/
│       │   │   │   ├── __init__.py
│       │   │   │   ├── dates.py
│       │   │   │   └── text.py
│       │   │   ├── __init__.py
│       │   │   └── main.py
│       │   ├── tests/
│       │   │   ├── __init__.py
│       │   │   ├── test_dates.py
│       │   │   ├── test_statistics.py
│       │   │   ├── test_text.py
│       │   │   └── test_validation.py
│       │   └── README.md
│       └── hw-03.md
├── lesson_04/
│   ├── class/
│   │   ├── cafe-report-starter/
│   │   │   ├── app/
│   │   │   │   ├── domain/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── order.py
│   │   │   │   │   └── shift.py
│   │   │   │   ├── services/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── calculator.py
│   │   │   │   │   ├── importer.py
│   │   │   │   │   ├── orders.py
│   │   │   │   │   └── report_file.py
│   │   │   │   ├── ui/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── console.py
│   │   │   │   ├── utils/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── clock.py
│   │   │   │   │   ├── formatter.py
│   │   │   │   │   └── text.py
│   │   │   │   └── __init__.py
│   │   │   ├── data/
│   │   │   │   └── shift.csv
│   │   │   ├── tests/
│   │   │   │   ├── test_calculator.py
│   │   │   │   ├── test_formatter.py
│   │   │   │   └── test_orders.py
│   │   │   ├── .gitignore
│   │   │   ├── main.py
│   │   │   ├── pyproject.toml
│   │   │   ├── README.md
│   │   │   ├── requirements.txt
│   │   │   └── type_examples.py
│   │   └── .gitkeep
│   └── hw/
│       └── hw-04.md
├── .gitignore
├── LICENSE
└── README.md
```
