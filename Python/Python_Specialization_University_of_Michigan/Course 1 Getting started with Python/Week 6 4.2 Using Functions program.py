# =============================================================================
# Program 1 (Calling function)
# =============================================================================

x = 5
print('Hello')
def print_lyrics():
    print('My name is Abdullah. And this line is within the function.')
# If we don't invoke the function, then it just stores the function.
print('Yo')
x = x + 2
print(x)
print_lyrics()

# Output
# Hello
# Yo
# 7
# My name is Abdullah. And this line is within the function.

# =============================================================================
# Program 2 (Arguments and parameters)
# =============================================================================

# Arguments are input values.e.g.'es','fr'. Parameters are a variable which
# we use in the function definition. e.g. 'lang'. It is a 'handle' that allows
# the code in the fn to access the arguments for a particular fn invocation

def greet(lang):
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')

# Output
# Hello
# Hola
# Bonjour

# =============================================================================
# Program 3 (Return value) 
# =============================================================================

# Often a function will take its argument, do some calculation and return 
# a value in the expression

def greet():
    return 'Hello'
print(greet(), 'Glenn')
print(greet(), 'Sally')

# Output
# Hello Glenn
# Hello Sally

# =============================================================================
# Program 4 (Combining the previous programs)
# =============================================================================

# A return command stops, determines the residual value and gives it back 
# to us. Once we can use the return command, the function stops there. 

def greet(lang):
    if lang=='es':
        return'Hola'
    elif lang=='fr':
        return'Bonjour'
    else:
        return'Hello'
print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

# Output
# Hello Glenn
# Hola Sally
# Bonjour Michael

# =============================================================================
# Program 5
# =============================================================================

# Function with a return value = 'fruitful' Function
# Function without a return value= 'Non-fruitful' Function

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)

# 8