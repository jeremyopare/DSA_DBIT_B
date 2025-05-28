
num = 1
def direct_recursion(num):
    print(f"{num} Direct recursion")
    num = num + 1
    # num += 1

    return direct_recursion(num)

direct_recursion(num)
