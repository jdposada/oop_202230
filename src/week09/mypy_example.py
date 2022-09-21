from typing import overload

@overload
def hello(s: int) -> str:
    ...

@overload
def hello(s: str) -> str:
    ...

def hello(s):
    if isinstance(s, int):
        return "got an integer!"
    if isinstance(s, str):
        return "got a string"
    raise ValueError("you must pass either int or str")
if __name__ == '__main__':
    print(hello(1))
    print(hello(1) + 'a')
    print(hello(1) + 1)

