In Python, type hinting is a mechanism that allows you to indicate the expected types of variables, function parameters, return values, and more. It doesn't enforce type checking at runtime but provides a way for developers to communicate intended types, making the code more readable and maintainable. Additionally, type hints can be used by static type checkers, like `mypy`, to catch potential type errors before the code is run.

Introduced in Python 3.5 with [PEP 484](https://www.python.org/dev/peps/pep-0484/), type hinting has since become a popular practice in many Python codebases.

Here are some basic examples:

1. **Function Annotations**:
   ```python
   def greet(name: str) -> str:
       return "Hello, " + name
   ```

2. **Variable Annotations** (Introduced in Python 3.6 with [PEP 526](https://www.python.org/dev/peps/pep-0526/)):
   ```python
   age: int = 25
   ```

3. **For Lists, Dicts, and Other Containers**:
   You can use the `List`, `Dict`, etc., from the `typing` module.
   ```python
   from typing import List, Dict
   
   names: List[str] = ["Alice", "Bob"]
   ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
   ```

4. **Optional Types**:
   For variables that can be a specific type or `None`, you can use `Optional`.
   ```python
   from typing import Optional
   
   def find_age(name: str) -> Optional[int]:
       if name in ages:
           return ages[name]
       return None
   ```

5. **For Custom Types**:
   You can define your own type using `TypeVar` or `NewType`.
   ```python
   from typing import TypeVar, NewType
   
   UserId = NewType('UserId', int)
   T = TypeVar('T')  # Can be used for generic functions or classes
   ```

It's important to note that type hints are just that—hints. Python remains a dynamically-typed language, and these hints don't affect the runtime behavior of the code. However, they are invaluable for documentation, code readability, and static analysis.