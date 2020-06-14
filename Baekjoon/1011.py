import math
import sys

t = int(input())
results = []
for _ in range(t):
    x, y = map(int, input().split())
    d = y - x

    factor = math.ceil(math.sqrt(d))

    flag1 = (factor - 1) ** 2
    flag2 = factor ** 2

    if d >= (flag1 + flag2) / 2:
        res = factor * 2 - 1
    else:
        res = factor * 2 - 2

    results.append(res)

for result in results:
    sys.stdout.write(str(result)+'\n')
