# =============================================================================
# Counting pattern
# =============================================================================

# The general pattern to count the words in a line of text is to split the
# line into words, then loop through the words and use a dictionary to 
# track the count of each word independently

counts = dict()                 # creates a dictionary

print('Enter a line of text: ') 
line = input('')                # let's you input a file 

words = line.split()            # splits the lines and returns a list of words

print('\nWords:', words)        # prints the individual words

print('\nCounting...')            

for word in words:
    counts[word] = counts.get(word, 0) + 1   # check previous program

print('\nCounts', counts)         

# =============================================================================
# Definite loops and dictionaries
# =============================================================================

# Even though dictionaries are not stored in order, we can write a for loop
# that goes through all the entries in a dictionary - actually it goes 
# through all of the keys in the dictionary and looks up the values. 

counts = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}

for key in counts:              # loop is going to go through keys of dict()
    print(key, counts[key])     # not the values of the dict()

# Output
# chuck 1
# fred 42
# jan 100

# =============================================================================
# Retrieving lists of keys and values
# =============================================================================

# You can get a list of keys, values, or items(both) from a dictionary

jjj = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}

print(list(jjj))
# ['chuck', 'fred', 'jan']

print(jjj.keys())
# dict_keys(['chuck', 'fred', 'jan'])

print(jjj.values())
# dict_values([1, 42, 100])

print(jjj.items())
# dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])
# this is a 3 item list
# each item is a tuple
# this is a new data structures

# =============================================================================
# Bonus: Two iteration variables! 
# =============================================================================

# We loop through the key-value pairs in a dict() using 'two' iteration variables.. 
# Each iteration, the first variable is the key and the second variable is the
# corresponding value for the key. 

jjj = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}

for key,value in jjj.items(): # here, key and value are two iteration variable
    print(key,value)

# Output
# chuck 1
# fred 42
# jan 100


name = input('Enter file: ')                    # line 1 
handle = open(name)                             # line 2

counts = dict()                                 # line 3

for line in handle:                             # line 4
    words = line.split()                        # line 5
    for word in words:                          # line 6
        counts[word] = counts.get(word,0) + 1   # line 7

bigcount = None                                 # line 8
bigword = None                                  # line 9

for word,count in counts.items():               # line 10
    if bigcount is None or count > bigcount:    # line 11
        bigword = word                          # line 12
        bigcount = count                        # line 13

print('\nThe word that is most used: ', bigword, '\n\nand it is used:             ', bigcount, 'times')


# Line 4 reads a line of the 'file'. 
# In line 5, 'words' returns the list of strings in that line. 
# In line 6, this nested for loop reads every item in 'words'.
# In line 7, it inserts the count of the item inside 'words'.

# In line 10, two iteration variables, 'word' and 'count' attaches with 
# key and values of 'counts' respectively.
# In line 11, if it is the first value then assign accordingly, otherwise,
# In line 12 and 13, the word that is most used is assigned to 'bigword' 
# and the number of times it is used is assigned to count. 

# Output
# Enter file: mbox-short.txt
# The word that is most used:  Jan 
# and it is used:              352 times