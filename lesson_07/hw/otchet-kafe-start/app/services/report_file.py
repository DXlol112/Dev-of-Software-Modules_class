"""Сохранение отчёта в текстовый файл."""

from pathlib import Path


def save_report(path: Path, lines: list[str]) -> int:
    """Сохранить строки отчёта в файл и вернуть их количество.

    Args:
        path: Путь к файлу отчёта.
        lines: Строки отчёта.

    Returns:
        Количество записанных строк.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return len(lines)
