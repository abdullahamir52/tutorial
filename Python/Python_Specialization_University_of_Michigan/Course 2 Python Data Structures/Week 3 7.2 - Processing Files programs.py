# =============================================================================
# File handle as a sequence
# =============================================================================

# * a file handle open for read can be treated as a sequence of strings
# where each line in the file is a string in the sequence.
# * we can use the for statement to iterate through a sequence.
# * Remember - a sequence is an ordered set.


xfile = open('1.txt') # xfile is a file handle, a way to get to data.
# xfile(handle) is a sequence (of lines)
for cheese in xfile:
    print(cheese)
    
# Output
# line 1
# line 2 
# line 3
# line 4
# This is line 5 
# line 6
# This is line 7
# line 8
# line 9
# line 10


# it is a determinate for loop. You put the handle (xfile) inside the for
# loop. The iteration variable (cheese) will look for each line in '1.txt'
# and print each line. 


# =============================================================================
# Counting lines in a file. 
# =============================================================================

# * Open a file read-only
# * Use a for loop to read each line
# * Count the lines and print out the number of lines. 

fhand = open('1.txt')
count = 0
for line in fhand:
    count = count + 1
print("Line count:", count)

# Output 
# Line count: 10


# =============================================================================
# Reading the *Whole* file
# =============================================================================

# We can read the whole file (newlines and all) into a single string

fhand = open('1.txt')
inp = fhand.read()
print('Number of characters in this text file:',len(inp))
print('\nContent of the text file is:', inp)
print('\nContent of the inp[:20] is:',inp[:20]) # Shows the first 20 chars

# Output
# Number of characters in this text file: 71
#
# Content of the text file is: line 1
# line 2 
# ......
# line 10 
#
# Content of the inp[:20] is: line 1
# line 2 
# line 


# =============================================================================
# Searching through a file
# =============================================================================

# We can put an if statement in our for loop to only print lines that meet
# some criteria.

fhand = open('1.txt')
for line in fhand:
    if line.startswith('This'):
        print(line)

# Output
# This is line 5 
#
# This is line 7


# There is an extra blank line in between the output. One newline is due to
# the newline within the text file. And another newline is added by the
# print statement. 


# =============================================================================
# Searching through a file (fixes the newline problem)
# =============================================================================

# * we can strip the whitespace from the right-hand side of the the string
# using the rstrip() from the string library. 
# * the newline is considered 'whitespace' and is stripped

fhand = open('1.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('This'):
        print(line)

# Output
# This is line 5
# This is line 7


# =============================================================================
# Skipping with Continue
# =============================================================================

# Sometimes you just want to flip the logic

fhand = open('1.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('This'):
        continue
    print(line)

# Output
# This is line 5
# This is line 7


# =============================================================================
# Using 'in' to select lines
# =============================================================================

# We can look for a string anywhere in a line as our selection criteria

fhand = open('1.txt')
for line in fhand:
    line = line.rstrip()
    if not 'This' in line :
        continue
    print(line)
    
# Output
# This is line 5
# This is line 7


# =============================================================================
# Same program with a prompt
# =============================================================================

filename = input('Enter the file name: ') # prompts for the file name 
fhand = open(filename)
count = 0
for line in fhand:
    if line.startswith('This'):
        count = count + 1
print('There are', count ,'lines that starts with THIS in', filename)

# Output
# Enter the file name: 1.txt
# There are 2 lines that starts with THIS in 1.txt


# =============================================================================
# What if the user types a bad file name? 
# =============================================================================

fname = input('Enter the file name: ') # prompts for the file name 

try:
    fhand = open(fname)

except:
    print('The file',fname,' cannot be opened!')
    quit()

count = 0
for line in fhand:
    if line.startswith('This'):
        count = count + 1
print('There are',count,'lines that starts with THIS in',fname)

# Output
# Enter the file name: 2.txt
# The file 2.txt  cannot be opened!
# Enter the file name: 1.txt
# There are 2 lines that starts with THIS in 1.txt