# Sample Python Program showing dictionary methods

# Creating a dictionary
student = {
    "name": "Abhijit",
    "age": 22,
    "course": "Computer Science"
}

print("Original Dictionary:")
print(student)

# 1. get(): Safely access a value
print("\nName (using get):", student.get("name"))
print("Marks (using get, default):", student.get("marks", "Not Found"))

# 2. keys(): Returns all keys
print("\nKeys:", student.keys())

# 3. values(): Returns all values
print("Values:", student.values())

# 4. items(): Returns all key-value pairs
print("Items:", student.items())

# 5. update(): Add or update multiple key-value pairs
student.update({"age": 23, "marks": 85})
print("\nAfter update:", student)

# 6. pop(): Removes a key and returns its value
removed = student.pop("marks")
print("\nRemoved 'marks':", removed)
print("After pop:", student)

# 7. popitem(): Removes the last inserted item
last_item = student.popitem()
print("\nRemoved last item:", last_item)
print("After popitem:", student)

# 8. setdefault(): Get value if key exists; else set and return default
course = student.setdefault("course", "Maths")
print("\nSet default (course exists):", course)
semester = student.setdefault("semester", 5)
print("Set default (new key):", semester)
print("After setdefault:", student)

# 9. clear(): Removes all items
student.clear()
print("\nAfter clear():", student)
