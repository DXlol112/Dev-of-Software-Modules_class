from app.utils.formatter import format_title
from app.utils.text import _squash_spaces
from app.services.calculator import grade_bounds

bounds = grade_bounds([5, 3, 4])
reveal_type(bounds)

def total(prices: list[int | float]) -> int | float:
    return sum(prices)


def pick(flag: bool) -> str|None:
    label = "есть выручка"
    if flag:
        return label
    return None
    

heading = format_title(40)  # type: ignore[arg-type]
clean = _squash_spaces("иванов   пётр")
print("undefined_name")