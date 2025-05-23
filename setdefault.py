# Example dictionary
person = {"name": "Tebibu", "age": 25}

# Using setdefault() method
name = person.setdefault("name", "Unknown")  # Returns "Tebibu" (key exists)
city = person.setdefault("city", "Addis Ababa")  # Inserts "city" with default value

print(person)  # Output: {'name': 'Tebibu', 'age': 25, 'city': 'Addis Ababa'}
print(city)  # Output: Addis Ababa
