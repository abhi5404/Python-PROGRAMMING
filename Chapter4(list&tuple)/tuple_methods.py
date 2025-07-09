# Define a sample tuple
my_tuple = (10, 20, 30, 20, 40, 20)

print("Original Tuple:", my_tuple)

# 1. count(value) — Count the number of times a value appears
count_20 = my_tuple.count(20)
print("Count of 20:", count_20)

# 2. index(value) — Return the first index of a value
index_30 = my_tuple.index(30)
print("Index of 30:", index_30)

# --- Other built-in functions that can be used with tuples ---

# 3. len() — Length of the tuple
print("Length:", len(my_tuple))

# 4. max() — Maximum value in the tuple
print("Maximum value:", max(my_tuple))

# 5. min() — Minimum value
print("Minimum value:", min(my_tuple))

# 6. sum() — Sum of all elements
print("Sum of elements:", sum(my_tuple))

# 7. sorted() — Returns a sorted list from the tuple
print("Sorted tuple (as list):", sorted(my_tuple))

# 8. any() — True if any element is true
bool_tuple = (0, 0, False, 5)
print("Any True?", any(bool_tuple))

# 9. all() — True if all elements are true
print("All True?", all(bool_tuple))

# 10. tuple() — Convert another iterable into a tuple
list_data = [1, 2, 3]
converted = tuple(list_data)
print("Converted from list:", converted)

# Tuple unpacking
a, b, c = (1, 2, 3)
print("Unpacked values:", a, b, c)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested)

# Tuple concatenation
t1 = (1, 2)
t2 = (3, 4)
print("Concatenated Tuple:", t1 + t2)

# Tuple repetition
print("Repeated Tuple:", t1 * 3)

# Membership test
print("Is 30 in my_tuple?", 30 in my_tuple)
