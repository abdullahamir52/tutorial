# =============================================================================
# Best friends: Strings and Lists
# =============================================================================

# Split breaks a string into parts and produces a list a strings. We think
# of these as words. We can access a particular word or loop through 
# all the words. 

abc = 'With three words'
stuff = abc.split()
# this split function returns a list

print(stuff)
# ['With', 'three', 'words']

print(len(stuff))
# 3

print(stuff[0])
# With

for w in stuff:
    print(w)

# Output
# With
# three
# words

# =============================================================================
# Couple of details about split()
# =============================================================================

# When you do not specify a 'delimiter', multiple spaces are treated like one
# delimiter. You can specify what delimiter character to use in the splitting.

line = 'A lot                       of spaces'
etc = line.split()
print(etc)
# ['A', 'lot', 'of', 'spaces']
# it ignores the long whitespace

line = 'first;second;third'
thing = line.split() # its looking for spaces. 
print(thing)
# ['first;second;third']
# one string because there is no spaces

print(len(thing))
# 1 

thing = line.split(';')
print(thing)
# ['first', 'second', 'third']
# looks for semicolon to split the string

print(len(thing))
# 3 

# =============================================================================
# An example using split function
# =============================================================================

fhand = open('mbox-short.txt')
for line in fhand: 
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])
# prints out the day of the week
# Sat
# Fri
# Fri
# Fri


line1 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words1 = line1.split()
print(words1)
# ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']


# =============================================================================
# The Double Split pattern
# =============================================================================

line1 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

words1 = line1.split()
print(words1)
# ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']

email = words1[1]
print(email)
# stephen.marquard@uct.ac.za

pieces = email.split('@')
print(pieces)
# ['stephen.marquard', 'uct.ac.za']