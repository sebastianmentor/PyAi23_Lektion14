Of course! Let's delve into some more complex examples using the `typing` module.

1. **Nested Generics**:
   Using nested generics to describe more complex data structures.
   ```python
   from typing import List, Dict
   
   # A dictionary where the keys are strings (representing usernames) 
   # and the values are lists of integers (representing purchase amounts).
   user_purchases: Dict[str, List[int]] = {
       "alice": [20, 50, 100],
       "bob": [5, 10, 15]
   }
   ```

2. **Function with Multiple Parameters**:
   Describing functions with multiple parameters of different types.
   ```python
   from typing import Tuple, Optional
   
   # A function that takes a tuple of two integers (representing coordinates),
   # an optional string (representing a label), and returns a string.
   def describe_point(coord: Tuple[int, int], label: Optional[str] = None) -> str:
       x, y = coord
       base_description = f"Point at ({x}, {y})"
       if label:
           return f"{base_description}, labeled {label}"
       return base_description
   ```

3. **Classes with Type Hints**:
   Using type hints in class definitions.
   ```python
   from typing import List, Union
   
   class Student:
       def __init__(self, name: str, grades: List[Union[int, float]]):
           self.name = name
           self.grades = grades

       def average_grade(self) -> float:
           return sum(self.grades) / len(self.grades)
   ```

4. **Using TypeVar for Generics**:
   Creating a simple generic storage class.
   ```python
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
   ```

5. **TypedDict for More Detailed Dictionary Types**:
   ```python
   from typing import TypedDict, List
   
   class Movie(TypedDict):
       title: str
       year: int
       genres: List[str]

   my_movie: Movie = {
       "title": "Inception",
       "year": 2010,
       "genres": ["Sci-Fi", "Thriller"]
   }
   ```

6. **Callable with Different Signatures**:
   Describing functions that accept and return various types.
   ```python
   from typing import Callable
   
   def apply_function(func: Callable[[int, str], float], x: int, y: str) -> float:
       return func(x, y)

   # An example function to use with the above:
   def combine_and_convert(a: int, b: str) -> float:
       return float(str(a) + b)

   result = apply_function(combine_and_convert, 5, "10.5")  # Returns 510.5
   ```

7. **Protocols for Structural Subtyping**:
   Using protocols to define required methods.
   ```python
   from typing import Protocol

   class Nameable(Protocol):
       def get_name(self) -> str: pass

   class Person:
       def __init__(self, name: str):
           self._name = name

       def get_name(self) -> str:
           return self._name

   # The Person class satisfies the Nameable protocol because it has a get_name method.
   ```

These examples showcase the versatility and expressiveness of the `typing` module. With type hints, you can better communicate the intent of your code, making it more readable and maintainable.