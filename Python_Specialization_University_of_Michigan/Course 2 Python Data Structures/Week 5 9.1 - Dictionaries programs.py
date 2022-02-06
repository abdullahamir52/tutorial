# =============================================================================
# What is a collection?
# =============================================================================

# A collection is nice because we can put more than one value in it and 
# carry them all around in one convenient package. 
# We have a bunch of values in a single variable. 
# We do this by having more than one place 'in' the variable.
# We have ways of finding the different places in the variable. 

# =============================================================================
# A story of two collections
# =============================================================================

# ---- List ----
# A linear collection of values that stay in order. 

# ---- Dictionary ----
# A 'bag' of values, each with it's own label. 
# 'Key-paired' items. You give it a key on it's way in, you give it a 
# key on it's way out. 

# =============================================================================
# Dictionaries
# =============================================================================

# Memory-based key-value stores. 
# Dictionaries are python's most powerfull data collection. 
# Dictionaries allow us to do fast database-like operations in python.
# Dictionaries have different names in different languages. 
# --- Associative arrays - Perl/PHP
# --- Properties or Map or HashMap - Java
# --- Property Bag - C# / .Net

# =============================================================================
# Dictionary making process
# =============================================================================

# Lists index their entries based on the position in the list. 
# Dictionaries are like bags - no order. 
# So we index the things we put in the dictionary with a 'lookup tag'. 

purse = dict()
purse['money'] = 12     # 12 is the value, money is the key. 
purse['candy'] = 3      # 3 is the value, candy is the key. 
purse['tissues'] = 75   # 75 is the value, tissures is the key. 
print(purse)
# {'money': 12, 'candy': 3, 'tissues': 75}

print(purse['candy'])
# 3

purse['candy'] = purse['candy'] + 2 
print(purse)
# {'money': 12, 'candy': 5, 'tissues': 75}

# =============================================================================
# Comparing lists and dictionaries 
# =============================================================================

# Dictionaries are like lists except that they use keys instead of 
# numbers to look up values. 

# creating a list and a dictionary
lst = list()

ddd = dict()

# adding something
lst.append(21)
lst.append(183)
print(lst)
# [21, 183]

ddd['age'] = 21
ddd['course'] = 182
print(ddd)
# {'age': 21, 'course': 182}

# changing something 
lst[0] = 23
print(lst) 
# [23, 183]

ddd['age'] = 23 
print(ddd)
# {'age': 23, 'course': 182}

# =============================================================================
# Differences
# =============================================================================

# Lists have position. Dictionaries have labels. 
# If you delete an element in lists, the lists get compacted. 
# Meaning, all the elements after that moves up one index. 
# If you delete an element in dictionary, it just deletes the key. 

# =============================================================================
# Dictionary Literals (Constants) 
# =============================================================================

# Dictionary literals use curly braces and have a list of key: value pairs. 
# You can make an empty dictionary using empty curly braces. 


jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100} 
print(jjj) 
# {'chuck': 1, 'fred': 42, 'jan': 100}

# dictionary can be empty
ooo = {}
print(ooo)
# {}

# dictionary can have numbers as keys, strings as values
kkk = { '1' : "chuck" , '2' : "fred", 'jan' : 100}
print(kkk['2'])
# fred
