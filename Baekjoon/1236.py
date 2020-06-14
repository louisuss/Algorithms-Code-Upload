n, m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(input())

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            col[j] = 1
row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

col_count = 0
for j in range(m):
    if col[j] == 0:
        col_count += 1
print(max(row_count, col_count))
# N, M = map(int, input().split())
# lis = []
# for _ in range(N):
#     a = list(map(str, input().split()))
#     lis.append(a)
# security = []
# for i in range(N):
#     for j in range(M):
#         if lis[i][j] == 'X':
#             security.append([i, j])
#
# for i in range(len(security)):
#