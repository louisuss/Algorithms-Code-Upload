s = input()
alpha = ''
number = ''
for c in s:
    if c.isalpha():
        alpha += c
    else:
        number += c

print(''.join(sorted(alpha) + sorted(number)))