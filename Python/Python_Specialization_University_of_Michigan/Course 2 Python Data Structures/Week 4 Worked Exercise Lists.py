han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print('Line', line)
    wds = line.split()
    # print('Words:',wds)
    
# =============================================================================
#     if line == '' :
#         # print('Skip Blank')
#         continue
#   # This might blow up 
#   if wds[0] != 'From':
#       # print('Ignore')
#       continue
#   print(wds[2])
# =============================================================================
   
 
# =============================================================================
#     # Guardian a bit stronger
#     if len(wds) < 3:
#         continue
# 
#     # This might blow up 
#     if wds[0] != 'From':
#         # print('Ignore')
#         continue
#     print(wds[2])
# =============================================================================

    
    # Guardian in a compound statement
    # Gotta get the order right
    if len(wds) < 3 or wds[0] != 'From':
        # print('Ignore')
        continue
    print(wds[2])

    # if wds[0] != 'From' or len(wds) < 3:
    #     continue
    # this would not work. 1st condition is checked first.
    # this is called short circuit evaluation. if first part is true, 
    # second part is irrelevant 

