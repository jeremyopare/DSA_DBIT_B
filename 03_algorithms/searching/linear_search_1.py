def linear_search(key, values):
    for value in values:
        if value == key:
            return value



key = int(input("Enter value to search "))
values = [9, 7, 6, 5, 4, 1, 2]
result =  linear_search(key, values)
print(result)
