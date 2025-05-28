from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __repr__(self) -> str:
        return f"Stack({self._items})"

if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    print(stack.peek())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.is_empty())
