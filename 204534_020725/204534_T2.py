def find_max(numbers):
    if not numbers:  
        return None

    max_number = numbers[0]

    for num in numbers[1:]:
        if num > max_number:
            max_number = num

    return max_number

print(find_max([17, 23, 54, 14]))  

