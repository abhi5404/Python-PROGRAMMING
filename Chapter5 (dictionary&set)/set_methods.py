# Creating sets with numbers
evens = {2, 4, 6, 8}
odds = {1, 3, 5, 7}
primes = {2, 3, 5, 7}

print("Original Sets:")
print("Evens:", evens)
print("Odds:", odds)
print("Primes:", primes)

# 1. add(): Add a number
evens.add(10)
print("\nAfter add(10) to evens:", evens)

# 2. update(): Add multiple numbers
odds.update([9, 11, 13])
print("After update([9, 11, 13]) to odds:", odds)

# 3. remove(): Remove a number (error if not found)
primes.remove(3)
print("After remove(3) from primes:", primes)

# 4. discard(): Remove safely
primes.discard(99)  # No error if 99 not present
print("After discard(99) from primes:", primes)

# 5. pop(): Randomly remove one item
removed = evens.pop()
print(f"\nRemoved using pop() from evens: {removed}")
print("Evens after pop():", evens)

# 6. union(): Combine sets
all_nums = evens.union(odds)
print("\nUnion of evens and odds:", all_nums)

# 7. intersection(): Common numbers
common = odds.intersection(primes)
print("Intersection of odds and primes:", common)

# 8. difference(): What's only in evens but not in primes
diff = evens.difference(primes)
print("Difference between evens and primes:", diff)

# 9. clear(): Remove all elements
odds.clear()
print("\nOdds after clear():", odds)
