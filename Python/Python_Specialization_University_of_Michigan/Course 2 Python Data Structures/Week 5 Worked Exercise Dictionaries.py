
=============================================================================
filename = input('Enter file: ')

if len(filename) < 1 :
    filename = 'clown.txt'

filehandle = open(filename)

my_dict = dict()

for line in filehandle:
    line = line.rstrip()
    # print(line)
    
    words = line.split()
    # print(words)
    
    # words is a list
    
    for word in words: 
        print(word) # prints out the word encountered
        
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1
            print('** Existing **')
        else:
            my_dict[word] = 1
            print('** New **')
        
        print(my_dict[word])
        # prints out the count of that word in the file
        
print(my_dict)
# give us the count
=============================================================================



=============================================================================
filename = input('Enter file: ')

if len(filename) < 1 :
    filename = 'clown.txt'

filehandle = open(filename)

my_dict = dict()

for line in filehandle:
    line = line.rstrip()
    
    words = line.split()
    
    for word in words: 
        print('**', word, my_dict.get(word,-99))
        # first time it encounters a new word, it prints out 99
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1
        
        print('Word is: ', word, '\ncount is: ', my_dict[word], '\n')
        # prints out the count of that word in the file
        
print(my_dict)
# give us the count

# Output
# ** the -99
# Word is:  the 
# count is:  1 

# ** clown -99
# Word is:  clown 
# count is:  1 

# ** ran -99
# Word is:  ran 
# count is:  1 

# ** after -99
# Word is:  after 
# count is:  1 

# ** the 1
# Word is:  the 
# count is:  2 

# ** car -99
# Word is:  car 
# count is:  1 

# ** and -99
# Word is:  and 
# count is:  1 

# ** the 2
# Word is:  the 
# count is:  3 

# ** car 1
# Word is:  car 
# count is:  2 

# ** ran 1
# Word is:  ran 
# count is:  2 

# ** into -99
# Word is:  into 
# count is:  1 

# ** the 3
# Word is:  the 
# count is:  4 

# ** tent -99
# Word is:  tent 
# count is:  1 

# ** and 1
# Word is:  and 
# count is:  2 

# ** the 4
# Word is:  the 
# count is:  5 

# ** tent 1
# Word is:  tent 
# count is:  2 

# ** fell -99
# Word is:  fell 
# count is:  1 

# ** down -99
# Word is:  down 
# count is:  1 

# ** on -99
# Word is:  on 
# count is:  1 

# ** the 5
# Word is:  the 
# count is:  6 

# ** clown 1
# Word is:  clown 
# count is:  2 

# ** and 2
# Word is:  and 
# count is:  3 

# ** the 6
# Word is:  the 
# count is:  7 

# ** car 2
# Word is:  car 
# count is:  3 

# {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 
#  'tent': 2, 'fell': 1, 'down': 1, 'on': 1}

=============================================================================


=============================================================================
filename = input('Enter file: ')

if len(filename) < 1 :
    filename = 'clown.txt'

filehandle = open(filename)

my_dict = dict()

for line in filehandle:
    line = line.rstrip()
    
    words = line.split()
    
    for word in words: 
        
        # print('**', word, my_dict.get(word,-99))
        # # first time it encounters a new word, it prints out 99
        
        oldcount = my_dict.get(word,0)
        print(word, 'old', oldcount)
# this is basically saying that look up the oldcount that we have, and if you 
# don't find one, use zero, and we will print that out. 
        
        newcount = oldcount + 1 
        my_dict[word] = newcount 
        print(word, 'new', newcount)
# But we don't do this big chunk of code. We write all of them in a short way.
# Check next program. 
        
        
        print('Word is: ', word, '\ncount is: ', my_dict[word], '\n')
        # prints out the count of that word in the file
        
print(my_dict)
# give us the count


# Output
# Enter file: 
# the old 0
# the new 1
# Word is:  the 
# count is:  1 

# clown old 0
# clown new 1
# Word is:  clown 
# count is:  1 

# ran old 0
# ran new 1
# Word is:  ran 
# count is:  1 

# after old 0
# after new 1
# Word is:  after 
# count is:  1 

