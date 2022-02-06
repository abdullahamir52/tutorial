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


print(di)
# Output
# {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1,
#  'tent': 2, 'fell': 1, 'down': 1, 'on': 1}


x = di.items()
print(x)        # gives us the key value pairs of the 'di'
# Output
# dict_items([('the', 7), ('clown', 2), ('ran', 2), ('after', 1), ('car', 3), 
#             ('and', 3), ('into', 1), ('tent', 2), ('fell', 1), ('down', 1), 
#             ('on', 1)])


x = sorted(di.items())
print(x)        # gives us the sorted version of 'di' (using the strings)
# Output
# [('after', 1), ('and', 3), ('car', 3), ('clown', 2), ('down', 1),
#  ('fell', 1), ('into', 1), ('on', 1), ('ran', 2), ('tent', 2), ('the', 7)]


x = sorted(di.items())
print(x[:5])        # gives us the first 5 elements of sorted version of 'di'
# Output
# [('after', 1), ('and', 3), ('car', 3), ('clown', 2), ('down', 1)]


tmp = list()
for k,v in di.items():
    print(k,v)          # prints out the items inside 
# Output
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


tmp = list()
for k,v in di.items():     
    newt = (v,k)        # Creates a new tuple, interchanging keys and values
    tmp.append(newt)    # Adds every value of 'newt' to 'tmp'
print('Flipped:\n', tmp)
# output
# Flipped:
#  [(7, 'the'), (2, 'clown'), (2, 'ran'), (1, 'after'), (3, 'car'), 
#   (3, 'and'), (1, 'into'), (2, 'tent'), (1, 'fell'), (1, 'down'), (1, 'on')]


tmp = sorted(tmp)
print('Sorted:\n', tmp)
# Output
# Sorted:
#  [(1, 'after'), (1, 'down'), (1, 'fell'), (1, 'into'), (1, 'on'), 
#   (2, 'clown'), (2, 'ran'), (2, 'tent'), (3, 'and'), (3, 'car'), (7, 'the')]


tmp = sorted(tmp, reverse = True)   # flips the sorting order
print('Sorted:\n', tmp [:5])        # prints out the first 5 elements
# Output
# Sorted:
#  [(7, 'the'), (3, 'car'), (3, 'and'), (2, 'tent'), (2, 'ran')]


for v,k in tmp[:5]:
    print(k,v)      # flips the list again 
# Output
# the 7
# car 3
# and 3
# tent 2
# ran 2


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

# =============================================================================
# # This is the loop that we use to find the most common word 
# largest = -1
# theword = None
# for k,v in di.items():
#     if v > largest:
#         largest = v
#         theword = k
# 
# print(theword,largest)
# =============================================================================
