# 1. Create a dictionary with at least 5 key-value pairs
students = {
    "S101": "Sai",
    "S102": "Bob",
    "S103": "Charan",
    "S104": "David",
    "S105": "Raju"
}

print("Initial Dictionary:")
print(students)

# 1.1. Adding values to dictionary
students["S106"] = "Frank"
print("\nAfter Adding S106:")
print(students)

# 1.2. Updating values in dictionary
students["S102"] = "Bobby"
print("\nAfter Updating S102 to Bobby:")
print(students)

# 1.3. Accessing a value in dictionary
print("\nAccessing value for S103:")
print(students["S103"])

# 1.4. Create a nested dictionary (e.g., student ID → {name, age, grade})
nested_students = {
    "S201": {"name": "Grace", "age": 20, "grade": "A"},
    "S202": {"name": "Harry", "age": 21, "grade": "B"},
    "S203": {"name": "Ivy", "age": 22, "grade": "A"},
}

print("\nNested Dictionary:")
print(nested_students)

# 1.5. Accessing values of nested dictionary
print("\nAccess name and grade for S202:")
print("Name:", nested_students["S202"]["name"])
print("Grade:", nested_students["S202"]["grade"])

# 1.6. Print the keys present in a dictionary
print("\nKeys in students dictionary:")
print(students.keys())

print("\nKeys in nested_students dictionary:")
print(nested_students.keys())

# 1.7. Delete a value from a dictionary
del students["S104"]
print("\nAfter deleting S104:")
print(students)

