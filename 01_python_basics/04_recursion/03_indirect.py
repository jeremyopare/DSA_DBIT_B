
def funA(n):
    if n > 1:
        print(f"Inside A {n}")
        return funB(n - 1)
    return None


def funB(n):
    if n > 1:
        print(f"Inside B {n}")
        return funA(n - 1)
    return None


funA(5)