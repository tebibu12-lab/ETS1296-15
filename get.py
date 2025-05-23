# Example dictionary
person = {"name": "Tebibu", "age": 25, "city": "Addis Ababa"}

# Using get() method
name = person.get("name")  # Returns "Tebibu"
salary = person.get("salary")  # Returns None (since "salary" is not in the dictionary)
default_salary = person.get("salary", 5000)  # Returns 5000 (default value provided)

print(name)  # Output: Tebibu
print(salary)  # Output: None
print(default_salary)  # Output: 5000
