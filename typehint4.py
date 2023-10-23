from typing import List, Union

class Student:
    def __init__(self, name: str, grades: List[Union[int, float]]):
        self.name = name
        self.grades = grades

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)
