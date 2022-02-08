# =============================================================================
# Algorithms
# =============================================================================

# A set of rules or steps used to solve a problem


# =============================================================================
# Data Structures
# =============================================================================

# A particular way of organizing data in a computer

x = 2
x = 4
# These two lines represent a variable, x, which is not a collection
# Here, the old value (2) is overwritten (4)


# =============================================================================
# List
# =============================================================================

# A collection allows us to put many values in a single variable
# We can carry many values around in one convenient package

friends = [ 'Joseph', 'Glenn', 'Sally']
z = ['socks', 'shirt', 'perfume']
# these two lines represent lists, where it contains a list of strings
# anything in square brackets are a list constants


# =============================================================================
# List Constants
# =============================================================================

# Lists constants are closed using square brackets and separated by comma.
# A list element can be any python object - even another list.
# A list can be empty. 

print([1,24,76])
# [1, 24, 76]
print(['red','yellow','blue'])
# ['red', 'yellow', 'blue']
print(['red','24','98.6'])
# ['red', '24', '98.6']
print(['1', [5,6], 7])
# ['1', [5, 6], 7]
# here, the second element is also a list.
print([])
# []
# here, we have printed out an empty list.


# =============================================================================
# We have already used lists
# =============================================================================

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')


# =============================================================================
# Lists and Definite Loops - Best Pals
# =============================================================================

friends = [ 'Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Output
# Happy New Year: Joseph
# Happy New Year: Glenn
# Happy New Year: Sally
# Done!

z = ['socks', 'shirt', 'perfume']
for x in z:
    print('Itenaries include: ', x)
print('Done!')

# =============================================================================
# Looking inside lists
# =============================================================================

friends = [ 'Joseph', 'Glenn', 'Sally']
print(friends[1])
# Glenn

# =============================================================================
# Lists are mutable
# =============================================================================

# Strings are immutable. Must make a new string to make any change.
# Lists are mutable. can change an element of a list using index operator.

fruit = 'Banana'
fruit[0] = 'b'
# Output
# Traceback (most recent call last):
#   File "1.py", line 3, in <module>
#     fruit[0] = 'b'
# TypeError: 'str' object does not support item assignment

x = fruit.lower()
print(x)
# banana

lotto = [2,14,26,41,63]
print(lotto)
# [2, 14, 26, 41, 63]

lotto[2] = 28
print(lotto)
# [2, 14, 28, 41, 63]

# =============================================================================
# How long is a list? 
# =============================================================================

# The len() function takes a list as a parameter and returns the number 
# of elements in the list.
# Actually len() tells us the number of elements of any set or sequence
# (such as a string...)

x = [1,2,'joe',99]
print(len(x))
# 4

greet = 'Hello Bob!'
print(len(greet))
# 10

# =============================================================================
# Using the Range function
# =============================================================================

# We usually use range function while constructing loops.
# The range function returns a list of numbers that range from zero to 
# one less than the parameter. (upto but not included to)
# We can construct an index loop using for and an integer iterator.

print(range(4))
# range(0, 4)

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
# 3

print(range(len(friends)))
# range(0, 3)

# =============================================================================
# A tale of two loops (How to create a counted loop)
# =============================================================================

list1 = ['Joseph', 'Glenn', 'Sally']
for index1 in list1:
    print('Happy New Year:', index1)
# index 1 takes one element in list 1 and then prints it out
# then moves to the next variable
# final value of index1 is Sally

for index2 in range(len(list1)):
    index3 = list1[index2]
    print('Happy New Year:', index3)
# index 2 finds the index of the element 
# index 3 then takes the value of the index2 element of the list
# then it prints out the element
# final value of index2 is 2 (0,1,2)
# final value of index3 is Sally

# Output (for both loops)
# Happy New Year: Joseph
# Happy New Year: Glenn
# Happy New Year: Sally