# empty list
list_items = []

my_list = [0,1,2,3,4,5,6,7,8]
print(f"The list {my_list}")
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

print(f"First element to 4th index {my_list[:4]}")

print(my_list[:])
print(my_list[4:])
print(my_list[-3:])

# add an element
my_list.append(9)
print(my_list)