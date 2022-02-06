# =============================================================================
# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.
# =============================================================================

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d=dict()

for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line=line.split()
        line=line[5]        # gets the timestamp
        line=line[0:2]      # gets the 1st 2 string of timestamp (hour)
        d[line]=d.get(line,0) + 1

lst=list()
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)

# =============================================================================
# Another Example
# =============================================================================

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
open_file=open(name)

file_dict={}
for line in open_file :
    line=line.rstrip()
    if line.startswith("From ") :
            words=line.split()
            time=words[5]       # gets the timestamp
            hours=time[:2]      # gets the 1st 2 string of timestamp (hour)
            file_dict[hours]=file_dict.get(hours,0) + 1

for k,v in sorted (file_dict.items()) :
    print(k,v)

# =============================================================================
# Code that I came up with
# =============================================================================

name = input("Enter file:")                     # Line 1
if len(name) < 1 :                              # Line 2
    name = "mbox-short.txt"                     # Line 3
handle = open(name)                             # Line 4

my_list = list()                                # Line 5
my_list1 = list()                               # Line 6
counts = dict()                                 # Line 7

for line in handle:                             # Line 8
    if line.startswith('From '):                # Line 9
        line = line.rstrip()                    # Line 10
        line = line.split()                     # Line 11
        my_list.append(line[5])                 # Line 12

for item in my_list:                            # Line 13
    item = item.split(':')                      # Line 14
    my_list1.append(item[0])                    # Line 15

for hour in my_list1:                           # Line 16
    counts[hour] = counts.get(hour,0) + 1       # Line 17

for k, v in sorted(counts.items()):             # Line 18
    print(k,v)                                  # Line 19

# Line 1-4, prompts user, takes input, creates a filehandle
# Line 5-7, creates two lists and a dictionary
# Line 8, reads every line in the file
# Line 9, separates lines that start with 'From '
# Line 10, strips the whitespace
# Line 11, returns a list of words in each lines.
# Line 12, adds the 6th element of each line (timestamp) to 'my_list'
# Line 13, reads every element in my_list (e.g.'09:14:16')
# Line 14, splits the timestamp using ':' as the delimiter
# Line 15, adds the first element (e.g. 09) to another list
# Line 16-17, creates a dictionary that counts the number of times an element
# is repeated.
# Line 18-19, sorts the key-value pair in 'counts' according to their key
