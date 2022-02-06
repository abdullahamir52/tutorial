# =============================================================================
# Program 1
# =============================================================================

n = 5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')
print(n)

# Output
# 5
# 4
# 3
# 2
# 1
# Blastoff!
# 0

# =============================================================================
# Program 2 : Infinite loop
# =============================================================================

n = 1
while n>0:
    print('Lather')
    print('Rinse')
print('Dry off!')

# =============================================================================
# Program 3 : Zero loop
# =============================================================================

n = 0
while n>0:
    print('Lather')
    print('Rinse')
# Because the iteration variable's value is not satisfied, it does not 
# execute the codes within the loop
print('Dry off!')

# Output
# Dry off!

# =============================================================================
# Program 4 : Breaking out of a loop
# =============================================================================

# The break statement ends the current loop and jumps to the statement 
# immediately following the loop

while True: 
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Program execution is over!')

# Output
# >Hello 
# Hello 
# >My name is Abdullah
# My name is Abdullah
# >done
# Program execution is over!

# =============================================================================
# Program 5 : Continue
# =============================================================================

# Finishing the iteration with continue. 
# The continue statement ends the current iteration and jumps to the top 
# of the loop and starts the next iteration
# when the program faces a continue statement, it goes up to the top of loop
# when the program faces a break statement, it exits the loop

while True: 
    line = input('>')
    if line [0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    
print('Program execution is over!')

# Output
# ># line 1
# >line 2
# line 2
# >done
# Program execution is over!