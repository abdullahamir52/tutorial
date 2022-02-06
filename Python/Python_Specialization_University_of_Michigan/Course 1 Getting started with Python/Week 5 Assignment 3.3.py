#  Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade.
score = input("Enter Score: ")

try:
    s = float(score)
    if (s>1):
        quit()
except:
    print('Error! The score is either out of range or is not a numeric value!')
    quit()
    
if (s>=0.9):
    print('A')
elif(s>=0.8):
    print('B')
elif(s>=0.7):
    print('C')
elif(s>=0.6):
    print('D')
else:
    print('F')

# Output
# Enter Score: .8
# B

# Output
# Enter Score: 1.2
# Error! The score is either out of range or is not a numeric value!

# Output
# Enter Score: asdf
# Error! The score is either out of range or is not a numeric value!