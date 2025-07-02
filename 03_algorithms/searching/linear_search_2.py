def linear_search(key, values):
    for index, item in enumerate(values):
        if item == key:
            return index
        
    return -1



values = [9, 7, 6, 5, 4, -1, 2]
print(values)

key = int(input("Enter value to search "))

result =  linear_search(key, values)

if result > -1:
    print(f"{values[result]} found at index {result}")
else:
    print(f"Item not found")