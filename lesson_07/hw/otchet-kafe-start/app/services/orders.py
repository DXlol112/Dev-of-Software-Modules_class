"""Модуль для работы с заказами."""
from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:  # noqa: D417
    """Загружает список заказов из файла по указанному пути.
    
    Args:
        Путь к файлу с данными; файл должен существовать 
            и содержать обязательные поля 'waiter' и 'kopeks'.
    
    Returns:
        Список объектов Order, созданных на основе прочитанных строк.
    """
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]



def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Считает выручку по каждому официанту.

    Args:
        orders (list[Order]): Заказы за смену, не пустой !
        top (int, optional): Сколько официантов оставить в результате. 
        Значение 0, возвращаются все.

    Raises:
        ValueError: Если список заказов пуст

    Returns:
        dict[str, int]: Выручка в копейках по именам официантов,
          в порядке убывания суммы.
    """    
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)

def sort_orders_in_place(orders: list[Order]) -> None:
    """Сортирует список заказов на месте по убыванию стоимости.

    Args:
        orders (list[Order]): Список объектов заказов, которые необходимо 
            отсортировать.
    """    
    orders.sort(key=lambda order: -order.kopeks)
