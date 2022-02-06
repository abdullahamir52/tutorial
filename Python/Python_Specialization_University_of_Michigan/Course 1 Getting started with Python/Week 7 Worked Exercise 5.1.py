# =============================================================================
# link: https://trinket.io/python/79b285a420

# Write a program which repeatedly reads numbers until the user enters 
# #“done”. Once “done” is entered, print out the total, count, and average 
# #of the numbers. If the user enters anything other than a number, detect 
# #their mistake using try and except and print an error message and skip to 
# #the next number.

# =============================================================================

sum = 0
count = 0
average = 0

while True:
    try:
        x = input('Enter a number: ')
        if (x == 'done'):
            break
        value = float(x)
        sum = value + sum
        count = count + 1
        average = sum/count
    except:
        print('Invalid output!')
print ('Total',sum,'Count', count,'Average', average)

# Output
# Enter a number: 5
# Enter a number: 5
# Enter a number: 5
# Enter a number: 5
# Enter a number: done
# Total 20.0 Count 4 Average 5.0

# =============================================================================
# ALTERNATE WAY TO SOLVE THIS 
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

# Output
# Enter a number:5
# Enter a number:5
# Enter a number:5
# Enter a number:5
# Enter a number:done
# All done!
# Total 20.0 Count 4 Average 5.0