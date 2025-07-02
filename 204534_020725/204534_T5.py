def linear_search(list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index
    return -1

my_list = [1013, 257, 908, 111, 69000]
target = 111

result = linear_search(my_list, target)
print(result)