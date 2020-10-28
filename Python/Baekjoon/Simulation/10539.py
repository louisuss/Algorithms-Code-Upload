# n = int(input())
# data = list(map(int, input().split()))
# solution = []
# temp = 0
# cnt = 1
# for d in data:
#     solution.append((cnt * d) - temp)
#     temp = cnt * d
#     cnt += 1
# for i in solution:
#     print(i, end=' ')
#

n, b = int(input()), list(map(int, input().split()))
a = [0 for i in range(len(b))]
a[0] = b[0]

for i in range(1, n):
    a[i] = (b[i]*(i+1) - sum(a))
for i in a:
    print(i, end=' ')
