items = {
    "name":"Jay",
    "age":22,
    "city":"Nairobi"
}
print(items)

print("Adding a new key value pair")
items["deposit"] = 100
print(items)

print("Modify name")
items["name"] = "John"
print(items)

print("After deleting")
del items["name"]
print(items)