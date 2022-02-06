# =============================================================================
# Concatenating lists using + 
# =============================================================================

# We can create a new list by adding two existing lists together.

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
# [1, 2, 3, 4, 5, 6]
print(a)
# [1, 2, 3]
# concatening doesn't hurt the previous list (a or b)

# =============================================================================
# Lists can be sliced using ':'
# =============================================================================

t = [9,41,12,3,74,15]

t[1:3]
# [41, 12]
# prints the index 1 and 2 elements (omits index 0 and 3 elements (9,3))
# Just like in strings, the second number is up to but not including

t[:4]
# [9, 41, 12, 3]
# prints out the last 4 elements

t[3:]
# [3, 74, 15]
# prints out the first 3 elements

t[:]
# [9, 41, 12, 3, 74, 15]
# prints out the entire list

# =============================================================================
# List methods 
# =============================================================================

x = list()
type(x)
# <class 'list'>

dir(x) 
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
#  '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
#  'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# ref: https://docs.python.org/tutorial/datastructures.html

# =============================================================================
# Building a list from scratch
# =============================================================================

# We can create an empty list and then add elements using the append method.
# The list stays in order and new elements are added at the end of the list. 

my_list1 = list()
my_list1.append('book')
my_list1.append(99)
print(my_list1)
# ['book', 99]

my_list1.append('cookie')
print(my_list1)
# ['book', 99, 'cookie']

# This, however, will not work on strings. 
# e.g. x = x.append('something') will not work 

# =============================================================================
# Is something in a list? 
# =============================================================================

# Python provides two operators that let you check if an item is in a list.
# These are logical operators that return True or False. 
# They do not modify the list. 

some = [1,9,21,10,16]
9 in some
# True

15 in some
# False

20 not in some 
# True

# =============================================================================
# Lists are in Order
# =============================================================================

# A list can hold many items and keeps those items in the order until we do 
# something to change the order. 
# A list can be sorted (i.e. change its order).
# The sort method (unlike in strings) means "sort yourself". 

friends = [ 'Joseph', 'Glenn', 'Sally']

print(friends)
# ['Joseph', 'Glenn', 'Sally']
print(friends[1])
# Glenn

friends.sort()
# x = sorted(friends)
# print(x)

print(friends)
# ['Glenn', 'Joseph', 'Sally']
print(friends[1])
# Joseph

# =============================================================================
# Built-in Functions and Lists
# =============================================================================

# There are a number of functions built into python that take
# lists as parameters. 
# Remember the loops we built? These are much simpler. 

nums = [3,41,12,9,74,15]

print(len(nums))
# 6

print(max(nums))
# 74

print(min(nums))
# 3

print(sum(nums))
# 154

print(sum(nums)/len(nums))
# 25.666666666666668

# =============================================================================
# Calculate average (previous example) 
# =============================================================================

# this program only uses three memory space> total, count, average

total = 0
count = 0
print("\n\n\nCalculating average of some numbers.\n")
print("Please enter 'done' if you are finished inputing.")
while True: # basically it creates an infinite loop with a break statement
    inp = input('Enter a number: ')
    if inp == 'done' : 
        break
    value = float(inp)
    total = total + value 
    count = count + 1 

average = total / count
print('\nAverage:', average)

# =============================================================================
# Using built-in functions to calculate average (using data structure)
# =============================================================================

# this program uses as many memory space as you input 

numlist = list()

print("\n\n\nCalculating average of some numbers.\n")
print("Please enter 'done' if you are finished inputing.")
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : 
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('\nAverage:', average)


# Output of previous two programs: 
# Calculating average of some numbers.
# Please enter 'done' if you are finished inputing.
# Enter a number: 5
# Enter a number: 5
# Enter a number: done
# Average: 5.0