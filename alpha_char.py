"""
Takes the index of each character in the string, and if the index is even,
the binary digit is 1, otherwise 0. Then convert the binary to decimal.
"""

s = "abzsd"
s_list = list(map(str, s))
n = 0
x = []
for i in s_list:
    if i.isalpha():
        n = ord(i) - 96
        if n % 2 == 0:
            
            x.append(1)
        else:
        
            x.append(0)


final = ''.join(map(str, x))
print(final)
# convert binary to decimal
final = int(final, 2)
print(final)