# =============================================================================
# # 1 
# =============================================================================
#  Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade.
score = input("Enter Score: ")

try:
    s = float(score)
    if (s>1):
        quit()
    if (s>=0.9):
        print('A')
    elif(s>=0.8):
        print('B')
    elif(s>=0.7):
        print('C')
    elif(s>=0.6):
        print('D')
    else:
        print('F')
except:
    print('Error! The score is either out of range or is not a numeric value!')
    quit()

# =============================================================================
# # 2 
# =============================================================================
while True: 
    line = input('>')
    if line [0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Program execution is over!')

# =============================================================================
# # 3 (largest so far)
# =============================================================================
largest = -1
print('Before', largest)

for num in [9,41,12,3,74,15]:
    if num > largest:
        largest = num
    print('The current number:', num, 'The largest so far:', largest)

print('Largest so far after calculation:', largest)

# =============================================================================
# # 4 (smallest so far)
# =============================================================================
smallest = None
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print('Value',value, 'Smallest',smallest)
    

# =============================================================================
# # 5 (Smallest and largest)
# =============================================================================

largest=None
smallest=None
while True: # we need this loop to use break statement
    num = input('Enter a number:')
    if (num == 'done'):
        break

# try - except to input an integer or show invalid output
    try:
        value = int(num)
    except:
        print('Invalid input')
        continue

# else if ladder to find the smallest and largest number
    if ((largest is None) and (smallest is None)):
        largest=smallest=value
    elif(value<=smallest):
        smallest=value
    elif(value>=largest):
        largest=value

print("Maximum", largest)
print("Minimum", smallest)


# =============================================================================
# # 6 (Calculating avg, count, total)
# =============================================================================

count = 0
total = 0.0
avg = 0.0
while True:
    sval = input('Enter a number:')
    
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input!')
        continue
    # print(fval)
    count = count + 1
    total = total + fval
    avg = total/count

print('All done!')
print('Total', total,'Count', count,'Average', avg)

# =============================================================================
# # 7 Looping through Strings (WHILE LOOP)
# =============================================================================

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
    
# =============================================================================
# # 8  Slicing Strings
# =============================================================================

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# Output
# Mont
# P
# Python

s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])

# Output
# Mo
# thon
# Monty Python

# =============================================================================
# # 9 (String library) Making everything upper case
# =============================================================================

# Often we lowercase everything before we use the find function
# within a string.

greet = 'Hello Bob'
nnn = greet.upper()
www = greet.lower()
print(nnn,www)
# HELLO BOB hello bob

# =============================================================================
# # 10 Searching a Strings
# =============================================================================

# We use the find() function to locate a substring within another string.
# If not found, then returns -1. String position starts at zero.

fruit = 'banana'
pos = fruit.find('na')
print(pos)
# 2
aa = fruit.find('z')
print(aa)
# -1

# =============================================================================
# # 11 Stripping Whitespace
# =============================================================================

# lstrip() and rstrip() to remove Whitespace on left and right side
# strip() to remove both sides
greet = '   Hello bob   '

greet.lstrip()
# 'Hello bob   '

greet.rstrip()
# '   Hello bob'

greet.strip()
# 'Hello bob'

# =============================================================================
# # 12 Prefixes
# =============================================================================

line = 'Please have a nice day!'
line.startswith('Please')
# True
line.startswith('p')
# False

# =============================================================================
# # 13 Parsing and Extracting
# =============================================================================

# We want to capture the uct.ac.za, not including the space afterwards.
# So we use the find functions to find relevant positions. Also, we can use
# where to start counting in find function (e.g. atpos). Then we add 1 with
# atpos to start counting after the @ position.

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
print(atpos)
# 21

spacepos = data.find(' ', atpos)
print(spacepos)
# 31

host = data[atpos + 1 : spacepos]
print(host)
# uct.ac.za

# =============================================================================
# # 14 (Find string data within a text)
# =============================================================================

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')

slice1 = text[pos:]
slice2 = float(slice1)

print(slice2)

# 0.8475

my_text = 'My name is Abdullah. What is your name?'

position1 = my_text.find('A')
position2 = my_text.find('.')

host = my_text[position1:position2]

print(host)

# =============================================================================
# File handle as a sequence
# =============================================================================

xfile = open('1.txt') 
for cheese in xfile:
    print(cheese)
    
# =============================================================================
# Counting lines in a file. 
# =============================================================================

