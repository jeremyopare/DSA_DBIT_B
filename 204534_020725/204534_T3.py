def find_min(list):
    if not list:
        return None

    smallest = list[0]
    for num in list[1:]:
        if num < smallest:
            smallest = num
    return smallest

print(find_min([4, 2, 9, -1, 5]))
