from typing import Final

def sum_up_to(n: int) -> int:
    def helper(current: int, acc: int) -> int:
        if current == 0:
            return acc
        return helper(current - 1, acc + current)
    
    return helper(n, 0)

print(sum_up_to(5))
