# sets => an unordered collection of values

books = { 
    "Confessions of Nairobi Men",
    "Confessions of Nairobi Women",
    "Other people's money",
    "Gifted Hands",
}

print(books)

books.add("Atomic Habits")
print(books)

# set operations => union, intersection, difference
set_a = {2, 4, 6, 8, 10}
set_b = {3, 6, 9, 12, 15}

# union => combination of 2 sets
set_c = set_a.union(set_b)
print(f"Union set {set_c}")
set_d = set_b.union(set_a)
print(f"Union set {set_d}")

# TODO: Find out why there seems to be an order when making a union set

# intersection => finds the common elements
set_e = set_b.intersection(set_a)
print(f"Intersection {set_e}")

# difference => the non-common elements
set_f = set_b.difference(set_a)
print(f"difference {set_f}")

# spread vs union
set_g = { *set_a, *set_b }
print(set_g)
list_h = [*set_a, *set_b]

set_i = "$".join("[10,20, 30, 40]")
print(set_i)
