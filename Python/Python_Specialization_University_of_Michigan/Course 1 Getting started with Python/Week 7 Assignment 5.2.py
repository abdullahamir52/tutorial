largest=None
smallest=None
while True: # we need this loop to use break statement
    num = input('Enter a number:')
    if (num == 'done'):
        break

# try - except to input an integer or show invalid output
    try:
        value = int(num)
    except:
        print('Invalid input')
        continue

# else if ladder to find the smallest and largest number
    if ((largest is None) and (smallest is None)):
        largest=smallest=value
    elif(value<=smallest):
        smallest=value
    elif(value>=largest):
        largest=value

print("Maximum", largest)
print("Minimum", smallest)

# Output
# Enter a number:done
# Maximum None
# Minimum None

# Output
# Enter a number:5
# Enter a number:done
# Maximum 5
# Minimum 5

# Output
# Enter a number:8
# Enter a number:9
# Enter a number:7
# Enter a number:5
# Enter a number:9
# Enter a number:done
# Maximum 9
# Minimum 5

# =============================================================================
#     for i in value: 
#         if l is 0:
#             l=i
#         elif i> l:
#             l=i
#     for j in value: 
#         if s is 0:
#             s=j
#         elif j<s:
#             s=j  
# 
# =============================================================================


# =============================================================================
# while True:
#     sval = input('Enter a number:')
#     
#     if sval == 'done':
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid input!')
#         continue
#     # print(fval)
#     num = num + 1
#     tot = tot + fval
#     avg = tot/num
# 
# print('All done!')
# print('Total',tot,'Count',num,'Average', avg)
# 
# =============================================================================
