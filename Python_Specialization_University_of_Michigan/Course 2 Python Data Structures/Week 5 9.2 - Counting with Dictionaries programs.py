# =============================================================================
# Histogram problem (Many counters with a dictionary)
# =============================================================================

# One common use of dictionaries is counting how often we 'see' something.

ccc = dict()

ccc['csev'] = 1
ccc['cwen'] = 1

print(ccc)
# {'csev': 1, 'cwen': 1}

ccc['cwen'] = ccc['cwen'] + 1

print(ccc) 
# {'csev': 1, 'cwen': 2}

# =============================================================================
# Dictionary tracebacks
# =============================================================================

# It is an error to reference a key which is not in the dictionary. 
# We can use the in operator to see if a key is in the dictionary. 

ccc = dict()
print(ccc['csev'])
# Output
# Traceback (most recent call last):
#   File "1.py", line 28, in <module>
#     print(ccc['csev'])
# KeyError: 'csev'

# There is a way to workaround this problem. 'in' operator. 
'csev' in ccc
# False

# So, we will be doing two things: 
    # 1. Looking for a string. If it is there, add 1 to its count.
    # 2. If it is not there, create it, and add 1 to its count. 

# =============================================================================
# When we see a new name 
# =============================================================================

# When we encounter a new name, we need to add a new entry in the 
# dictionary and if this the second or later time we have seen the name, 
# we simply add one to the count in the dictionary under that name. 

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:          # for each element in 'names' list
    if name not in counts:  # if an element is not in 'counts'
        counts[name] = 1    # create a new label and a count to it
    else:
        counts[name] = counts[name] + 1     # else just do another count

print(counts) 

# Output
# {'csev': 2, 'cwen': 2, 'zqian': 1}

# =============================================================================
# The 'get' method for dictionaries 
# =============================================================================

# We do the previous example so much, python has a built-in function for that.
# The pattern of checking to see if a key is already in a dictionary and
# assuming a default value if the key is not there is so common that there
# is a method called get() that does this for us. 
# Default value if key does not exist. (and no traceback)


    if name in counts:
        x = counts[name]
    else:
        x = 0
    
    x = counts.get(name,0)
    # This means, go to 'counts', look for a key with 'name' tag,
    # use '0' as the default value.
    # Does not give a traceback. Works even if the key does not exist. 

# =============================================================================
# Simplified counting with get()
# =============================================================================

# We can use get() and provide a default value of zero when the key is
# not yet in the dictionary - and then just add one. 

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts) 

# Output
# {'csev': 2, 'cwen': 2, 'zqian': 1}










