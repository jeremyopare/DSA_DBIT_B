from typing import List, TypeVar

T = TypeVar('T')

def reverse_list(items: List[T]) -> List[T]:
    return items[::-1]

def rotate_list(items: List[T], k: int) -> List[T]:
    if not items:
        return []
    k = k % len(items)
    return items[-k:] + items[:-k]

original = [1, 2, 3, 4, 5]

print(reverse_list(original))
print(rotate_list(original, 2))
print(rotate_list(original, -2))
