# Flood Fill
# Flood Fill 처리한 후 어떻게 처리할 것인가
# 이차원 배열에서 배열내부의 요소들을 어떻게 잘 이동할것인가

def new_array(n):
    return [[False for _ in range(10)] for _ in range(n)]

n, k = map(int, input().split())
m = [list(input()) for _ in range(n)]

dx, dy = [0,1,0,-1], [1,0,-1,0]

def dfs(x,y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y+dy[i]
        if xx < 0 or xx >=n or yy < 0 or yy >=10:
            continue
        if ck[xx][yy] or m[x][y] != m[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret


def dfs2(x,y,val):
    ck2[x][y] = True
    m[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] or m[xx][yy] != val:
            continue
        dfs2(xx, yy, val)

def down():
    # 세로방향으로 차례대로
    for i in range(10):
        temp = []
        for j in range(n):
            if m[j][i] != '0':
                temp.append(m[j][i])
        # 세로 배열에서 남아있는 숫자 개수만큼 행 갯수에서 빼고 이만큼 0으로 채움
        for j in range(n-len(temp)):
            m[j][i] = '0'
        for j in range(n-len(temp), n):
            m[j][i] = temp[j-(n-len(temp))]

# dfs 돌리고 맞으면 다시 dfs 돌려서 없애고
while True:
    exist = False
    ck = new_array(n)
    ck2 = new_array(n)

    for i in range(n):
        for j in range(10):
            if m[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j) # 개수 세기
            if res >= k:
                # 함수 틀렸는지 체크하기 위해서는 함수 다음에서 디버깅
                dfs2(i, j, m[i][j]) # 지우기
                exist = True

    if not exist:
        break
    down() # 내리기

for i in m:
    print(''.join(i))


# n, k = map(int, input().split())
# m = [list(map(int, ' '.join(input()).split())) for _ in range(n)]
#
# def make_ck(n):
#     return [[False]*10 for _ in range(n)]
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
# def dfs_cnt(x,y):
#     ck[x][y] = True
#     ret = 1
#     idx.append((x,y))
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >= 10:
#             continue
#         if not ck[nx][ny] and m[x][y] == m[nx][ny]:
#             ret += dfs_cnt(nx, ny)
#     return ret
#
# def dfs_erase(idx):
#     for x, y in idx:
#         m[x][y] = 0
#
#
# def move_down():
#     for i in range(10):
#         temp = []
#         for j in range(n):
#             if m[j][i] != 0:
#                 temp.append(m[j][i])
#             m[j][i] = 0
#         cnt = 0
#         for j in range(n-len(temp), n):
#             m[j][i] = temp[cnt]
#             cnt += 1
#
# while True:
#     exist = False
#     ck = make_ck(n)
#     for i in range(n):
#         for j in range(10):
#             if m[i][j] == 0 or ck[i][j]:
#                 continue
#             idx = []
#             cnt = dfs_cnt(i,j)
#             if cnt >= k:
#                 dfs_erase(idx)
#                 exist = True
#
#     if not exist:
#         break
#
#     move_down()
#
# for i in m:
#     print(''.join(map(str, i)))