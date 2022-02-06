# =============================================================================
# 7.1 Write a program that prompts for a file name, then opens that file and 
# reads through the file, and print the contents of the file in upper case. 
# Use the file 'words.txt' to produce the output below.
# =============================================================================

# Use words.txt as the file name
fname = input("Enter file name: ") # prompts for a filename
fhandle = open(fname) # creates a connection with the file

for line in fhandle: # reads every line of the file 
    fline = line.rstrip() # deletes the whitespace
    print(fline.upper()) # prints every line in uppercase
    
# Output
# Enter file name: 1.txt
# LINE 1
# LINE 2
# LINE 3
# LINE 4
# THIS IS LINE 5
# LINE 6
# THIS IS LINE 7
# LINE 8
# LINE 9
# LINE 10