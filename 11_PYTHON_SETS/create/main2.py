# Creating sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {1, 2, 3, 4, 5}
set4 = {2, 3, 4}

# Checking if sets are disjoint
print(f'Are set1 and set2 disjoint? {set1.isdisjoint(set2)}')  # Output: True
print(f'Are set1 and set3 disjoint? {set1.isdisjoint(set3)}')  # Output: False

# Checking if set1 is a subset of set3
print(f'Is set1 a subset of set3? {set1.issubset(set3)}')  # Output: True

# Checking if set1 is a subset of set4
print(f'Is set1 a subset of set4? {set1.issubset(set4)}')  # Output: False

# Checking if set3 is a superset of set1
print(f'Is set3 a superset of set1? {set3.issuperset(set1)}')  # Output: True

# Checking if set1 is a superset of set4
print(f'Is set1 a superset of set4? {set1.issuperset(set4)}')  # Output: False
