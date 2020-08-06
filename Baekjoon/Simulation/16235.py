n,m,k = map(int, input().split())

# 땅 양분 상태
land = [[5]*n for _ in range(n)]

# 겨울에 추가되는 양분
a = [list(map(int, input().split())) for _ in range(n)]

# x,y : 위치 / z : 나이
trees = []
for i in range(m):
    trees.append(list(map(int, input().split())))
    trees[i][0] -= 1
    trees[i][1] -= 1

tree_cnt = [[0]*n for _ in range(n)]
for tree in trees:
    tree_cnt[tree[0]][tree[1]] += 1

dead_trees = [[0]*n for _ in range(n)]
dead_trees_idx = []

def spring():
    trees.sort()
    save_data = []
    for i in range(len(trees)):
        x = trees[i][0]
        y = trees[i][1]
        z = trees[i][2]

        if land[x][y] - z >= 0:
            land[x][y] -= z
            trees[i][2] += 1
        else:
            dead_trees[x][y] += (z // 2)
            dead_trees_idx.append((x,y))
            tree_cnt[x][y] -= 1
            save_data.append([x,y,z])
    for x,y,z in save_data:
        trees.remove([x,y,z])

def summer():
    if dead_trees_idx:
        for x, y in dead_trees_idx:
            land[x][y] += dead_trees[x][y]

def fall():
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for x, y, z in trees:
        if z % 5 == 0:
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    tree_cnt[nx][ny] += 1
                    trees.append([nx,ny,1])

def winter():
    for i in range(n):
        for j in range(n):
            land[i][j] += a[i][j]

year = 0
while year != k:
    spring()
    summer()
    fall()
    winter()
    year += 1

total = 0
for i in range(n):
    total += sum(tree_cnt[i])
print(total)


