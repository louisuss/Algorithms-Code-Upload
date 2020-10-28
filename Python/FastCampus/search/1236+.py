n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]

pos_r = set()
pos_c = set()


for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            pos_r.add(i)
            pos_c.add(j)
len_pos_r = len(pos_r)
len_pos_c = len(pos_c)
print(max(n-len_pos_r, m-len_pos_c))




