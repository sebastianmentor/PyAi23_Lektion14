from typing import Optional, TypeVar, NewType, List, Dict, Tuple, Set, Union


def greet(name: str) -> str:
    return "Hello, " + name

MAX_AGE = 100
MAX_AGE:int = 100

age: int|str|None = 25

my_list: list = []

names: List[str] = ["Alice", "Bob"]
ages: Dict[str, int] = {"Alice": 25, "Bob": 30}


def find_age(name: str) -> Optional[int]:
    if name in ages:
        return ages[name]
    return None

class MyClass:
    ...

def print_my_class(klass: MyClass) -> None:
    print(MyClass)


UserId = NewType("UserId", int)
T = TypeVar("T")  # Can be used for generic functions or classes


point: Tuple[int, int, str, List[MyClass]] = (5, 3, 'add')
values: Tuple[int, ...] = (1, 2, 3, 4)

unique_names: Set[str] = {"Alice", "Bob"}


def parse(value: str) -> Union[int, float, str]:
    ...
