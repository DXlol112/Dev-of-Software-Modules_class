# Разработка программных модулей

## О чём этот репозиторий

Он служит заменой тетради: здесь будут публиковаться записи лекций, домашние работы и другие материалы по предмету **«Разработка программных модулей»**.

## Оглавление

| Номер |                  Занятие                  |                                  Домашняя работа                                  |
| :---: | :---------------------------------------: | :-------------------------------------------------------------------------------: |
|   1   | [Введение](lesson_01/class/1.Введение.md) |                     [Задание № 1](lesson_01/homework/hw_1.md)                     |
|   2   | [Структура Python-проекта](lesson_02/class/2.Структура_Python-проекта.md) | [Задание № 2](lesson_02/hw/hw_02.md) |
|   3   |                     -                     |               [Практикум «Структура проекта»](lesson_03/hw/hw-03.md)               |
|   4   |                     -                     | [Практикум «Младший разработчик: первая неделя»](lesson_04/hw/podpisi-practic.md) |

## Структура

Дерево включает все файлы рабочей папки, в том числе скрытые. Каталоги `.git` и `.venv`, папки кеша и файлы `.gitkeep` исключены; пустые папки сохранены.

```text
├── .github/
│   └── assets/
│       ├── lesson_01/
│       │   ├── Pasted image 20260902173817.png
│       │   ├── Pasted image 20260902180750.png
│       │   └── Pasted image 20260902180920.png
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
│       └── lesson_04/
├── lesson_01/
│   ├── class/
│   │   └── 1.Введение.md
│   └── homework/
│       └── hw_1.md
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
│   │   └── 2.Структура_Python-проекта.md
│   └── hw/
│       ├── student-tools/
│       │   ├── app/
│       │   │   ├── services/
│       │   │   │   ├── __init__.py
│       │   │   │   └── calculator.py
│       │   │   ├── utils/
│       │   │   │   ├── __init__.py
│       │   │   │   └── formatter.py
│       │   │   ├── __init__.py
│       │   │   └── main.py
│       │   ├── tests/
│       │   │   └── test_calculator.py
│       │   ├── .gitignore
│       │   ├── README.md
│       │   └── requirements.txt
│       └── hw_02.md
├── lesson_03/
│   ├── class/
│   └── hw/
│       ├── praktikum-1-cafe-report/
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
│       │   │   └── adout.md
│       │   ├── tests/
│       │   │   ├── __init__.py
│       │   │   ├── test_orders.py
│       │   │   └── test_report.py
│       │   ├── .gitignore
│       │   ├── README.md
│       │   └── requirements.txt
│       ├── praktikum-2-text-kit/
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
│       │   └── tests/
│       │       ├── __init__.py
│       │       ├── test_dates.py
│       │       ├── test_statistics.py
│       │       ├── test_text.py
│       │       └── test_validation.py
│       └── hw-03.md
├── lesson_04/
│   ├── class/
│   └── hw/
│       └── podpisi-practic.md
├── .gitignore
├── LICENSE
└── README.md
```
