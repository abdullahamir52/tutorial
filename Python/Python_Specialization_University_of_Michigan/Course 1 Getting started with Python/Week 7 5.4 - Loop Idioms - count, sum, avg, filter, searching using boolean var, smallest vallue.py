# =============================================================================
# Program 1 : Counting numbers
# =============================================================================

zork = 0
# zork is the count variable here

print('Before counting: ', zork)

# i is the iteration variable here
for i in [9,41,12,3,74,15]:
    zork = zork + 1
    print ('Count: ', zork, 'Current number: ', i)
print('After counting: ',zork)

# Output
# Before counting:  0
# Count:  1 Current number:  9
# Count:  2 Current number:  41
# Count:  3 Current number:  12
# Count:  4 Current number:  3
# Count:  5 Current number:  74
# Count:  6 Current number:  15
# After counting:  6

# =============================================================================
# Program 2 : summing in a loop
# =============================================================================

total = 0
print('Sum before calculation: ', total)
 
for i in [9,41,12,3,74,15]:
    total = total + i 
    print('Current number: ', i , 'Total: ',total)
print('Sum after calculation: ', total)

# Output
# Sum before calculation:  0
# Current number:  9 Total:  9
# Current number:  41 Total:  50
# Current number:  12 Total:  62
# Current number:  3 Total:  65
# Current number:  74 Total:  139
# Current number:  15 Total:  154
# Sum after calculation:  154

# =============================================================================
# Program 3 : Finding the avg in a loop
# =============================================================================

count = 0
sum = 0 
print('Before', count, sum)

for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print('Count:',count,'Sum:',sum,'Value:',value)

print('After')
print('Count:',count,'Sum:',sum,'Avg:',sum/count)

# Output
# Before 0 0
# Count: 1 Sum: 9 Value: 9
# Count: 2 Sum: 50 Value: 41
# Count: 3 Sum: 62 Value: 12
# Count: 4 Sum: 65 Value: 3
# Count: 5 Sum: 139 Value: 74
# Count: 6 Sum: 154 Value: 15
# After
# Count: 6 Sum: 154 Avg: 25.666666666666668

# =============================================================================
# Program 4 : Filtering in a loop
# =============================================================================

print('Before')

for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number',value)
print('After')

# Output
# Before
# Large number 41
# Large number 74
# After

# =============================================================================
# Program 5 : Search using a boolean variable
# =============================================================================

found = False
print('Before', found)

for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found,value)
print('After',found)

# Output
# Before False
# False 9
# False 41
# False 12
# True 3
# True 74
# True 15
# After True

# =============================================================================
# Program 6 : Finding the smallest value
# =============================================================================

smallest = None
print('Before')

for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print('Value',value, 'Smallest',smallest)
print('After', 'Smallest', smallest)

# Output
# Before
# Value 9 Smallest 9
# Value 41 Smallest 9
# Value 12 Smallest 9
# Value 3 Smallest 3
# Value 74 Smallest 3
# Value 15 Smallest 3
# After Smallest 3