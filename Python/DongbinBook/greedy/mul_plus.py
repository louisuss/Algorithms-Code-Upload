s = list(map(int, list(input())))
result = s[0]

for i in range(1, len(s)):
    if result <= 1 or s[i] <= 1:
        result += s[i]
    else:
        result *= s[i]
print(result)
