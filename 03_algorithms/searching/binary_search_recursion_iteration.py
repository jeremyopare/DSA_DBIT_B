def binary_search(key, values):
    low = 0
    high = len(values) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        print("\n")
        print(values[low])
        print(values[mid])
        print(values[high])
        
        if values[mid] == key:
            return mid
        
        elif key > values[mid]:
            low = mid + 1
        else:
            high = mid - 1
            
    # return -1


values = [1,2,3,4,5,6,7,8,9]
print(values)

key = int(input("Enter value to search "))

result =  binary_search(key, values)
print(f"After call {result}")

if result != -1:
    print(f"{values[result]} found at index {result}")
else:
    print(f"Item not found")