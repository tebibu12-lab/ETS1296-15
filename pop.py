# Example dictionary
person = {"name": "Tebibu", "age": 25, "city": "Addis Ababa"}

# Using pop() method
age = person.pop("age")  # Removes "age" and returns 25
print(age)  # Output: 25
print(person)  # Output: {'name': 'Tebibu', 'city': 'Addis Ababa'}

# Using pop() with a default value
salary = person.pop("salary", "Not Found")  # Key doesn't exist, returns "Not Found"
print(salary)  # Output: Not Found
