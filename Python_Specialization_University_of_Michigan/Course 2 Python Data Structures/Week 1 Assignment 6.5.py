text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')

slice1 = text[pos:]
slice2 = float(slice1)

print(slice2)

# 0.8475


# my_text = 'My name is Abdullah. What is your name?'

# position1 = my_text.find('A')
# position2 = my_text.find('.')

# host = my_text[position1:position2]

# print(host)
# # Abdullah
