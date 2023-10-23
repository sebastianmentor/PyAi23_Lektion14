from typing import Protocol

class Nameable(Protocol):
    def get_name(self) -> str: pass

class Person:
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

# The Person class satisfies the Nameable protocol because it has a get_name method.