fhand = open('1.txt')
count = 0
for line in fhand:
    count = count + 1
print("Line count:", count)

# =============================================================================
# Reading the *Whole* file
# =============================================================================

fhand = open('1.txt')
inp = fhand.read()
print('Number of characters in this text file:',len(inp))
print('\nContent of the text file is:', inp)
print('\nContent of the inp[:20] is:',inp[:20]) # Shows the first 20 chars


# =============================================================================
# Searching through a file (fixes the newline problem)
# =============================================================================

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


# =============================================================================
# 7.2 Write a program that prompts for a file name, then opens that file 
# and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of 
# the lines and compute the average of those values and produce an 
# output as shown below. Do not use the sum() function or a variable 
# named sum in your solution.
# You can download the sample data at 
# http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.
# =============================================================================

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
total = 0
avg = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    total = total + float(line[20:].strip())
    avg = total/count
    # print(line)
print("Average spam confidence:", avg)
# print("Done")

# Output
# Enter file name: mbox-short.txt
# Average spam confidence: 0.7507185185185187


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


# =============================================================================
# 8.4 Open the file romeo.txt and read it line by line. For each line, split 
# the line into a list of words using the split() method. The program should
# build a list of words. For each word on each line check to see if the word
# is already in the list and if not append it to the list. When the program 
# completes, sort and print the resulting words in alphabetical order.
# =============================================================================

# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()                    # list for the desired output

for line in fh:                 # to read every line in the file
    line1 = line.rstrip()       # to eliminate the unwanted blanks
    words = line1.split()       # turn the line into a list of words
    
    for element in words:       # check every element in word 
        if element in lst:      # if element is repeated
            continue            # do nothing
        else:                   # else if element is not in the list
            lst.append(element) # append     
lst.sort()                      # sort the list (after the loop ends)
print(lst)

# =============================================================================
# 8.5 Open the file mbox-short.txt and read it line by line. When you find a 
# line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word 
# in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# =============================================================================

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

filename = input("Enter file name: ")
if len(filename) < 1 :
    filename = "mbox-short.txt"

filehandle = open(filename)
count = 0

for line in filehandle:             # reads every line in filehandle
    if not line.startswith('From '): 
        continue                    # starts the loop again 

    line = line.rstrip()            # takes away the whitespace at the end
    words = line.split()            # creates a list of words from line
    print(words[1])                 # prints the 2nd element in the words
    count = count + 1 
    
print("There were", count, "lines in the file with From as the first word")


# =============================================================================
# Print out when the email was sent
# =============================================================================

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])

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


# =============================================================================
# 9.4 Write a program to read through the mbox-short.txt and figure out 
# who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those 
# lines as the person who sent the mail. The program creates a Python 
# dictionary that maps the sender's mail address to a count of the number 
# of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to 
# find the most prolific committer.
# =============================================================================

filename = input("Enter file:")
if len(filename) < 1 :
    filename = "mbox-short.txt"
filehandle = open(filename)

my_list = list()
counts = dict()

for line in filehandle:             
    if line.startswith('From '):
        line = line.rstrip() 
        line = line.split()
        my_list.append(line[1])
        
for word in my_list:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None         
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

# =============================================================================
# Counting
# =============================================================================
filename = input('Enter file: ')
if len(filename) < 1 :
    filename = 'clown.txt'
filehandle = open(filename)
my_dict = dict()


for line in filehandle:
    line = line.rstrip()
    words = line.split()
    
    for word in words: 
        my_dict[word] = my_dict.get(word,0) + 1 

# Most used words loop: 
largest_value = -1
largest_key = None

for key,value in my_dict.items():
    print(key,value)
    if value > largest_value: 
        largest_value = value
        largest_key = key 
        
print('Most common word:', largest_key, '\nUsed: ', largest_value, 'times')

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

# =============================================================================
# Final Program
# =============================================================================

fname = input('Enter file: ')

if len(fname) < 1 : 
    fname = 'clown.txt'

hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create update counter
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items():     
    newt = (v,k)        # Creates a new tuple, interchanging keys and values
    tmp.append(newt)    # Adds every value of 'newt' to 'tmp'

tmp = sorted(tmp, reverse = True)   # flips the sorting order

for v,k in tmp[:5]:
    print(k,v)      # flips the list again 
    
# Output
# Enter file: intro.txt
# the 226
# to 204
# a 165
# and 160
# you 130