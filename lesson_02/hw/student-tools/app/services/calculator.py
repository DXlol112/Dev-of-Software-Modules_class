def calculate_average(values: list[int]) -> float:
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return sum(values) / len(values)

def calculate_min(values : list):
    if not values:
        raise ValueError("Пустой список")
    return min(values)

def calculate_max(values: list):
    if not values:
        raise ValueError("Пустой список")
    return max(values)
