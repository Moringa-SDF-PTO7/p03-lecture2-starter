# Dictionary => key-value pair set (liken to JSON in JS)
student = {
    "lname": "Daniel",
    "age": 30,
    "email": "joe.daniel@student.moringaschool.com",
    "course": "SDF-PT07",
    "fname": "Joe",
}
print(f"Original Dict {student}")

# access values => []
course = student["course"]
# print(f"Course {course}")

# access values => .get()
age = student.get("ages", 18)
# print(f"access using get {age}")

balance = student.get("balance", ZeroDivisionError) # TODO for Ian (Indicate how to throw errors when default is not found)
# print(f"thrown error {balance}")

# add value to dictionary
student["current_phase"] = "Phase 03"
# print(student)

# update value
student["course"] = "DSF-FT02"
# print(student)

# delete a value
del student["age"]
# print(student)

# fetch all keys as a list
keys = student.keys()
# print(keys)

# fetch all values
values =  student.values()
# print(values)

farmer = {
    "farm_loc": "Kisumu",
}
# print(farmer)

# get all items (key-value) => tuples
key_value = student.items()
print(key_value)

# email stuff
print(f"email stuff {key_value}") # TODO: Find how to access specific value from items
