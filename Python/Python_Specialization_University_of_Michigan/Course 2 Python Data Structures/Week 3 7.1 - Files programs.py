# =============================================================================
# File processing
# =============================================================================

# A text file can be thought of as a sequence of lines.

# =============================================================================
# Opening a file
# =============================================================================

# Before we can work with a file, we need to tell python about that file.
# It's called 'opening'. Done with open() function.
# Open() returns a "file handle", a variable that performs operations on a file.
# Similar to "File -> Open" in a word processor.

# =============================================================================
# Using open()
# =============================================================================

# handle = open(filename, mode)
# mode = tells whether we are going to read or write it.
# filename is a string.
# mode is optional and should be 'r'> read, 'w'>write

# fhand = open('mbox.txt', 'r') it returns the file handle

# =============================================================================
# What is a handle?
# =============================================================================

# file handle is not the data, it's just a way to get at the data.
# Handle is some sort of a porthole/connection, between program and file. 

fhand = open('mbox.txt')
print(fhand)
# <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>

# =============================================================================
# When files are missing
# =============================================================================

fhand = open('stuff.txt')

# Traceback (most recent call last):
#   File "1.py", line 2, in <module>
#     fhand = open('stuff.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'


# =============================================================================
# The Newline character
# =============================================================================

stuff1 = 'Hello\nWorld!'
stuff1
# Hello\nWorld!

print(stuff1)
# Output
# Hello
# World!

# so basically, if you write stuff1, it shows the \n. if you print it,
# it treats \n like a new line. 

stuff2 = 'X\nY'
print(stuff2)

# Output
# X
# Y

len(stuff2)
# 3
