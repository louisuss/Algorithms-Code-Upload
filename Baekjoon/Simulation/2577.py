from collections import Counter

A = int(input())
B = int(input())
C = int(input())

res = A*B*C
res = str(res)

cnt = Counter(res)
for i in range(0,10):
    i = str(i)
    print(cnt[i])
