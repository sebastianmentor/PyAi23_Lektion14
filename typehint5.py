from typing import TypeVar, Generic

T = TypeVar('T')

class Storage(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def retrieve(self) -> T:
        return self.item

# Usage:
int_storage = Storage[int](10)
str_storage = Storage[str]("Hello")
