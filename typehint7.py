from typing import Callable

def apply_function(func: Callable[[int, str], float], x: int, y: str) -> float:
    return func(x, y)

# An example function to use with the above:
def combine_and_convert(a: int, b: str) -> float:
    return float(str(a) + b)

result = apply_function(combine_and_convert, 5, "10.5")  # Returns 510.5
