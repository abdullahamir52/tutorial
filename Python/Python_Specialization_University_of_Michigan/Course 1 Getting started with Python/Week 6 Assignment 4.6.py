# =============================================================================
# My practice to understand the return function
# =============================================================================

# This user-defined function takes the value of var1 and floats it then 
# assigns it to var2. Then it multiplies var2 by 10 and assigns it to pay. 
# Then the return value/residual value is pay

def computepay(var1):
    var2 = float(var1)
    pay = var2*10
    return pay

# Abovementioned user-defined function is used below

# This statement will take the input value of h and assign it into var1
var1 = input('Hours: ')

# then computepay function will take the value of var1 as its argument 
# and execute the codes within it
p = computepay(var1)
print("Pay",p)

# Output
# Hours: 10
# Pay 100.0

# =============================================================================
# Assignment 4.6
# =============================================================================

def computepay(h,r):
    if (h>40):
    	pay = ((h-40)*(1.5*r)) + (40*r)
    else:
    	pay = (h*r)
    return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error! Please enter a numeric input!")
    quit()
p = computepay(h,r)
print("Pay",p)

# Output
# Enter Hours:50
# Enter rate:10
# Pay 550.0