# the old 1
# the new 2
# Word is:  the 
# count is:  2 

# car old 0
# car new 1
# Word is:  car 
# count is:  1 

# and old 0
# and new 1
# Word is:  and 
# count is:  1 

# the old 2
# the new 3
# Word is:  the 
# count is:  3 

# car old 1
# car new 2
# Word is:  car 
# count is:  2 

# ran old 1
# ran new 2
# Word is:  ran 
# count is:  2 

# into old 0
# into new 1
# Word is:  into 
# count is:  1 

# the old 3
# the new 4
# Word is:  the 
# count is:  4 

# tent old 0
# tent new 1
# Word is:  tent 
# count is:  1 

# and old 1
# and new 2
# Word is:  and 
# count is:  2 

# the old 4
# the new 5
# Word is:  the 
# count is:  5 

# tent old 1
# tent new 2
# Word is:  tent 
# count is:  2 

# fell old 0
# fell new 1
# Word is:  fell 
# count is:  1 

# down old 0
# down new 1
# Word is:  down 
# count is:  1 

# on old 0
# on new 1
# Word is:  on 
# count is:  1 

# the old 5
# the new 6
# Word is:  the 
# count is:  6 

# clown old 1
# clown new 2
# Word is:  clown 
# count is:  2 

# and old 2
# and new 3
# Word is:  and 
# count is:  3 

# the old 6
# the new 7
# Word is:  the 
# count is:  7 

# car old 2
# car new 3
# Word is:  car 
# count is:  3 

# {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 
#  'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
==============================================================================


==============================================================================
filename = input('Enter file: ')
if len(filename) < 1 :
    filename = 'clown.txt'
filehandle = open(filename)
my_dict = dict()


for line in filehandle:
    
    line = line.rstrip()
    words = line.split()
    
    for word in words: 
    
        # oldcount = my_dict.get(word,0)
        # newcount = oldcount + 1 
        # my_dict[word] = newcount 
        # These three lines are combined into the next statement
        
        # idiom: retrieve/create/update counter
        my_dict[word] = my_dict.get(word,0) + 1 
        
        print('Word is: ', word, '\ncount is: ', my_dict[word], '\n')

# Output
# Enter file: 
# Word is:  the 
# count is:  1 

# Word is:  clown 
# count is:  1 

# Word is:  ran 
# count is:  1 

# Word is:  after 
# count is:  1 

# Word is:  the 
# count is:  2 

# Word is:  car 
# count is:  1 

# Word is:  and 
# count is:  1 

# Word is:  the 
# count is:  3 

# Word is:  car 
# count is:  2 

# Word is:  ran 
# count is:  2 

# Word is:  into 
# count is:  1 

# Word is:  the 
# count is:  4 

# Word is:  tent 
# count is:  1 

# Word is:  and 
# count is:  2 

# Word is:  the 
# count is:  5 

# Word is:  tent 
# count is:  2 

# Word is:  fell 
# count is:  1 

# Word is:  down 
# count is:  1 

# Word is:  on 
# count is:  1 

# Word is:  the 
# count is:  6 

# Word is:  clown 
# count is:  2 

# Word is:  and 
# count is:  3 

# Word is:  the 
# count is:  7 

# Word is:  car 
# count is:  3 
==============================================================================



==============================================================================

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
        
print(my_dict)

# Output
# Enter file: 
# {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 
#  'tent': 2, 'fell': 1, 'down': 1, 'on': 1}      
==============================================================================



=============================================================================
Now we want to find the most common word
=============================================================================

largest_value = -1
largest_key = None

for key,value in my_dict.items(): # items() takes one two iteration variables
    print(key,value)
    if value > largest_value: 
        largest_value = value
        largest_key = key 
        

print('Most common word:', largest_key, '\nUsed: ', largest_value, 'times')

# Output
# Most common word: the 
# Used:  7 times


=============================================================================
Final program
=============================================================================

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

# Output
# Enter file: 
# the 7
# clown 2
# ran 2
# after 1
# car 3
# and 3
# into 1
# tent 2
# fell 1
# down 1
# on 1
# Most common word: the 
# Used:  7 times
