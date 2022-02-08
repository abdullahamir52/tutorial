# =============================================================================
# Tuples are like lists
# =============================================================================

# Tuples are another kind of sequence that functions much like a list
# they have elements which are indexed starting at 0.
# You cannot modify tuples. (Just like strings)

x = ('Glenn', 'Sally', 'Joseph')
print(x)
# ('Glenn', 'Sally', 'Joseph')

y = (1, 9, 2)
print(y)
# (1, 9, 2)

print(max(y))
# 9


for iter in y:
    print(iter)

# Output
# 1
# 9
# 2

# =============================================================================
# but... Tuples are "immutable"
# =============================================================================

# Unlike a list, once you create a tuple, you cannot alter its contents -
# similar to a string. 

listx = [9, 8, 7]
listx[2] = 6
print(listx)
# [9, 8, 6]

string_y = 'ABC'
string_y[2] = 'D'

# Output
# Traceback (most recent call last):
#   File "1.py", line 2, in <module>
#     string_y[2] = 'D'
# TypeError: 'str' object does not support item assignment

tuplez = (5, 4, 3)
tuplez[2] = 0

# Output
# Traceback (most recent call last):
#   File "1.py", line 2, in <module>
#     tuplez[2] = 0
# TypeError: 'tuple' object does not support item assignment

# =============================================================================
# Things not to do with Tuples
# =============================================================================

x = (3, 2, 1)

x.sort()
# Output
# Traceback (most recent call last):
#   File "1.py", line 2, in <module>
#     x.sort()
# AttributeError: 'tuple' object has no attribute 'sort'

x.append(5)
# Output
# Traceback (most recent call last):
#   File "1.py", line 2, in <module>
#     x.append(5)
# AttributeError: 'tuple' object has no attribute 'append'

x.reverse()
# Output
# Traceback (most recent call last):
#   File "1.py", line 2, in <module>
#     x.reverse()
# AttributeError: 'tuple' object has no attribute 'reverse'

# =============================================================================
# A tale of two sequences
# =============================================================================

list1 = list()
dir(list1)
# Output
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
#  '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
#  'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

tuple1 = tuple()
dir(tuple1)
# Output
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# =============================================================================
# Tuples are more efficient
# =============================================================================

# Since python doesn't have to build tuple structures to be modifiable, they are
# simpler and more efficient in terms of memory use and performance than lists.

# So in our program when we are making "temporary variables" we prefer tuples
# over lists. 

# =============================================================================
# Tuples and Assignment
# =============================================================================

# We can also put a tuple on the LHS of an assignment statement.
# We can even omit the parenthesis. 
# Tuple and their value must have one-one correspondence

(x,y) = (4, 'Fred')
print(y)
# Fred

(a,b) = (99, 98)
print(a)
# 99

# =============================================================================
# Tuples and dictionaries
# =============================================================================

# The items() method in dictionaries returns a list of (key, value) tuples.

d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k,v) in d.items():
    print(k,v)

# Output
# csev 2
# cwen 4

tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 4)])

# =============================================================================
# Tuples are comparable
# =============================================================================

# The comparison operators work with tuples and other sequences. If the first
# item is equal, python goes on to the next element, and so on, until it finds
# elements that differ. 

( 0, 1, 2) < (5, 1, 2)
# True

(0, 1, 2000000) < (0, 3, 4)
# True 

(0, 1, 4) < (0, 3, 4)
# True

(0, 4, 4) < (0, 3, 4)
# False

(0, 3, 4) < (0, 3, 4)
# False

(0, 3, 4) < (0, 3, 5)
# True

('Jones', 'Sally') < ('Jones', 'Sam')
# True

('Jones', 'Sally') > ('Adams', 'Sam')
# True

# =============================================================================
# Sorting lists of tuples
# =============================================================================

# We can take advantage of the ability to sort a list of tuples to get a sorted
# version of a dictionary. 
# First we sort the dictionary by the key using the items() method and sorted()
# function. 

d = { 'a' : 10,'c' : 22 , 'b' : 1, }

d.items()
# dict_items([('a', 10), ('c', 22), ('b', 1)])

sorted(d.items())
# [('a', 10), ('b', 1), ('c', 22)]

# =============================================================================
# Using sorted()
# =============================================================================

# We can do this even more directly using the built-in function sorted that
# takes a sequence as a parameter and returns a sorted sequence.

d = { 'a' : 10, 'c' : 22, 'b' : 1 }

t = sorted(d.items())
t
# [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()): # goes through this dictionary by keys
    print(k,v)

# Output
# a 10
# b 1
# c 22

# =============================================================================
# Sort by values instead of key
# =============================================================================

# If we could construct a list of tuples of the form (value, key) we could sort
# by value. We do this with a for loop that creates a list of tuples. 

c = { 'a' : 10, 'c' : 22, 'b' : 1 }

tmp = list()

for k,v in c.items():
    tmp.append( (v,k) ) 
# this loop changes the key-value order in 'c' and assigns it to 'tmp'

print(tmp)
# [(10, 'a'), (22, 'c'), (1, 'b')]

tmp = sorted(tmp, reverse = True)
print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]

# =============================================================================
# The top 10 most common words
# =============================================================================

fhand = open('romeo.txt')

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1
        
lst = list()

for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val, key in lst[:10]:
    print(key,val)

# Output
# the 3
# is 3
# and 3
# sun 2
# yonder 1
# with 1
# window 1
# what 1
# through 1
# soft 1

# =============================================================================
# Even Shorter version
# =============================================================================

c = { 'a' : 10, 'c' : 22, 'b' : 1}

print(sorted( [ (v,k) for k,v in c.items() ] ) )
# [(1, 'b'), (10, 'a'), (22, 'c')]

# 'List comprehension' creates a dynamic list. In this case, we make a list of 
# reversed tuples and then sort it. 

# [ (v,k) for k,v in c.items() ] is same as 

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

print(sorted( [ (v,k) for k,v in c.items() ] , reverse = True ) )
# [(22, 'c'), (10, 'a'), (1, 'b')]