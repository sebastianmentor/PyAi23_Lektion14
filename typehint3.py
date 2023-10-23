from typing import Tuple, Optional

# A function that takes a tuple of two integers (representing coordinates),
# an optional string (representing a label), and returns a string.
def describe_point(coord: Tuple[int, int], label: Optional[str] = None) -> str:
    x, y = coord
    base_description = f"Point at ({x}, {y})"
    if label:
        return f"{base_description}, labeled {label}"
    return base_description
