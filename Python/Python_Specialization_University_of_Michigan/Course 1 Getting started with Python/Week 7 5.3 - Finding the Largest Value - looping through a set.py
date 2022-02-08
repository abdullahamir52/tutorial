# =============================================================================
# Program 1 : Looping through a set
# =============================================================================

print('Before')

for thing in [9,41,12,3,74,15]:
    print(thing)

print('After')

# Output
# Before
# 9
# 41
# 12
# 3
# 74
# 15
# After

# =============================================================================
# Program 2 : Finding the largest value
# =============================================================================

largest_so_far = -1

print('Before', largest_so_far)

for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print('The current number:', the_num, 'The largest so far:', largest_so_far)

print('Largest so far after calculation:', largest_so_far)

# Output
# Before -1
# The current number: 9 The largest so far: 9
# The current number: 41 The largest so far: 41
# The current number: 12 The largest so far: 41
# The current number: 3 The largest so far: 41
# The current number: 74 The largest so far: 74
# The current number: 15 The largest so far: 74
# Largest so far after calculation: 74