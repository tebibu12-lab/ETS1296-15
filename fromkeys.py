# Creating a dictionary with fromkeys()
keys = ["name", "age", "city"]
value = "Unknown"

new_dict = dict.fromkeys(keys, value)

# Output
print(new_dict)  # {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
