import pytest

from app.services.calculator import calculate_average, calculate_min, calculate_max
from app.utils.formatter import format_average

TEST_LIST = [5, 4, 5, 3, 5]

def test_average():
    assert calculate_average(TEST_LIST) == pytest.approx(4.4)

def test_min():
    assert calculate_min(TEST_LIST) == pytest.approx(3)

def test_max():
    assert calculate_max(TEST_LIST) == pytest.approx(5)

def test_format():
    result = format_average(4.4, 3, 5)

    expected = (
        "Средний результат: 4.40\n"
        "Минимальная оценка: 3\n"
        "Максимальная оценка: 5"
    )

    assert result == expected

def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])

    with pytest.raises(ValueError):
        calculate_min([])

    with pytest.raises(ValueError):
         calculate_max([])
