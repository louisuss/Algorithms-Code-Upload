a = list(input().upper())
b = list()
count = 0

for i in set(a):
    b.append([a.count(i), i])

for i in range(len(b)):
    if max(b)[0] == b[i][0]:
        count+=1
if count > 1:
    print('?')
else:
    print(max(b)[1])
