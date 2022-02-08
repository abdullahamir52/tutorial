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
