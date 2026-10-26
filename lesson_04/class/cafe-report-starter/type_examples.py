"""Примеры аннотаций типов и форматирования для занятия 04."""

from typing import TYPE_CHECKING

from app.services.calculator import grade_bounds
from app.utils.formatter import format_title
from app.utils.text import normalize_name

if TYPE_CHECKING:
    from typing_extensions import reveal_type


def total(prices: list[int | float]) -> int | float:
    """Возвращает сумму цен."""
    return sum(prices)


def pick(flag: bool) -> str | None:
    """Возвращает подпись при наличии выручки."""
    label = "есть выручка"
    if flag:
        return label
    return None


def main() -> None:
    """Печатает результаты примеров без ошибок времени выполнения."""
    bounds = grade_bounds([5, 3, 4])
    if TYPE_CHECKING:
        reveal_type(bounds)

    print(format_title(" Примеры типов ", 40))
    print("Границы оценок:", bounds)
    print("Имя:", normalize_name("иванов   пётр"))
    print("Сумма:", total([100, 25.5]))
    print("Подпись:", pick(True))


if __name__ == "__main__":
    main()
