# dictionaries.py

# Dictionary: Key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "Nairobi"}
print(f"Original Dictionary: {my_dict}")

# Accessing values
print(f"Name: {my_dict['name']}")

# Adding and updating values
my_dict["age"] = 26  # Update age
my_dict["country"] = "Kenya"  # Add new key-value pair
print(f"Updated Dictionary: {my_dict}")

# Deleting a key-value pair
del my_dict["city"]
print(f"Dictionary after deletion: {my_dict}")

# TODO: Write a function that merges two dictionaries
