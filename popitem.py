# Example dictionary
person = {"name": "Tebibu", "age": 25, "city": "Addis Ababa"}

# Using popitem() method
last_item = person.popitem()

print(last_item)  # Output: ('city', 'Addis Ababa')
print(person)  # Output: {'name': 'Tebibu', 'age': 25}
