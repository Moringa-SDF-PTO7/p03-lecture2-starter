# sets.py

# Set: An unordered collection of unique elements
my_set = {1, 2, 3, 4, 5}
print(f"Original Set: {my_set}")

# Adding elements to a set
my_set.add(6)
print(f"Set after adding an element: {my_set}")

# Set operations: union, intersection, difference
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set = set_a.difference(set_b)
print(f"Union: {union_set}, Intersection: {intersection_set}, Difference: {difference_set}")

# TODO: Explore other set operations like symmetric difference and disjoint sets
